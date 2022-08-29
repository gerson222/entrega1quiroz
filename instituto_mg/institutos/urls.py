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
]