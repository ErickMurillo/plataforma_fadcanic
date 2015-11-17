from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.IndexMapeo.as_view(), name='index-mapeo'),   
]