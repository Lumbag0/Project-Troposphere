# Class for setting the colors on the maps
import matplotlib.colors as mcolors

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