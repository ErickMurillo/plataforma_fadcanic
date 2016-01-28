from django.conf.urls import *
from . import views

urlpatterns = patterns('violencia_juvenil.views',
	url(r'^$', 'index', name='index-violencia'),
	url(r'^mapa/$', 'obtener_lista', name='obtener-lista-violencia'),
	url(r'^consulta/$', 'consulta', name='consulta-violencia'),
    url(r'^dashboard/',  'dashboard', name='dashboard-violencia'),
    url(r'^conocimiento/',  'conocimiento', name='conocimiento'),
    url(r'^actitud/',  'actitud', name='actitud'),
)