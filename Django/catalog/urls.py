from django.urls import re_path as url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index')   # cuando la petición sea NADA dispara la función index del módulo views
]
