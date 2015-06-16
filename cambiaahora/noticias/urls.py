from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^noticias/$', views.ListNewsView.as_view(), name='noticias-list'),
	url(r'^noticias/(?P<slug>[-\w]+)/$', views.DetailNewsView.as_view(), name='noticia-detail'),
	#url(r'^contactenos/$', views.ContactView.as_view(), name='contactenos'),
    
]