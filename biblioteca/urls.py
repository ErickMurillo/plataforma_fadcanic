from django.conf.urls import *
from . import views

urlpatterns = patterns('biblioteca.views',
	url(r'^$', 'index', name='index-biblioteca'),
	url(r'^detalle/(?P<slug>[-\w]+)/$', 'detalle_guia', name='detalle-guia'),
	url(r'^busqueda/$', 'buscar_guia', name='buscar-guia'),
	url(r'^tema/(?P<id>[0-9]+)/$', 'buscar_tema', name='buscar-tema'),

)
