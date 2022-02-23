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
    if request.method == "POST":
        user = request.POST.getlist('user')

        if 'u1' in user:
            print(searches["User1"])
        if 'u2' in user:
            print(searches["User2"])
        if 'u3' in user:
            print(searches["User3"])

    return render(request, 'filterPage.html', searches)
