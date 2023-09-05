from django.http import HttpResponseForbidden


class MediaAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/media/'):
            if request.user.is_authenticated:
                if request.path.endswith(request.user.image.name) or request.user.is_superuser:
                    pass
                else:
                    return HttpResponseForbidden("Access denied to this media file")
        response = self.get_response(request)
        return response
