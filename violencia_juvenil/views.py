# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import *
from .forms import *
import collections
import json as simplejson
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def _queryset_filtrado(request):
	params = {}

	if request.session['year']:
		params['year__in'] = request.session['year']

	if request.session['grupos']:
		params['grupos__in'] = request.session['grupos']

	if request.session['sexo']:
		params['informacionentrevistado__sexo'] = request.session['sexo']

	if request.session['edad']:
		params['informacionentrevistado__edad__in'] = request.session['edad']

	if request.session['etnia']:
		params['informacionentrevistado__etnia__in'] = request.session['etnia']

	if request.session['departamento']:
		if not request.session['municipio']:
			municipios = Municipio.objects.filter(departamento__in=request.session['departamento'])
			params['informacionentrevistado__municipio1__in'] = municipios
		else:
			params['informacionentrevistado__municipio1__in'] = request.session['municipio']

	unvalid_keys = []
	for key in params:
		if not params[key]:
			unvalid_keys.append(key)

	for key in unvalid_keys:
		del params[key]

	return Encuesta.objects.filter(**params)

def index(request,template="violencia_juvenil/index.html"):
	return render(request, template, locals())

def consulta(request,template="violencia_juvenil/consulta.html"):
	if request.method == 'POST':
		form = ViolenciaConsulta(request.POST)
		if form.is_valid():
			request.session['year'] = form.cleaned_data['year']
			request.session['grupos'] = form.cleaned_data['grupos']
			request.session['sexo'] = form.cleaned_data['sexo']
			request.session['edad'] = form.cleaned_data['edad']
			request.session['etnia'] = form.cleaned_data['etnia']
			request.session['departamento'] = form.cleaned_data['departamento']
			request.session['municipio'] = form.cleaned_data['municipio']

			return HttpResponseRedirect('/violencia_juvenil/dashboard/')		
	else:
		form = ViolenciaConsulta()
		try:
			del request.session['year']
			del request.session['grupos']
			del request.session['departamento']
			del request.session['municipio']
		except:
			pass

	return render(request, template, locals())

def dashboard(request,template='violencia_juvenil/dashboard.html'):
	filtro = _queryset_filtrado(request)
	encuestas = filtro.count()

	#sexo----------------
	sexo = {}
	for x in CHOICE_SEXO:
		count_sexo = filtro.filter(informacionentrevistado__sexo=x[0]).count()
		sexo[x[1]] = count_sexo
	#edad----------------
	edad = {}
	for x in EDAD_CHOICES:
		count_edad = filtro.filter(informacionentrevistado__edad=x[0]).count()
		edad[x[1]] = count_edad
	#etnia---------------
	etnia = {}
	for x in ETNIAS_CHOICES:
		count_etnia = filtro.filter(informacionentrevistado__etnia=x[0]).count()
		etnia[x[1]] = saca_porcentajes(count_etnia,encuestas,False)

	#tab conocimiento--------------------------------------------------
	#preg 3
	pregunta3 = collections.OrderedDict()
	for obj in CHOICE_TIPO_VIOLENCIA_3:
		conteo = filtro.filter(conocimiento__pregunta3__contains=obj[0]).count()
		pregunta3[obj[1]] = saca_porcentajes(conteo,encuestas,False)

	#preg 4
	pregunta4 = collections.OrderedDict()
	for obj in CHOICE_LUGARES_4:
		conteo = filtro.filter(conocimiento__pregunta4__contains=obj[0]).count()
		pregunta4[obj[1]] = saca_porcentajes(conteo,encuestas,False)

	#preg 7
	pregunta7 = collections.OrderedDict()
	for obj in CHOICE_SOLUCIONES_7:
		conteo = filtro.filter(conocimiento__pregunta7__contains=obj[0]).count()
		pregunta7[obj[1]] = saca_porcentajes(conteo,encuestas,False)

	#preg 9
	pregunta9 = collections.OrderedDict()
	for obj in CHOICE_FEMINICIDIO_9:
		conteo = filtro.filter(conocimiento__pregunta9__contains=obj[0]).count()
		pregunta9[obj[1]] = saca_porcentajes(conteo,encuestas,False)

	#preg 13
	pregunta13 = collections.OrderedDict()
	for obj in CHOICE_SEGURIDAD_CIUDADA_13:
		conteo = filtro.filter(conocimiento__pregunta13__contains=obj[0]).count()
		pregunta13[obj[1]] = saca_porcentajes(conteo,encuestas,False)

	#tab actitud-------------------------------------------------------
	#preg 15
	pregunta15 = collections.OrderedDict()
	for obj in CHOICE_15:
		conteo = filtro.filter(actitud__pregunta15__contains=obj[0]).count()
		pregunta15[obj[1]] = saca_porcentajes(conteo,encuestas,False)

	#preg 19
	pregunta19 = collections.OrderedDict()
	for obj in CHOICE_19:
		conteo = filtro.filter(actitud__pregunta19__contains=obj[0]).count()
		pregunta19[obj[1]] = saca_porcentajes(conteo,encuestas,False)
		
	#tab practicas-------------------------------------------------------
	#preg 23
	pregunta23 = collections.OrderedDict()
	for obj in CHOICE_23:
		conteo = filtro.filter(practicas__pregunta23__contains=obj[0]).count()
		pregunta23[obj[1]] = saca_porcentajes(conteo,encuestas,False)
	
	#preg 24
	pregunta24 = collections.OrderedDict()
	for obj in CHOICE_24:
		conteo = filtro.filter(practicas__pregunta24__contains=obj[0]).count()
		pregunta24[obj[1]] = saca_porcentajes(conteo,encuestas,False)

	#tab persepcion-------------------------------------------------------
	#preg 30
	pregunta30 = collections.OrderedDict()
	for obj in CHOICE_30:
		conteo = filtro.filter(percepcion__pregunta30__contains=obj[0]).count()
		pregunta30[obj[1]] = saca_porcentajes(conteo,encuestas,False)

	#preg 31
	pregunta31 = collections.OrderedDict()
	for obj in CHOICE_31:
		conteo = filtro.filter(percepcion__pregunta31__contains=obj[0]).count()
		pregunta31[obj[1]] = saca_porcentajes(conteo,encuestas,False)

	#tab estado actual-------------------------------------------------------
	#preg 36
	pregunta36 = collections.OrderedDict()
	for obj in CHOICE_36:
		conteo = filtro.filter(estadoactual__pregunta36__contains=obj[0]).count()
		pregunta36[obj[1]] = saca_porcentajes(conteo,encuestas,False)

	#preg 37
	pregunta37 = collections.OrderedDict()
	for obj in CHOICE_37:
		conteo = filtro.filter(estadoactual__pregunta37__contains=obj[0]).count()
		pregunta37[obj[1]] = saca_porcentajes(conteo,encuestas,False)
			
	return render(request, template, locals())

def saca_porcentajes(dato, total, formato=True):
	if dato != None:
		try:
			porcentaje = (dato/float(total)) * 100 if total != None or total != 0 else 0
		except:
			return 0
		if formato:
			return porcentaje
		else:
			return '%.2f' % porcentaje
	else:
		return 0

#ajax filtros
def get_munis(request):
	'''Metodo para obtener los municipios via Ajax segun los departamentos selectos'''
	ids = request.GET.get('ids', '')
	dicc = {}
	resultado = []
	if ids:
		lista = ids.split(',')
		for id in lista:
			try:
				encuesta = Encuesta.objects.filter(informacionentrevistado__municipio1__departamento__id=id).distinct().values_list('informacionentrevistado__municipio1__id', flat=True)
				departamento = Departamento.objects.get(pk=id)
				municipios = Municipio.objects.filter(departamento__id=departamento.pk,id__in=encuesta).order_by('nombre')
				lista1 = []
				for municipio in municipios:
					muni = {}
					muni['id'] = municipio.pk
					muni['nombre'] = municipio.nombre
					lista1.append(muni)
					dicc[departamento.nombre] = lista1
			except:
				pass

	#filtrar segun la organizacion seleccionada
	org_ids = request.GET.get('org_ids', '')
	if org_ids:
		lista = org_ids.split(',')
		municipios = [encuesta.municipio for encuesta in Encuesta.objects.filter(organizacion__id__in=lista)]
		#crear los keys en el dicc para evitar KeyError
		for municipio in municipios:
			dicc[municipio.departamento.nombre] = []

		#agrupar municipios por departamento padre
		for municipio in municipios:
			muni = {'id': municipio.id, 'nombre': municipio.nombre}
			if not muni in dicc[municipio.departamento.nombre]:
				dicc[municipio.departamento.nombre].append(muni)

	resultado.append(dicc)

	return HttpResponse(simplejson.dumps(resultado), content_type='application/json')

def obtener_lista(request):
	if request.is_ajax():
		lista = []
		for objeto in InformacionEntrevistado.objects.all():
			dicc = dict(nombre=objeto.municipio1.nombre, id=objeto.id,
						lon=float(objeto.municipio1.longitud),
						lat=float(objeto.municipio1.latitud)
						)
			lista.append(dicc)

		serializado = simplejson.dumps(lista)
		return HttpResponse(serializado, content_type='application/json')