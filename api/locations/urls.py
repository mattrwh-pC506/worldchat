from django.urls import path

from locations.views import (get_location, get_latlng_from_address, 
        get_address_from_latlng, calculate_distance_in_miles_from_friend)

urlpatterns = [
    path('lookup/ip/<ip>', get_location, name='get_location'),
    path('lookup/address/<latlng>', get_address_from_latlng, name='get_address_from_latlng'),
    path('lookup/latlng/<address>', get_latlng_from_address, name='get_latlng_from_address'),
    path('lookup/distanceFromFriend/<friends_username>', 
        calculate_distance_in_miles_from_friend, name='calculate_distance_in_miles_from_friend'),
]
