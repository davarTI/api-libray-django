from django.db import models
from django.utils import timezone

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    correo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return ('%s %s' % (self.nombre, self.apellido))

