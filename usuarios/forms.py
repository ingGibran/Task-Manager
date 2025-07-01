from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(
        label='Correo Electrónico',
        widget=forms.EmailInput(attrs={
            'class':'user-form',
        })
    )
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class':'user-form',
        })
    )
    password2 = forms.CharField(
        label='Repetir Contraseña',
        widget=forms.PasswordInput(attrs={
            'class':'user-form',
        })
    )
    
    class Meta:
        model = Usuario
        fields = ['email', 'password1', 'password2']


class InicioSesionUsuarioForm(AuthenticationForm):
    username = forms.EmailField(
        label='Correo Electrónico',
        widget=forms.EmailInput(attrs={
            'class':'user-form',
        })
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class':'user-form',
        })
    )
    