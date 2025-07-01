from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm, InicioSesionUsuarioForm
from django.contrib.auth import get_user, login

def menu(request):
    return render(request, 'usuarios/menu.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request)
        if form.is_valid():
            form.save()
            return redirect('inicio_sesion')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/registro.html', {'form':form})
    
def inicio_sesion(request):
    if request.method == 'POST':
        form = InicioSesionUsuarioForm(request)
        if form.is_valid():
            usuario = form.get_user()
            login(request,usuario)
            return redirect('menu_usuario')
    else:
        form = InicioSesionUsuarioForm()
    return render(request, 'usuarios/inicio_sesion.html', {'form':form})
