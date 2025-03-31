# Description: Class that contains classes for countries along with their dictionary and functions
# Methods in Class:
#    get_states -- Get each state
#    get_state_abbr(state) -- Get the abbreviated version of a state
#    get_capital(state) -- Get the capital of a state
#    get_capital_coord() -- Get the coordinates of a state's capital
class World:
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
            return list(World.United_States.__states.keys())
        
        '''
        Description: Gets the Abbreviation of the State based on the name of the state
        Parameters: Name of the state to get abbreviation for
        Returns: String entry for the state, if state is not found, return None
        '''
        @staticmethod
        def get_state_abbr(state):
            state_abbr = World.United_States.__states.get(state)["abbr"]
            
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
            state_capital = World.United_States.__states.get(state)["capital"]

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
            coord = World.United_States.__states.get(state)["capital_coord"]

            if not coord:
                print(f"[ERROR]: {state} not found...")
            else:
                return coord
    class Countries:
        __countries = {
        "Afghanistan": {"capital": "Kabul", "capital_coord": {"lat": 34.5281, "lon": 69.1723}},
        "Albania": {"capital": "Tirana", "capital_coord": {"lat": 41.3275, "lon": 19.8189}},
        "Algeria": {"capital": "Algiers", "capital_coord": {"lat": 36.7538, "lon": 3.0588}},
        "Andorra": {"capital": "Andorra la Vella", "capital_coord": {"lat": 42.5078, "lon": 1.5211}},
        "Angola": {"capital": "Luanda", "capital_coord": {"lat": -8.839, "lon": 13.2894}},
        "Antigua and Barbuda": {"capital": "Saint John's", "capital_coord": {"lat": 17.1274, "lon": -61.8468}},
        "Argentina": {"capital": "Buenos Aires", "capital_coord": {"lat": -34.6037, "lon": -58.3816}},
        "Armenia": {"capital": "Yerevan", "capital_coord": {"lat": 40.1792, "lon": 44.4991}},
        "Australia": {"capital": "Canberra", "capital_coord": {"lat": -35.2809, "lon": 149.1300}},
        "Austria": {"capital": "Vienna", "capital_coord": {"lat": 48.2082, "lon": 16.3738}},
        "Azerbaijan": {"capital": "Baku", "capital_coord": {"lat": 40.4093, "lon": 49.8671}},
        "Bahamas": {"capital": "Nassau", "capital_coord": {"lat": 25.0343, "lon": -77.3963}},
        "Bahrain": {"capital": "Manama", "capital_coord": {"lat": 26.2275, "lon": 50.5860}},
        "Bangladesh": {"capital": "Dhaka", "capital_coord": {"lat": 23.8103, "lon": 90.4125}},
        "Barbados": {"capital": "Bridgetown", "capital_coord": {"lat": 13.1, "lon": -59.6167}},
        "Belarus": {"capital": "Minsk", "capital_coord": {"lat": 53.9, "lon": 27.5667}},
        "Belgium": {"capital": "Brussels", "capital_coord": {"lat": 50.8503, "lon": 4.3517}},
        "Belize": {"capital": "Belmopan", "capital_coord": {"lat": 17.25, "lon": -88.7667}},
        "Benin": {"capital": "Porto-Novo", "capital_coord": {"lat": 6.4969, "lon": 2.6285}},
        "Bhutan": {"capital": "Thimphu", "capital_coord": {"lat": 27.4715, "lon": 89.6395}},
        "Bolivia": {"capital": "Sucre", "capital_coord": {"lat": -19.0333, "lon": -65.2628}},
        "Bosnia and Herzegovina": {"capital": "Sarajevo", "capital_coord": {"lat": 43.8486, "lon": 18.3564}},
        "Botswana": {"capital": "Gaborone", "capital_coord": {"lat": -24.6545, "lon": 25.9086}},
        "Brazil": {"capital": "Brasília", "capital_coord": {"lat": -15.7801, "lon": -47.9292}},
        "Brunei": {"capital": "Bandar Seri Begawan", "capital_coord": {"lat": 4.9031, "lon": 114.9398}},
        "Bulgaria": {"capital": "Sofia", "capital_coord": {"lat": 42.6975, "lon": 23.3242}},
        "Burkina Faso": {"capital": "Ouagadougou", "capital_coord": {"lat": 12.3711, "lon": -1.5197}},
        "Burundi": {"capital": "Gitega", "capital_coord": {"lat": -3.4264, "lon": 29.9305}},
        "Cabo Verde": {"capital": "Praia", "capital_coord": {"lat": 14.9333, "lon": -23.5133}},
        "Cambodia": {"capital": "Phnom Penh", "capital_coord": {"lat": 11.5625, "lon": 104.9282}},
        "Cameroon": {"capital": "Yaoundé", "capital_coord": {"lat": 3.8480, "lon": 11.5021}},
        "Canada": {"capital": "Ottawa", "capital_coord": {"lat": 45.4215, "lon": -75.6992}},
        "Central African Republic": {"capital": "Bangui", "capital_coord": {"lat": 4.3947, "lon": 18.5582}},
        "Chad": {"capital": "N'Djamena", "capital_coord": {"lat": 12.6348, "lon": 15.0557}},
        "Chile": {"capital": "Santiago", "capital_coord": {"lat": -33.4489, "lon": -70.6693}},
        "China": {"capital": "Beijing", "capital_coord": {"lat": 39.9042, "lon": 116.4074}},
        "Colombia": {"capital": "Bogotá", "capital_coord": {"lat": 4.7110, "lon": -74.0721}},
        "Comoros": {"capital": "Moroni", "capital_coord": {"lat": -11.7014, "lon": 43.2551}},
        "Congo (Congo-Brazzaville)": {"capital": "Brazzaville", "capital_coord": {"lat": -4.2634, "lon": 15.2429}},
        "Congo (Democratic Republic of the Congo)": {"capital": "Kinshasa", "capital_coord": {"lat": -4.4419, "lon": 15.2663}},
        "Costa Rica": {"capital": "San José", "capital_coord": {"lat": 9.9281, "lon": -84.0907}},
        "Croatia": {"capital": "Zagreb", "capital_coord": {"lat": 45.8131, "lon": 15.9780}},
        "Cuba": {"capital": "Havana", "capital_coord": {"lat": 23.1136, "lon": -82.3666}},
        "Cyprus": {"capital": "Nicosia", "capital_coord": {"lat": 35.1856, "lon": 33.3823}},
        "Czechia (Czech Republic)": {"capital": "Prague", "capital_coord": {"lat": 50.0755, "lon": 14.4378}},
        "Denmark": {"capital": "Copenhagen", "capital_coord": {"lat": 55.6761, "lon": 12.5683}},
        "Djibouti": {"capital": "Djibouti", "capital_coord": {"lat": 11.8251, "lon": 42.5903}},
        "Dominica": {"capital": "Roseau", "capital_coord": {"lat": 15.3017, "lon": -61.3881}},
        "Dominican Republic": {"capital": "Santo Domingo", "capital_coord": {"lat": 18.4861, "lon": -69.9312}},
        "Ecuador": {"capital": "Quito", "capital_coord": {"lat": -0.1807, "lon": -78.4678}},
        "Egypt": {"capital": "Cairo", "capital_coord": {"lat": 30.0444, "lon": 31.2357}},
        "El Salvador": {"capital": "San Salvador", "capital_coord": {"lat": 13.6929, "lon": -89.2182}},
        "Equatorial Guinea": {"capital": "Malabo", "capital_coord": {"lat": 3.75, "lon": 8.7833}},
        "Eritrea": {"capital": "Asmara", "capital_coord": {"lat": 15.338, "lon": 38.9334}},
        "Estonia": {"capital": "Tallinn", "capital_coord": {"lat": 59.4370, "lon": 24.7535}},
        "Eswatini": {"capital": "Mbabane", "capital_coord": {"lat": -26.3225, "lon": 31.1416}},
        "Ethiopia": {"capital": "Addis Ababa", "capital_coord": {"lat": 9.03, "lon": 38.74}},
        "Fiji": {"capital": "Suva", "capital_coord": {"lat": -18.1416, "lon": 178.4419}},
        "Finland": {"capital": "Helsinki", "capital_coord": {"lat": 60.1692, "lon": 24.9402}},
        "France": {"capital": "Paris", "capital_coord": {"lat": 48.8566, "lon": 2.3522}},
        "Gabon": {"capital": "Libreville", "capital_coord": {"lat": 0.4167, "lon": 9.4670}},
        "Gambia": {"capital": "Banjul", "capital_coord": {"lat": 13.4549, "lon": -16.5790}},
        "Georgia": {"capital": "Tbilisi", "capital_coord": {"lat": 41.7151, "lon": 44.8271}},
        "Germany": {"capital": "Berlin", "capital_coord": {"lat": 52.52, "lon": 13.4050}},
        "Ghana": {"capital": "Accra", "capital_coord": {"lat": 5.6037, "lon": -0.1870}},
        "Greece": {"capital": "Athens", "capital_coord": {"lat": 37.9838, "lon": 23.7275}},
        "Grenada": {"capital": "St. George's", "capital_coord": {"lat": 12.0561, "lon": -61.7488}},
        "Guatemala": {"capital": "Guatemala City", "capital_coord": {"lat": 14.6349, "lon": -90.5069}},
        "Guinea": {"capital": "Conakry", "capital_coord": {"lat": 9.5095, "lon": -13.7125}},
        "Guinea-Bissau": {"capital": "Bissau", "capital_coord": {"lat": 11.8817, "lon": -15.6170}},
        "Guyana": {"capital": "Georgetown", "capital_coord": {"lat": 6.8013, "lon": -58.1552}},
        "Haiti": {"capital": "Port-au-Prince", "capital_coord": {"lat": 18.5944, "lon": -72.3074}},
        "Honduras": {"capital": "Tegucigalpa", "capital_coord": {"lat": 13.9676, "lon": -14.3136}},
        "Hungary": {"capital": "Budapest", "capital_coord": {"lat": 47.4979, "lon": 19.0402}},
        "Iceland": {"capital": "Reykjavik", "capital_coord": {"lat": 64.1355, "lon": -21.8954}},
        "India": {"capital": "New Delhi", "capital_coord": {"lat": 28.6139, "lon": 77.2090}},
        "Indonesia": {"capital": "Jakarta", "capital_coord": {"lat": -6.2088, "lon": 106.8456}},
        "Iran": {"capital": "Tehran", "capital_coord": {"lat": 35.6892, "lon": 51.3890}},
        "Iraq": {"capital": "Baghdad", "capital_coord": {"lat": 33.3152, "lon": 44.3661}},
        "Ireland": {"capital": "Dublin", "capital_coord": {"lat": 53.3498, "lon": -6.2603}},
        "Israel": {"capital": "Jerusalem", "capital_coord": {"lat": 31.7683, "lon": 35.2137}},
        "Italy": {"capital": "Rome", "capital_coord": {"lat": 41.9028, "lon": 12.4964}},
        "Jamaica": {"capital": "Kingston", "capital_coord": {"lat": 17.9970, "lon": -76.7936}},
        "Japan": {"capital": "Tokyo", "capital_coord": {"lat": 35.6762, "lon": 139.6503}},
        "Jordan": {"capital": "Amman", "capital_coord": {"lat": 31.9634, "lon": 35.9304}},
        "Kazakhstan": {"capital": "Astana", "capital_coord": {"lat": 51.1694, "lon": 71.4491}},
        "Kenya": {"capital": "Nairobi", "capital_coord": {"lat": -1.2867, "lon": 36.8172}},
        "Kiribati": {"capital": "South Tarawa", "capital_coord": {"lat": 1.4510, "lon": 173.0305}},
        "Korea (North)": {"capital": "Pyongyang", "capital_coord": {"lat": 39.0194, "lon": 125.7385}},
        "Korea (South)": {"capital": "Seoul", "capital_coord": {"lat": 37.5665, "lon": 126.9780}},
        "Kuwait": {"capital": "Kuwait City", "capital_coord": {"lat": 29.3759, "lon": 47.9774}},
        "Kyrgyzstan": {"capital": "Bishkek", "capital_coord": {"lat": 42.8746, "lon": 74.6122}},
        "Laos": {"capital": "Vientiane", "capital_coord": {"lat": 17.9757, "lon": 102.6331}},
        "Latvia": {"capital": "Riga", "capital_coord": {"lat": 56.946, "lon": 24.1059}},
        "Lebanon": {"capital": "Beirut", "capital_coord": {"lat": 33.8886, "lon": 35.4955}},
        "Lesotho": {"capital": "Maseru", "capital_coord": {"lat": -29.314, "lon": 27.4932}},
        "Liberia": {"capital": "Monrovia", "capital_coord": {"lat": 6.2906, "lon": -9.4295}},
        "Libya": {"capital": "Tripoli", "capital_coord": {"lat": 32.8872, "lon": 13.1913}},
        "Liechtenstein": {"capital": "Vaduz", "capital_coord": {"lat": 47.1415, "lon": 9.5215}},
        "Lithuania": {"capital": "Vilnius", "capital_coord": {"lat": 54.6892, "lon": 25.2798}},
        "Luxembourg": {"capital": "Luxembourg City", "capital_coord": {"lat": 49.6117, "lon": 6.13}},
        "Madagascar": {"capital": "Antananarivo", "capital_coord": {"lat": -18.8792, "lon": 47.5079}},
        "Malawi": {"capital": "Lilongwe", "capital_coord": {"lat": -13.978, "lon": 33.7825}},
        "Malaysia": {"capital": "Kuala Lumpur", "capital_coord": {"lat": 3.139, "lon": 101.6869}},
        "Maldives": {"capital": "Malé", "capital_coord": {"lat": 4.1755, "lon": 73.5093}},
        "Mali": {"capital": "Bamako", "capital_coord": {"lat": 12.6392, "lon": -8.0029}},
        "Malta": {"capital": "Valletta", "capital_coord": {"lat": 35.8997, "lon": 14.5147}},
        "Marshall Islands": {"capital": "Majuro", "capital_coord": {"lat": 7.1315, "lon": 171.1947}},
        "Mauritania": {"capital": "Nouakchott", "capital_coord": {"lat": 18.0745, "lon": -15.9812}},
        "Mauritius": {"capital": "Port Louis", "capital_coord": {"lat": -20.1603, "lon": 57.4971}},
        "Mexico": {"capital": "Mexico City", "capital_coord": {"lat": 19.4326, "lon": -99.1332}},
        "Micronesia": {"capital": "Palikir", "capital_coord": {"lat": 6.9167, "lon": 158.1496}},
        "Moldova": {"capital": "Chisinau", "capital_coord": {"lat": 47.0105, "lon": 28.8638}},
        "Monaco": {"capital": "Monaco", "capital_coord": {"lat": 43.7333, "lon": 7.4167}},
        "Mongolia": {"capital": "Ulaanbaatar", "capital_coord": {"lat": 47.8860, "lon": 106.9057}},
        "Montenegro": {"capital": "Podgorica", "capital_coord": {"lat": 42.4411, "lon": 19.2636}},
        "Morocco": {"capital": "Rabat", "capital_coord": {"lat": 34.0206, "lon": -6.8416}},
        "Mozambique": {"capital": "Maputo", "capital_coord": {"lat": -25.9653, "lon": 32.5892}},
        "Myanmar": {"capital": "Naypyidaw", "capital_coord": {"lat": 19.7633, "lon": 96.0785}},
        "Namibia": {"capital": "Windhoek", "capital_coord": {"lat": -22.5597, "lon": 17.0836}},
        "Nauru": {"capital": "Yaren", "capital_coord": {"lat": -0.5477, "lon": 166.9205}},
        "Nepal": {"capital": "Kathmandu", "capital_coord": {"lat": 27.7172, "lon": 85.3240}},
        "Netherlands": {"capital": "Amsterdam", "capital_coord": {"lat": 52.3676, "lon": 4.9041}},
        "New Zealand": {"capital": "Wellington", "capital_coord": {"lat": -41.2867, "lon": 174.7751}},
        "Nicaragua": {"capital": "Managua", "capital_coord": {"lat": 12.1364, "lon": -86.2514}},
        "Niger": {"capital": "Niamey", "capital_coord": {"lat": 13.5123, "lon": 2.1128}},
        "Nigeria": {"capital": "Abuja", "capital_coord": {"lat": 9.0575, "lon": 7.4951}},
        "North Macedonia": {"capital": "Skopje", "capital_coord": {"lat": 41.9981, "lon": 21.4254}},
        "Norway": {"capital": "Oslo", "capital_coord": {"lat": 59.9127, "lon": 10.7461}},
        "Oman": {"capital": "Muscat", "capital_coord": {"lat": 23.5880, "lon": 58.3829}},
        "Pakistan": {"capital": "Islamabad", "capital_coord": {"lat": 33.6844, "lon": 73.0479}},
        "Palau": {"capital": "Ngerulmud", "capital_coord": {"lat": 7.5000, "lon": 134.6217}},
        "Panama": {"capital": "Panama City", "capital_coord": {"lat": 8.9833, "lon": -79.5167}},
        "Papua New Guinea": {"capital": "Port Moresby", "capital_coord": {"lat": -9.4438, "lon": 147.1803}},
        "Paraguay": {"capital": "Asunción", "capital_coord": {"lat": -25.2637, "lon": -57.5759}},
        "Peru": {"capital": "Lima", "capital_coord": {"lat": -12.0464, "lon": -77.0428}},
        "Philippines": {"capital": "Manila", "capital_coord": {"lat": 14.5995, "lon": 120.9842}},
        "Poland": {"capital": "Warsaw", "capital_coord": {"lat": 52.2298, "lon": 21.0118}},
        "Portugal": {"capital": "Lisbon", "capital_coord": {"lat": 38.7169, "lon": -9.1395}},
        "Qatar": {"capital": "Doha", "capital_coord": {"lat": 25.276987, "lon": 51.520008}},
        "Romania": {"capital": "Bucharest", "capital_coord": {"lat": 44.4268, "lon": 26.1025}},
        "Russia": {"capital": "Moscow", "capital_coord": {"lat": 55.7558, "lon": 37.6173}},
        "Rwanda": {"capital": "Kigali", "capital_coord": {"lat": -1.9403, "lon": 30.0602}},
        "Saint Kitts and Nevis": {"capital": "Basseterre", "capital_coord": {"lat": 17.3026, "lon": -62.7177}},
        "Saint Lucia": {"capital": "Castries", "capital_coord": {"lat": 13.9897, "lon": -61.9881}},
        "Saint Vincent and the Grenadines": {"capital": "Kingstown", "capital_coord": {"lat": 13.1533, "lon": -61.2248}},
        "Samoa": {"capital": "Apia", "capital_coord": {"lat": -13.8342, "lon": -172.0842}},
        "San Marino": {"capital": "San Marino", "capital_coord": {"lat": 43.9333, "lon": 12.45}},
        "Sao Tome and Principe": {"capital": "São Tomé", "capital_coord": {"lat": 0.3364, "lon": 6.7272}},
        "Saudi Arabia": {"capital": "Riyadh", "capital_coord": {"lat": 24.7136, "lon": 46.6753}},
        "Senegal": {"capital": "Dakar", "capital_coord": {"lat": 14.6928, "lon": -17.4467}},
        "Serbia": {"capital": "Belgrade", "capital_coord": {"lat": 44.8176, "lon": 20.4633}},
        "Seychelles": {"capital": "Victoria", "capital_coord": {"lat": -4.6167, "lon": 55.4547}},
        "Sierra Leone": {"capital": "Freetown", "capital_coord": {"lat": 8.4657, "lon": -13.2317}},
        "Singapore": {"capital": "Singapore", "capital_coord": {"lat": 1.2903, "lon": 103.8519}},
        "Slovakia": {"capital": "Bratislava", "capital_coord": {"lat": 48.1482, "lon": 17.1067}},
        "Slovenia": {"capital": "Ljubljana", "capital_coord": {"lat": 46.0511, "lon": 14.5051}},
        "Solomon Islands": {"capital": "Honiara", "capital_coord": {"lat": -9.4333, "lon": 159.9522}},
        "Somalia": {"capital": "Mogadishu", "capital_coord": {"lat": 2.0469, "lon": 45.3182}},
        "South Africa": {"capital": "Pretoria", "capital_coord": {"lat": -25.7461, "lon": 28.1881}},
        "South Sudan": {"capital": "Juba", "capital_coord": {"lat": 4.8594, "lon": 31.5713}},
        "Spain": {"capital": "Madrid", "capital_coord": {"lat": 40.4168, "lon": -3.7038}},
        "Sri Lanka": {"capital": "Colombo", "capital_coord": {"lat": 6.9271, "lon": 79.8612}},
        "Sudan": {"capital": "Khartoum", "capital_coord": {"lat": 15.5007, "lon": 32.5599}},
        "Suriname": {"capital": "Paramaribo", "capital_coord": {"lat": 5.8667, "lon": -55.1667}},
        "Sweden": {"capital": "Stockholm", "capital_coord": {"lat": 59.3293, "lon": 18.0686}},
        "Switzerland": {"capital": "Bern", "capital_coord": {"lat": 46.9481, "lon": 7.4474}},
        "Syria": {"capital": "Damascus", "capital_coord": {"lat": 33.5138, "lon": 36.2765}},
        "Taiwan": {"capital": "Taipei", "capital_coord": {"lat": 25.0330, "lon": 121.5654}},
        "Tajikistan": {"capital": "Dushanbe", "capital_coord": {"lat": 38.5598, "lon": 68.7870}},
        "Tanzania": {"capital": "Dodoma", "capital_coord": {"lat": -6.1659, "lon": 35.7516}},
        "Thailand": {"capital": "Bangkok", "capital_coord": {"lat": 13.7563, "lon": 100.5018}},
        "Timor-Leste": {"capital": "Dili", "capital_coord": {"lat": -8.5560, "lon": 125.6022}},
        "Togo": {"capital": "Lomé", "capital_coord": {"lat": 6.1375, "lon": 1.2125}},
        "Tonga": {"capital": "Nukuʻalofa", "capital_coord": {"lat": -21.1375, "lon": -175.2000}},
        "Trinidad and Tobago": {"capital": "Port of Spain", "capital_coord": {"lat": 10.6515, "lon": -61.2235}},
        "Tunisia": {"capital": "Tunis", "capital_coord": {"lat": 36.7982, "lon": 10.1585}},
        "Turkey": {"capital": "Ankara", "capital_coord": {"lat": 39.9334, "lon": 32.8597}},
        "Turkmenistan": {"capital": "Ashgabat", "capital_coord": {"lat": 37.9601, "lon": 58.3796}},
        "Tuvalu": {"capital": "Funafuti", "capital_coord": {"lat": -7.4813, "lon": 179.1940}},
        "Uganda": {"capital": "Kampala", "capital_coord": {"lat": 0.3136, "lon": 32.5811}},
        "Ukraine": {"capital": "Kyiv", "capital_coord": {"lat": 50.4501, "lon": 30.5031}},
        "United Arab Emirates": {"capital": "Abu Dhabi", "capital_coord": {"lat": 24.4539, "lon": 54.3773}},
        "United Kingdom": {"capital": "London", "capital_coord": {"lat": 51.5074, "lon": -0.1278}},
        "United States": {"capital": "Washington, D.C.", "countriescapital_coord": {"lat": 38.8954, "lon": -77.0365}},
        "Uruguay": {"capital": "Montevideo", "capital_coord": {"lat": -34.9011, "lon": -56.1645}},
        "Uzbekistan": {"capital": "Tashkent", "capital_coord": {"lat": 41.2995, "lon": 69.2401}},
        "Vanuatu": {"capital": "Port Vila", "capital_coord": {"lat": -17.7333, "lon": 168.3167}},
        "Vatican City": {"capital": "Vatican City", "capital_coord": {"lat": 41.9029, "lon": 12.4534}},
        "Venezuela": {"capital": "Caracas", "capital_coord": {"lat": 10.4880, "lon": -66.8792}},
        "Vietnam": {"capital": "Hanoi", "capital_coord": {"lat": 21.0285, "lon": 105.8542}},
        "Yemen": {"capital": "Sana'a", "capital_coord": {"lat": 15.3694, "lon": 44.1910}},
        "Zambia": {"capital": "Lusaka", "capital_coord": {"lat": -15.3875, "lon": 28.3228}},
        "Zimbabwe": {"capital": "Harare", "capital_coord": {"lat": -17.8292, "lon": 31.0522}}}

        '''
        Description: Gets the Countries
        Parameters: N\A
        Returns: List of Countries
        '''
        @staticmethod
        def get_countries():
            return list(World.Countries.__countries.keys())
        
        '''
        Description: Gets the Capital of the Country provided
        Parameters: Name of the Country to get capital for
        Returns: String entry for capital, returns None if it cannot get the capital
        '''
        @staticmethod
        def get_country_capital(country):
            country_capital = World.Countries.__countries.get(country)["capital"]

            # Make sure that entry was pulled
            if not country_capital:
                print(f"[ERROR]: {country} not found...")
            else:
                return country_capital
        
        '''
        Description: Gets the coordinates for the capital 
        Parameters: Name of the country to get capital coordinates for
        Returns: dictionary entry for the coordinates
        '''
        @staticmethod
        def get_country_capital_coord(country):
            coord = World.Countries.__countries.get(country)["capital_coord"]
            if not coord:
                print(f"[ERROR]: {country} not found...")
            else:
                return coord