import json
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpRequest, JsonResponse, Http404
from django.forms.models import model_to_dict

from common.utils.distance import add_distance_to_chatter
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
    chatters = Chatter.objects.filter(online=True).all()
    chatters = map(add_distance_to_chatter(request.user), chatters)
    return JsonResponse({ "chatters": list(chatters) })

