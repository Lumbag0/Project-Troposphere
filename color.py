# Class for setting the colors on the maps
import matplotlib.colors as mcolors
import math

class Color:
    # Description: Returns the final color based on how hot or cold the temperature is
    # Example: If C1 is red and C2 is orange, the factor is .5, it will return a reddish orange
    # Parameters: Starting color, ending color, how much between they are from one another
    # Returns: Hex color value
    @staticmethod
    def interpolate_color(c1, c2, factor):
        factor = max(0, min(1, factor))
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
            (-50, -10, "#0000FF", "#ADD8E6"),  # Blue → Light Blue
            (-10, 10, "#ADD8E6", "#008000"),  # Light Blue → Green
            (10, 20, "#008000", "#FFFF00"),  # Green → Yellow
            (20, 30, "#FFFF00", "#FFA500"),  # Yellow → Orange
            (30, 50, "#FFA500", "#FF0000"),  # Orange → Red
            (50, 60, "#FF0000", "#8B0000"),  # Red → Dark Red
        ]
        if temperature is None or math.isnan(temperature):
            return "#808080"
        
        # Loop through color ranges to find correct color
        for low, high, start_color, end_color in color_ranges:
            if low <= temperature < high:
                factor = (temperature - low) / (high - low)
                return self.interpolate_color(start_color, end_color, factor)


        # Fallback to gray
        return "#808080"