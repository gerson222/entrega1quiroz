from django.urls import path
from seguridad.views import iniciar_sesion, deslogueo

urlpatterns = [
    path ("iniciar_sesion/", iniciar_sesion, name= "Inicio_sesion"),
    path("deslogueo/", deslogueo, name="cerrar_sesion"),
    
]
