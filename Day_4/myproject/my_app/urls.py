from django.urls import path
from .views import greet_user #, home_view

urlpatterns = [
    # path('', home_view, name='home'),
    path('greet/', greet_user, name="greet_default"),
    path('greet/<str:user_name>/', greet_user, name="greet_user")
]