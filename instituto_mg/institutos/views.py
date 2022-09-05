from ast import Delete
from typing import List
from django.shortcuts import render, redirect
from django.http import HttpResponse
from institutos.forms import *
from institutos.models import *
from django.template import loader
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LogoutView


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
            "cursos":cursos
        }
        
        return render (request, "institutos/cursos/cursos.html", contexto)
    
def crear_cursos (request):
    
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)
        print (formulario)
        
        if formulario.is_valid():
        
            infoC = formulario.cleaned_data
            
            curso = Curso(Nombre=infoC['curso'], Camada=infoC['camada']) 
        
            curso.save()
        
        return render (request, "institutos/cursos/cursos.html")
    
    else:   
        
        formulario = CursoFormulario()
        
        return render (request, "institutos/cursos/crear_cursos.html",  {"formulario":formulario})
    
def buscar (request):
    if request.GET["curso"]:
        curso = request.GET ["curso"]
        curso = Curso.objects.filter(curso__icontains=curso)
        return render (request, "institutos/resultado_busqueda.html", {"curso":curso})
    
    else:
        respuesta = "No enviaste datos"
    
    return HttpResponse(respuesta)
        
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

    return render(request, "institutos/clases/fisica.html")

def quimica(request):

    return render(request, "institutos/clases/quimica.html")

def matematica(request):

    return render(request, "institutos/clases/matematica.html")

def login(request):

    return render(request, "institutos/usuario/iniciar_sesion.html")

@login_required
def editar_usuario (request):
    usuario = request.user
    
    if request.method == "POST":
        formulario = EditarUsuario (request.POST)
        if formulario.is_valid:
                informacion = formulario.cleaned_data
                
                usuario.email = ["email"]
                usuario.password1 = ["password1"]
                usuario.password2 = ["password2"]
                usuario.save()
                    
                return render (request, "institutos/index.html")
                
        else:
                
                formulario = EditarUsuario (initial = {"email": usuario.email})
                
                return render (request, "institutos/usuarios/editar_usuario.html", {"formulario": formulario, "usuario": usuario})
    
    
    
class ProfesorLista(ListView):
    model = Profesor
    template_name = "institutos/profesores/lista_profesores.html"

class AgregarProfesor(LoginRequiredMixin, CreateView):
    model = Profesor
    success_url = "/appinstituto/profesores/"
    fields = ["nombre", "apellido", "email", "profesion"]
    template_name = "institutos/profesores/profesor_formulario.html"
                
def agregar_profesor (request, id_profesor):
    if request.method == "GET":
        formulario = CursoFormulario()
        contexto = {
            "formulario": formulario 
        }
        
        return render (request, "institutos/agregar_profesor.html", contexto)

    else:
        formulario = ProfesorFormulario(request.POST)
        
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
        
def registrar(request):
    
    if request.method == "GET":
        formulario = FormularioRegistroUsuario()
        return render(request, "institutos/registros.html", {"formulario": formulario})
    
    else:
        formulario = FormularioRegistroUsuario(request.POST)
        
        if formulario.is_valid():
            formulario.save()
            return redirect("inicio")
        
        else:
            return render(request, "institutos/registros.html", {"formulario": formulario, "error": "Formulario NO valido"})

def Pagos(request):

    if request.method == "POST":

        formulario_pagos = InformePagoFormulario(request.POST)

        print(formulario_pagos)

        if formulario_pagos.is_valid():

            data = formulario_pagos.cleaned_data

            Infopago = Pago(Nombre=data['Nombre_del_estudiante'], Apellido=data['Apellido_del_estudiante'], Email=data['Email_del_estudiante'], Dni=data['Numero_de_documento_de_Identidad'], Curso=data['Curso_abonado'], Telefono=data['Telefono_WhastApp'])

            Infopago.save()

            return render(request, "institutos/index.html")

    else:
        formulario_pagos = InformePagoFormulario()

        return render(request, "institutos/pagos.html", {'formularioP':formulario_pagos})
