from django import forms
from .models import Task

class CrearTaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ['titulo', 'descripcion', 'estado', 'urgencia']
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-tarea'}),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-tarea',
                'rows': 5,
                'cols': 40,
                'class': 'text-area',
                }),
            'estado': forms.Select(attrs={'class':'form-tarea'}),
            'urgencia': forms.Select(attrs={'class':'form-tarea'}),
        }

class EditarTaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ['titulo', 'descripcion', 'estado', 'urgencia']
        