from django.http import HttpResponse


def index(request):
    """
    Index page controller
    """
    return HttpResponse('Hello, World!')
