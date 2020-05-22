import math

import requests
from django.shortcuts import render
from django.http import HttpRequest, JsonResponse

from common.types.typedtuple import typed_tuple_to_dict
from common.types.http import Response
from common.auth.jwt import when_authenticated
from common.utils.distance import calculate_distance_in_miles, build_matrix
from locations.clients.ipfinder import ip_lookup 
from locations.clients.geolocation import address_to_latlng_lookup, latlng_to_address_lookup
from locations.types.location import Location
from chat.models import Chatter

@ip_lookup
def get_location(request: HttpRequest, *args, location: Location = None, **kwargs) -> JsonResponse:
    return JsonResponse(typed_tuple_to_dict(Response(data=location)))

@address_to_latlng_lookup
def get_latlng_from_address(request: HttpRequest, *args, latlng: str = None, **kwargs) -> JsonResponse:
    print ("latlng", latlng)
    return JsonResponse(typed_tuple_to_dict(Response(data=latlng)))

@latlng_to_address_lookup
def get_address_from_latlng(request: HttpRequest, *args, address: str = None, **kwargs) -> JsonResponse:
    return JsonResponse(typed_tuple_to_dict(Response(data=address))) 

@when_authenticated
def calculate_distance_in_miles_from_friend(request: HttpRequest, friends_username): 
    user_chat_profile = Chatter.objects.get(user=request.user)
    friend_chat_profile = Chatter.objects.get(user__username=friends_username)
    matrix = build_matrix(user_chat_profile.geocode, friend_chat_profile.geocode)
    distance_in_miles = calculate_distance_in_miles(matrix)
    return JsonResponse(typed_tuple_to_dict(Response(data=distance_in_miles)))

