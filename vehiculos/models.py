from django.db import models

# Create your models here.


class Vehiculo(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    tipo = models.CharField(max_length=25)
    marca = models.CharField(max_length=25)
    modelo = models.CharField(max_length=25)
    version = models.FloatField()
    placa = models.CharField(max_length=25)
    kilometraje = models.IntegerField()
