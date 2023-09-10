from django.urls import path

from . import views
from . import forms

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.loginPage, name="login"),
    path("register/", views.register, name="register"),

]