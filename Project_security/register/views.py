from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import  CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import VerifiedUsers
from .forms import FileUploadForm
from django.contrib.auth.decorators import login_required
# Create your views here.



def register(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account is succesvol aangemaakt')

            return redirect('register:login')
    else:
        form = CreateUserForm()
    print('test')
    context = {'form':form}
    return render(request, "register/register.html", context)


def loginPage(request):
    context = {"login_error": ''}
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                try:
                    # Probeer de verificatiestatus van de gebruiker op te halen
                    verified_user = VerifiedUsers.objects.get(user=user)
                    if verified_user.verified:
                        # Als de gebruiker is geverifieerd, stuur hem door naar de homepage
                        return redirect('home')
                    else:
                        # Als de gebruiker niet is geverifieerd, stuur hem naar het dashboard
                        return redirect('register:dashboard')
                except VerifiedUsers.DoesNotExist:
                    # Als er geen VerifiedUsers-record is, ga gewoon door
                    return redirect('register:dashboard')

        context['login_error'] = "Invalid username or password."

    form = AuthenticationForm()
    context['login_form'] = form
    return render(request, "register/login.html", context=context)


@login_required
def dashboard(request):
    return render(request, 'register/dashboard.html', {})



@login_required
def upload_id(request):
    user = request.user
    form = FileUploadForm()  
    verified_user = None  

    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # Try to retrieve the existing VerifiedUsers record for the user
                verified_user = VerifiedUsers.objects.get(user=user)
                verified_user.uploaded_file = form.cleaned_data['id']
                verified_user.verified = True
                verified_user.save()
            except VerifiedUsers.DoesNotExist:
                # Create a new VerifiedUsers instance for the user
                verified_user = VerifiedUsers(user=user, uploaded_file=form.cleaned_data['id'], verified=True)
                verified_user.save()
                
            uploaded_file = form.cleaned_data['id']  # Retrieve the uploaded file
            # Voeg hier logica toe om het geüploade ID te verwerken
            return render(request, 'register/upload_success.html', {'id_name': uploaded_file.name})
        else:
            # Geen bestand geüpload, toon een foutmelding aan de gebruiker
            error_message = "U heeft geen bestand geüpload. Probeer opnieuw."
            return render(request, 'dashboard/upload_id.html', {'error_message': error_message, 'form': form})

    return render(request, 'register/upload_id.html', {'form': form, 'verified_user': verified_user})




#@login_required
#def upload_id(request):
#    user = request.user
#    form = FileUploadForm()  
#    verified_user = None  
#
#    if request.method == 'POST':
#        form = FileUploadForm(request.POST, request.FILES)
#        if form.is_valid():
#            if not verified_user:
#                verified_user = VerifiedUsers(user=user, uploaded_file=form.cleaned_data['id'], verified=True)
#                verified_user.save()
#                uploaded_file = form.cleaned_data['id']  # Retrieve the uploaded file
#                # Voeg hier logica toe om het geüploade ID te verwerken
#                return render(request, 'dashboard/upload_success.html', {'id_name': uploaded_file.name})
#        else:
#            # Geen bestand geüpload, toon een foutmelding aan de gebruiker
#            error_message = "U heeft geen bestand geüpload. Probeer opnieuw."
#            return render(request, 'dashboard/upload_id.html', {'error_message': error_message, 'form': form})
#
#    return render(request, 'register/upload_id.html', {'form': form, 'verified_user': verified_user})





def logout(request):
	if request.user.is_authenticated:
		logout(request)
	
	return redirect('/login')