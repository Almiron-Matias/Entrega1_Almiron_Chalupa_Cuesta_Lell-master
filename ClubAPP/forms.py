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
    
    nombre = forms.CharField(label="Nombre:",required=False)
    apellido = forms.CharField(label="Apellido:",required=False)
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput) 
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','nombre','apellido', 'email', 'password1', 'password2']

        #help_texts = {k:"" for k in fields}

roles = [("estudiante", "Estudiante"), ("profesor", "Profesor")]
class Selector(UserCreationForm):

    roles = forms.MultipleChoiceField(choices=roles, label="Roles", widget=forms.Select(choices=roles))