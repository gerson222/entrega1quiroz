from django.urls import path
from seguridad.views import iniciar_sesion, deslogueo, mensajes



urlpatterns = [
    path ("iniciar_sesion/", iniciar_sesion, name= "Inicio_sesion"),
    path("deslogueo/", deslogueo, name="cerrar_sesion"),
    path ("mensajes/", mensajes, name = "Mensajes")
]



