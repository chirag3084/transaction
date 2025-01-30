from urllib import request
from django.shortcuts import render
import fastapi


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def logout(request):
    return render(request, "logout.html")


def home(request):
    return render(request, "home.html")


def dashboard(request):
    return render(request, "dashboard.html")


def forgetPassword(request):
    return render(request, "forgetPassword.html")
