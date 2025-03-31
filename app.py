import map
import requests

# App class
class App:
    def __init__(self, root):
        self.app = root
        self.app.title("Project Troposphere")
        map.Map()

    # Description: Gets the key from the user to use to authenticate with Weatherbit.io
    # Parameters: N\A
    # Returns: String
    def get_key() -> str:
        valid_key = False
        # Loop until valid key is entered
        while not valid_key:
            key = input("Please enter the API Key for Weatherbit.io: ")
            response = requests.get(f"https://api.weatherbit.io/v2.0/current?city=Denver&key={key}")
            # If the response is 200 (ok) then break out of loop, otherwise print error
            if response.status_code == 200:
                valid_key = True
            else:
                print(f"ERROR: Invalid key {key}")
        return key