import json

from django.http import HttpRequest, JsonResponse

from common.types.typedtuple import typed_tuple_to_dict
from locations.views import get_location, get_address_from_latlng, get_latlng_from_address

def test_get_location_from_ip(requests_factory, mock_ip_location_data):
    mock_ip_data, is_equal_to_mock_ip_data = mock_ip_location_data
    mock_response_data = typed_tuple_to_dict(mock_ip_data)
    mock_requests = requests_factory(json.dumps(mock_response_data))
    
    http_request = HttpRequest()
    http_request.method = "GET"
    response: JsonResponse = get_location(http_request, mock_ip_data.ip)
    print ("RESPONSE", response.content)
    assert is_equal_to_mock_ip_data(json.loads(response.content)["data"]) == True

def test_get_address_from_latlng(requests_factory, mock_location_data):
    mock_response_data = {"results": [{"formatted_address": mock_location_data.address}]}
    mock_requests = requests_factory(json.dumps(mock_response_data))
    
    http_request = HttpRequest()
    http_request.method = "GET"
    response: JsonResponse = get_address_from_latlng(http_request, mock_location_data.latlng)
    assert json.loads(response.content)["data"] == mock_location_data.address

def test_get_latlng_from_address(requests_factory, mock_location_data):
    lat, lng = mock_location_data.lat, mock_location_data.lng
    mock_response_data = {"results": [{"geometry": { "location": {"lat": lat, "lng": lng} }}]}
    mock_requests = requests_factory(json.dumps(mock_response_data))
    
    http_request = HttpRequest()
    http_request.method = "GET"
    response: JsonResponse = get_latlng_from_address(http_request, mock_location_data.address)
    expected_result = mock_response_data["results"][0]["geometry"]
    assert json.loads(response.content)["data"] == mock_location_data.latlng
