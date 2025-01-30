from django.urls import path
from . import views

# Registering the app's namespace
app_name = "home"

urlpatterns = [
    path("", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout, name="logout"),
    path("home/dashboard/", views.dashboard, name="dashboard"),
    path("forgetPassword/", views.forgetPassword, name="forgetPassword"),
    path("home/", views.home, name="home"), 
]
