#map for class

class Dict_map:
    def __init__(self):
    
        self.lightning_map = {
            'Daylight: Street light present': 0,
            'Darkness: Street lights present and lit': 1,
            'Darkness: Street lighting unknown': 2,
            'Darkness: Street lights present but unlit': 3,
            'Darkeness: No street lighting': 4,
        }

        self.road_type_map = {
            'Single carriageway': 0,
            'Dual carriageway': 1,
            'Roundabout': 2,
            'One way street': 3,
            'Slip road': 4,
            'Unknown': 5,
        }

        self.junction_control_map = {
            'no_control': 0,
            'Giveway or uncontrolled': 1,
            'Automatic traffic signal': 2,
            'Stop Sign': 3,
            'Authorised person': 4,
        }

        self.pedestrian_physical_facilities_map = {
            'No physical crossing within 50 meters': 0,
            'Pedestrian phase at traffic signal junction': 1,
            'non-junction pedestrian crossing': 2,
            'Zebra crossing': 3,
            'Central refuge': 4,
            'Footbridge or subway': 5,
        }

        self.weather_map = {
            'Fine without high winds': 0,
            'Raining without high winds': 1,
            'Other': 2,
            'Unknown': 3,
            'Raining with high winds': 4,
            'Fine with high winds': 5,
            'Snowing without high winds': 6,
            'Fog or mist': 7,
            'Snowing with high winds': 8,
        }

        self.road_surface_map = {
            'Dry': 0,
            'Wet/Damp': 1,
            'Frost/Ice': 2,
            'Snow': 3,
            'Flood (Over 3cm of water)': 4,
            'Normal': 5,
        }

        self.police_attend_map = {
            'No': 0,
            'Yes': 1,
        }


        self.column_maps = {
            "Road_Type": self.road_type_map,
            "Junction_Control": self.junction_control_map,
            "Pedestrian_Crossing-Physical_Facilities": self.pedestrian_physical_facilities_map,
            "Light_Conditions": self.lightning_map,
            "Weather_Conditions": self.weather_map,
            "Road_Surface_Conditions": self.road_surface_map,
            "Did_Police_Officer_Attend_Scene_of_Accident": self.police_attend_map,
        }
