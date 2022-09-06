from django.urls import path
from institutos.views import *


urlpatterns = [
    #generico
    path("", inicio, name='inicio'),
    path("comentarios/", comentarios, name='comentarios'),
    path ("buscar/", buscar, name='buscar'), 
    path ("pagos/", Pagos, name= 'formulariopagos'),
    path ("buscar/", buscar, name='buscar'),
    #profesores
    path ("profesores/", ProfesorLista.as_view(), name="profesores"),
    path ("eliminar_profesor/<pk>", EliminarProfesor.as_view(), name ="eliminar_profesor"),
    path("profesor_detalle/<pk>", ProfesorDetalle.as_view(), name="profesor_detalle"),
    path ("agregar_profesor/", agregar_profesor, name ="Agregar"),
    
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
    path("info_cursos/", info_cursos, name='info_cursos'),
    #campus
    path("campus/", campus, name='campus'),
    path("cursosadm/", cursos, name='cursosadm'),
    path ("crear_cursos/", crear_cursos, name="crear_cursos"),
    path("actualizar_curso/", actualizar_curso, name = "actualizar"),
    path ("eliminar_curso", eliminar_curso, name = "eliminar"),
]