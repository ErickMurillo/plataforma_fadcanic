"""actividades URL Configuration

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
from django.conf.urls import include, url, patterns
from django.contrib import admin
from plataforma_fadcanic.settings import MEDIA_ROOT, DEBUG


urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'actividades.views.home', name='home'),    
    url(r'^xls/$', 'actividades.utils.save_as_xls', name='save_xls' ),
    url(r'^report/$', 'actividades.contraparte.views.generate_report', name='generate_report' ),    
    url(r'^ajax/proyectos/$', 'actividades.contraparte.views.get_proyectos', name='get_proyectos' ),
    url(r'^ajax/salidas/$', 'actividades.contraparte.views.get_salidas', name='get_salidas' ),
    url(r'^fillout/', include('actividades.formutils.urls')),
    url(r'^proyecto/', include('actividades.contraparte.urls')),
    url(r'^programa/', include('actividades.fadcanic.urls')),    
    
    url(r'^chaining/', include('smart_selects.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^i/(?P<hash>\w+)$', 'actividades.contraparte.views.shortview', name='shortview'),
]

urlpatterns += patterns('actividades.contraparte.views',    
    url(r'^variables/$', 'variables', name='variables'),
    url(r'^variables/output/$', 'output', name='output'),    
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

if DEBUG:
    urlpatterns += patterns('',
                (r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
                )




