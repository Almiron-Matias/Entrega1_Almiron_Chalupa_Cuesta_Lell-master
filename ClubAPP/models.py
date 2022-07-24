from msilib.schema import Class
from django.db import models

# Create your models here.

class Estudiante(models.Model):

    nombre = models.CharField(max_length=30) 
    apellido = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)
    deporte = models.CharField(max_length=30,blank=True, null=True)   
    

class Profesor(models.Model):

    nombre = models.CharField(max_length=30) 
    apellido = models.CharField(max_length=30) 
    email = models.EmailField(blank=True, null=True)
    deporte = models.CharField(max_length=30)   

class Curso(models.Model):

    nombre = models.CharField(max_length=30) 
    deporte = models.CharField(max_length=30)
    fecha = models.DateField(max_length=30)

class Deporte(models.Model):

    nombre = models.CharField(max_length=30)
    fecha = models.DateField(max_length=30)

