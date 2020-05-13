# -*- coding: utf-8 -*-

from django.db import models


# Create your models here.

class Parametro(models.Model):
    descripcion = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits = 5, decimal_places = 2)
    valido = models.CharField(max_length=1)
    fecha = models.DateTimeField(blank=True, null=True, )


class Kilometro(models.Model):
    fechaini = models.DateTimeField(auto_now=True)
    kmini = models.IntegerField()
    fechafin = models.DateTimeField(auto_now=True)
    kmfin = models.IntegerField()
    tipo = models.CharField(max_length=1)
    entrada = models.IntegerField()




