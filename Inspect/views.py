from django.http import HttpResponse

from BaseAsyncClassView import AsyncView


# Create your views here.
def get_health(_) -> HttpResponse:
    return HttpResponse('Server is fine', status=200)


class CheckAsync(AsyncView):
    async def get(self, _):
        return HttpResponse('Eto blyat` rabataet', status=200)
