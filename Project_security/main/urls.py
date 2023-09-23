from django.urls import path

from . import views



urlpatterns = [
    path("", views.home, name="home"),
    #path("login/", views.loginPage, name="login"),
    #path("register/", views.register, name="register"),
    # path('dashboard/', views.dashboard, name='dashboard'),
    #path('dashboard/upload_id/', views.upload_id, name='upload_id'),

]