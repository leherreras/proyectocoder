from django.db import models

# Create your models here.
class Curso(models.Model):

    nombre = models.CharField(max_length=40, null=False)
    camada = models.IntegerField(unique=True, null=False)

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