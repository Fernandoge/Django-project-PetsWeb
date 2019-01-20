from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
                'run',
                'first_name',
                'last_name',
                'email',
                'edad',
                'fono',
                'direccion',

        ]
        widgets = {
            'run': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.TextInput(attrs={'class': 'form-control'}),
            'fono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
                'run': 'RUN',
                'first_name': 'Nombres',
                'last_name': 'Apellidos',
                'email': 'Correo',
                'edad': 'Edad',
                'fono': 'Fono',
                'direccion': 'Direccion',

        }