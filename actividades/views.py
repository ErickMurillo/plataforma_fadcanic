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
		sum_menor_12 = Actividad.objects.filter(municipio__nombre=y.nombre).aggregate(Sum('menor_12'))
		sum_mayor_12 = Actividad.objects.filter(municipio__nombre=y.nombre).aggregate(Sum('mayor_12'))
		sum_mayor_18 = Actividad.objects.filter(municipio__nombre=y.nombre).aggregate(Sum('mayor_18'))
		sum_mayor_30 = Actividad.objects.filter(municipio__nombre=y.nombre).aggregate(Sum('mayor_30'))
		actividades = Actividad.objects.filter(municipio__nombre=y.nombre).count()

		if actividades != 0:
			municipios[y.nombre] = (actividades,sum_hombres,sum_mujeres,sum_menor_12,sum_mayor_12,
										sum_mayor_18,sum_mayor_30)

	# for xd,yd in municipios.items():
	# 	for asd in yd[1].values():
	# 		if asd != None:
	# 			print  '%s : %s' % (xd, asd)
	# 	for asd in yd[2].values():
	# 		if asd != None:
	# 			print  '%s : %s' % (xd, asd)
	# 	if yd[0] != 0:
	# 		print  'Actividades : %s' % (yd[2])

	return render(request, template, locals())