from django.db import models

class Paises(models.Model):
    nombrecompleto = models.CharField(max_length=255)
    idioma = models.CharField(max_length=255)
    poblaciontotal = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    activo = models.BooleanField(default=True)
    class Meta:
        db_table= "paises"

