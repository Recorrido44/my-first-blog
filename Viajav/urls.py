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
"""
from django.conf.urls import url
from django.contrib import admin
from gestion_viaje import views




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^viaje/nuevo/$', views.Km_Nuevo_Vista.as_view(), name='kilometro_nuevo'),
    url(r'^viaje/final/(?P<pk>[0-9]+)/$', views.Km_Final_Vista.as_view(), name='kilometro_final'),
    url(r'^viaje/resumen/$', views.Km_Resumen_Vista.as_view(), name='kilometro_resumen'),
    url(r'^viaje/finalizar/$', views.Km_Finalizar_Vista.as_view(), name='kilometro_finalizar'),
    url(r'^viaje/borrar/(?P<pk>[0-9]+)/$', views.Km_Eliminar_Vista.as_view(), name='kilometro_borrar'),
    url(r'^alimento/nuevo/$', views.Alimento_Nuevo_Vista.as_view(), name='alimento_nuevo'),
    url(r'^alimento/consumo/$', views.Alimento_Consumo_Vista.as_view(), name='alimento_consumo'),
    url(r'^alimento/resumen/$', views.Alimento_Resumen_Vista.as_view(), name='consumo_resumen'),

]
