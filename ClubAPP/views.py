from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

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

def usuarios(request):
    
    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            usuarios  = User.objects.filter( Q(nombre__icontains=search) | Q(apellido__icontains=search) | Q(email__icontains=search) | Q(tipo__icontains=search) ).values()

            return render(request,"usuarios.html",{"usuarios":usuarios , "search":True, "busqueda":search})
    
    usuarios = User.objects.all()
    
    return render(request,"usuarios.html",{"usuarios":usuarios})

def selector(request):
   return render(request,"selector.html")  

def eliminardor(request):
    return render(request,"eliminador.html")   
 
#LOGIN Y LOGOUT

def login_req (request):
    
    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("Inicio")
            else:
                return redirect("Entrada")
        else:
            return redirect("Entrada")
    
    form = AuthenticationForm()

    return render(request,"entrada.html",{"form":form})
       
def register_req(request):

    if request.method == "POST":
        
        
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1') 

            form.save()
            
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("Inicio")
            else:
                return redirect("Entrada")
        
    form = UserRegisterForm(request.POST)

    return render(request,"registro.html",{"form":form})

def logout_req(request):
    logout(request)
    return redirect("Inicio")


#COSAS SECUNDARIAS 

def calendario(request):
    return render(request,"calendario.html",{})

def contacto(request):
    return render(request,"contacto.html",{})

def membresias(request):
    return render(request,"membresia.html",{})

def inscripcion(request):
    return render(request,"inscripcion.html",{})

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

@staff_member_required
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

@staff_member_required
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

@staff_member_required
def eliminar_deporte(request, deporte_id):

    deporte = Deporte.objects.get(id=deporte_id)
    deporte.delete()

    return redirect("Deportes")

@staff_member_required
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

@staff_member_required
def eliminar_curso(request, curso_id):

    curso = Curso.objects.get(id=curso_id)
    curso.delete()

    return redirect("Cursos")

@staff_member_required
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


