from functools import wraps, lru_cache
import json

import requests
from requests import Request
from django.http import HttpRequest
from django.conf import settings

from locations.types.location import locationFactory, Location


class IPFinderClient:
    url = "https://ip-geo-location.p.rapidapi.com/ip/{}"
    querystring = {"format":"json"}
    headers = {
        'x-rapidapi-host': "ip-geo-location.p.rapidapi.com",
        'x-rapidapi-key': settings.RAPIDAPI_KEY
        }

    @lru_cache(maxsize=1000)
    def get(ip: str) -> Request:
        client = IPFinderClient
        return requests.request("GET", 
                client.url.format(ip), 
                headers=client.headers, 
                params=client.querystring) 

def get_location(ip: str) -> str:
    return IPFinderClient.get(ip).content

def ip_lookup(view):
    @wraps(view)
    def wrapper(request: HttpRequest, ip, *args, **kwargs):
        location: str = get_location(ip)
        location: Dict = json.loads(location)
        location: Location = locationFactory(location)
        return view(request, *args, location=location, **kwargs)

    return wrapper
