from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Q

# Create your views here.

def inicio(request):

    return render(request,"index.html",{})

def profesores(request):
    return render(request,"profesores.html",{})

def estudiantes(request):
    return HttpResponse("Vista de estudiantes")

def cursos(request):

    cursos = Curso.objects.all()

    return render(request,"cursos.html",{"cursos":cursos})

def deportes(request):
    
    deportes = Deporte.objects.all()
    
    return render(request,"deporte.html",{"deportes":deportes})

def calendario(request):
    return render(request,"calendario.html",{})

def contacto(request):
    return render(request,"contacto.html",{})

def membresias(request):
    return render(request,"membresia.html",{})

def base(request):
    return render(request,"base.html",{})

def registro(request):
    if request.method == "POST":

        formulario = NuevoCurso(request.POST)

        if formulario.is_valid():

            info_registro = formulario.cleaned_data

            registro = Curso(nombre=info_registro["nombre"])
            registro.save() # guardamos en la bd

            return redirect("Registro")

        else:

            return render(request,"formulario_curso.html",{"form":formulario,"accion":"Crear registro"})


    else: # get y otros

        formularioVacio = EstudianteFormulario()
        return render(request,"registro.html",{"form":formularioVacio,"accion":"Crear Deporte"})


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


def busqueda_deporte(request):
    if request.method == "POST":

        deporte = request.POST["deporte"]

        deportes = Deporte.objects.filter(deporte__icontains=deporte)
        deportes = Deporte.objects.filter( Q(nombre__icontains=deporte) | Q(comision__icontains=deporte) ).values()
        # User.objects.filter(Q(income__gte=5000) | Q(income__isnull=True))

        return render(request,"busqueda_deporte.html",{"deportes":deportes})

    else: # get y otros
        deportes =  []  #Curso.objects.all()
        
        return render(request,"busqueda_deporte.html",{"deportes":deportes})

def busqueda_curso(request):
    if request.method == "POST":

        curso = request.POST["curso"]

        cursos = Curso.objects.filter(curso__icontains=curso)
        cursos = Curso.objects.filter( Q(nombre__icontains=curso) | Q(comision__icontains=curso) ).values()
        # User.objects.filter(Q(income__gte=5000) | Q(income__isnull=True))

        return render(request,"busqueda_curso.html",{"cursos":cursos})

    else: # get y otros
        cursos =  []  #Curso.objects.all()
        
        return render(request,"busqueda_curso.html",{"cursos":cursos})