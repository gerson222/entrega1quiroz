from django.shortcuts import render
from django.http import HttpResponse
from institutos.forms import CursoFormulario
from institutos.models import Curso, Profesor, Estudiante, Entregable
from django.template import loader
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):

    return render(request, "institutos/index.html")

def comentarios(request):

    return render(request, "institutos/comentarios.html")

def cursos (request):
    if request.method == "POST":
        miFormulario = CursoFormulario (request.POST)
        print (miFormulario)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso (request.POST ["curso"], request.POST ["camada"] )
            curso.save()
            return render (request, "institutos/index.html")

    else:     
        miFormulario= CursoFormulario() 
        
    return render (request, "institutos/curso_formulario.html", {"miFormulario": miFormulario})

def leer_cursos(request):
    cursos = Curso.objects.all()
    contexto = {"cursos": cursos}
    return render (request, "institutos/leer_cursos.html", contexto)

def crear_curso (request):  
    if request.method == "POST":
        miFormulario = CursoFormulario (request.POST)
        print (miFormulario)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso (request.POST ["curso"], request.POST ["camada"] )
            curso.save()
            return render (request, "institutos/index.html")

    else:     
        miFormulario= CursoFormulario() 
        
    return render (request, "institutos/crear_curso.html", {"miFormulario": miFormulario})

def buscar_curso (request):
    return render (request, "institutos/buscar_curso.html")

def buscar (request):
    if request.GET["curso"]:
        curso = request.GET ["curso"]
        curso = Curso.objects.filter(curso__icontains=curso)
        return render (request, "institutos/resultado_busqueda.html", {"curso":curso})
    
    else:
        respuesta = "No enviaste datos"
    
    return HttpResponse(respuesta)
        
def borrar_curso (request, curso_nombre):
    curso = Curso.objects.get (nombre = curso_nombre)
    curso.delete ()
    
    curso = Curso.objects.all()
    contexto = {"curso": curso}
    
    return render (request, "institutos/leer_cursos.html", contexto)


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



@login_required
def editar_usuario (request):
    
    if request.method== "GET":
        return render (request, "institutos/editar_usuario.html", {"formulario":None})