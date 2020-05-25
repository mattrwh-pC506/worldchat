from collections import namedtuple
from typing import Callable

import pytest
import requests

@pytest.fixture
def requests_response_factory() -> Callable:
    def initialize(content: str):
        MockResponse = namedtuple("MockResponse", ["content"])
        return MockResponse(content=content)
    return initialize

@pytest.fixture
def requests_factory(mocker, requests_response_factory) -> Callable:
    def initialize(return_value=None):
        mocked_requests = mocker.patch('requests.request')
        mocked_response = requests_response_factory(return_value)
        mocked_requests.return_value = mocked_response
    return initialize

@pytest.fixture
def mock_request_factory():
    class MockRequest:
        def __init__(self, method=None, body=None):
            self.method = method
            self.body = body

    def factory(method=None, body=None):
        body = body.encode("UTF-8") if body else b""
        return MockRequest(method=method, body=body)

    return factory
