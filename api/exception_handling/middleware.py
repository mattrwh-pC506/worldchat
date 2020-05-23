from typing import Callable
from django.http import HttpRequest, JsonResponse

from common.utils.safe_getattr import safe_getattr

class BaseExceptionHandler:
    def __init__(self, get_response: Callable):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        return self.get_response(request)

class ExceptionHandler(BaseExceptionHandler):
    def process_exception(self, request: HttpRequest, exception: Exception):
        status_code = safe_getattr(exception, "status_code")
        message = safe_getattr(exception, "message", exception.__class__.__name__)
        if status_code:
            return JsonResponse( { "message": message }, status=status_code)
        else:
            return JsonResponse( { "message": message }, status=400)


exception_handling_middleware = ('exception_handling.middleware.ExceptionHandler',)
