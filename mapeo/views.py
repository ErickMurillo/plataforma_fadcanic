# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import TemplateView, ListView, DetailView
from actividades.contraparte.models import *
import collections

# Create your views here.
def DetailOrg(request,template='mapeo/detalle.html',slug=None):
	object = Organizaciones.objects.filter(slug=slug)
	actividades = Actividad.objects.filter(comite__slug=slug)
	return render(request, template, locals())

def _queryset_filtrado(request):
	params = {}

	if request.session['anno']:
		params['tipo'] = request.session['tipo']

	unvalid_keys = []
	for key in params:
		if not params[key]:
			unvalid_keys.append(key)

	for key in unvalid_keys:
		del params[key]

	return Organizaciones.objects.filter(**params)

def index(request,template="mapeo/index.html"):
	TIPO_CHOICES = ((1,'Comité municipal de prevención de violencia'),(2,'Comité comunal'),
					(3,'Diplomado de promotoría'),(4,'Diplomado de comunicación'),
					(5,'Acción docente'),(6,'Comité comunal y municipal'),(7,'Acción masiva'),
					(8,'Debate escolar'))

	tipo_org = collections.OrderedDict()
	for obj in TIPO_CHOICES:
		count = Organizaciones.objects.filter(tipo=obj[0]).count()
		tipo_org[obj[1]] = count

	if request.method == 'POST':
		mensaje = None
		form = OrganizacionConsulta(request.POST)
		if form.is_valid():
			request.session['tipo'] = form.cleaned_data['tipo']

			mensaje = "Todas las variables estan correctamente :)"
			request.session['activo'] = True
			centinela = 1

			tipo = request.session['tipo']
			if tipo != '':
				list_municipio = Organizaciones.objects.filter(tipo=tipo).values_list('municipio', flat=True).distinct('municipio')
				lista = []
				for x in list_municipio:
					municipio = Municipio.objects.filter(id=x)
					organizaciones = Organizaciones.objects.filter(municipio=x,tipo=tipo)
					for y in municipio:
						lista.append((y,float(y.latitud),float(y.longitud),organizaciones))
				municipios = lista
			else:
				list_municipio = Organizaciones.objects.values_list('municipio', flat=True).distinct('municipio')
				lista = []
				for x in list_municipio:
					municipio = Municipio.objects.filter(id=x)
					organizaciones = Organizaciones.objects.filter(municipio=x)
					for y in municipio:
						lista.append((y,float(y.latitud),float(y.longitud),organizaciones))
				municipios = lista

	else:
		form = OrganizacionConsulta()
		mensaje = "Existen alguno errores"
		centinela = 0

		list_municipio = Organizaciones.objects.values_list('municipio', flat=True).distinct('municipio')
		lista = []
		for x in list_municipio:
			municipio = Municipio.objects.filter(id=x)
			organizaciones = Organizaciones.objects.filter(municipio=x)
			for y in municipio:
				lista.append((y,float(y.latitud),float(y.longitud),organizaciones))
		municipios = lista

		try:
			del request.session['tipo']
		except:
			pass

	return render(request, template, locals())
