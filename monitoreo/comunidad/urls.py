from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^$', MonitoreoView.as_view(), name='monitoreo'),
]