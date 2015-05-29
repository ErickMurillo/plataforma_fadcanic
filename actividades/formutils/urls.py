from django.conf.urls import *

urlpatterns = patterns('actividades.formutils.views',    
    url(r'^$', 'fill', name='fill'),
)