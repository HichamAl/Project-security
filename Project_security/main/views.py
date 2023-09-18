from django.shortcuts import render, redirect
from django import forms
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages


# Create your views here.
from .models import *




def home(request):
    return render(request, "main/home.html")


def register(response):
    
    return render(response, "register/register.html", {})

def loginPage(response):
    return render(response, "register/login.html", {})

def dashboard(request):
    return render(request, 'dashboard/dashboard.html', {})


def upload_id(request):
    # if request.method == 'POST':
    #     if 'id' in request.FILES:
    #         uploaded_id = request.FILES['id']
    #         # Voeg hier logica toe om het geüploade ID te verwerken
    #         return render(request, 'dashboard/upload_success.html', {'id_name': uploaded_id.name})
    #     else:
    #         # Geen bestand geüpload, toon een foutmelding aan de gebruiker
    #         error_message = "U heeft geen bestand geüpload. Probeer opnieuw."
    #         return render(request, 'dashboard/upload_id.html', {'error_message': error_message})

    return render(request, 'dashboard/upload_id.html', {})


