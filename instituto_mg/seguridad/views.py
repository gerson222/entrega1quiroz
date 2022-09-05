from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView



# Create your views here.


def iniciar_sesion (request):
    if request.method == "GET":
        formulario = AuthenticationForm()
        
        contexto = {
            "formulario": formulario
        }
        return render (request, "seguridad/inicio_sesion.html", contexto )
    
    else:
        formulario = AuthenticationForm (request, data=request.POST)
        
        if formulario.is_valid():
            
            data=formulario.cleaned_data
            
            user = authenticate (username=data.get("username"), password=data.get("password"))
            
            if user is not None:
                login (request, user)
                return redirect ("campus")
            
            else:
                contexto = {
                    "error": "Credenciales no validas",
                    "formulario": formulario
                }
                return render(request, "seguridad/inicio_sesion.html", contexto)
        else:
            contexto = {
                "error": "Formulario NO valido",
                "formulario": formulario
            }
            return render(request, "seguridad/inicio_sesion.html", contexto)
            

def deslogueo (request):
    
    logout(request)
    return redirect ("inicio")

