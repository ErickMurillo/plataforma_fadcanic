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
from mapeo import urls as mapeo_urls
from django.conf.urls.i18n import i18n_patterns
from cambiaahora.noticias import views as viewsNews
from actividades.views import *
from rest_framework import routers
from django.views.generic import TemplateView
from violencia_juvenil import urls as violencia_juvenil_urls
from actividades.contraparte.views import BusquedaView
from biblioteca import urls as biblioteca_urls

admin.site.site_header = "FADCANIC administración"
admin.site.site_title = "FADCANIC sitio admin"

router = routers.DefaultRouter()
router.register(r'news', viewsNews.NewsViewSet)


urlpatterns = [

	url(r'', include('cambiaahora.noticias.urls')),
    url(r'^multimedias/', include(multimedias_urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^actividades/', include('actividades.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'actividades/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'actividades/logout.html'}),
    url(r'^admin/comite/$', BusquedaView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns('',
    url(r'', include('cambiaahora.noticias.urls')),
    url(r'^noticias/', include(noticias_urls)),
    url(r'^multimedias/', include(multimedias_urls)),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('actividades.views',
    url(r'^monitoreo/$', TemplateView.as_view(template_name="panel/base.html"), name='monitoreo-panel'),
    url(r'^cambiaahora_app/$', TemplateView.as_view(template_name="panel/cambiaahoraapp.html"), name='cambiaahora-app'),
    url(r'^mapa/$', 'obtener_lista', name='obtener-lista'),
    url(r'^municipios/$', 'datos', name='obtener-datos'),
    url(r'^jsonnews/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

#mapeo
urlpatterns += patterns('mapeo.views',
    url(r'^mapeo/', include(mapeo_urls)),
)

#violencia juvenil
urlpatterns += patterns('violencia_juvenil.views',
    url(r'^encuesta_cap/', include(violencia_juvenil_urls)),
    url(r'^ajax/munis/$', 'get_munis', name='get-munis'),
)

urlpatterns += patterns('biblioteca.views',
    url(r'^biblioteca/', include(biblioteca_urls)),
)

urlpatterns += staticfiles_urlpatterns()
