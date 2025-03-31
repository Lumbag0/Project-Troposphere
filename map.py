# Description: Class used to build out the map on the application

from concurrent.futures import ThreadPoolExecutor, as_completed # For multi-threading to speed up web requests
import requests # For making HTTP requests
import sys
from shapely.geometry import shape
import matplotlib.colors as mcolors

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
        
class Color:
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