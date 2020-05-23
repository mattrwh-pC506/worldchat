from functools import wraps, lru_cache
from typing import Dict, List
import json

import requests
from requests import Request, Response
from django.http import HttpRequest
from django.conf import settings


class GeolocationClient:
    API_KEY = settings.GOOGLE_API_KEY
    url = "https://maps.googleapis.com/maps/api/geocode/json"

    @lru_cache(maxsize=1000)
    def get_address(latlng: str) -> Request: 
        client = GeolocationClient 
        querystring = { "latlng": latlng, "key": GeolocationClient.API_KEY }
        return requests.request("GET", client.url, params=querystring) 

    @lru_cache(maxsize=1000)
    def get_latlng(address: str) -> Request: 
        client = GeolocationClient
        querystring = { "address": address, "key": GeolocationClient.API_KEY }
        return requests.request("GET", client.url, params=querystring) 

def find_neighborhood(results: List) -> str:
    next(result for result in results if result.get("data"))

def latlng_to_address_lookup(view):
    @wraps(view)
    def wrapper(request: HttpRequest, latlng, *args, **kwargs):
        response: Response = GeolocationClient.get_address(latlng)
        results: List = json.loads(response.content).get("results", [])
        first_match = results[0].get("formatted_address")
        return view(request, *args, address=first_match, **kwargs)

    return wrapper

def address_to_latlng_lookup(view):
    @wraps(view)
    def wrapper(request: HttpRequest, address, *args, **kwargs):
        response: Response = GeolocationClient.get_latlng(address)
        results: List = json.loads(response.content).get("results", [])
        print ("RESULTS", results)
        first_match = results[0].get("geometry", {}).get("location", {})
        latlng = "{},{}".format(first_match.get("lat"), first_match.get("lng"))
        return view(request, *args, latlng=latlng, **kwargs)

    return wrapper
