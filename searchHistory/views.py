from re import search
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def say_hello(request):
    searches = {
        "User1": "what is django",
        "User2": "django stack overflow",
        "User3": "what is ajax"
    }
    return render(request, 'filterPage.html', searches)
