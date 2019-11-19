from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from autores.models import Autor
from editoriales.models import Editorial
import datetime

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    autores = models.ManyToManyField(Autor)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    fecha_pub = models.DateTimeField('date published', default=timezone.now())

    def __str__(self):
        return self.titulo
