from datetime import datetime

from django import forms
from django.forms import ModelForm, Textarea, DateTimeInput

from gestion_viaje.models import Parametro, Kilometro
import datetime


class Km_Nuevo_Form(ModelForm):
    class Meta:
        model = Kilometro
        fields = ['kmini', 'tipo', 'vehiculo', ]
        labels = {'kmini': ('Kilometro inicial'),
                  'tipo': ('Tipo de viaje'),
                  'vehiculo':('Comentarios adicionales')}
        widgets = {
            'vehiculo': Textarea(attrs={'cols': 20, 'rows': 3}),
        }


class Km_Final_Form(ModelForm):
    class Meta:
        model = Kilometro
        fields = ['kmfin', 'entrada', ]
        labels = {'kmfin': ('Kilometro final'), }


