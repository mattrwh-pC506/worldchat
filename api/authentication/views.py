import json
from django.contrib.auth.models import User
from django.http import HttpRequest, JsonResponse
from django.forms.models import model_to_dict

from common.auth.jwt import jwt_authenticate, when_authenticated
from common.utils.http import supported_methods
from chat.models import Chatter
from exception_handling.exceptions.auth import UsernameTaken, UserDoesNotExist


@supported_methods("POST")
def login(request: HttpRequest) -> JsonResponse:
    body = json.loads(request.body.decode('utf-8'))
    username = body.get('username')
    password = body.get('password')
    user, token = jwt_authenticate(username=username, password=password)
    chatter = Chatter.objects.filter(user=user).first()
    if not chatter:
        raise UserDoesNotExist(username)
    return JsonResponse({ "chatter": model_to_dict(chatter), "token": token.decode("UTF-8") })

@supported_methods("POST")
def register(request: HttpRequest) -> JsonResponse:
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

@supported_methods("GET")
@when_authenticated
def ping(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"message": "logged in"})

@supported_methods("GET")
def username_available(request: HttpRequest, username: str) -> JsonResponse:
    user = User.objects.filter(username=username).first()
    if not user:
        return JsonResponse({"data": "{} is available".format(username) })

    raise UsernameTaken(username)
