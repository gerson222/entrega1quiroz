from typing import List
from django.shortcuts import render, redirect
from django.http import HttpResponse
from institutos.forms import ProfesorFormulario, CursoFormulario
from institutos.models import Curso, Profesor, Estudiante, Entregable
from django.template import loader
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

# Create your views here.

def inicio(request):

    return render(request, "institutos/index.html")

def comentarios(request):

    return render(request, "institutos/comentarios.html")

def cursos (request):
    
    curso= Curso.objects.all()
    
    if request.method == "GET":
        formulario = CursoFormulario ()
        
        contexto = {
            "mensaje_bienvenida": "Te damos la bienvenida",
            "curso": curso ,
            "formulario": formulario
        }
        
        return render (request, "institutos/cursos.html", contexto)
    else:     
        formulario= CursoFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data    
            nombre = data.get("nombre")
            camada = data.get("camada")
            curso = Curso (nombre=nombre,camada=camada )
            curso.save()
            
            contexto = {
            "mensaje_bienvenida": "Te damos la bienvenida",
            "curso": curso ,
            "formulario": formulario
        }
        return render (request, "institutos/index.html",contexto)

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
        
def borrar_curso (request, id_curso) :
    
    try:
        
        curso = Curso.objects.get (id = id_curso)
        curso.delete()
        
        return HttpResponse(f"Estas a punto de borrar el curso: {curso}")
    
    except:
        return HttpResponse(f"Error! No se pudo borrar el curso: {id_curso}")

def leer_cursos (request):
    curso = Curso.objects.all()
    contexto ={"curso":curso}
    return render (request, "institutos/leer_cursos.html", contexto )

def crear_cursos (request):
    if request.method == "GET":
        formulario = CursoFormulario()
        return render (request, "institutos/curso_formulario.html", {"formulario":formulario})
    
    else:   
        
        formulario = CursoFormulario(request.POST)
    
        if formulario.is_valid():
        
            informacion = formulario.cleaned_data
            print (informacion)
            
            nombre=  informacion.get ("nombre")
            camada=  informacion.get ("camada")
            curso = Curso (nombre= nombre, camada = camada) 
        
            curso.save()
            
            return render (request, "institutos/index.html")
    
        else:
            return HttpResponse ("Formulario no válido")

def actualizar_curso (request, id_curso):
    if request.method == "GET":
        formulario = CursoFormulario()
        contexto = {
            "formulario": formulario 
        }
        
        return render (request, "institutos/actualizar_curso.html", contexto)

    else:
        formulario = CursoFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            try:  
                curso = Curso.objects.get(id=id_curso)
                curso.nombre = data.get("nombre")
                curso.camada = data.get("camada")
                curso.save()
            except:
                return HttpResponse ("Error en la actualizacion")
            
        return redirect("info_cursos")
                
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
    
    
    
class ProfesorLista(ListView):
    model = Profesor
    template_name = "institutos/lista_profesores.html"

def agregar_profesor (request):
    
    if request.method == "GET":
        formulario = ProfesorFormulario()
        return render (request, "institutos/profesor_formulario.html", {"formulario":formulario})
    
    else:   
        
        formulario = ProfesorFormulario(request.POST)
    
        if formulario.is_valid():
        
            informacion = formulario.cleaned_data
            print (informacion)
            
            nombre =  informacion.get ("nombre")
            apellido =  informacion.get ("apellido")
            mail =  informacion.get ("mail")
            profesion =  informacion.get ("profesion")
            profesor = ProfesorFormulario (nombre= nombre, apellido = apellido, mail = mail, profesion = profesion) 
        
            profesor.save()
            
            return render (request, "institutos/index.html")
    
        else:
            return HttpResponse ("Formulario no válido")
                
def actualizar_profesor (request, id_profesor):
    if request.method == "GET":
        formulario = CursoFormulario()
        contexto = {
            "formulario": formulario 
        }
        
        return render (request, "institutos/actualizar_profesor.html", contexto)

    else:
        formulario = CursoFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            try:  
                profesor = Profesor.objects.get(id=id_profesor)
                profesor.nombre = data.get("nombre")
                profesor.apellido = data.get("apellido")
                profesor.mail = data.get("mail")
                profesor.profesion = data.get("profesion")
                profesor.save()
            except:
                return HttpResponse ("Error en la actualizacion")
            
        return redirect("info_cursos")
        
def borrar_profesor (request, id_profesor) :
    
    try:
        
        profesor = Profesor.objects.get (id = id_profesor)
        profesor.delete()
        
        return HttpResponse(f"Estas a punto de borrar al profesor: {profesor}")
    
    except:
        return HttpResponse(f"Error! No se pudo borrar al profesor: {id_profesor}")