from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User

# Create your views here.

#BASE E INICIO

def base(request):
    return render(request,"base.html",{})

def inicio(request):

    return render(request,"index.html",{})

def about_me(request):
    return render(request,"about_me.html",{})

def about_me_cursed(request):
    return render(request,"about_me_cursed.html",{})

#PROFESORES Y ESTUDIANTES

def profesores(request):
    return render(request,"profesores.html",{})

def estudiantes(request):
    return HttpResponse("Vista de estudiantes")

@staff_member_required
def usuarios(request):
    
    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            usuarios  = User.objects.filter( (Q(username__icontains=search) ) | Q(email__icontains=search) | Q(tipo__icontains=search) ).values()

            return render(request,"usuarios.html",{"usuarios":usuarios , "search":True, "busqueda":search})
    
    usuarios = User.objects.all()
    
    return render(request,"usuarios.html",{"usuarios":usuarios})

def selector(request):
   return render(request,"selector.html",{})  

@staff_member_required
def eliminardor(request,usuario_id):
    usuario = User.objects.get(id=usuario_id)
    usuario.delete()

    return redirect("Usuarios")

@login_required
def perfil(request):
    try:
        avatar = Avatar.objects.get(usuario=request.user)
        url = avatar.imagen.url
    except:
        url = "/media/generica.jpg"
    
    perfil=request.user
    return render(request,"perfil.html",{"Usuario":perfil,"url":url}) 

@login_required
def editar_perfil(request):
    user = request.user 

    if request.method == "POST":
        
        form = UserEditForm(request.POST) 

        if form.is_valid():

            info = form.cleaned_data
            user.email = info["email"]
            user.first_name = info["first_name"]
            user.last_name = info["last_name"]

            user.save()

            return redirect("Perfil")

    else:
        form = UserEditForm(initial={"email":user.email, "first_name":user.first_name, "last_name":user.last_name})

    return render(request,"editar_perfil.html",{"form":form})

def agregar_avatar(request):
        
    if request.method == "POST":
            
        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():

            user = User.objects.get(username=request.user.username)

            avatar = Avatar(usuario=user, imagen=form.cleaned_data["imagen"])

            avatar.save()

            return redirect("Perfil")

    else:
        form = AvatarForm()
        
    return render(request,"agregar_avatar.html",{"form":form})

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

@login_required
def membresias(request):
    return render(request,"membresia.html",{})

@login_required
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


