from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect


# Create your views here.


def index(request):
    return render(request, "index.html")


def cart(request):
    return render(request, "cart.html")


def login(request):
    return render(request, "login.html")


def searchmed(request):
    return render(request, "searchmed.html")


def signup(request):
    return render(request, "signup.html")


def ordercomplete(request):
    return render(request, "ordercomplete.html")
