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



class Tipo (models.Model):
    txtDescripcion = models.CharField(max_length=100)
    txtColor = models.CharField(max_length=45)
    fecha = models.DateField()
    usuario = models.CharField(max_length=45)

    def __str__(self):
        """
        Cadena para representar el objeto MyModelName (en el sitio de Admin, etc.)
        """
        return self.txtDescripcion


class Porcion (models.Model):
    txtMedida = models.CharField(max_length=45)
    fecha = models.DateField()
    usuario = models.CharField(max_length=45)

    def __str__(self):
        """
        Cadena para representar el objeto MyModelName (en el sitio de Admin, etc.)
        """
        return self.txtMedida


class Alimento (models.Model):
    txtNomAlim = models.CharField(max_length=100)
    txtDescrip = models.CharField(max_length=100)
    intKCal = models.IntegerField()
    usuario = models.CharField(max_length=45)
    fecha = models.DateField()
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    porcion = models.ForeignKey(Porcion, on_delete=models.CASCADE)
    fuente = models.CharField(max_length=200)
    cantpor = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        """
        Cadena para representar el objeto MyModelName (en el sitio de Admin, etc.)
        """
        return self.txtNomAlim + ', ' + str(self.cantpor)+' '+ str(self.porcion)+ ', kcal: '+ str(self.intKCal) +'.'



class Aldia (models.Model):
    txtAldia = models.CharField(max_length=45)
    fecha = models.DateField()
    usuario = models.CharField(max_length=45)

    def __str__(self):
        """
        Cadena para representar el objeto MyModelName (en el sitio de Admin, etc.)
        """
        return self.txtAldia

class Consumo (models.Model):
    fecha = models.DateTimeField()
    usuario = models.CharField(max_length=45)
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE)
    aldia = models.ForeignKey(Aldia, on_delete=models.CASCADE)
    porciones = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        """
        Cadena para representar el objeto MyModelName (en el sitio de Admin, etc.)
        """
        return str(self.aldia) + ' - ' + str(self.porciones) + ' porciones de ' + str(self.alimento)

class Peso (models.Model):
    peso = models.DecimalField(max_digits = 5, decimal_places = 2)
    fecha = models.DateTimeField()
    usuario = models.CharField(max_length=45)

    def __str__(self):
        """
        Cadena para representar el objeto MyModelName (en el sitio de Admin, etc.)
        """
        return self.peso



