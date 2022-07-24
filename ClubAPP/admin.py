from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

class CursoAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'deporte','fecha')
    search_fields = ('nombre', 'deporte','fecha')


class EstudianteAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'apellido', 'deporte','email')
    search_fields = ('nombre', 'deporte')


class ProfesorAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'apellido', 'deporte','email')
    search_fields = ('nombre', 'deporte')
    
class DeporteAdmin(admin.ModelAdmin):

    list_display = ('nombre','fecha')
    search_fields = ('nombre','fecha')

admin.site.register(Curso, CursoAdmin)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Deporte, DeporteAdmin)

# admin, admin -> python manage.py createsuperuser