import folium
import requests
import os
import sys

from map import Map
from weather import Weather

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtCore import QUrl

# App class
class App:
    def __init__(self):
        # Import function that has to be created for the map to be displayed on the UI window
        app = QApplication([])

        # Create the map window using the folium based map system
        window=MapWindow()

        # Create said window
        window.show()

        # Start the system for UI, User input, etc.
        sys.exit(app.exec_())
    
    @staticmethod
    def create_folium_map(city_coordinates):
        print("Creating map...")
        map_instance = Map()

        map_file_path = os.path.join(os.getcwd(), "map.html")

        folium_map = folium.Map(location=[37.8, -96], zoom_start=5, control_scale=True)

        countries_layer = folium.FeatureGroup(name="CountriesLayer")
        subdivisions_layer = folium.FeatureGroup(name="TerritoriesLayer")

        countries_data = Map.get_country_data()
        subdivisions_data = Map.get_subdivisions_data()

        key = App.get_key()

        Weather.fetch_temperature_data(f"{key}")
        temperature_data = Weather.parse_temperature_data(city_coordinates)

        # Plot the borders for the countries
        map_instance.plot_borders(countries_layer, countries_data, temperature_data, city_coordinates)

        # Plot the borders for the territories
        map_instance.plot_borders(subdivisions_layer, subdivisions_data, temperature_data, city_coordinates)

        # Add layer of countries plotted to the map
        folium_map.add_child(countries_layer)

        # Add layer of territories plotted to the map
        folium_map.add_child(subdivisions_layer)

        # Add capital markers to the map
        Map.add_capital_markers(folium_map, city_coordinates, temperature_data)

        # Add other city markers to the map
        Map.add_city_markers(folium_map, city_coordinates, temperature_data)

        # Implement JS into the application
        folium_map.get_root().html.add_child(folium.Element("""<script>
            document.addEventListener("DOMContentLoaded", function () {
                window.map = Object.values(window).find(obj => obj instanceof L.Map);

                window.countriesLayer = null;
                window.subdivisionsLayer = null;
                window.capitalsLayer = null;
                window.capitalsLayer2 = null;

                let layerCount = 0;
                window.map.eachLayer(function (layer) {
                    if (layer instanceof L.FeatureGroup) {
                        if (!window.countriesLayer) window.countriesLayer = layer;
                        else if (!window.subdivisionsLayer) window.subdivisionsLayer = layer;
                        else if (!window.capitalsLayer) window.capitalsLayer = layer;
                        else if (!window.capitalsLayer2) window.capitalsLayer2 = layer;
                    }
                });

                function updateLayers() {
                    let zoom = window.map.getZoom();

                    if (zoom > 4) {
                        window.map.removeLayer(window.countriesLayer);
                        window.map.addLayer(window.subdivisionsLayer);
                    } else {
                        window.map.removeLayer(window.subdivisionsLayer);
                        window.map.addLayer(window.countriesLayer);
                    }

                    if (zoom > 3) {
                        window.map.addLayer(window.capitalsLayer);
                    } else {
                        window.map.removeLayer(window.capitalsLayer);
                    }

                    if (zoom > 6) {
                        window.map.addLayer(window.capitalsLayer2);
                    } else {
                        window.map.removeLayer(window.capitalsLayer2);
                    }
                }

                window.map.removeLayer(window.subdivisionsLayer);
                window.map.removeLayer(window.capitalsLayer); 
                window.map.removeLayer(window.capitalsLayer2); 
                window.map.on('zoomend', updateLayers);
                updateLayers();
            });
        </script>
        """))

        folium_map.get_root().html.add_child(folium.Element("""
            <script>
                document.addEventListener("DOMContentLoaded", function () {
                    window.map = Object.values(window).find(obj => obj instanceof L.Map);

                    let southWest = L.latLng(-60, -180); 
                    let northEast = L.latLng(85, 180);
                    let bounds = L.latLngBounds(southWest, northEast);

                    window.map.setMaxBounds(bounds);
                    window.map.on('drag', function () {
                        window.map.panInsideBounds(bounds, { animate: false });
                    });

                });
            </script>
        """))

        folium_map.save(map_file_path)
        return map_file_path

    # Description: Gets the key from the user to use to authenticate with Weatherbit.io
    # Parameters: N\A
    # Returns: String
    @staticmethod
    def get_key() -> str:
        valid_key = False
        # Loop until valid key is entered
        while not valid_key:
            key = input("Please enter the API Key for Weatherbit.io: ")
            response = requests.get(f"https://api.weatherbit.io/v2.0/current?city=Denver&key={key}")
            # If the response is 200 (ok) then break out of loop, otherwise print error
            print(response.status_code)
            if response.status_code == 200:
                valid_key = True
            else:
                print(f"ERROR: Invalid key {key}")
        return key
    
class CustomWebEnginePage(QWebEnginePage):
    def javaScriptConsoleMessage(self, level, message, line, source_id):
        print(f"JS Console [{level}]: {message} (Line {line}) in {source_id}")

class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        print("Creating window...")
        # Set up the window name / window size / position
        self.setWindowTitle("Project Troposphere")
        self.setGeometry(0, 0, 2000, 1000)

        # Use QWidget Built in stuff to display folium in app
        self.container = QWidget(self)
        self.setCentralWidget(self.container)
        self.browser = QWebEngineView(self.container)

        # Set size of browser window
        self.browser.setGeometry(0, 0, 2000, 1000)

        # Assign a custom web engine page to handle additional web functionality
        self.browser.setPage(CustomWebEnginePage(self.browser))

        # Load City coordinates from CSV file
        city_coordinates = Weather.load_city_coordinates()

        # Start creating the map with resource found
        map_file_path = App.create_folium_map(city_coordinates)
        
        # Load folium map into the web in app
        self.browser.setUrl(QUrl.fromLocalFile(map_file_path))

        # Run JS code to make sure you can get output from JS to python for later use
        self.browser.loadFinished.connect(self.run_debug_script)
    
    def run_debug_script(self):
        self.browser.page().runJavaScript('console.log("Javascrpt Ran");')