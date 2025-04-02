from django.shortcuts import render
from datetime import datetime

def greet(request, username="Guest"):
    context = {
        "username": username,
        "current_time": datetime.now(),
        "fruits": ["Apple", "Banana", "Cherry"],
    }

    return render(request, "my_app/greeting.html", context)
