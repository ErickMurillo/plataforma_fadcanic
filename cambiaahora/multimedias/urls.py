from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.MultimediaView.as_view(), name='index-multimedia'),
	url(r'^videos/$', views.ListVideosView.as_view(), name='videos'),
	url(r'^videos/(?P<pk>[0-9]+)/$', views.DetailVideosView.as_view(), name='videos-detail'),
	url(r'^fotos/$', views.ListFotosView.as_view(), name='fotos'),
	url(r'^fotos/(?P<pk>[0-9]+)/$', views.DetailFotosView.as_view(), name='fotos-detail'),
	url(r'^documentales/$', views.ListDocumentalesView.as_view(), name='documentales'),
	url(r'^documentales/(?P<pk>[0-9]+)/$', views.DetailDocumentalView.as_view(), name='documental-detail'),
	url(r'^audios/$', views.ListAudiosView.as_view(), name='audios'),
	url(r'^audios/(?P<pk>[0-9]+)/$', views.DetailAudiosView.as_view(), name='audios-detail'),
    
]