from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_tareas, name="listar_tareas"),
    path('crear_tas', views.crear_task, name="crear_task"),
    path('logout/', views.salir, name='salir'),
    path('editar/<int:pk>/', views.editar_task, name="editar_task"),
    path('eliminar/<int:pk>', views.eliminar_task, name="eliminar_task"),
]