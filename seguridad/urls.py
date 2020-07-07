from django.conf.urls import  url
from django.contrib.auth.views import LogoutView

from seguridad.views import Login

urlpatterns = [
                url(r'^$', Login.as_view(), name="login"),
                url(r'^logout$', LogoutView.as_view(),  name='logout'),
            ]
