from django.http import HttpResponseForbidden


class AuthorizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            denied_routes = ['/book/create/', '/book/update/', '/book/delete/',
                             '/group/create/', '/group/update/', '/group/delete/',
                             '/book/borrows/', '/book/late-loans/']
            if request.user.role == 'client_role' and request.path in denied_routes:
                return HttpResponseForbidden()
        response = self.get_response(request)
        return response
