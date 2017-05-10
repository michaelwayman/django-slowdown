from time import sleep
from django.conf import settings


class SlowDownMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        try:
            delay = settings.SLOW_DOWN
        except AttributeError:
            delay = 0.5

        sleep(delay)
        return response
