import tkinter as tk
import map

# App class
class App:
    def __init__(self, root):
        self.app = root
        self.app.title("Project Troposphere")
        map.set_up_map()