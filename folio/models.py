from django.db import models
from datetime import datetime
# Create your models here.

class Lista(models.Model):

    imagen = models.ImageField(upload_to="listafolio", null=True, blank=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    fecha = models.DateField()

    def _str_(self):
        return self.nombre

    