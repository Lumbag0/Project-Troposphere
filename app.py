import tkinter as tk
import map

class App:
    def __init__(self, root):
        self.app = root
        self.app.title("Project Troposphere")
        map.Map()
