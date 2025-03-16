from urllib import request
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .models import Register
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

# def login(request):
#     if request.method == "POST":
#         data = request.POST
#         Email = data.get("Email")
#         Password = data.get("Password")

#         print(f"Received Email: {Email}, Password: {Password}")

#         if not Email or not Password:
#             return render(request, "login.html", {"error": "Email and Password are required"})

#         user = Register.objects.filter(Email=Email).first()

#         # if user and check_password(Password, user.Password):
#         #     request.session["user_id"] = user.id
#         #     request.session["user_email"] = user.Email
#         #     print("Login successful:", user.Email)
#         #     return redirect("/dashboard/")
#         # if
#         # else:
#         #     print("Login failed for:", Email)
#         #     return render(request, "login.html", {"error": "Invalid credentials"})

#         if user:
#             print("User already exists in database")
#         else:
#             # Store email and hashed password in the database
#             hashed_password = make_password(Password)
#             new_user = Register.objects.create(Email=Email, Password=hashed_password)
#             print("New user registered:", new_user.Email)  # Debugging
#             return redirect("/dashboard/")

#     return render(request, "login.html")


def register(request):

    if request.method == "POST":
        data = request.POST
        First_Name = data.get("First_Name")
        Last_Name = data.get("Last_Name")
        Email = data.get("Email")
        Password = data.get("Password")
        Confirm_Password = data.get("Confirm_Password")
        if Password != Confirm_Password:
            return render(request, "register.html", {"error": "Passwords do not match"})

        if Register.objects.filter(Email=Email).exists():
            return render(
                request, "register.html", {"error": "Email already registered"}
            )

        Register.objects.create(
            First_Name=First_Name,
            Last_Name=Last_Name,
            Email=Email,
            Password=make_password(Password),
        )

        return redirect("/login/")
    queryset = Register.objects.all()
    context = {"register": queryset}

    return render(request, "register.html", context)


def login(request):
    if request.method == "POST":
        Email = request.POST.get("Email")
        Password = request.POST.get("Password")

        if not User.objects.filter(Email=Email).exists():
            messages.error(request, "Invalid Email")
    
            # Successful login, you might want to set a session or use Django's built-in authentication system
            # For simplicity, we'll just redirect to a dashboard or home page
            return redirect("/login/")
        user = authenticate(Email=Email, Password=Password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect("/login/")
        else:
            login(request, user)
            return redirect("/dashboard/")
        
    return render(request, "login.html")


def logout(request):
    return render(request, "logout.html")


def home(request):
    return render(request, "home.html")


def dashboard(request):
    return render(request, "dashboard.html")


def forgetPassword(request):
    return render(request, "forgetPassword.html")
