# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from actividades.contraparte.models import *
from django.db.models import Sum
import json as simplejson
from fadcanic.models import *
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    organizaciones = Organizacion.objects.all()
    return render_to_response('actividades/index.html', RequestContext(request, locals()))

#Monitoreo de actividades
class MonitoreoView(TemplateView):
    template_name = "monitoreo_actividades/index.html"

    def get_context_data(self, **kwargs):
        context = super(MonitoreoView, self).get_context_data(**kwargs)
        context['masculino'] = Actividad.objects.all().aggregate(Sum('hombres'))
        context['femenino'] = Actividad.objects.all().aggregate(Sum('mujeres'))
        context['actividades'] = Actividad.objects.all().count()
  
        return context

def obtener_lista(request):
    if request.is_ajax():
        lista = []
        for objeto in Actividad.objects.all():
            dicc = dict(nombre=objeto.municipio.nombre, id=objeto.id,
                        lon=float(objeto.municipio.longitud),
                        lat=float(objeto.municipio.latitud)
                        )
            lista.append(dicc)

        serializado = simplejson.dumps(lista)
        return HttpResponse(serializado, content_type='application/json')

class DatosView(TemplateView):
    template_name = 'monitoreo_actividades/datos.html'
