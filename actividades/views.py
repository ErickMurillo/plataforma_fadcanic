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
def monitoreo_index(request,template='monitoreo_actividades/index.html'):
	masculino = Actividad.objects.all().aggregate(Sum('hombres'))
	femenino = Actividad.objects.all().aggregate(Sum('mujeres'))
	actividades = Actividad.objects.all().count()

	return render(request, template, locals())


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

def datos(request,template='monitoreo_actividades/datos.html'):
	lista = []
	for x in Actividad.objects.all():
		municipios = Municipio.objects.filter(nombre=x.municipio.nombre).distinct()
		lista.append(municipios)

	return render(request, template, locals())