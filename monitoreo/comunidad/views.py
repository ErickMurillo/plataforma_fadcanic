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