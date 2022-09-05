from django.urls import path
from institutos.views import *


urlpatterns = [
    #generico
    path("", inicio, name='inicio'),
    path("comentarios/", comentarios, name='comentarios'),
    path ("buscar/", buscar, name='buscar'), 
    path ("pagos/", Pagos, name= 'formulariopagos'),
    #profesores
    path ("profesores/", ProfesorLista.as_view(), name="profesores"),
    path("agregar_profesor", AgregarProfesor.as_view(), name="agregar_profesor"),
    #usuario
    path ("logout/",LogoutView.as_view(template_name="institutos/usuario/cerrar_sesion.html"), name ="Logout"),
    path ("editar_usuario/", editar_usuario, name= "editar_usuario"),
    path("login/", login, name='login'),
    path("perfil/", usuario, name='perfil'),
    path("registrar/", registrar, name="registrar"),
    #cursos
    path("fisica/", fisica, name= 'fisica'),
    path("quimica/", quimica, name= 'quimica'),
    path("matematica/", matematica, name= 'matematica'),
    path("cursos/", cursos, name='info_cursos'),
    path ("crear_cursos/", crear_cursos, name="crear_cursos"),
    #campus
    path("campus/", campus, name='mis cursos'),
]