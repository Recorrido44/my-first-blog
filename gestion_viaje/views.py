# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import F
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from gestion_viaje.forms import Km_Nuevo_Form, Km_Final_Form, Alimento_Nuevo_Form, Alimento_Consumo_Form
from gestion_viaje.models import Parametro, Kilometro, Alimento, Consumo


class Km_Muestra_Vista(ListView):
    modelo = Kilometro
    template_name = 'km_muestra.html'

class Km_Nuevo_Vista(CreateView):
    model = Kilometro
    form_class = Km_Nuevo_Form
    template_name = 'km_nuevo.html'
    success_url = reverse_lazy('kilometro_resumen')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.entrada = 0
        self.object.kmfin = self.object.kmini
        self.object.fechaini = timezone.now()
        self.object.fechafin = timezone.now()
        self.object.parametro = Parametro.objects.get(pk=1)
        self.object.usuario = 'javier'
        self.object.save()

        return super(Km_Nuevo_Vista, self).form_valid(form)



class Km_Resumen_Vista(ListView):
    model = Kilometro
    template_name = 'km_resumen.html'
    def get_queryset(self):
        return Kilometro.objects.raw("SELECT id, fechafin, (kmfin-kmini) distancia, "
                                     " ((kmfin-kmini) / (select valor from gestion_viaje_parametro where id = 2 )) "
                                     " litros, "
                                     " ((kmfin-kmini)/ "
                                     " (select valor from gestion_viaje_parametro where id = 2 )) * "
                                     " (select valor from gestion_viaje_parametro where id = 1 ) gasto, "
                                     " entrada, "
                                     " entrada - (((kmfin-kmini)/ "
                                     " (select valor from gestion_viaje_parametro where id = 2 )) * "
                                     " (select valor from gestion_viaje_parametro where id = 1 )) ganancia, "
                                     " ((((kmfin-kmini)/ "
                                     " (select valor from gestion_viaje_parametro where id = 2 )) * "
                                     " (select valor from gestion_viaje_parametro where id = 1 ))*100) / entrada "
                                     " indica_gasto, tipo, substr (vehiculo,1,20) "
                                     " from gestion_viaje_kilometro"
                                     " where usuario like 'javier' "
                                     " and kmfin-kmini > 0 "
                                     " order by fechafin desc ")

class Km_Final_Vista(UpdateView):
    model = Kilometro
    form_class = Km_Final_Form
    template_name = 'km_final_form.html'
    success_url = reverse_lazy('kilometro_resumen')


class Km_Finalizar_Vista(ListView):
    model = Kilometro
    template_name = 'km_final_list.html'
    def get_queryset(self):
        return Kilometro.objects.filter(kmfin=F('kmini'))

class Km_Eliminar_Vista(DeleteView):
    model = Kilometro
    template_name = 'km_borrar.html'
    success_url = reverse_lazy('kilometro_resumen')

class Alimento_Nuevo_Vista(CreateView):
    model = Alimento
    form_class = Alimento_Nuevo_Form
    template_name = 'alimento_nuevo.html'
    success_url = reverse_lazy('consumo_resumen')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.fecha = timezone.now()
        self.object.usuario = 'adminjav'
        self.object.save()

        return super(Alimento_Nuevo_Vista, self).form_valid(form)



class Alimento_Consumo_Vista(CreateView):
    model = Consumo
    form_class = Alimento_Consumo_Form
    template_name = 'alimento_consumo.html'
    success_url = reverse_lazy('consumo_registro')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.fecha = timezone.now()
        self.object.usuario = 'adminjav'
        self.object.save()

        return super(Alimento_Consumo_Vista, self).form_valid(form)


class Alimento_Resumen_Vista(ListView):
    model = Consumo
    template_name = 'alimento_resumen.html'
    def get_queryset(self):
        return Consumo.objects.raw("select id,date(fecha), sum(porciones * ( "
                                                "select intKCal "
                                                "from  gestion_viaje_alimento "
                                                "where alimento_id = gestion_viaje_consumo.alimento_id"
                                                ") )calorias "
                                            " from gestion_viaje_consumo "
                                            " group by date(fecha)")


class Alimento_Verconsumo_Vista(ListView):
    model = Consumo
    template_name = 'consumo_muestra.html'


class Alimento_Eliminar_Vista(DeleteView):
    model = Consumo
    template_name = 'alimento_borrar.html'
    success_url = reverse_lazy('consumo_resumen')