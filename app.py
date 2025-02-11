import tkinter as tk
import map



# Hard coded function to get state info (just so you know format I have it grab from) you can delete whenever
def fetch_capital_coordinates():
    states = {}

    states["Florida"] = {
        "capital": "Tallahassee",
        "lat": 30.4383,
        "lon": -84.2807,
    }

    states["California"] = {
        "capital": "Sacramento",
        "lat": 38.5816,
        "lon": -121.4944,
    }

    states["Texas"] = {
        "capital": "Austin",
        "lat": 30.2672,
        "lon": -97.7431,
    }

    states["New York"] = {
        "capital": "Albany",
        "lat": 42.6526,
        "lon": -73.7562,
    }

    states["Illinois"] = {
        "capital": "Springfield",
        "lat": 39.7817,
        "lon": -89.6501,
    }

    return states





# App class
class App:
    def __init__(self, root):
        self.app = root
        self.app.title("Project Troposphere")

        capital_data = fetch_capital_coordinates()

        map.Map.set_up_map(capital_data)





