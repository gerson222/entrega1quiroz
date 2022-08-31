from django.forms import Form, IntegerField, CharField, EmailField, DateField, BooleanField, PasswordInput, ImageField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CursoFormulario (Form):
    curso = CharField()
    camada = IntegerField()
    
    
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
