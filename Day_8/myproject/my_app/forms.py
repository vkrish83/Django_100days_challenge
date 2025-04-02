from django import forms

class GreetingForm(forms.Form):
    username = forms.CharField(label="Enter your name", max_length=100)