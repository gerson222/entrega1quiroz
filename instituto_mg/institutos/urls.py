from django.urls import path
from institutos.views import *


urlpatterns = [
    path("", inicio, name='inicio'),
    path("comentarios/", comentarios, name='comentarios'),
    path("fisica/", fisica, name= 'fisica'),
    path("quimica/", quimica, name= 'quimica'),
    path("matematica/", matematica, name= 'matematica'),
    path("perfil/", usuario, name='perfil'),
    path("campus/", campus, name='mis cursos'),
    path("login/", login, name='login'),
    path("registrar/", registrar, name="registrar"),
    path ("editar_usuario/", editar_usuario, name= "editar_usuario"),
    path ("logout/",LogoutView.as_view(template_name="institutos/usuario/cerrar_sesion.html"), name ="Logout"),
    path("cursos/", cursos, name='info_cursos'),
    path ("crear_cursos/", crear_cursos, name="crear_cursos"),
    path("actualizar_curso/", actualizar_curso, name = "actualizar"),
    path ("eliminar_curso", eliminar_curso, name = "eliminar"),
    path ("buscar/", buscar, name='buscar'), 
    path ("profesores/", ProfesorLista.as_view(), name="profesores"),
    path ("eliminar_profesor/<pk>", EliminarProfesor.as_view(), name ="eliminar_profesor"),
    path("agregar_profesor/", AgregarProfesor.as_view(), name="agregar_profesor"),
    path("profesor_detalle/<pk>", ProfesorDetalle.as_view(), name="profesor_detalle"),
    path ("pagos/", Pagos, name= 'formulariopagos'),

]