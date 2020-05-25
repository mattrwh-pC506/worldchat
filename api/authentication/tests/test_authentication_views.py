import json

from django.http import HttpRequest, JsonResponse
from django.forms.models import model_to_dict
from django.conf import settings

from authentication.views import login, register, username_available 

def test_login(sample_user, sample_chatter, mock_request_factory, fake_password):
    body = json.dumps({"username": sample_user.username, "password": fake_password})
    request = mock_request_factory(method="POST", body=body)
    response = login(request)
    chatter = json.loads(response.content)["chatter"]
    assert chatter == model_to_dict(sample_chatter)
    assert chatter["user"] == sample_user.id

def test_register(sample_user, sample_chatter, mock_request_factory, fake_password):
    new_username = sample_user.username + "_new"
    body = json.dumps({
        "username": new_username, 
        "password": fake_password, 
        "email": sample_user.email,
        "usertag": sample_chatter.usertag,
        "geocode": sample_chatter.geocode,
        "address": sample_chatter.address,
        })
    request = mock_request_factory(method="POST", body=body)
    response = register(request)
    chatter = json.loads(response.content)["chatter"]
    assert chatter["user"] == 2
    assert chatter["usertag"] == sample_chatter.usertag
    assert chatter["geocode"] == sample_chatter.geocode
    assert chatter["address"] == sample_chatter.address

def test_username_is_available(sample_user, sample_chatter, mock_request_factory):
    new_username = sample_user.username + "_new"
    request = mock_request_factory(method="GET")
    response = username_available(request, new_username)
    data = json.loads(response.content)["data"]
    assert data == "{} is available".format(new_username)
