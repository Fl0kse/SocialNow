from Profile import views
from django.urls import path


urlpatterns = [
    path('test/', views.test)
]