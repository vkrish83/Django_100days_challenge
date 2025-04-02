from django.urls import path
from .views import greet, greet_form_view

urlpatterns = [
    path('greet/', greet, name='greet_default'),
     path('greet/<str:username>/', greet, name='greet_user'),
    path("greet-form/", greet_form_view, name="greet_form")
]