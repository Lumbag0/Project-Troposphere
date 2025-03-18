# Description: Class used to build out the map on the application

import tkintermapview # Displaying interactive map
from concurrent.futures import ThreadPoolExecutor, as_completed # For multi-threading to speed up web requests
import requests # For making HTTP requests to fetch weather data
import urllib.parse # For encoding city names in URLS
import countries 

# Set initial zoom level
ZOOM_LEVEL = 4.6

# Coordinates for Colorado Springs, Colorado
COS_LAT = 38.8339
COS_LONG = -104.8214

class Map:
    def __init__(self):
        map_widget = tkintermapview.TkinterMapView(
            width=1920,
            height=1080,
            corner_radius=0
        )

        # Set Initial Zoom
        map_widget.set_zoom(ZOOM_LEVEL)
        
        # Center on Colorado Springs
        map_widget.set_position(COS_LAT, COS_LONG)

        # Add Capital Markers for all state capitals
        self.add_capital_markers(map_widget)

        map_widget.pack()

    # Description: Core functionality to grab the temperature along with placing on the map
    # Parameters: the map widget
    # Returns: N\A
    def add_capital_markers(self, map_widget):
        united_states = countries.United_States
        states = united_states.get_states()
        capital_data = {}

        # Loop through each state and add the capital name and coordinate of capital
        for state in states:
            capital_data[state] = {
                "name": united_states.get_capital(state),
                "coord": united_states.get_capital_coord(state)
            }

        with ThreadPoolExecutor(max_workers=10) as thread_pool:
            # Dictionary to map future tasks to their state
            future_to_state = {}

            # Obtain the temperature of each state asynchronously
            for state in capital_data:
                future_task = thread_pool.submit(self.fetch_average_temperature, capital_data[state]["name"])
                future_to_state[future_task] = state

            # For each state
            for completed_future in as_completed(future_to_state):
                state = future_to_state[completed_future]

                try:
                    # Retrieve the temperature result from the completed future task
                    average_temperature = completed_future.result()
                    
                    # print out each state, the temperature of the capital, and the coordinates in the terminal for debugging purposes
                    print(f"Temperature for {state}: {average_temperature}, Coordinates: {capital_data[state]['coord']}")

                    # Format the label to display the temperature or "N/A if no data is available"
                    temperature_label = f"{average_temperature if average_temperature is not None else 'N/A'}"

                    # Retrieve the lat and long of the states capital
                    latitude = capital_data[state]["coord"]["lat"]
                    longitude = capital_data[state]["coord"]["lon"]

                    # Add marker to the map with the temperature as the label
                    map_widget.set_marker(latitude, longitude, text=temperature_label)
                except Exception as error:
                    print(f"ERROR: Could not fetch temperature for {state}")
                    print(f"Exception: {error}")

    # Description: Get the temperature for the capital
    # Parameters: Capital to get temperature for
    # Returns: the temperature as a string or None if unable to get the temperature
    def fetch_average_temperature(self, capital):
        # URL Encode each city for search
        location_encoded = urllib.parse.quote(capital)
        url = f"http://wttr.in/{location_encoded}?format=%t"

        try:
            # Make request
            response = requests.get(url, timeout=3)
            response.raise_for_status()

            # Pulls temperature from wttr.io format to string
            temperature_str = response.text.strip()

            return temperature_str

        except Exception:
            pass

        return None