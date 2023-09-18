from django.urls import path, include
from . import views

app_name = "register"
urlpatterns = [
    path("register/", views.register, name="register_1"),
    path("login/",  views.loginPage, name= "login"),
    path("logout/", views.logout, name="logout")
]