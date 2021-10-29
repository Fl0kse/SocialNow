from asgiref.sync import sync_to_async
from django.http import JsonResponse
from BaseAsyncClassView import AsyncView
from util.auth import authenticated
from Profile.models import Profile


# Create your views here.
class GetProfileInfo(AsyncView):
    # @authenticated
    @sync_to_async
    def get(self, request) -> JsonResponse:
        user_id = 1
        profile = Profile.objects.get(id=user_id)
        data = {"user_name": profile.user_name,
                "email": profile.email}
        return JsonResponse(data=data, safe=False)
