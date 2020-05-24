import math
from  typing import List

from django.forms.models import model_to_dict
from django.contrib.auth.models import User

from chat.models import Chatter

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


def add_distance_to_chatter(user: User) -> Chatter:
    def add_to_chatter(friend_chat_profile: Chatter) -> Chatter:
        user_chat_profile = Chatter.objects.get(user=user)
        user_latlng = user_chat_profile.geocode.split(",")
        friend_latlng = friend_chat_profile.geocode.split(",")
        matrix = [[float(user_latlng[0]), float(friend_latlng[0])], [float(user_latlng[1]), float(friend_latlng[1])]]
        distance = calculate_distance_in_miles(matrix)
        chatter = { **model_to_dict(friend_chat_profile), "distance": distance, "username": 
                friend_chat_profile.user.username }
        return chatter
    return add_to_chatter
