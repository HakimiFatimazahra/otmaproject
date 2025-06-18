from django.shortcuts import render

# Create your views here.
def signup (request):


    return render(request,'signup.html')


def checklist_view(request):
    return render(request, 'htmlfile.html')  # crée aussi le fichier checklist.html dans templates

def pageentre(request):

    return render(request, 'pageentre.html')

def htmlfile_view(request):
    return render(request, 'htmlfile.html')

def validefile_view(request):
    return render(request, 'validefile.html')

def login(request):

    return render(request, 'login.html')
def loginn(request):

    return render(request, 'loginn.html')

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


from django.contrib.auth.decorators import login_required, user_passes_test

# Fonction pour vérifier si l'utilisateur est un saisisseur
def is_saisisseur(user):
    return user.groups.filter(name='Saisisseur').exists()

# Fonction pour vérifier si l'utilisateur est un validateur
def is_validateur(user):
    return user.groups.filter(name='Validateur').exists()





from django.shortcuts import redirect

def redirect_user(request):
    if request.user.groups.filter(name='Saisisseur').exists():
        return redirect('saisie')
    elif request.user.groups.filter(name='Validateur').exists():
        return redirect('validation')
    else:
        return redirect('login')


