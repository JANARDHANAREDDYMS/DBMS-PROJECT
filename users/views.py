from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from flights.views import flight,book
from flights.models import Flight,Passenger,Airport
# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return render(request,"flights/index.html",{
        "flights": Flight.objects.all()
    })
    #     return HttpResponseRedirect(reverse("login"))

    # return render(request, "users/user.html")


def usr_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html",{
                "message": "Invalid Credentials"
            })

    return render(request, "users/login.html")

def usr_logout(request):
    logout(request)
    return render(request, "users/login.html",{
        "message": "Logged Out"
    })