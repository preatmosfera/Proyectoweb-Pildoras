from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Agregamos el campo email obligatorio

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]  # Agregamos email aquí
