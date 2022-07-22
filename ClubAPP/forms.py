from django import forms

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
