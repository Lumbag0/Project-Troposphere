# Description: Map class, used to build out the map on the application
import tkintermapview
# Import for speeding up webscraping
from concurrent.futures import ThreadPoolExecutor, as_completed
# Import for webscraping
import requests
import urllib.parse
import re

# Set zoom level
ZOOM_LEVEL = 4.6

# Used for formatting temp to find
# Removes + from 
temperature_regex = re.compile(r"([+-]?\d+(\.\d+)?)")


# Function to get average temp
def fetch_average_temperature(location):
    # URL Encode each city for search
    location_encoded = urllib.parse.quote(location)
    url = f"http://wttr.in/{location_encoded}?format=%t"

    try:
        # Make request
        response = requests.get(url, timeout=3)
        response.raise_for_status()

        # Pulls temperature from wttr.io format to string
        temperature_str = response.text.strip()
        
        # Remove degree sign
        match = temperature_regex.search(temperature_str)
        
        # If there is a temperature
        if match:
            # Strip the plus again
            num_str = match.group(1)
            return float(num_str.lstrip('+'))
    except Exception:
        pass

    return None


# Function to add capital markers on the map
def add_capital_markers(map_widget, capitals):
    with ThreadPoolExecutor(
            max_workers=10) as executor:  # Change max workers for faster but slower speed, we can test with larger datasets
        future_to_city = {executor.submit(fetch_average_temperature, city): city for city in capitals}
        
        # Loop through each completed thread
        for future in as_completed(future_to_city):
            city = future_to_city[future]
            try:
                # Place temperature result from returned thread
                temp = future.result()
                print(temp, city, capitals[city]["lat"], capitals[city]["lon"])
                # Set label to N/A if no results
                label = f"{temp if temp is not None else 'N/A'}"

                # Set marker on the map
                map_widget.set_marker(capitals[city]["lat"], capitals[city]["lon"], text=label)
            
            # If there is an error grabbing the city, print the city
            except Exception as e:
                print(f"ERROR: {city}")

class Map:
    def set_up_map(capital_data):
        # Set the map size
        map_widget = tkintermapview.TkinterMapView(width=1920, height=1080, corner_radius=0)
        map_widget.pack()

        # Set starting position and zoom level
        map_widget.set_zoom(ZOOM_LEVEL)
        map_widget.set_position(38.8339, -104.8214)

        # Set the zoom out level to show US capitals
        map_widget.pack()

        add_capital_markers(map_widget, capital_data)