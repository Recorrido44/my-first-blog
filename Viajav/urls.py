"""Viajav URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))

    from django.conf.urls import url, include
    from django.views.generic import TemplateView

    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'', TemplateView.as_view(template_name='home.html'), name='home'),
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required



from gestion_viaje import views, api

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(('seguridad.urls','seguridad'),namespace='seguridad')),
    url(r'^viaje/nuevo/$', views.Km_Nuevo_Vista.as_view(), name='kilometro_nuevo'),
    url(r'^viaje/final/(?P<pk>[0-9]+)/$', views.Km_Final_Vista.as_view(), name='kilometro_final'),
    url(r'^viaje/resumen/$', views.Km_Resumen_Vista.as_view(), name='kilometro_resumen'),
    url(r'^viaje/finalizar/$', views.Km_Finalizar_Vista.as_view(), name='kilometro_finalizar'),
    url(r'^viaje/borrar/(?P<pk>[0-9]+)/$', views.Km_Eliminar_Vista.as_view(), name='kilometro_borrar'),
    url(r'^alimento/nuevo/$', views.Alimento_Nuevo_Vista.as_view(), name='alimento_nuevo'),
    url(r'^alimento/consumo/$', views.Alimento_Consumo_Vista.as_view(), name='consumo_registro'),
    url(r'^alimento/resumen/$', views.Alimento_Resumen_Vista.as_view(), name='consumo_resumen'),
    url(r'^alimento/verconsumo/$', views.Alimento_Verconsumo_Vista.as_view(), name='consumo_mostrar'),
    url(r'^alimento/borrar/(?P<pk>[0-9]+)/$', views.Alimento_Eliminar_Vista.as_view(), name='consumo_borrar'),
    url(r'^peso/resumen/$', login_required(views.Peso_Resumen_Vista.as_view()), name='peso_resumen'),
    url(r'^peso/nuevo/$', views.Peso_Nuevo_Vista.as_view(), name='peso_nuevo'),
    url(r'^peso/borrar/(?P<pk>[0-9]+)/$', views.Peso_Eliminar_Vista.as_view(), name='peso_borrar'),
]
