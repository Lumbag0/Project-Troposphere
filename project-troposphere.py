# Description: Main program that starts the map

import tkinter as tk
from app import App

if __name__ == "__main__":
    # Get API key and store it here
    key = App.get_key()
    
    root = tk.Tk()
    app = App(root)
    root.mainloop()