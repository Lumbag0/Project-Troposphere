
# Project-Troposphere
Weather map application written in Python for CS-3300 Intro to Software Engineering at the University of Colorado Colorado Springs.

**Project-Troposphere is a interactive map of the world's current temperature**
  - Easy at-a-glance view
  - Zoom-based map changes
  - Color coded temperatures
  - Key location temperatures shown

![image](https://github.com/user-attachments/assets/6eae6474-a81a-4a1d-a9a2-9a54ae779277)

**How does it work? What are some benefits?**
  - Uses free to use API Weatherbit to bulk grab weather information with accuraccy.
  - Weatherbit provides us with plenty of information you can add onto this project with.
  - We use high performance interactive map; folium, to plot the temperature on.
  - Systems to integrate the web based folium system to in-app usable.
  - We use a modular tiling system for countries and territories, which can be used else where.
  - Gradient calculation system for color coded tiles.
  - Can click on the tiles to get corresponding temperature information.
  - A simplistic design for features to be added onto it.

![image](https://github.com/user-attachments/assets/331b2655-255e-4344-923b-4d6f15b11c1f)

# Installation
**Step 1: Get Weatherbit.io API Key**
- Navigate to weatherbit.io and create an account to use their API key.
- Make sure to save it as the program will prompt you for the key.

**Step 2: Install Packages**
`pip3 install -r requirements.txt`

**Step 3: Run Program**
`python3 project-troposphere.py`

# Credit
[Weatherbit](https://www.weatherbit.io/) - Live Weather Data

[Natual Earth Vector](https://github.com/nvkelso/natural-earth-vector) - Territory Regions

[World Geo Json](https://github.com/johan/world.geo.json) - Country Regions

# License 
GPL 3.0 ©