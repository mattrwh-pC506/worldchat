import math
from  typing import List

def build_matrix(source: str, target: str) -> List[List[str]]:
    source_latlng = source.split(",")
    target_latlng = target.split(",")
    return [[float(source_latlng[0]), float(target_latlng[0])], [float(source_latlng[1]), float(target_latlng[1])]]

def calculate_distance_in_miles(matrix: List[List[int]]):
    miles_conversion = 0.621371
    R = 6372800  # Earth radius in meters
    lat1 = matrix[0][0]
    lat2 = matrix[0][1]
    lng1 = matrix[1][0]
    lng2 = matrix[1][1]
    
    phi1, phi2 = math.radians(lat1), math.radians(lat2) 
    dphi       = math.radians(lat2 - lat1)
    dlambda    = math.radians(lng2 - lng1)
    
    a = math.sin(dphi/2)**2 + \
        math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    
    distance_in_m =  2*R*math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance_in_km = distance_in_m / 1000
    return str(round(distance_in_km * miles_conversion, 2))
