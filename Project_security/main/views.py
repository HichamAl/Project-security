from django.shortcuts import render, redirect
from django import forms
from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .models import *
from .forms import OrderForm, CreateUserForm




def home(request):
    return render(request, "home.html")


def register(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account is succesvol aangemaakt')

            return redirect('login')



    context = {'form':form}
    return render(request, "register.html", context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')


    return render(request, "login.html")

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def upload_id(request):
    if request.method == 'POST':
        uploaded_id = request.FILES['id']
        # Add logic to process the uploaded ID here
        return render(request, 'dashboard/upload_success.html', {'id_name': uploaded_id.name})

    return render(request, 'dashboard/upload_id.html')

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form}
    return render(request, "register.html", context)