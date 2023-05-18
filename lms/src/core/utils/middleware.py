import datetime


class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Before view")
        setattr(request, "current_time", datetime.datetime.now())
        response = self.get_response(request)
        print("After view")

        return response
