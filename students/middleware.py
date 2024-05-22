from functools import wraps
from django.http import HttpResponseServerError, HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin
from django.core.exceptions import PermissionDenied

class CustomExceptionMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        @wraps(self.get_response)
        def inner(request):
            try:
                response = self.get_response(request)
            except PermissionDenied:
                # Handle specific exception
                response = HttpResponseForbidden("Custom Permission Denied Message")
            except Exception as exc:
                # Handle other exceptions
                response = self.response_for_exception(request, exc)
            return response

        return inner(request)

    def response_for_exception(self, request, exception):
        # Your custom exception handling logic here
        return HttpResponseServerError(f"An error occurred: {exception}")
