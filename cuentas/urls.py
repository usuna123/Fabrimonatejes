from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
     path('recuperar/', views.Contrasena, name='Contrasena'),
]


