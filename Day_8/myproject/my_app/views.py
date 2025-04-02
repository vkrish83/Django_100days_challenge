from django.shortcuts import render
from django.http import HttpResponse
from .forms import GreetingForm

def greet(request, username="Guest"):
    return HttpResponse(f'Hello, {username}!')

def greet_form_view(request):
    form = GreetingForm(request.GET or None)

    if request.method == "POST":
        form = GreetingForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            return render(request, "my_app/greet.html", {"username": username})
        
    username = request.GET.get('username')
    if username:
        return render(request, "my_app/greet.html", {"username": username})

    return render(request, "my_app/greet_form.html", {"form": form})
