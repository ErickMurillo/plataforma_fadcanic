from django.conf.urls import *
from . import views

urlpatterns = patterns('biblioteca.views',
	url(r'^$', 'index', name='index-biblioteca'),
	url(r'^detalle$', 'bdetalle', name='bdetalle-biblioteca'),

)
