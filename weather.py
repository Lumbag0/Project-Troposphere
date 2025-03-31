import csv
import requests
import sys
import gzip

class Weather:
    # Description: Create a list of each location ID from the list of cities from weatherbit.io
    # Parameters: N\A
    # Returns: Dictionary of cities by location ID with corresponding latitude and longitude
    def load_city_coordinates() -> dict:
        city_coordinates = {}
        with open('cities_full.csv', 'r', encoding='utf-8') as csvfile:
            # Read CSV as a dictionary
            reader = csv.DictReader(csvfile)

            for row in reader:
                location_id = int(row["city_id"])
                lat = float(row["lat"])
                lon = float(row["lon"])

                # Store latitude and longitude with a key ID
                city_coordinates[location_id] = (lat, lon)
        return city_coordinates
    
    # Description: Grab and save the file of the dataset of cities with corresponding temperatures
    # Parameters: API Key to Weatherbit.io
    # Returns: N\A
    def fetch_temperature_data(api_key):
        weather_bit = f"https://api.weatherbit.io/v2.0/bulk/files/current.csv.gz?key={api_key}"
        try:
            response = requests.get(weather_bit, timeout=10)
        
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
            # Download csv if connection successful
            # Otherwise print error messages
            if response.status_code == 200:
                with open('current_weather.csv.gz', "wb") as file:
                    file.write(response.content)
                    print("Data downloaded successfully")
            else:
                print(f"ERROR: Failed to download data")
                print(f"Source: Weatherbit.io")
                print(f"Status Code: {response.status_code}")
                print(f"Details: {response.text}")
    # Description: Read in the current weather file foor all the cities and create a list of coordinates
    # That correspond to a temperature, this way we know the temperature at said coordiantes
    # Parameters: Dictionary of cities by location ID with Longitude and Latitude as values
    # Returns: Dictionary of Coordinates and the temperatures at the coordinates
    def parse_temperature_data(city_coordinates):
        temperature_data = {}
        with gzip.open('current_weather.csv.gz', 'rt', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            # Iterate through each row
            for row in reader:
                try:
                    # Extract the location ID
                    location_id = int(row['Location ID'])

                    # If the location ID is within the dictionary city_coordinates
                    # Extract the latitude and longitude from the city_coordinates dictionary and store the 
                    # temperature where the latitude and longitude is the key and the value is the temperature
                    if location_id in city_coordinates:
                        lat, lon = city_coordinates[location_id]
                        temperature_data[(lat, lon)] = float(row['Temperature (C)'])
              
                except(ValueError, KeyError) as error:
                    print(f"ERROR: Skipping row: {error}")
        return temperature_data
    