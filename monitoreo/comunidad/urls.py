from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.MonitoreoView.as_view(), name='monitoreo'),
	# url(r'^lang/(?P<lang_code>\w+)/$', views.set_lang, name='set_lang'),
	# url(r'^noticias/$', views.ListNewsView.as_view(), name='noticias-list'),
	# url(r'^noticias/(?P<slug>[-\w]+)/$', views.DetailNewsView.as_view(), name='noticia-detail'),
	#url(r'^contactenos/$', views.ContactView.as_view(), name='contactenos'),
    
]