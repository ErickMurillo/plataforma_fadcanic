from django.conf.urls import *
from . import views

urlpatterns = patterns('mapeo.views',
	#url(r'^$', views.IndexMapeo.as_view(), name='index-mapeo'), 
	url(r'^$', 'index', name='index-mapeo'),
	url(r'^detalle/(?P<slug>[\w-]+)/$', 'DetailOrg', name='detail-org')
)