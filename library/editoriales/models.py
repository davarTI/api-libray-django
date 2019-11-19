from django.db import models

# Create your models here.
class Editorial(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    website = models.CharField(max_length=80)
    ciudad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre