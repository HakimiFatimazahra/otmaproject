# omtaapp/forms/login_form.py
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=100)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
