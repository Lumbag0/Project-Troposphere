import csv

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
    
    # Description: Grab and save the file of the dataset of ci
    def fetch_temperature_data(api_key)