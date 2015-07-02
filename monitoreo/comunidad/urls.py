from django.conf.urls import *
from .views import *

urlpatterns = patterns('monitoreo.comunidad.views',
	url(r'^$', MonitoreoView.as_view(), name='monitoreo'),
	url(r'^mapa/$', 'obtener_lista', name='obtener-lista'),
	url(r'^datos/$', DatosView.as_view(), name='obtener-datos'),
)