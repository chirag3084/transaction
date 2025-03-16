from django.urls import path
from . import views

# Registering the app's namespace
app_name = "home"

urlpatterns = [
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("forgetPassword/", views.forgetPassword, name="forgetPassword"),
    path("", views.home, name="home"), 
]
