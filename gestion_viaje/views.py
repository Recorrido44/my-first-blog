# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import decimal

from django.contrib.auth.decorators import permission_required
from django.db.models import F
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from gestion_viaje.forms import Km_Nuevo_Form, Km_Final_Form, Alimento_Nuevo_Form, Alimento_Consumo_Form, \
    Peso_Nuevo_Form, Ubicacion_Form, Measurements_Form, Alimento_Consumo_aldia_Form, Alimento_Alta_Form
from gestion_viaje.models import Parametro, Kilometro, Alimento, Consumo, Peso, Ubicacion, Measurements

from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.template import loader

class MyView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')

class HomePageView(TemplateView):

    template_name = "alimento.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['latest_alimento'] = Alimento.objects.all()[:5]
        return context

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
    success_url = reverse_lazy('alimento_nuevo')

    # @method_decorator(permission_required('gestion_viaje.add_alimento', reverse_lazy('consumo_resumen')))
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

class Alimento_Consumo_Alta(CreateView):
    model = Consumo
    form_class = Alimento_Alta_Form
    template_name = 'alimento_alta.html'
    success_url = reverse_lazy('consumo_registro_1')

    def mialta(request, offset,offset2):
        offset = int(offset)
        offset2= int (offset2)
        return reverse_lazy('consumo_alta_1')

    def form_valid(self, form,offset):
        self.object = form.save(commit=False)
        self.object.fecha = timezone.now()
        self.object.usuario = 'adminjav'
        assert False
        self.object.save()

        return super(Alimento_Consumo_Vista, self).form_valid(form)

class Alimento_Consumo_Aldia_Vista(ListView):
    model = Consumo
    form = Alimento_Alta_Form
    template_name = 'alimento_consumo_aldia.html'
    mitemp = ' 1 '
    success_url = reverse_lazy('consumo_registro_1')

    def get_queryset(self):
        return Consumo.objects.raw(" select s.id,t.alimento_id,t.txtNomAlim ,t.aldia_id,t.txtAldia "
                                   " FROM gestion_viaje_consumo s, ( "
                                   " select alimento_id,txtNomAlim ,aldia_id,txtAldia " 
                                     " from  gestion_viaje_consumo c, "
                                     " 		gestion_viaje_alimento a, "
                                     "  	gestion_viaje_aldia b " 
									 " where c.alimento_id=a.id " 
									 " and c.aldia_id=b.id " 
									 " and aldia_id = 5  "
                                     " and alimento_id = 11 "
									 " and c.fecha < date('now') "
                                     " group by alimento_id "
									 " EXCEPT "
                                     " select alimento_id,txtNomAlim ,aldia_id,txtAldia " 
                                     " from  gestion_viaje_consumo c, "
                                     " 		gestion_viaje_alimento a, "
                                     " 		gestion_viaje_aldia b " 
									 " where c.alimento_id=a.id " 
									 " and c.aldia_id=b.id " 
									 " and aldia_id = 5  "
                                     " and alimento_id = 11 "
									 " and c.fecha > date('now','-1 day') "
                                     " group by alimento_id "									 
									 " ORDER by txtNomAlim ) t "
                                     " group by t.alimento_id "									 
                                     " ORDER by txtNomAlim "
                                   )

    def carga(request):


        return HttpResponse(request.object_list)
        ## return HttpResponseRedirect(reverse_lazy('consumo_registro_1'))



class Alimento_Resumen_Vista(ListView):
    model = Consumo
    template_name = 'alimento_resumen.html'
    def get_queryset(self):
        return Consumo.objects.raw("select id,date(fecha,'localtime'), sum(porciones * ( "
                                                "select intKCal "
                                                "from  gestion_viaje_alimento ga "
                                                "where ga.id = gestion_viaje_consumo.alimento_id"
                                                ") )calorias "
                                            " from gestion_viaje_consumo "
                                            " group by date(fecha,'localtime')"
                                            " order by date(fecha,'localtime') desc")


class Alimento_Verconsumo_Vista(ListView):
    model = Consumo
    paginate_by = 10
    ordering = ['-fecha']
    template_name = 'consumo_muestra.html'


class Alimento_Eliminar_Vista(DeleteView):
    model = Consumo
    template_name = 'alimento_borrar.html'
    success_url = reverse_lazy('consumo_resumen')

class Peso_Resumen_Vista(ListView):
    model = Peso
    template_name = 'peso_resumen.html'


class Peso_Nuevo_Vista(CreateView):
    model = Peso
    form_class = Peso_Nuevo_Form
    template_name = 'peso_nuevo.html'
    success_url = reverse_lazy('peso_resumen')

    # @method_decorator(permission_required('gestion_viaje.add_peso', reverse_lazy('peso_resumen')))

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.fecha = timezone.now()
        self.object.usuario = 'adminjav'
        self.object.save()

        return super(Peso_Nuevo_Vista, self).form_valid(form)

class Peso_Eliminar_Vista(DeleteView):
    model = Peso
    template_name = 'peso_borrar.html'
    success_url = reverse_lazy('peso_resumen')

    @method_decorator(permission_required('gestion_viaje.delete_peso', reverse_lazy('peso_resumen')))

    def form_valid(self, form):

        return super(Peso_Nuevo_Vista, self).form_valid(form)

class Mapa_Ver(CreateView):
    model = Ubicacion
    form_class = Ubicacion_Form
    template_name = 'ubicacion_nuevo.html'
    success_url = reverse_lazy('peso_resumen')

    # @method_decorator(permission_required('gestion_viaje.add_peso', reverse_lazy('peso_resumen')))

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.fecha = timezone.now()
        self.object.usuario = 'adminjav'
        self.object.save()


class Mapa_VerMea(ListView):
    model = Measurements
    template_name = 'mainmea.html'


class Mapa_VerMeaNvo(CreateView):
    model = Measurements
    form_class = Measurements_Form
    template_name = 'mainmeanvo.html'
    success_url = reverse_lazy('mapa_verm')

    # @method_decorator(permission_required('gestion_viaje.add_peso', reverse_lazy('peso_resumen')))

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.location = 'CDMX'
        self.object.distance = 5000.00
        self.object.created = timezone.now()
        self.object.save()

        return super(Mapa_VerMeaNvo, self).form_valid(form)


class Mivista(View):

    # def current_datetime(request):
    def current_datetime(request):
        now = datetime.datetime.now()
        html = "<html><body>It is now %s.</body></html>" % now
        return HttpResponse(html)

    def hours_ahead(request, offset,offset2):
        offset = int(offset)
        # assert False
        dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
        html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
        return HttpResponse(html)

    def carga(request):
        consumo = Consumo()
        consumo.fecha = timezone.now()
        consumo.usuario = 'adminjav'
        consumo.alimento_id = 5
        consumo.aldia_id = 5
        consumo.porciones = 2
        consumo.save()

        template = loader.get_template('consumo_alta_1')
        context = {
            'new_consumo_id': consumo.pk,
        }
        return HttpResponse(template.render(context, request))
