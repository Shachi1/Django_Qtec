from re import search
from django.shortcuts import render
from django.http import HttpResponse
# from testapp.models import User


# Create your views here.

def filter_history(request):
    searches = {
        "User1": "what is django",
        "User2": "django stack overflow",
        "User3": "what is ajax"
    }
    if request.method == "POST":
        user = request.POST.getlist('user')
        # u1, u2, u3 = user
        # User.objects.create(
        #     u1=u1
        #     u2=u2
        #     u3=u3
        # )

        if 'u1' in user:
            print(searches["User1"])
        if 'u2' in user:
            print(searches["User2"])
        if 'u3' in user:
            print(searches["User3"])

    return render(request, 'filterPage.html', searches)
