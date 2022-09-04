from django.forms import Form, IntegerField, CharField, EmailField, DateField, BooleanField, PasswordInput, ImageField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from institutos.models import Estudiante

class CursoFormulario (Form):
    curso = CharField()
    camada = IntegerField()

class EditarUsuario (Form):
    email = EmailField(label="Modificar E-Mail")
    password1 = CharField (label= "Contraseña", widget= PasswordInput)
    password2 = CharField (label= "Repetí la contraseña", widget= PasswordInput)
    nombre = CharField()
    apellido = CharField ()
    
    class Meta:
        model = Estudiante
        fields = ["email", "password1", "password2", "nombre", "apellido"]
        help_texts = {k: "" for k in fields}
        
class ProfesorFormulario (Form):
    nombre = CharField()
    apellido = CharField()
    email = EmailField()
    profesion = CharField()
    
class FormularioRegistroUsuario(UserCreationForm):

    email = EmailField()
    password1 = CharField(label="Contraseña", widget=PasswordInput)
    password2 = CharField(label="Confirmar contraseña", widget=PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = { "username": "", "email": "", "password1": "", "password2": "" }

class InformePagoFormulario (Form):
    Nombre_del_estudiante= CharField()
    Apellido_del_estudiante= CharField()
    Email_del_estudiante= EmailField()
    Numero_de_documento_de_Identidad= IntegerField()
    Curso_abonado= CharField()
    Telefono_WhastApp= IntegerField()

class Comentarios (Form):
    tu_nombre= CharField()