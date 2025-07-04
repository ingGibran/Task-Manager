from django.shortcuts import render, redirect, get_object_or_404
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
            tarea = form.save(commit=False)
            tarea.usuario = request.user
            tarea.save()
            return redirect('listar_tareas')
    else:
        form = CrearTaskForm()
    return render(request, 'manager/crear_task.html',  {'form':form})

@login_required
def editar_task(request, pk):
    tarea = get_object_or_404(Task, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = CrearTaskForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('listar_tareas')
    else:
        form = CrearTaskForm(instance=tarea)
    return render(request, 'manager/editar_task.html', {'form':form})
    
@login_required
def eliminar_task(request, pk):
    tarea = get_object_or_404(Task, pk=pk, usuario=request.user)
    tarea.delete()
    return redirect('listar_tareas')
    
def salir(request):
    logout(request)
    return redirect('menu')