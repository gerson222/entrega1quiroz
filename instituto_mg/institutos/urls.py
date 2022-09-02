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
    path ("logout/",LogoutView.as_view(template_name="institutos/usuario/cerrar_sesion.html"), name ="Logout"),
    path("cursos/", cursos, name='info_cursos'),
    path("leer_cursos/", leer_cursos, name='leer_cursos'),
    path("crear_cursos/", crear_cursos, name='crear_cursos'),
    # path("curso_formulario/", curso_formulario, name='curso_formulario'),
    path ("buscar/", buscar, name='buscar'),
    path("cursos/<pk>", CursoDetalle.as_view(), name="curso_detalle"),
    path("curso/crear", CrearCurso.as_view(), name="crear_curso"),
    path("cursos/actualizar/<pk>", ActualizarCurso.as_view(), name="actualizar_curso"),
    path ("cursos/borrar/<pk>", CursoBorrar.as_view(), name="cursos_borrar"),
    path ("borrar_curso/<id_curso>", borrar_curso, name='borrar_curso'),
    path ("actualizar_curso/<id_curso>", actualizar_curso, name= "actualizar_curso"),
    path ("profesores/", ProfesorLista.as_view(), name="profesores"),
    path("agregar_profesor", AgregarProfesor.as_view(), name="agregar_profesor"),
    path("registrar/", registrar, name="registrar"),
    path ("pagos/", Pagos, name= 'formulariopagos'),
    path ("editar_usuario/", editar_usuario, name= "editar_usuario")
]