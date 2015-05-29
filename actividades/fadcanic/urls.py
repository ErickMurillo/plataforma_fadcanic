from django.conf.urls import *

urlpatterns = patterns('actividades.fadcanic.views',    
    url(r'^$', 'filtro_programa', name='filtro_programa'),    
)