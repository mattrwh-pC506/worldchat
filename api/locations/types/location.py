from typing import Dict
from common.types.typedtuple import TypedTuple

Area = TypedTuple("Area", ["code", "name"])
City = TypedTuple("City", ["name", "population", "geonameid"])
Continent = TypedTuple("Continent", ["name"])
Country = TypedTuple("Country", ["area_size", "capital", "code", "name", "population"])
Security = TypedTuple("Security", ["is_crawler", "is_proxy", "is_tor"]) 
Geolocation = TypedTuple("Geolocation", ["latitude", "longitude", ]) 
Location = TypedTuple("Location", [
    "ip", "postcode", "status", "type", 
    "area", "city", "continent", "country", "geolocation", "security"
    ])

def locationFactory(location: Dict) -> Location:
    return Location(
            ip=location.get("ip"),
            postcode=location.get("postcode"),
            status=location.get("status"),
            type=location.get("type"),
            area=Area(**location.get("area", {})),
            city=City(**location.get("city", {})),
            continent=Continent(**location.get("continent", {})),
            country=Country(**location.get("country", {})),
            geolocation=Geolocation(**location.get("location", {})),
            security=Security(**location.get("security", {})),
            )
