from datetime import datetime

from django import forms
from django.forms import ModelForm, Textarea, DateTimeInput

from gestion_viaje.models import Parametro, Kilometro
import datetime

TOPIC_CHOICES = (
    ('general', 'General enquiry'),
    ('bug', 'Bug report'),
    ('suggestion', 'Suggestion'),
)

class ContactForm(forms.Form):
    topic = forms.ChoiceField(choices=TOPIC_CHOICES)
    message = forms.CharField(widget=forms.Textarea())
    sender = forms.EmailField(required=False)


class ParametroForm(forms.Form):
    descripcion = forms.CharField(max_length=100)
    valor = forms.DecimalField(max_digits = 5, decimal_places = 2)
    valido = forms.CharField(max_length=1)
    fecha = forms.DateTimeField(initial=datetime.datetime.now())


# Create the form class.
class ParametroForm(ModelForm):
     class Meta:
        model = Parametro
        fields = ['descripcion', 'valor', 'fecha', 'valido']


class PostForm(ModelForm):
    class Meta:
        model = Parametro
        fields = ['descripcion', 'valor', ]

class ViajeForm(ModelForm):
    class Meta:
        model = Kilometro
        fields = ['kmini', 'tipo', ]




