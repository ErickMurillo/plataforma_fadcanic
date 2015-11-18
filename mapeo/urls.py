from django.conf.urls import *
from . import views

urlpatterns = [
	url(r'^$', views.IndexMapeo.as_view(), name='index-mapeo'), 
	url(r'^detalle/(?P<slug>[\w-]+)/$', views.DetailOrg.as_view(), name='detail-org')
]