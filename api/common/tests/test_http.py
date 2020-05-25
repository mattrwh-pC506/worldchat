from typing import Any, List

from django.http import HttpRequest
import pytest

from common.utils.http import supported_methods
from exception_handling.exceptions.http import MethodNotSupported

methods = ('GET', 'DELETE', 'PUT', 'POST',)

def view_factory(*methods):
    @supported_methods(*methods)
    def view(request: HttpRequest) -> Any:
        pass
    return view

def rotate_methods(methods: List[str]):
    return [*methods[1:], *methods[0:1]] 

def methods_without_test_case(methods: List[str], remove_method: str):
    return [method for method in methods if method != remove_method]

def assert_supported_methods_work(method: str, excepted_methods: List[str]):
    try:
        request = HttpRequest()
        request.method = method
        view_factory(*excepted_methods)(request)
    except MethodNotSupported:
        pytest.fail("Unexpected MethodNotSupported ..")

def assert_supported_methods_throw_exception_when_needed(method: str):
    with pytest.raises(MethodNotSupported):
        request = HttpRequest()
        request.method = method 
        view_factory(methods_without_test_case(methods, method))(request)

def test_supported_methods_does_not_throw_error_when_supported_methods_passed():
    for i in range(len(methods) - 1):
        test_methods = [method for method in methods]
        for j in range(len(methods) - 1):
            assert_supported_methods_work(methods[i], test_methods)
            test_methods = rotate_methods(test_methods)

def test_supported_methods_throws_error_when_supported_methods_passed(): 
    for i in range(len(methods) - 1):
        assert_supported_methods_throw_exception_when_needed(methods[i])
