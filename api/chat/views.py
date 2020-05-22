import json
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpRequest, JsonResponse, Http404
from django.forms.models import model_to_dict

from common.utils.distance import calculate_distance_in_miles
from common.auth.jwt import jwt_authenticate, when_authenticated
from chat.models import Chatter


def index(request: HttpRequest):
    return render(request, 'chat/index.html', {})

def room(request: HttpRequest, conversation: str):
    return render(request, 'chat/room.html', {'conversation': conversation})

def login(request: HttpRequest) -> JsonResponse:
    if request.method == "POST":
        body = json.loads(request.body.decode('utf-8'))
        username = body.get('username')
        password = body.get('password')
        user, token = jwt_authenticate(username=username, password=password)
        chatter = Chatter.objects.get(user=user)
        return JsonResponse({ "chatter": model_to_dict(chatter), "token": token.decode("UTF-8") })
    else:
        return Http404()

def register(request: HttpRequest) -> JsonResponse:
    if request.method == "POST":
        body = json.loads(request.body.decode('utf-8'))
        username = body.get('username')
        email = body.get('email')
        password = body.get('password')
        usertag = body.get('usertag')
        geocode = body.get('geocode')
        address = body.get('address')
        
        user = User.objects.create_user(username, email, password)
        user.save()

        chatter = Chatter(user=user, usertag=usertag, geocode=geocode, address=address)
        chatter.save()
        
        user, token = jwt_authenticate(username=username, password=password)
        
        return JsonResponse({ "chatter": { "username": username, **model_to_dict(chatter) }, "token": token.decode("UTF-8") })
    else:
        return Http404()

@when_authenticated
def get_chatter_user(request: HttpRequest) -> JsonResponse:
    if request.method == 'GET':
        chatter = Chatter.objects.get(user=request.user)
        return JsonResponse({ "chatter": { **model_to_dict(chatter), "username": chatter.user.username} })
    else:
        return Http404()

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

@when_authenticated
def get_chatters(request: HttpRequest) -> JsonResponse:
    if request.method == 'GET':
        chatters = Chatter.objects.filter(online=True).all()
        chatters = map(enrich_user_data(request), chatters)
        return JsonResponse({ "chatters": list(chatters) })
    else:
        return Http404()

@when_authenticated
def ping(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"message": "logged in"})
