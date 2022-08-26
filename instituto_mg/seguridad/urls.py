from django.urls import path
from seguridad.views import iniciar_sesion, registrar_usuario

urlpatterns = [
    path ("login/", iniciar_sesion, name= "Inicio_sesion"),
    path("registrar/", registrar_usuario, name="registrar"),
]
