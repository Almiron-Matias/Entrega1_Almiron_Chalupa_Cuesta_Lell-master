from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

#BASE E INICIO

def base(request):
    return render(request,"base.html",{})

def inicio(request):

    return render(request,"index.html",{})

#PROFESORES Y ESTUDIANTES

def profesores(request):
    return render(request,"profesores.html",{})

def estudiantes(request):
    return HttpResponse("Vista de estudiantes")

#COSAS SECUNDARIAS 

def calendario(request):
    return render(request,"calendario.html",{})

def contacto(request):
    return render(request,"contacto.html",{})

def membresias(request):
    return render(request,"membresia.html",{})

def registro(request):
    if request.method == "POST":

        formulario = EstudianteFormulario(request.POST)

        if formulario.is_valid():

            info_registro = formulario.cleaned_data

            registro = Estudiante(nombre=info_registro["nombre"])
            registro.save() # guardamos en la bd
            return redirect("Registro")

        else:

            return render(request,"formulario_curso.html",{"form":formulario,"accion":"Crear registro"})


    else: # get y otros

        formularioVacio = EstudianteFormulario()
        return render(request,"registro.html",{"form":formularioVacio,"accion":"Crear Registro"})


#DEPORTES Y CURSOS

def cursos(request):
    
    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            cursos = Curso.objects.filter( Q(nombre__icontains=search) | Q(deporte__icontains=search) | Q(fecha__icontains=search) ).values()

            return render(request,"cursos.html",{"cursos":cursos, "search":True, "busqueda":search})
        
    cursos = Curso.objects.all()

    return render(request,"cursos.html",{"cursos":cursos})

def deportes(request):
    
    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            deportes = Deporte.objects.filter( Q(nombre__icontains=search) | Q(fecha__icontains=search) ).values()

            return render(request,"deporte.html",{"deportes":deportes, "search":True, "busqueda":search})
    
    deportes = Deporte.objects.all()
    
    return render(request,"deporte.html",{"deportes":deportes})

def nuevo_curso(request):
    if request.method == "POST":

        formulario = NuevoCurso(request.POST)

        if formulario.is_valid():

            info_curso = formulario.cleaned_data

            curso = Curso(nombre=info_curso["nombre"],deporte=info_curso["deporte"],fecha=info_curso["fecha"])
            curso.save() 

            return redirect("Cursos")

        else:

            return render(request,"nuevo_curso.html",{"form":formulario,"accion":"Crear Curso"})


    else: # get y otros

        formularioVacio = NuevoCurso()

        return render(request,"nuevo_curso.html",{"form":formularioVacio,"accion":"Crear Curso"})

def nuevo_deporte(request):
    if request.method == "POST":

        formulario = NuevoDeporte(request.POST)

        if formulario.is_valid():

            info_deporte = formulario.cleaned_data

            deporte = Deporte(nombre=info_deporte["nombre"],fecha=info_deporte["fecha"])
            deporte.save() 

            return redirect("Deportes")

        else:

            return render(request,"nuevo_deporte.html",{"form":formulario,"accion":"Crear Deporte"})


    else: # get y otros

        formularioVacio = NuevoDeporte()

        return render(request,"nuevo_deporte.html",{"form":formularioVacio,"accion":"Crear Deporte"})
   
def eliminar_deporte(request, deporte_id):

    deporte = Deporte.objects.get(id=deporte_id)
    deporte.delete()

    return redirect("Deportes")

def editar_deporte(request, deporte_id):

    # post
    
    deporte = Deporte.objects.get(id=deporte_id)

    if request.method == "POST":

        formulario = NuevoDeporte(request.POST)

        if formulario.is_valid():

            info_deporte = formulario.cleaned_data
        
            deporte.nombre = info_deporte["nombre"]
            deporte.fecha = info_deporte["fecha"]
            deporte.save() 
            
            return redirect("Deportes")

            
    formulario = NuevoDeporte(initial={"nombre":deporte.nombre,"fecha":deporte.fecha})

    return render(request,"nuevo_deporte.html",{"form":formulario,"accion":"Editar Deporte"})

def eliminar_curso(request, curso_id):

    curso = Curso.objects.get(id=curso_id)
    curso.delete()

    return redirect("Cursos")

def editar_curso(request, curso_id):
    
    curso = Curso.objects.get(id=curso_id)

    if request.method == "POST":

        formulario = NuevoCurso(request.POST)

        if formulario.is_valid():

            info_curso = formulario.cleaned_data
        
            curso.nombre = info_curso["nombre"]
            curso.deporte = info_curso["deporte"]
            curso.fecha = info_curso["fecha"]
            curso.save() # guardamos en la bd
            
            return redirect("Cursos")

            
    formulario = NuevoCurso(initial={"nombre":curso.nombre,"deporte":curso.deporte,"fecha":curso.fecha})

    return render(request,"nuevo_curso.html",{"form":formulario,"accion":"Editar Curso"})
