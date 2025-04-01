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
            (-float('inf'), -10, "#0000FF"), # Blue
            (-10, 10, "#ADD8E6"), # Light Blue
            (10, 20, "#008000"), # Green
            (20, 30, "#FFFF00"), # Yellow
            (30, 50, "#FFA500"), # Orange
            (50, float('inf'), "#FF0000") # Red
        ]
        if temperature is None or math.isnan(temperature):
            return "#808080"
        
        # Loop through color ranges to find correct color
        for i, (low, high, color) in enumerate(color_ranges):
            if low <= temperature < high:
                # If temperature is inside a range, return the base color
                return color
            
            if i < len(color_ranges) - 1:
                next_low, next_high, next_color = color_ranges[i + 1]

                # Ensure there is a valid temperature range before computing
                if high != next_low:
                    factor = (temperature - low) / (high - low)
                    print(f"Temperature: {temperature}, Factor: {factor}")

                    return self.interpolate_color(color, next_color, factor)
        
        # Fallback to gray
        return "#808080"