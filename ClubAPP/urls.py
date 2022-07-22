from django.urls import path
from .views import *

urlpatterns = [
    # URLS Base
    path('base/', base),
    path('', inicio, name="Inicio"),
    
    # URLS Barra del Navegador
    path('profesores/', profesores, name="Profesores"),
    path('calendario/', calendario, name="Calendario"),
    path('contacto/', contacto, name="Contacto"),
    
    # URLS Secundarias
    path('membresias/', membresias, name="Membresias"),
    path('registro/', registro, name="Registro"),

    # URLS Cursos y Deportes
    path('cursos/', cursos, name="Cursos"),
    path('deportes/', deportes, name="Deportes"),
    path('nuevo_curso/', nuevo_curso, name="Nuevo_curso"),
    path('nuevo_deporte/', nuevo_deporte, name="Nuevo_deporte"),
    path('eliminar_curso/<deporte_id>/', eliminar_deporte, name="Eliminar_deporte"),
    path('editar_curso/<deporte_id>/', editar_deporte, name="Editar_deporte"),
]
