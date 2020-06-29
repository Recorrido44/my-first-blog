from datetime import datetime

from django import forms
from django.forms import ModelForm, Textarea, DateTimeInput

from gestion_viaje.models import Parametro, Kilometro, Alimento, Consumo, Peso
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



class Alimento_Nuevo_Form(ModelForm):
    class Meta:
        model = Alimento
        fields = ['txtNomAlim', 'txtDescrip', 'intKCal','tipo', 'cantpor', 'porcion', 'fuente', ]
        labels = {'txtNomAlim': ('Alimento nuevo'),
                  'txtDescrip': ('Descripciòn'),
                  'intKCal':('Calorìas'),
                  'tipo': ('Tipo'),
                  'porcion': ('Porciòn'),
                  'cantpor': ('Cantidad'),
                  'fuente': ('Fuente')
                  }
        widgets = {
            'txtDescrip': Textarea(attrs={'cols': 20, 'rows': 2}),
            'fuente': Textarea(attrs={'cols': 20, 'rows': 2}),

        }

class Alimento_Consumo_Form(ModelForm):
    class Meta:
        model = Consumo
        fields = ['alimento', 'aldia', 'porciones', ]
        labels = {'alimento': ('Alimento'),
                  'aldia': ('Cuando'),
                  'porciones':('Porciones consumidas'),
                  }


class Peso_Nuevo_Form(ModelForm):
    class Meta:
        model = Peso
        fields = ['peso', ]
        labels = {'peso': ('Mi peso de hoy es '),

                  }
