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
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from cambiaahora.noticias import urls as noticias_urls
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
	url(r'', include(noticias_urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^actividades/', include('actividades.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'actividades/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'actividades/logout.html'}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    url(r'^noticias/', include(noticias_urls)),
)