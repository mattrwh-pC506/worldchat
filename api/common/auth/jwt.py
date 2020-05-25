from typing import Callable, Any
from functools import wraps
from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.conf import settings
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import authenticate
import jwt

from exception_handling.exceptions.auth import UserDoesNotExist, IncorrectPassword

JWT_SECRET = settings.JWT_SECRET
JWT_ALGORITHM = settings.JWT_ALGORITHM
JWT_EXP_DELTA_SECONDS = settings.JWT_EXP_DELTA_SECONDS

def when_authenticated(view: Callable):
    @wraps(view)
    def wrapper(request: HttpRequest, *args, **kwargs) -> HttpResponse:
        request.user = None
        authorization = request.headers.get('Authorization', None)
        remove_token = 'Bearer '
        jwt_token = authorization[len(remove_token):]
        if jwt_token:
            payload = jwt.decode(jwt_token, JWT_SECRET,
                                 algorithms=[JWT_ALGORITHM])

            username = payload.get('username') 
            request.user = User.objects.filter(username=username).first()
            if not request.user:
                raise UserDoesNotExist(username)

        if request.user:
            return view(request, *args, **kwargs)
        else:
            return HttpResponse('Unauthorized', status=401)

    return wrapper

def build_jwt_token(username: str, exp: Any):
    payload = { 'username': username, 'exp': exp }
    return jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)

def jwt_authenticate(username='', password='') -> (User, str):
    if not User.objects.filter(username=username).first():
        raise UserDoesNotExist(username)
    authenticated_user = authenticate(username=username, password=password)
    if not authenticated_user:
        raise IncorrectPassword("{} submitted incorrect password".format(username))
    else:
        exp = datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
        token = build_jwt_token(username, exp)
        return authenticated_user, token 

