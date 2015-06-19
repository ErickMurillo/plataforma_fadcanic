from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.MultimediaView.as_view(), name='index-multimedia'),
	url(r'^videos/$', views.ListVideosView.as_view(), name='videos'),
	url(r'^fotos/$', views.ListFotosView.as_view(), name='fotos'),
	url(r'^documentales/$', views.ListDocumentalesView.as_view(), name='documentales'),
	url(r'^audios/$', views.ListAudiosView.as_view(), name='audios'),

    
]