from django import forms
from .models import Task

class CrearTaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ['titulo', 'descripcion', 'estado', 'urgencia']
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-tarea'}),
            'descripcion': forms.TextInput(attrs={'class':'form-tarea'}),
            'estado': forms.Select(attrs={'class':'form-tarea'}),
            'urgencia': forms.Select(attrs={'class':'form-tarea'}),
        }

class EditarTaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ['titulo', 'descripcion', 'estado', 'urgencia']
        