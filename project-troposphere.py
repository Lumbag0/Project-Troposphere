# Description: Main program that starts the map

import tkinter as tk
from app import App
import sys
import requests

@staticmethod
def get_cities_data():
    print("Getting city data...")
    url = "https://cdn.weatherbit.io/static/exports/cities_full.csv"
    try:
        response = requests.get(url, timeout=10)
            # Exit on timeout
    except requests.exceptions.Timeout:
        print("ERROR: request timed out")
        sys.exit(1)
    
    # Exit on connection issues
    except requests.exceptions.ConnectionError:
        print("ERROR: Could not connect to Weatherbit.io")
        sys.exit(1)

     # Exit on unexpected errors
    except requests.exceptions.RequestException as error:
        print(f"ERROR: An unexcepted error occurred -- {error}")
    else:
        if response.status_code == 200:
            with open('cities_full.csv', "wb") as file:
                file.write(response.content)
        else:
            print(f"ERROR: Failed to download data")
            print(f"Source: {url}")
            print(f"Status Code: {response.status_code}")
            print(f"Details: {response.text}")

if __name__ == "__main__":
    # Get API key and store it here
    get_cities_data()
    
    root = tk.Tk()
    app = App()
    root.mainloop()