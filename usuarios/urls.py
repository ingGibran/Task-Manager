from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('inicio_sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('registro/', views.registro, name='registro'),
]