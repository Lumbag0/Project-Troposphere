# Description: Map class, used to build out the map on the application
import tkintermapview

ZOOM_LEVEL=4.6

class Map:
    def __init__(self):
        # Set the map size
        map_widget = tkintermapview.TkinterMapView(width=1920, height=1080, corner_radius=0)
        map_widget.pack()

        # Set starting position and zoom level
        map_widget.set_zoom(ZOOM_LEVEL)
        map_widget.set_position(38.8339, -104.8214)
        
        # Set the zoom out level to show US capitals 
        map_widget.pack()
