from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def iniciar_sesion (request):
    if request.method == "GET":
        formulario = AuthenticationForm()
        return render (request, "seguridad/inicio_sesion.html", {"formulario": formulario})
    else:
        formulario = AuthenticationForm (request, data=request.POST)
        
        if formulario.is_valid():
            data=formulario.cleaned_data
            
            user = authenticate (username=data["username"], password=data["password"])
            
            if user is not None:
                login (request, user)
                return redirect ("institutos/index.html")
            
        return HttpResponse ("Formulario no valido") # Sino se puede renderizar el login pero mepa que la view de eso todavia no esta hecha.
    # en afterclass del 12/8 a los 36 min muestra formulario de errores
    
    
def registrar_usuario (request):
    if request.method == "GET":
        formulario = UserCreationForm()  
        return render (request, "seguridad/registros.html", {"formulario": formulario})  

    else: 
        formulario = UserCreationForm(request.POST)
        
        if formulario.is_valid():
            formulario.save()
            
    return redirect (request, "inicio", {"mensaje": "USUARIO CREADO "})


def deslogueo (request):
    
    
    logout(request)
    return redirect ("inicio")