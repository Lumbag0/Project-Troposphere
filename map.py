# Description: Class used to build out the map on the application

import requests # For making HTTP requests
import sys
from shapely.geometry import shape
from weather import Weather
import numpy as np
import folium
from countries import World
from color import Color
import random


class Map:
    # Description: Get the borders of the countries so they can be plotted
    # Parameters: N\A
    # Returns: Borders of the countries in JSON
    @staticmethod
    def get_country_data():
        print("Getting the border data...")
        url = "https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json"

        # Obtain the borders from the URL
        # Handle unknown exceptions
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        
        except requests.exceptions.RequestException as error:
            print(f"ERROR: Failed to fetch data -- {error}")
            sys.exit(1)
        
        else:
            return response.json()["features"]
    
    # Description: Get the borders of the territories for them to be plotted on the map
    # Parameters: N\A
    # Returns: Borders of the territories for them to be plotted on the map
    @staticmethod
    def get_subdivisions_data():
        print("Getting border territory data...")
        url = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_10m_admin_1_states_provinces.geojson"
        
        # Get JSON of each state and province
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as error:
            print(f"ERROR: Failed to fetch data -- {error}")
            sys.exit(1)
        else:
            return response.json()["features"]
        
    # Description: Uses built in geomtry country to find the center point of a certain territory 
    # Parameters: N\A
    # Returns: The center point latitude and longitude of said country / territory
    @staticmethod
    def get_polygon_center(geometry):
        if geometry.geom_type == "Polygon":
            return geometry.centroid.y, geometry.centroid.x
        elif geometry.geom_type == "MultiPolygon":
            return geometry.representative_point().y, geometry.representative_point().x
        else:
            return None, None
        
    # Description: Goes through the countries and territories and plots them on the map
    # Parameters: Layer of which countries or territories are stored, data from the big list sent from 
    # countries / territories file, the file of temperatures from all of the cities, and coordinates from 
    # the city file with corresponding city lat/lon and location ID
    # Returns: N\A
    def plot_borders(self, layer, data, temperature_data, city_coordinates):
        print("Plotting borders...")
        color_instance = Color()
        weather_instance = Weather()

        # Turn the list of city ID's with corresponding latitude and longitude into a certain Numpy array for
        # easier math using cKDTree for nearest neighbor finding
        city_tree =  weather_instance.create_city_tree(city_coordinates)
        city_coords_array = np.array(list(city_coordinates.values()))

        centers = []
        features_info = []

        for i, feature in enumerate(data):
            geometry = shape(feature["geometry"])

            # Run function to get geometric center to the territories/countries
            lat, lon = self.get_polygon_center(geometry)

            if lat is not None and lon is not None:
                # Add center locations to list
                centers.append([lat, lon])
                
                # Stores the shape of countries/territories and center of them in to a list
                features_info.append((feature, geometry, (lat, lon)))

        # Find nearest city to the corresponding territory/countries geometric center, and assign it to nearest_indicies accordingly
        centers_np = np.array(centers)
        distances, nearest_indicies = city_tree.query(centers_np, k=1)

        valid_result_idx = 0

        # Loop through the geometries and centers of them to map out the correct colors and shapes on the map for the territories/countries
        for feature, geometry, center in features_info:
            if center is not None:
                city_idx = nearest_indicies[valid_result_idx]
                valid_result_idx += 1
                closest_city_coords = tuple(city_coords_array[city_idx])

                # Get temperature from coordinates of the city closest to the center of the shape of the territory/country
                temperature = temperature_data.get(closest_city_coords, None)

                # Use color function to get the corresponding color for the temperature
                color = color_instance.get_temperature_color(temperature) if temperature is not None else "gray"
            else:
                # Debugging if broken
                color = "gray"
                temperature = None
            
            # Plot the shape of the territory/country on the map for multiple geometries with the given temperatures, colors, coordinates, etc.
            if geometry.geom_type == "Polygon":
                coords = [(lat, lon) for lon, lat in geometry.exterior.coords]
                folium.Polygon(
                    locations=coords,
                    color=color,
                    fill=True,
                    fill_opacity=0.5,
                    popup=f"Temp: {temperature}°C"
                ).add_to(layer)
            elif geometry.geom_type == "MultiPolygon":
                for polygon in geometry.geoms:
                    coords = [(lat, lon) for lon, lat in polygon.exterior.coords]
                    folium.Polygon(
                        locations=coords,
                        color=color,
                        fill=True,
                        fill_opacity=0.5,
                        popup=f"Temp: {temperature}°C"
                    ).add_to(layer)

    @staticmethod
    def add_capital_markers(folium_map, city_coordinates, temperature_data):

        print("Adding capital markers...")

        # Create a feature group layer for capital markers
        capitals_layer = folium.FeatureGroup(name="capitalsLayer")

        capital_data = {}

        # Get the United States
        united_states = World.United_States
        states = united_states.get_states()

        # Get Countries
        world = World.Countries
        countriesFromCountries = world.get_countries()

        # Loop through the US states add to list with coordinates
        for state in states:
            capital_name = united_states.get_capital(state)
            capital_coord = united_states.get_capital_coord(state)

            if capital_name and capital_coord:
                capital_data[state] = {"name": capital_name, "coord":(capital_coord["lat"], capital_coord["lon"])}

        # Loop through countries and add to list with coordinates
        for country in countriesFromCountries:
            capital_name = world.get_country_capital(country)
            capital_coord = world.get_country_capital_coord(country)

            if capital_name and capital_coord:
                capital_data[country] = {"name": capital_name, "coord": (capital_coord["lat"], capital_coord["lon"])}

        # Iterate through states and countries and get the average temperatures to be displayed in text on the map
        for state, data in capital_data.items():
            capital_name = data["name"]
            lat, lon = data["coord"]

            average_temperature = Weather.fetch_average_temperature((lat, lon), city_coordinates, temperature_data)
            if average_temperature is not None:
                text_color = "black"
                label_html = f'<div style="color: {text_color}; font-weight: bold; font-size: 12px;">{average_temperature}°C</div>'
                label = folium.Marker(
                    location=[lat, lon],
                    icon=folium.DivIcon(html=label_html)
                )
                capitals_layer.add_child(label)
            else:
                print("No Temp")

        # add layer of text temps to the map
        folium_map.add_child(capitals_layer)

    @staticmethod
    def add_city_markers(folium_map, city_coordinates, temperature_data):
        print("Adding city markers...")

        # Create a feature group layer for more city markers
        cities_layer = folium.FeatureGroup(name="capitalsLayer2")

        # Shuffle and limit to 1000 cities at random
        city_items = list(city_coordinates.items())
        random.shuffle(city_items)
        city_items = city_items[:1000]

        for city, coord in city_items:
            lat, lon = coord

            # Fetch temperature for the city from the temperature data
            temperature = temperature_data.get(coord, None)

            # If a valid temperature is available, plot the marker with temperature
            if temperature is not None:
                text_color = "black"  # You can customize text color based on temperature if needed
                label_html = f'<div style="color: {text_color}; font-weight: bold; font-size: 12px;">{temperature}°C</div>'
                label = folium.Marker(
                    location=[lat, lon],
                    icon=folium.DivIcon(html=label_html)
                )
                cities_layer.add_child(label)
            else:
                print(f"No temperature data for city at {lat}, {lon}")

        # Add the cities layer to the map
        folium_map.add_child(cities_layer)

