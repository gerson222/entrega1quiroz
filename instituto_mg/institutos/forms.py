from typing import Text
from django.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from institutos.models import Estudiante

class CursoFormulario (Form):
    curso = CharField(widget=TextInput(attrs={'size': '40'}))
    camada = IntegerField()

class EditarUsuario (Form):
    email = EmailField(label="Modificar E-Mail")
    password1 = CharField (label= "Contraseña", widget= PasswordInput)
    password2 = CharField (label= "Repetí la contraseña", widget= PasswordInput)
    nombre = CharField(widget=TextInput(attrs={'size': '40'}))
    apellido = CharField (widget=TextInput(attrs={'size': '40'}))
    
    class Meta:
        model = Estudiante
        fields = ["email", "password1", "password2", "nombre", "apellido"]
        help_texts = {k: "" for k in fields}
        
class ProfesorFormulario(Form):
    nombre = CharField(widget=TextInput(attrs={'size': '40'}))
    apellido = CharField(widget=TextInput(attrs={'size': '40'}))
    email = EmailField(widget=TextInput(attrs={'size': '40'}))
    profesion = CharField(widget=TextInput(attrs={'size': '40'}))
    
class FormularioRegistroUsuario(UserCreationForm):

    email = EmailField()
    password1 = CharField(label="Contraseña", widget=PasswordInput)
    password2 = CharField(label="Confirmar contraseña", widget=PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = { "username": "", "email": "", "password1": "", "password2": "" }

OPCIONES_curso=(
    ("1", "Quimica XXI a distancia"),
    ("2", "Quimica CBC a distancia"),
    ("3", "Quimica Completo"),
    ("4", "Matematica XXI a distancia"),
    ("5", "Matematica CBC a distancia"),
    ("6", "Matematica Completo"),
    ("7", "Biofisica XXI a distancia"),
    ("8", "Biofisica CBC a distancia"),
    ("9", "Biofisica XXI Completo"),
    ("10", "Biofisica CBC Completo"),
    )


class InformePagoFormulario (Form):
    Nombre_del_estudiante= CharField(widget=TextInput(attrs={'size': '40'}))
    Apellido_del_estudiante= CharField(widget=TextInput(attrs={'size': '40'}))
    Email_del_estudiante= EmailField(widget=TextInput(attrs={'size': '40'}))
    Numero_de_documento_de_Identidad=()
    Curso_abonado= ChoiceField(choices=OPCIONES_curso)
    Telefono_WhastApp= IntegerField()
    Comprobante = FileField()

OPCIONES_Valoracion=(
    ("1", "Excelente"),
    ("2", "Muy bueno"),
    ("3", "Bueno"),
    ("4", "Normal"),
    ("5", "Malo")
    )

class Comentario_nuevo (Form):
    Tu_nombre= CharField(widget=TextInput(attrs={'size': '40'}))
    Email= CharField(widget=TextInput(attrs={'size': '40'}))
    Seleccionar_el_curso= ChoiceField(choices=OPCIONES_curso)
    Valoracion= ChoiceField(choices=OPCIONES_Valoracion)
    Tu_comentario= CharField(widget=Textarea)