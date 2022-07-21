from django.urls import path
from .views import *

urlpatterns = [
    # URLS de ProyectoCoderApp
    path('', inicio, name="Inicio"),
    path('profesores/', profesores, name="Profesores"),
    path('cursos/', cursos, name="Cursos"),
    path('deportes/', deportes, name="Deportes"),
    path('calendario/', calendario, name="Calendario"),
    path('contacto/', contacto, name="Contacto"),
    path('membresias/', membresias, name="Membresias"),
    path('registro/', registro, name="Registro"),
    path('nuevo_curso/', nuevo_curso, name="Nuevo_curso"),
    path('nuevo_deporte/', nuevo_deporte, name="Nuevo_deporte"),
    path('base/', base),
    
    path('eliminar_curso/<deporte_id>/', eliminar_deporte, name="Eliminar_deporte"),
    path('editar_curso/<deporte_id>/', editar_deporte, name="Editar_deporte"),
]
