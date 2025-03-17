# Description: Class that contains classes for countries along with their dictionary and functions
# Methods in Class:
#    get_states -- Get each state
#    get_state_abbr(state) -- Get the abbreviated version of a state
#    get_capital(state) -- Get the capital of a state
#    get_capital_coord() -- Get the coordinates of a state's capital 
class United_States:
    __states = {
        "Alabama": {"abbr": "AL", "capital": "Montgomery", "capital_coord": {"lat": 32.3777, "lon": -86.3000}},
        "Alaska": {"abbr": "AK", "capital": "Juneau", "capital_coord": {"lat": 58.3019, "lon": -134.4197}},
        "Arizona": {"abbr": "AZ", "capital": "Phoenix", "capital_coord": {"lat": 33.4484, "lon": -112.0740}},
        "Arkansas": {"abbr": "AR", "capital": "Little Rock", "capital_coord": {"lat": 34.7465, "lon": -92.2896}},
        "California": {"abbr": "CA", "capital": "Sacramento", "capital_coord": {"lat": 38.5767, "lon": -121.4944}},
        "Colorado": {"abbr": "CO", "capital": "Denver", "capital_coord": {"lat": 39.7392, "lon": -104.9903}},
        "Connecticut": {"abbr": "CT", "capital": "Hartford", "capital_coord": {"lat": 41.7640, "lon": -72.6823}},
        "Delaware": {"abbr": "DE", "capital": "Dover", "capital_coord": {"lat": 39.1582, "lon": -75.5244}},
        "Florida": {"abbr": "FL", "capital": "Tallahassee", "capital_coord": {"lat": 30.4383, "lon": -84.2807}},
        "Georgia": {"abbr": "GA", "capital": "Atlanta", "capital_coord": {"lat": 33.7490, "lon": -84.3880}},
        "Hawaii": {"abbr": "HI", "capital": "Honolulu", "capital_coord": {"lat": 21.3069, "lon": -157.8583}},
        "Idaho": {"abbr": "ID", "capital": "Boise", "capital_coord": {"lat": 43.6150, "lon": -116.2023}},
        "Illinois": {"abbr": "IL", "capital": "Springfield", "capital_coord": {"lat": 39.7980, "lon": -89.6444}},
        "Indiana": {"abbr": "IN", "capital": "Indianapolis", "capital_coord": {"lat": 39.7684, "lon": -86.1581}},
        "Iowa": {"abbr": "IA", "capital": "Des Moines", "capital_coord": {"lat": 41.5868, "lon": -93.6250}},
        "Kansas": {"abbr": "KS", "capital": "Topeka", "capital_coord": {"lat": 39.0473, "lon": -95.6752}},
        "Kentucky": {"abbr": "KY", "capital": "Frankfort", "capital_coord": {"lat": 38.1867, "lon": -84.8753}},
        "Louisiana": {"abbr": "LA", "capital": "Baton Rouge", "capital_coord": {"lat": 30.4515, "lon": -91.1871}},
        "Maine": {"abbr": "ME", "capital": "Augusta", "capital_coord": {"lat": 44.3106, "lon": -69.7795}},
        "Maryland": {"abbr": "MD", "capital": "Annapolis", "capital_coord": {"lat": 38.9784, "lon": -76.4922}},
        "Massachusetts": {"abbr": "MA", "capital": "Boston", "capital_coord": {"lat": 42.3601, "lon": -71.0589}},
        "Michigan": {"abbr": "MI", "capital": "Lansing", "capital_coord": {"lat": 42.7325, "lon": -84.5555}},
        "Minnesota": {"abbr": "MN", "capital": "Saint Paul", "capital_coord": {"lat": 44.9537, "lon": -93.0900}},
        "Mississippi": {"abbr": "MS", "capital": "Jackson", "capital_coord": {"lat": 32.2998, "lon": -90.1848}},
        "Missouri": {"abbr": "MO", "capital": "Jefferson City", "capital_coord": {"lat": 38.5767, "lon": -92.1735}},
        "Montana": {"abbr": "MT", "capital": "Helena", "capital_coord": {"lat": 46.5891, "lon": -112.0391}},
        "Nebraska": {"abbr": "NE", "capital": "Lincoln", "capital_coord": {"lat": 40.8136, "lon": -96.7026}},
        "Nevada": {"abbr": "NV", "capital": "Carson City", "capital_coord": {"lat": 39.1638, "lon": -119.7674}},
        "New Hampshire": {"abbr": "NH", "capital": "Concord", "capital_coord": {"lat": 43.2081, "lon": -71.5376}},
        "New Jersey": {"abbr": "NJ", "capital": "Trenton", "capital_coord": {"lat": 40.2206, "lon": -74.7699}},
        "New Mexico": {"abbr": "NM", "capital": "Santa Fe", "capital_coord": {"lat": 35.6870, "lon": -105.9378}},
        "New York": {"abbr": "NY", "capital": "Albany", "capital_coord": {"lat": 42.6526, "lon": -73.7562}},
        "North Carolina": {"abbr": "NC", "capital": "Raleigh", "capital_coord": {"lat": 35.7796, "lon": -78.6382}},
        "North Dakota": {"abbr": "ND", "capital": "Bismarck", "capital_coord": {"lat": 46.8083, "lon": -100.7837}},
        "Ohio": {"abbr": "OH", "capital": "Columbus", "capital_coord": {"lat": 39.9612, "lon": -82.9988}},
        "Oklahoma": {"abbr": "OK", "capital": "Oklahoma City", "capital_coord": {"lat": 35.4676, "lon": -97.5164}},
        "Oregon": {"abbr": "OR", "capital": "Salem", "capital_coord": {"lat": 44.9429, "lon": -123.0351}},
        "Pennsylvania": {"abbr": "PA", "capital": "Harrisburg", "capital_coord": {"lat": 40.2732, "lon": -76.8867}},
        "Rhode Island": {"abbr": "RI", "capital": "Providence", "capital_coord": {"lat": 41.8236, "lon": -71.4222}},
        "South Carolina": {"abbr": "SC", "capital": "Columbia", "capital_coord": {"lat": 34.0007, "lon": -81.0348}},
        "South Dakota": {"abbr": "SD", "capital": "Pierre", "capital_coord": {"lat": 44.3683, "lon": -100.3510}},
        "Tennessee": {"abbr": "TN", "capital": "Nashville", "capital_coord": {"lat": 36.1627, "lon": -86.7816}},
        "Texas": {"abbr": "TX", "capital": "Austin", "capital_coord": {"lat": 30.2672, "lon": -97.7431}},
        "Utah": {"abbr": "UT", "capital": "Salt Lake City", "capital_coord": {"lat": 40.7608, "lon": -111.8910}},
        "Vermont": {"abbr": "VT", "capital": "Montpelier", "capital_coord": {"lat": 44.2624, "lon": -72.5800}},
        "Virginia": {"abbr": "VA", "capital": "Richmond", "capital_coord": {"lat": 37.5407, "lon": -77.4360}},
        "Washington": {"abbr": "WA", "capital": "Olympia", "capital_coord": {"lat": 47.0379, "lon": -122.9007}},
        "West Virginia": {"abbr": "WV", "capital": "Charleston", "capital_coord": {"lat": 38.3498, "lon": -81.6326}},
        "Wisconsin": {"abbr": "WI", "capital": "Madison", "capital_coord": {"lat": 43.0731, "lon": -89.4012}},
        "Wyoming": {"abbr": "WY", "capital": "Cheyenne", "capital_coord": {"lat": 41.1400, "lon": -104.8202}}
    }
    
    '''
    Description: Gets the States
    Parameters: N\A
    Returns: List of States
    '''
    @staticmethod
    def get_states():
        return list(United_States.__states.keys())
    
    '''
    Description: Gets the Abbreviation of the State based on the name of the state
    Parameters: Name of the state to get abbreviation for
    Returns: String entry for the state, if state is not found, return None
    '''
    @staticmethod
    def get_state_abbr(state):
        state_abbr = United_States.__states.get(state)["abbr"]
        
        # Make sure that the entry was pulled
        if not state_abbr:
            print(f"[ERROR]: {state} not found...")
        else:
            return state_abbr

    '''
    Description: Gets the Capital of the State provided
    Parameters: Name of the State to get capital for
    Returns: String entry for capital, returns None if it cannot get the capital
    '''
    @staticmethod
    def get_capital(state):
        state_capital = United_States.__states.get(state)["capital"]

        # Make sure that entry was pulled
        if not state_capital:
            print(f"[ERROR]: {state} not found...")
        else:
            return state_capital
    '''
    Description: Gets the coordinates for the capital 
    Parameters: Name of the State to get capital coordinates for
    Returns: dictionary entry for the coordinates
    '''
    @staticmethod
    def get_capital_coord(state):
        coord = United_States.__states.get(state)["capital_coord"]

        if not coord:
            print(f"[ERROR]: {state} not found...")
        else:
            return coord