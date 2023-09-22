from django.urls import path, include
from . import views

app_name = "register"
urlpatterns = [
    path("register/", views.register, name="register_1"),
    path("login/",  views.loginPage, name= "login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path('dashboard/upload_id/', views.upload_id, name='upload_id'),
    path('dashboard/upload_id/upload_success/', views.upload_success, name='upload_success'),
    path("logout/", views.logout, name="logout")
]