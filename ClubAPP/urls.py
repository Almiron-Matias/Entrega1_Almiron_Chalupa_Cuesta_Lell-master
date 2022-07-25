from django.urls import path
from .views import *

urlpatterns = [
    # URLS Base
    path('base/', base),
    path('', inicio, name="Inicio"),
    path('entrada/', login_req, name="Entrada"), 
    path('registro/', register_req, name="Registro"),
    path('salida/', logout_req, name="Salida"),
    path('about_me/',about_me, name="About_me"),
    path('about_me_cursed/',about_me_cursed, name="About_me_cursed"),
    
    # URLS Barra del Navegador
    path('profesores/', profesores, name="Profesores"),
    path('calendario/', calendario, name="Calendario"),
    path('contacto/', contacto, name="Contacto"),
    path('inscripcion/',inscripcion, name="Inscripcion"),
    path('usuarios/',usuarios, name="Usuarios"),
    path('selector/',selector,name="Selector"),
    path('eliminador/',eliminardor,name="Eliminador"),
    
    # URLS Secundarias
    path('membresias/', membresias, name="Membresias"),

    # URLS Cursos y Deportes
    path('cursos/', cursos, name="Cursos"),
    path('deportes/', deportes, name="Deportes"),
    path('nuevo_curso/', nuevo_curso, name="Nuevo_curso"),
    path('nuevo_deporte/', nuevo_deporte, name="Nuevo_deporte"),
    path('eliminar_deporte/<deporte_id>/', eliminar_deporte, name="Eliminar_deporte"),
    path('editar_deporte/<deporte_id>/', editar_deporte, name="Editar_deporte"),
    path('eliminar_curso/<curso_id>/', eliminar_curso, name="Eliminar_curso"),
    path('editar_curso/<curso_id>/', editar_curso, name="Editar_curso"),

]
