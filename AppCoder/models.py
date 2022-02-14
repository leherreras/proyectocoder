from django.db import models
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Curso(models.Model):

    nombre = models.CharField(max_length=40, null=False)
    camada = models.IntegerField()

    def __str__(self):
        return f'El nombre del curso es: {self.nombre} con numero de camada: {self.camada}'


class Estudiante(models.Model):

    nombre = models.CharField(max_length=40)
    aplellido = models.CharField(max_length=40)
    email = models.EmailField()


class Profesor(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profecion = models.CharField(max_length=40)


class Entregable(models.Model):

    nombre = models.CharField(max_length=40)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()


# Create your models here.
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)