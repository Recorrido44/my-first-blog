# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Parametro, Kilometro, Tipo, Porcion, Alimento, Aldia, Consumo, Peso

admin.site.register(Parametro)
admin.site.register(Kilometro)

admin.site.register(Tipo)
admin.site.register(Porcion)
admin.site.register(Alimento)
admin.site.register(Aldia)
admin.site.register(Consumo)
admin.site.register(Peso)

# Register your models here.
