from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}-{self.camada}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()

class Pago(models.Model):
    Nombre= models.CharField(max_length=30)
    Apellido= models.CharField(max_length=30)
    Email= models.EmailField()
    Dni= models.IntegerField()
    Curso= models.CharField(max_length=50)
    Telefono= models.IntegerField()

    def __str__(self):
        return f"{self.Nombre} {self.Apellido} {self.Dni}"
    
class Comentarios(models.Model):
    Tu_nombre= models.CharField(max_length=30)
    Seleccionar_curso= models.DateField()
    Email= models.EmailField()
    Valoracion= models.BooleanField()
    Tu_comentario= models.BooleanField
    
    def __str__(self):
        return f"{self.Nombre} {self.Apellido} {self.Dni}"
    