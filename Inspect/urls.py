from Inspect import views
from django.urls import path


urlpatterns = [
    path('get_health/', views.get_health)
]