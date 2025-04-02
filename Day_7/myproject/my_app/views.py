from django.shortcuts import render
from datetime import datetime

def greet(request, username="Guest"):
    favourite_languages = ['Python', 'Javascript', 'Django', 'SQL']

    return render(request, "my_app/greeting.html", {
        "username": username,
        "languages": favourite_languages
    })
