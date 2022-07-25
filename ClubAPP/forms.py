from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NuevoDeporte(forms.Form):

    nombre = forms.CharField(max_length=30,label="Deporte:")
    fecha = forms.CharField(max_length=30,label="Inserte la fecha (xx/xx):")

class EstudianteFormulario(forms.Form):

    nombre = forms.CharField(max_length=30,label="Nombre:")
    apellido = forms.CharField(max_length=30,label="Apellido:")
    email = forms.EmailField(label="Email:")
    
class NuevoCurso(forms.Form):

    nombre = forms.CharField(max_length=30,label="Curso:")
    deporte = forms.CharField(max_length=30,label="Deporte:")
    fecha = forms.CharField(max_length=30,label="Inserte la fecha (año-mes-dia):")

class UserRegisterForm(UserCreationForm):
    
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput) 
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']

class UserEditForm(UserCreationForm):

    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=False) # la contraseña no se vea
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ['email','first_name', 'last_name', 'password1', 'password2']
