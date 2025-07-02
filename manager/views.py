from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import CrearTaskForm

# Create your views here.
@login_required
def listar_tareas(request):
    tasks = Task.objects.filter(usuario = request.user)
    return render(request, 'manager/listar_tareas.html', {'tasks':tasks})

@login_required
def crear_task(request):
    if request.method == "POST":
        form = CrearTaskForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=True)
            tarea.usuario = request.user
            tarea.save()
            return redirect('listar_tareas')
    else:
        form = CrearTaskForm()
    return render(request, 'manager/crear_task.html',  {'form':form})



def salir(request):
    logout(request)
    return redirect('menu')