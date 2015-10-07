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
from .forms import *
from django.template import Context
import ho.pisa as pisa
import cStringIO as StringIO
import cgi
from django.template.loader import get_template

def _consulta_query(request):
	pass

@login_required
def home(request):
    organizaciones = Organizacion.objects.all()
    form = PanelForm()
    try:
        #salidas por organizacion
        personas_hombre_org = Actividad.objects.filter(tipo=1).aggregate(suma=Sum('hombres'))['suma']
        personas_mujer_org = Actividad.objects.filter(tipo=1).aggregate(suma=Sum('mujeres'))['suma']
        total_personas_org = personas_hombre_org + personas_mujer_org
        #salida por etnias
        creole_org = Actividad.objects.filter(tipo=1).aggregate(suma=Sum('creole'))['suma']
        miskito_org = Actividad.objects.filter(tipo=1).aggregate(suma=Sum('miskito'))['suma']
        ulwa_org = Actividad.objects.filter(tipo=1).aggregate(suma=Sum('ulwa'))['suma']
        rama_org = Actividad.objects.filter(tipo=1).aggregate(suma=Sum('rama'))['suma']
        mestizo_org = Actividad.objects.filter(tipo=1).aggregate(suma=Sum('mestizo'))['suma']
        mayagna_org = Actividad.objects.filter(tipo=1).aggregate(suma=Sum('mayagna'))['suma']
        garifuna_org = Actividad.objects.filter(tipo=1).aggregate(suma=Sum('garifuna'))['suma']
        extranjero_org = Actividad.objects.filter(tipo=1).aggregate(suma=Sum('extranjero'))['suma']
        #salida por rango de edad
        menor_12_org = Actividad.objects.filter(tipo=1).aggregate(suma=Sum('menor_12'))['suma']
        mayor_12_org = Actividad.objects.filter(tipo=1).aggregate(suma=Sum('mayor_12'))['suma']
        mayor_18_org = Actividad.objects.filter(tipo=1).aggregate(suma=Sum('mayor_18'))['suma']
        mayor_30_org = Actividad.objects.filter(tipo=1).aggregate(suma=Sum('mayor_30'))['suma']

        #salidas por comites comunales
        personas_hombre_comunal = Actividad.objects.filter(tipo=2).aggregate(suma=Sum('hombres'))['suma']
        personas_mujer_comunal = Actividad.objects.filter(tipo=2).aggregate(suma=Sum('mujeres'))['suma']
        total_personas_comunal = personas_hombre_comunal + personas_mujer_comunal
        #salida por etnias
        creole_comunal = Actividad.objects.filter(tipo=2).aggregate(suma=Sum('creole'))['suma']
        miskito_comunal = Actividad.objects.filter(tipo=2).aggregate(suma=Sum('miskito'))['suma']
        ulwa_comunal = Actividad.objects.filter(tipo=2).aggregate(suma=Sum('ulwa'))['suma']
        rama_comunal = Actividad.objects.filter(tipo=2).aggregate(suma=Sum('rama'))['suma']
        mestizo_comunal = Actividad.objects.filter(tipo=2).aggregate(suma=Sum('mestizo'))['suma']
        mayagna_comunal = Actividad.objects.filter(tipo=2).aggregate(suma=Sum('mayagna'))['suma']
        garifuna_comunal = Actividad.objects.filter(tipo=2).aggregate(suma=Sum('garifuna'))['suma']
        extranjero_comunal = Actividad.objects.filter(tipo=2).aggregate(suma=Sum('extranjero'))['suma']
        #salida por rango de edad
        menor_12_comunal = Actividad.objects.filter(tipo=2).aggregate(suma=Sum('menor_12'))['suma']
        mayor_12_comunal = Actividad.objects.filter(tipo=2).aggregate(suma=Sum('mayor_12'))['suma']
        mayor_18_comunal = Actividad.objects.filter(tipo=2).aggregate(suma=Sum('mayor_18'))['suma']
        mayor_30_comunal = Actividad.objects.filter(tipo=2).aggregate(suma=Sum('mayor_30'))['suma']
    except:
        pass

    if request.user.is_superuser:
        actividad = Actividad.objects.all()
    else:
        actividad = Actividad.objects.filter(user=request.user)

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
										sum_estudiante,sum_docente,sum_periodista,
										sum_representantes,sum_autoridades,sum_comunitarios)

	return render(request, template, locals())

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("utf-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('Houston tenemos errores<pre>%s</pre>' % escape(html))

def actividad_pdf(request, id_actividad):
    actividad = Actividad.objects.filter(id=id_actividad)
    return render_to_pdf(
            'actividades/actividad_pdf.html',
            {
                'pagesize':'A4',
                'actividad': actividad,
            }
        )
