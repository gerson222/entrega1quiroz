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
    path("cursos/", cursos, name='info cursos'),
    path("leer_cursos/", leer_cursos, name='leer_cursos'),
    path("crear_curso/", crear_curso, name='crear_curso'),
    # path("curso_formulario/", curso_formulario, name='curso_formulario'),
    path("buscar_curso/", buscar_curso, name='buscar_curso'),
    path ("buscar/", buscar, name='buscar'),
    path("borrar_curso/", borrar_curso, name='borrar_curso')
]