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
	municipios = {}
	for y in Municipio.objects.all():
		sum_hombres = Actividad.objects.filter(municipio__nombre=y.nombre).aggregate(Sum('hombres'))
		sum_mujeres = Actividad.objects.filter(municipio__nombre=y.nombre).aggregate(Sum('mujeres'))
		#edad
		sum_menor_12 = Actividad.objects.filter(municipio__nombre=y.nombre).aggregate(Sum('menor_12'))
		sum_mayor_12 = Actividad.objects.filter(municipio__nombre=y.nombre).aggregate(Sum('mayor_12'))
		sum_mayor_18 = Actividad.objects.filter(municipio__nombre=y.nombre).aggregate(Sum('mayor_18'))
		sum_mayor_30 = Actividad.objects.filter(municipio__nombre=y.nombre).aggregate(Sum('mayor_30'))
		#identidad etnica
		sum_creole = Actividad.objects.filter(municipio__nombre=y.nombre).aggregate(Sum('creole'))
		sum_miskito = Actividad.objects.filter(municipio__nombre=y.nombre).aggregate(Sum('miskito'))
		sum_ulwa = Actividad.objects.filter(municipio__nombre=y.nombre).aggregate(Sum('ulwa'))
		sum_rama = Actividad.objects.filter(municipio__nombre=y.nombre).aggregate(Sum('rama'))
		sum_mestizo = Actividad.objects.filter(municipio__nombre=y.nombre).aggregate(Sum('mestizo'))
		sum_mayagna = Actividad.objects.filter(municipio__nombre=y.nombre).aggregate(Sum('mayagna'))
		sum_garifuna = Actividad.objects.filter(municipio__nombre=y.nombre).aggregate(Sum('garifuna'))
		sum_extranjero = Actividad.objects.filter(municipio__nombre=y.nombre).aggregate(Sum('extranjero'))
		#tipos de actores
		sum_estudiante = Actividad.objects.filter(municipio__nombre=y.nombre).aggregate(Sum('estudiante'))
		sum_docente = Actividad.objects.filter(municipio__nombre=y.nombre).aggregate(Sum('docente'))
		sum_periodista = Actividad.objects.filter(municipio__nombre=y.nombre).aggregate(Sum('periodista'))
		sum_lideres = Actividad.objects.filter(municipio__nombre=y.nombre).aggregate(Sum('lideres'))
		sum_representantes = Actividad.objects.filter(municipio__nombre=y.nombre).aggregate(Sum('representantes'))
		sum_autoridades = Actividad.objects.filter(municipio__nombre=y.nombre).aggregate(Sum('autoridades'))
		sum_comunitarios = Actividad.objects.filter(municipio__nombre=y.nombre).aggregate(Sum('comunitarios'))

		actividades = Actividad.objects.filter(municipio__nombre=y.nombre).count()

		if actividades != 0:
			municipios[y.nombre] = (actividades,sum_hombres,sum_mujeres,sum_menor_12,sum_mayor_12,
										sum_mayor_18,sum_mayor_30,sum_creole,sum_miskito,sum_ulwa,
										sum_rama,sum_mestizo,sum_mayagna,sum_garifuna,sum_extranjero,
										sum_estudiante,sum_docente,sum_periodista,sum_lideres,
										sum_representantes,sum_autoridades,sum_comunitarios)

	return render(request, template, locals())