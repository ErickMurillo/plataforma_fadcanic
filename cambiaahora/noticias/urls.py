from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^lang/(?P<lang_code>\w+)/$', views.set_lang, name='set_lang'),
	url(r'^noticias/$', views.ListNewsView.as_view(), name='noticias-list'),
	url(r'^noticias/imagen/$', views.listar_noticias_imagen, name='noticias-imagen'),
	url(r'^noticias/video/$', views.listar_noticias_video, name='noticias-video'),
	url(r'^noticias/audio/$', views.listar_noticias_audio, name='noticias-audio'),
	url(r'^noticias/(?P<slug>[-\w]+)/$', views.DetailNewsView.as_view(), name='noticia-detail'),
	
	#url(r'^contactenos/$', views.ContactView.as_view(), name='contactenos'),
    #url(r'^jsonoticias/$', views.NoticiasList.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
