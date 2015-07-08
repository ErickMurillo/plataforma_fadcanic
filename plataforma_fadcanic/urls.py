# -*- coding: utf-8 -*-
"""plataforma_fadcanic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
import settings
from django.conf.urls.static import static
from cambiaahora.noticias import urls as noticias_urls
from cambiaahora.multimedias import urls as multimedias_urls
from django.conf.urls.i18n import i18n_patterns
from cambiaahora.noticias import views
from actividades.views import *

admin.site.site_header = "FADCANIC administración"
admin.site.site_title = "FADCANIC sitio admin"


urlpatterns = [
    
	url(r'', include('cambiaahora.noticias.urls')),
    url(r'^multimedias/', include(multimedias_urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^actividades/', include('actividades.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'actividades/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'actividades/logout.html'}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns('',
    url(r'', include('cambiaahora.noticias.urls')),
    url(r'^noticias/', include(noticias_urls)),
    url(r'^multimedias/', include(multimedias_urls)),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('actividades.views',
    url(r'^monitoreo/$', 'monitoreo_index', name='monitoreo'),
    url(r'^mapa/$', 'obtener_lista', name='obtener-lista'),
    url(r'^municipios/$', 'datos', name='obtener-datos'),
)

urlpatterns += staticfiles_urlpatterns()