from django.urls import path
from .views import greet

urlpatterns = [
    path('greet/', greet, name="greet_default"),
    path('greet/<str:username>/', greet, name="greet_user")
]