from django.http import HttpResponse


# Create your views here.
def get_health(_) -> HttpResponse:
    return HttpResponse('Server is fine', status=200)
