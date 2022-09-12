from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from institutos.forms import *
from institutos.models import *
from django.template import loader
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.views import LogoutView



# Create your views here.

def inicio(request):

    return render(request, "institutos/index.html")

def info_cursos(request):
    
    return render(request, "institutos/cursosinfo.html")

def nosotros(request):
    
    return render(request, "institutos/profesores/nosotros.html")

@login_required
def cursos (request):
    
    cursos = Curso.objects.all()
    
    contexto = {
        "cursos":cursos
        }
        
    return render (request, "institutos/cursos/cursosadm.html", contexto)

@login_required
def crear_cursos (request):

    if request.method == "POST":

        formulario = CursoFormulario(request.POST)
            
        if formulario.is_valid():
            
            informacion = formulario.cleaned_data
                
            curso = Curso(Nombre=informacion['curso'], Camada=informacion['camada']) 
            
            curso.save()
        
        
            return render(request, "institutos/cursos/cursosadm.html")
    
    else:      
        formulario = CursoFormulario()
        return render (request, "institutos/cursos/crear_cursos.html", {"formulario":formulario})

    
def buscar (request):
    if request.GET["curso"]:
        curso = request.GET ["curso"]
        curso = Curso.objects.filter(curso__icontains=curso)
        return render (request, "institutos/resultado_busqueda.html", {"curso":curso})
    
    else:
        respuesta = "No enviaste datos"
    
    return HttpResponse(respuesta)

@login_required        
def actualizar_curso (request, curso_nombre):
    if request.method == "GET":
        formulario = CursoFormulario()
        contexto = {
            "formulario": formulario 
        }
        
        return render (request, "institutos/cursos/actualizar_curso.html", contexto)

    else:
        formulario = CursoFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            try:  
                curso = Curso.objects.get(nombre= curso_nombre)
                
                curso.nombre = data.get("Nombre")
                curso.camada = data.get("Camada")
                curso.save()
            except:
                return HttpResponse ("Error en la actualizacion")
            
        return redirect("institutos/cursos/cursosadm.html")
    
    
    
@login_required
def eliminar_curso (request, curso_nombre):

    
    curso = Curso.objects.get (id= curso_nombre)
    curso.delete()
    
    cursos = Curso.objects.all ()

    contexto = {"cursos" : cursos
                }
    
    return render (request, "institutos/cursos/cursosadm.html", contexto )



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

def agregar_profesor (request):

    formulario = ProfesorFormulario(request.POST)
        
    if formulario.is_valid():
        
        informacion = formulario.cleaned_data
            
        profesor = Profesor (nombre= informacion ['nombre'], apellido = informacion ['apellido'], email = informacion ['email'], profesion = informacion ['profesion']) 
        
        profesor.save()
    
        return render (request, "institutos/profesores/lista_profesores.html")
    
    else:   
        
        formulario = ProfesorFormulario()
        
        return render (request, "institutos/profesores/agregar_profesor.html",  {"formulario":formulario})

    


  
class ProfesorDetalle (DetailView):
    model = Profesor
    template_name = "institutos/profesores/profesor_detalle.html"

class EliminarProfesor (DeleteView):
    model = Profesor
    success_url= "/appinstituto/profesores/"
    template_name = "institutos/profesores/eliminar_profesor.html"
        
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

        if formulario_pagos.is_valid():

            data = formulario_pagos.cleaned_data

            Infopago = Pago(Nombre=data['Nombre_del_estudiante'], Apellido=data['Apellido_del_estudiante'], Email=data['Email_del_estudiante'], Dni=data['Numero_de_documento_de_Identidad'], Curso=data['Curso_abonado'], Telefono=data['Telefono_WhastApp'])

            Infopago.save()

            return render(request, "institutos/index.html")

    else:
        formulario_pagos = InformePagoFormulario()

        return render(request, "institutos/pagos.html", {'formularioP':formulario_pagos})


def comentario_nuevo(request):

    if request.method == "POST":

        formulario_comentarios = Comentario_nuevo(request.POST)

        if formulario_comentarios.is_valid():

            com = formulario_comentarios.cleaned_data

            coment = Comentarios(Tu_comentario=com['Tu_comentario'], Valoracion=com['Valoracion'], Email=com['Email'], Seleccionar_curso=com['Seleccionar_curso'], Tu_nombre=com['Tu_nombre'])

            coment.save()

            return render(request, "institutos/index.html")

    else:
        formulario_comentarios = Comentario_nuevo()

        return render(request, "institutos/comentario_nuevo.html", {'formularioCom':formulario_comentarios})

def comentarios(request):

    return render(request, "institutos/comentarios.html")
