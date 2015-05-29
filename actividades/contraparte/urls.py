from django.conf.urls import *

urlpatterns = patterns('actividades.contraparte.views',    
    url(r'^$', 'filtro_proyecto', name='filtro_proyecto'),
)