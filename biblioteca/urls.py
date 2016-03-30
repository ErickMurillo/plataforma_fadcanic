from django.conf.urls import *
from . import views

urlpatterns = patterns('biblioteca.views',
	url(r'^$', 'index', name='index-biblioteca'),
	url(r'^detalle/(?P<slug>[-\w]+)/$', 'detalle_guia', name='detalle-guia'),
	url(r'^busqueda/$', 'buscar_guia', name='buscar-guia'),

)
