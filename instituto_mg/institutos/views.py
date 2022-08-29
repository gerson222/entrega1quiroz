from django.shortcuts import render
from django.http import HttpResponse
from institutos.models import Curso, Profesor, Estudiante, Entregable
from django.template import loader
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):

    return render(request, "institutos/index.html")

def comentarios(request):

    return render(request, "institutos/comentarios.html")

def cursos(request):

    return render(request, "institutos/cursos.html")

def campus(request):

    return render(request, "institutos/campus.html")

def usuario(request):

    return render(request, "institutos/usuario.html")

def fisica(request):

    return render(request, "institutos/fisica.html")

def quimica(request):

    return render(request, "institutos/quimica.html")

def matematica(request):

    return render(request, "institutos/matematica.html")

def login(request):

    return render(request, "institutos/iniciar_sesion.html")

def leer_cursos(request):
    cursos = Curso.objects.all()
    contexto = {"cursos": cursos}
    return render (request, "institutos/leer_cursos.html", contexto)


def crear_curso (request):   # DEBERIA ACA UNIRLO CON EL FORMULARIO, PERO NOSE SI INCLUIRLO PORQUE ME PARECE QUE UDS YA LO HICIERON
    if request.method == "POST":
        curso = Curso (request.POST ["curso"], request.POST ["camada"])
        curso.save ()
        return render (request, "institutos/index.html")
    
    
    return render (request, "institutos/crear_curso.html")


@login_required
def editar_usuario (request):
    
    if request.method== "GET":
        return render (request, "institutos/editar_usuario.html", {"formulario":None})