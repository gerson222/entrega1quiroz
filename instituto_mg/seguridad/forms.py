from django.forms import Form, IntegerField, CharField, EmailField, DateField, BooleanField, PasswordInput, ImageField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from seguridad.models import Mensajes

class FormularioMensajes (Form):
    autor = CharField ()
    mensaje =  CharField ()
    destinatario = CharField ()
    


