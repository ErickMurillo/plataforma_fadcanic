# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from .models import *
from django.db.models import Sum
import json as simplejson


# Create your views here.
class MonitoreoView(TemplateView):
    template_name = "monitoreo_actividades/index.html"

    def get_context_data(self, **kwargs):
        context = super(MonitoreoView, self).get_context_data(**kwargs)
        context['masculino'] = Monitoreo.objects.all().aggregate(Sum('masculino'))
        context['femenino'] = Monitoreo.objects.all().aggregate(Sum('femenino'))
        context['actividades'] = Monitoreo.objects.all().count()
        

        #sumatoria municipios masculino
        context['sum_municipio_waspan'] =  Monitoreo.objects.filter(municipio__nombre='Waspán').aggregate(Sum('masculino'))
        context['sum_municipio_blue'] =  Monitoreo.objects.filter(municipio__nombre='Bluefields').aggregate(Sum('masculino'))
        context['sum_municipio_bilwi'] =  Monitoreo.objects.filter(municipio__nombre='Bilwi').aggregate(Sum('masculino'))
        context['sum_municipio_laguna'] = Monitoreo.objects.filter(municipio__nombre='Laguna de Perlas').aggregate(Sum('masculino'))
        context['sum_municipio_rio'] =  Monitoreo.objects.filter(municipio__nombre='Desembocadura de Río Grande').aggregate(Sum('masculino'))
        context['sum_municipio_sandino'] =  Monitoreo.objects.filter(municipio__nombre='Ciudad Sandino').aggregate(Sum('masculino'))
        context['sum_municipio_managua'] =  Monitoreo.objects.filter(municipio__nombre='Managua').aggregate(Sum('masculino'))
        context['sum_municipio_mateare'] =  Monitoreo.objects.filter(municipio__nombre='Mateare').aggregate(Sum('masculino'))
        
        #sumatoria municipios femenino
        context['sum_municipio_waspan_f'] =  Monitoreo.objects.filter(municipio__nombre='Waspán').aggregate(Sum('femenino'))
        context['sum_municipio_blue_f'] =  Monitoreo.objects.filter(municipio__nombre='Bluefields').aggregate(Sum('femenino'))
        context['sum_municipio_bilwi_f'] =  Monitoreo.objects.filter(municipio__nombre='Bilwi').aggregate(Sum('femenino'))
        context['sum_municipio_laguna_f'] = Monitoreo.objects.filter(municipio__nombre='Laguna de Perlas').aggregate(Sum('femenino'))
        context['sum_municipio_rio_f'] =  Monitoreo.objects.filter(municipio__nombre='Desembocadura de Río Grande').aggregate(Sum('femenino'))
        context['sum_municipio_sandino_f'] =  Monitoreo.objects.filter(municipio__nombre='Ciudad Sandino').aggregate(Sum('femenino'))
        context['sum_municipio_managua_f'] =  Monitoreo.objects.filter(municipio__nombre='Managua').aggregate(Sum('femenino'))
        context['sum_municipio_mateare_f'] =  Monitoreo.objects.filter(municipio__nombre='Mateare').aggregate(Sum('femenino'))

        return context

def obtener_lista(request):
    if request.is_ajax():
        lista = []
        for objeto in Monitoreo.objects.all():
            dicc = dict(nombre=objeto.municipio.nombre, id=objeto.id,
                        lon=float(objeto.municipio.longitud) ,
                        lat=float(objeto.municipio.latitud)
                        )
            lista.append(dicc)

        serializado = simplejson.dumps(lista)
        return HttpResponse(serializado, content_type='application/json')

class DatosView(TemplateView):
    template_name = 'monitoreo_actividades/datos.html'