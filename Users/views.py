from django.http import JsonResponse


# Create your views here.
def test(request, user_id: str) -> JsonResponse:
    return JsonResponse(data={'user_if': user_id}, safe=False)
