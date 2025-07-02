from django.db import models
from django.conf import settings

# Create your models here.
class Task(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=50)
    fecha_inicio = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    OPCIONES_ESTADO = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En progreso'),
        ('completada', 'Completada'),
    ]
    estado = models.CharField(max_length=15, choices=OPCIONES_ESTADO, default='pendiente')
    OPCIONES_URGENCIA = [
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
    ]
    urgencia = models.CharField(max_length=10, choices=OPCIONES_URGENCIA, default='media')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tareas')
    
    def __str__(self):
        return f'{self.titulo} - {self.estado} - {self.usuario.email}'