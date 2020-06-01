# -*- coding: utf-8 -*-

from django.db import models


# Create your models here.

class Parametro(models.Model):
    descripcion = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits = 5, decimal_places = 2)
    valido = models.CharField(max_length=1)
    fecha = models.DateTimeField(blank=True, null=True, )
    usuario = models.CharField(max_length=100)


class Kilometro(models.Model):
    fechaini = models.DateTimeField(auto_now=True)
    kmini = models.IntegerField()
    fechafin = models.DateTimeField(auto_now=True)
    kmfin = models.IntegerField()
    TOPIC_CHOICES = (
        ('1', 'Didi'),
        ('2', 'Uber'),
        ('3', 'Cabify'),
        ('99', 'Familiar'),
    )
    tipo = models.CharField(
        max_length=2,
        choices=TOPIC_CHOICES,
        default='99',
    )
    entrada = models.IntegerField()
    vehiculo = models.CharField(max_length=100)
    parametro = models.ForeignKey(Parametro, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=100)







