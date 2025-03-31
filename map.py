# Description: Class used to build out the map on the application

from concurrent.futures import ThreadPoolExecutor, as_completed # For multi-threading to speed up web requests
import requests # For making HTTP requests
import sys

# Set initial zoom level
ZOOM_LEVEL = 4.6

# Coordinates for Colorado Springs, Colorado
COS_LAT = 38.8339
COS_LONG = -104.8214

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
    