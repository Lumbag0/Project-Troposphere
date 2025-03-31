# Description: Class used to build out the map on the application

import requests # For making HTTP requests
import sys
from shapely.geometry import shape
import matplotlib.colors as mcolors
from weather import Weather
import numpy as np
import folium
from countries import World

class Map:
    # Description: Get the borders of the countries so they can be plotted
    # Parameters: N\A
    # Returns: Borders of the countries in JSON
    def get_country_data():
        url = "https://raw.githubusercontent/johan/world.geo.json/master/countries.geo.json"

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
    def get_subdivisions_data():
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
        # Turn the list of city ID's with corresponding latitude and longitude into a certain numpy array 
        # for easier math using compressed KD Tree for nearest neighbor finding
        city_tree = Weather.create_city_tree(city_coordinates)
        city_coords_array = np.array(list(city_coordinates.values()))

        centers = []
        features_info = []

        for i, feature in enumerate(data):
            geometry = shape(feature["geometry"])

            lat, lon = self.get_polygon_center(geometry)
            if lat is not None and lon is not None:
                # Add center locations to the list
                centers.append([lat, lon])

                # Store the shape of countries/territories and center of it in a lilst
                features_info.append((feature, geometry, (lat, lon)))

            # Find the nearest city to the corresponding territory/countries geometric center and
            # assign it to the nearest indicies variable accordingly
            centers_np = np.array(centers)
            distances, nearest_indices = city_tree.quimportery(centers_np, k=1)
            valid_result_idx = 0

            # Loop through the geometries and centers of them to map out the correct colors and shapes
            # On the map for the territories/countries
            for feature, geometry, center in features_info:
                if center is not None:
                    city_idx = nearest_indices[valid_result_idx]
                    valid_result_idx += 1
                    closest_city_coords = tuple(city_coords_array[city_idx])

                    # Get temperature from coordinates of the city closest to the center of the shape 
                    # of the territory/country
                    temperature = temperature_data.get(closest_city_coords, None)

                    # Use color function to get the corresponding color from the temperature
                    color = Color.get_temperature_color(temperature) if temperature is not None else "gray"
                else:
                    # Debugging if broken
                    color = "gray"
                    temperature = None

                # Plot the shape of the territory/country on the map for multiple geometries with the 
                # given temperatures, colors, coordinates, etc.
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

    def add_capital_markers(folium_map, city_coordinates, temperature_data):
        # Create a feature group layer for capital markers
        capitals_layer = folium.FeatureGroup(name="CapitalsLayer")

        # Get the United States
        united_states = World.United_States
        states = united_states.get_states()

        # Get Countries
        world = World.Countries
        countriesFromCountries = world.get_countries()
        capital_data = {}

        # Loop through the US states add to list with coordinates
        for state in states:
            capital_name = united_states.get_capital(state)
            capital_coord = united_states.get_capital_coord(state)

            if capital_name and capital_coord:
                capital_data[state] = {"name": capital_name, "coord": (capital_coord["lat"], capital_coord["lon"])}
        
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

class Color:
    # Description: Returns the final color based on how hot or cold the temperature is
    # Example: If C1 is red and C2 is orange, the factor is .5, it will return a reddish orange
    # Parameters: Starting color, ending color, how much between they are from one another
    # Returns: Hex color value
    def interpolate_color(c1, c2, factor):
        r1, g1, b1 = mcolors.hex2color(c1)
        r2, g2, b2 = mcolors.hex2color(c2)

        r = r1 + (r2 - r1) * factor
        g = g1 + (g2 - g1) * factor
        b = b1 + (b2 - b1) * factor

        return mcolors.rgb2hex((r, g, b))
    
    # Description: Goes through the temperature and returns a color based off of how high/low the temperature is after 
    # making calculations on it
    # Returns: Corresponding color for the temperature sent
    def get_temperature_color(self, temperature):
        # Color Range
        color_ranges = [
            (-float('inf'), -10, "#0000FF"),
            (-10, 10, "#ADD8E6"),
            (10, 20, "#008000"),
            (20, 30, "#FFFF00"),
            (30, 50, "#FFA500"),
            (50, float('inf'), "#FF0000")
        ]

        # Set temperature to gray for no temperature data
        if temperature is None:
            return "#808080"
        
        # Loop through color ranges
        for i, (low, high, color) in enumerate(color_ranges):
            if low <= temperature < high:
                return color
            
            elif i < len(color_ranges) - 1:
                next_color = color_ranges[i + 1][2]
                factor = (temperature - low) / (high - low)
                return self.interpolate_color(color, next_color, factor)
            
        return "#808080" # Fallback (gray)