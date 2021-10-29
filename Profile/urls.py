from Profile import views
from django.urls import path


urlpatterns = [
    path('info/', views.GetProfileInfo.as_view())
]