from django.urls import path, include
from register.views import register
from . import views

app_name = "register"
urlpatterns = [
    path("register", register, name="register_1"),
    path("login/",  views.login, name= "login"),
    path("logout/", views.logout, name="logout")
]