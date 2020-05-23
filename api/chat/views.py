import json
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpRequest, JsonResponse, Http404
from django.forms.models import model_to_dict

from common.utils.distance import calculate_distance_in_miles
from common.utils.http import supported_methods
from common.auth.jwt import jwt_authenticate, when_authenticated
from chat.models import Chatter

@supported_methods("GET")
@when_authenticated
def get_chatter_user(request: HttpRequest) -> JsonResponse:
    chatter = Chatter.objects.get(user=request.user)
    return JsonResponse({ "chatter": { **model_to_dict(chatter), "username": chatter.user.username} })

@supported_methods("GET")
@when_authenticated
def get_chatters(request: HttpRequest) -> JsonResponse:
    def enrich_user_data(request: HttpRequest):
        def mapper(friend_chat_profile: Chatter) -> Chatter:
            user_chat_profile = Chatter.objects.get(user=request.user)
            user_latlng = user_chat_profile.geocode.split(",")
            friend_latlng = friend_chat_profile.geocode.split(",")
            matrix = [[float(user_latlng[0]), float(friend_latlng[0])], [float(user_latlng[1]), float(friend_latlng[1])]]
            distance = calculate_distance_in_miles(matrix)
            chatter = { **model_to_dict(friend_chat_profile), "distance": distance, "username": 
                    friend_chat_profile.user.username }
            return chatter
        return mapper

    chatters = Chatter.objects.filter(online=True).all()
    chatters = map(enrich_user_data(request), chatters)
    return JsonResponse({ "chatters": list(chatters) })

