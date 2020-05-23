from typing import Callable, List
from functools import wraps

from django.http import HttpRequest

from exception_handling.exceptions.http import MethodNotSupported

def supported_methods(*methods: List[str]):
    def view_wrapper(view: Callable):
        @wraps(view)
        def wrapper(request: HttpRequest, *args, **kwargs):
            if request.method not in methods:
                raise MethodNotSupported(request.method)
            else:
                return view(request, *args, **kwargs)
        return wrapper
    return view_wrapper
