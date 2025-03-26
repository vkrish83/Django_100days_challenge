from django.shortcuts import render
from django.http import HttpResponse

# def home_view(request):
#     return HttpResponse("Welcome to Day 4 of Django Challenge!")

def greet_user(request, user_name="Guest"):
    return render(request, 'greeting.html', {'username': user_name.capitalize()})
