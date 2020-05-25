from typing import Dict
from collections import namedtuple

import pytest

from common.types.typedtuple import typed_tuple_to_dict

@pytest.fixture
def mock_location_data():
    MockLocationData = namedtuple("MockedLocationData", ["address", "latlng", "lat", "lng"])
    MockIpLocationData = namedtuple("MockIpLocationData", [
            "ip",
            "postcode",
            "status",
            "type",
            "area",
            "city",
            "continent",
            "country",
            "location",
            "security",
        ])

    return MockLocationData(
            address="55 Road St, City, State, 99999", 
            latlng="10,-10", lat="10", lng="-10")

@pytest.fixture
def mock_ip_location_data():
    MockIpLocationData = namedtuple("MockIpLocationData", [
            "ip",
            "postcode",
            "status",
            "type",
            "area",
            "city",
            "continent",
            "country",
            "location",
            "security",
        ])

    ip_data = MockIpLocationData(
            ip="1", 
            postcode="2", 
            status="3", 
            type="4", 
            area={"code": "5", "name": "6"},
            city={"name": "7", "population": "8", "geonameid": "9"},
            continent={"name": "10"},
            country={"area_size": "11", "capital": "12", "code": "13", "name": "14", "population": "15"},
            location={"latitude": "16", "longitude": "17"},
            security={"is_crawler": "18", "is_proxy": "19", "is_tor": "20"},
            )

    def is_equal_to_mock_ip_data(data: Dict) -> bool:
        return ip_data.ip == data["ip"] \
            and ip_data.postcode == data["postcode"] \
            and ip_data.status == data["status"] \
            and ip_data.type == data["type"] \
            and typed_tuple_to_dict(ip_data.area) == data["area"] \
            and typed_tuple_to_dict(ip_data.city) == data["city"] \
            and typed_tuple_to_dict(ip_data.continent) == data["continent"] \
            and typed_tuple_to_dict(ip_data.country) == data["country"] \
            and typed_tuple_to_dict(ip_data.location) == data["geolocation"] \
            and typed_tuple_to_dict(ip_data.security) == data["security"]


    return ip_data, is_equal_to_mock_ip_data
