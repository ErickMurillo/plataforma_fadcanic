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
	depto = {}
	municipio = {}
	for x in Departamento.objects.all():
		conteo_depto = InformacionEntrevistado.objects.filter(departamento=x).count()
		if conteo_depto != 0:
			depto[x] = conteo_depto

		for y in Municipio.objects.filter(departamento=x):
			conteo_municipio = InformacionEntrevistado.objects.filter(municipio1=y).count()
			if conteo_municipio != 0:
				municipio[x,y] = conteo_municipio

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

	year = {}
	for y in request.session['year']:
		encuestas = filtro.filter(year=y).count()

		#sexo----------------
		sexo = {}
		for x in CHOICE_SEXO:
			count_sexo = filtro.filter(informacionentrevistado__sexo=x[0],year=y).count()
			sexo[x[1]] = count_sexo
		#edad----------------
		edad = {}
		for x in EDAD_CHOICES:
			count_edad = filtro.filter(informacionentrevistado__edad=x[0],year=y).count()
			edad[x[1]] = count_edad
		#etnia---------------
		etnia = {}
		for x in ETNIAS_CHOICES:
			count_etnia = filtro.filter(informacionentrevistado__etnia=x[0],year=y).count()
			etnia[x[1]] = saca_porcentajes(count_etnia,encuestas,False)

		#tab conocimiento--------------------------------------------------
		#preg 3
		pregunta3 = collections.OrderedDict()
		for obj in CHOICE_TIPO_VIOLENCIA_3:
			conteo = filtro.filter(conocimiento__pregunta3__contains=obj[0],year=y).count()
			pregunta3[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		#preg 4
		pregunta4 = collections.OrderedDict()
		for obj in CHOICE_LUGARES_4:
			conteo = filtro.filter(conocimiento__pregunta4__contains=obj[0],year=y).count()
			pregunta4[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		#preg 7
		pregunta7 = collections.OrderedDict()
		for obj in CHOICE_SOLUCIONES_7:
			conteo = filtro.filter(conocimiento__pregunta7__contains=obj[0],year=y).count()
			pregunta7[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		#preg 9
		pregunta9 = collections.OrderedDict()
		for obj in CHOICE_FEMINICIDIO_9:
			conteo = filtro.filter(conocimiento__pregunta9__contains=obj[0],year=y).count()
			pregunta9[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		#preg 13
		pregunta13 = collections.OrderedDict()
		for obj in CHOICE_SEGURIDAD_CIUDADA_13:
			conteo = filtro.filter(conocimiento__pregunta13__contains=obj[0],year=y).count()
			pregunta13[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		#tab actitud-------------------------------------------------------
		#preg 15
		pregunta15 = collections.OrderedDict()
		for obj in CHOICE_15:
			conteo = filtro.filter(actitud__pregunta15__contains=obj[0],year=y).count()
			pregunta15[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		#preg 19
		pregunta19 = collections.OrderedDict()
		for obj in CHOICE_19:
			conteo = filtro.filter(actitud__pregunta19__contains=obj[0],year=y).count()
			pregunta19[obj[1]] = saca_porcentajes(conteo,encuestas,False)
			
		#tab practicas-------------------------------------------------------
		#preg 23
		pregunta23 = collections.OrderedDict()
		for obj in CHOICE_23:
			conteo = filtro.filter(practicas__pregunta23__contains=obj[0],year=y).count()
			pregunta23[obj[1]] = saca_porcentajes(conteo,encuestas,False)
		
		#preg 24
		pregunta24 = collections.OrderedDict()
		for obj in CHOICE_24:
			conteo = filtro.filter(practicas__pregunta24__contains=obj[0],year=y).count()
			pregunta24[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		#tab persepcion-------------------------------------------------------
		#preg 30
		pregunta30 = collections.OrderedDict()
		for obj in CHOICE_30:
			conteo = filtro.filter(percepcion__pregunta30__contains=obj[0],year=y).count()
			pregunta30[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		#preg 31
		pregunta31 = collections.OrderedDict()
		for obj in CHOICE_31:
			conteo = filtro.filter(percepcion__pregunta31__contains=obj[0],year=y).count()
			pregunta31[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		#tab estado actual-------------------------------------------------------
		#preg 36
		pregunta36 = collections.OrderedDict()
		for obj in CHOICE_36:
			conteo = filtro.filter(estadoactual__pregunta36__contains=obj[0],year=y).count()
			pregunta36[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		#preg 37
		pregunta37 = collections.OrderedDict()
		for obj in CHOICE_37:
			conteo = filtro.filter(estadoactual__pregunta37__contains=obj[0],year=y).count()
			pregunta37[obj[1]] = saca_porcentajes(conteo,encuestas,False)
		
		year[y] = (encuestas,sexo,edad,etnia,
					#conocimiento
					pregunta3,pregunta4,pregunta7,pregunta9,pregunta13,
					#actitud
					pregunta15,pregunta19,
					#practicas
					pregunta23,pregunta24,
					#percepcion
					pregunta30,pregunta31,
					#estado actual
					pregunta36,pregunta37
					)

	return render(request, template, locals())

def conocimiento(request,template='violencia_juvenil/conocimiento.html'):
	filtro = _queryset_filtrado(request)

	year = {}
	for y in request.session['year']:
		encuestas = filtro.filter(year=y).count()

		pregunta1 = collections.OrderedDict()
		for obj in CHOICE_VIOLENCIA_1:
			conteo = filtro.filter(conocimiento__pregunta1__contains=obj[0],year=y).count()
			pregunta1[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		pregunta2 = collections.OrderedDict()
		for obj in CHOICE_ABUSO_DROGA_2:
			conteo = filtro.filter(conocimiento__pregunta2__contains=obj[0],year=y).count()
			pregunta2[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		pregunta5 = collections.OrderedDict()
		for obj in CHOICE_JOVEN_VIOLENTO_5:
			conteo = filtro.filter(conocimiento__pregunta5__contains=obj[0],year=y).count()
			pregunta5[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		pregunta6 = collections.OrderedDict()
		for obj in CHOICE_PERJUDICADOS_6:
			conteo = filtro.filter(conocimiento__pregunta6__contains=obj[0],year=y).count()
			pregunta6[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		pregunta8 = collections.OrderedDict()
		for obj in CHOICE_RESPONSABLES_8:
			conteo = filtro.filter(conocimiento__pregunta8__contains=obj[0],year=y).count()
			pregunta8[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		pregunta10 = collections.OrderedDict()
		for obj in CHOICE_ABUSO_SEXUAL_10:
			conteo = filtro.filter(conocimiento__pregunta10__contains=obj[0],year=y).count()
			pregunta10[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		pregunta11 = collections.OrderedDict()
		for obj in CHOICE_LUGARES_11:
			conteo = filtro.filter(conocimiento__pregunta11__contains=obj[0],year=y).count()
			pregunta11[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		pregunta12 = collections.OrderedDict()
		for obj in CHOICE_PREVENIR_ABUSO_12:
			conteo = filtro.filter(conocimiento__pregunta12__contains=obj[0],year=y).count()
			pregunta12[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		pregunta14 = collections.OrderedDict()
		for obj in CHOICE_EDUCAR_NINOS_14:
			conteo = filtro.filter(conocimiento__pregunta14__contains=obj[0],year=y).count()
			pregunta14[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		year[y] = (encuestas,pregunta1,pregunta2,pregunta5,pregunta6,pregunta8,pregunta10,pregunta11,pregunta12,pregunta14)

	return render(request, template, locals())

def actitud(request,template='violencia_juvenil/actitud.html'):
	filtro = _queryset_filtrado(request)
	
	year = {}
	for y in request.session['year']:
		encuestas = filtro.filter(year=y).count()

		pregunta16 = collections.OrderedDict()
		for obj in CHOICE_16:
			conteo = filtro.filter(actitud__pregunta16__contains=obj[0],year=y).count()
			pregunta16[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		pregunta17 = collections.OrderedDict()
		for obj in CHOICE_17:
			conteo = filtro.filter(actitud__pregunta17__contains=obj[0],year=y).count()
			pregunta17[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		pregunta18 = collections.OrderedDict()
		for obj in CHOICE_18:
			conteo = filtro.filter(actitud__pregunta18__contains=obj[0],year=y).count()
			pregunta18[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		year[y] = (encuestas,pregunta16,pregunta17,pregunta18)

	return render(request, template, locals())

def practicas(request,template='violencia_juvenil/practicas.html'):
	filtro = _queryset_filtrado(request)
	
	year = {}
	for y in request.session['year']:
		encuestas = filtro.filter(year=y).count()

		pregunta21 = collections.OrderedDict()
		for obj in CHOICE_21:
			conteo = filtro.filter(practicas__pregunta21__contains=obj[0],year=y).count()
			pregunta21[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		pregunta22 = collections.OrderedDict()
		for obj in CHOICE_22:
			conteo = filtro.filter(practicas__pregunta22__contains=obj[0],year=y).count()
			pregunta22[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		year[y] = (encuestas,pregunta21,pregunta22)

	return render(request, template, locals())

def percepcion(request,template='violencia_juvenil/percepcion.html'):
	filtro = _queryset_filtrado(request)
	
	year = {}
	for y in request.session['year']:
		encuestas = filtro.filter(year=y).count()

		pregunta25 = collections.OrderedDict()
		for obj in CHOICE_25:
			conteo = filtro.filter(percepcion__pregunta25__contains=obj[0],year=y).count()
			pregunta25[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		pregunta26 = collections.OrderedDict()
		for obj in CHOICE_26:
			conteo = filtro.filter(percepcion__pregunta26__contains=obj[0],year=y).count()
			pregunta26[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		pregunta27 = collections.OrderedDict()
		for obj in CHOICE_27:
			conteo = filtro.filter(percepcion__pregunta27__contains=obj[0],year=y).count()
			pregunta27[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		pregunta28 = collections.OrderedDict()
		for obj in CHOICE_28:
			conteo = filtro.filter(percepcion__pregunta28__contains=obj[0],year=y).count()
			pregunta28[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		pregunta29 = collections.OrderedDict()
		for obj in CHOICE_29:
			conteo = filtro.filter(percepcion__pregunta29_1=obj[0],year=y).count()
			pregunta29[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		pregunta32 = collections.OrderedDict()
		for obj in CHOICE_32_33:
			conteo = filtro.filter(percepcion__pregunta32_1=obj[0],year=y).count()
			pregunta32[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		pregunta33 = collections.OrderedDict()
		for obj in CHOICE_32_33:
			conteo = filtro.filter(percepcion__pregunta33=obj[0],year=y).count()
			pregunta33[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		year[y] = (encuestas,pregunta25,pregunta26,pregunta27,pregunta28,pregunta29,pregunta32,pregunta33)

	return render(request, template, locals())

def estado_actual(request,template='violencia_juvenil/estado_actual.html'):
	filtro = _queryset_filtrado(request)
	
	year = {}
	for y in request.session['year']:
		encuestas = filtro.filter(year=y).count()

		pregunta34 = collections.OrderedDict()
		for obj in CHOICE_SI_NO:
			conteo = filtro.filter(estadoactual__pregunta34=obj[0],year=y).count()
			pregunta34[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		si_respuesta_34 = collections.OrderedDict()
		for obj in CHOICE_34_SI:
			conteo = filtro.filter(estadoactual__si_respuesta_34__contains=obj[0],year=y).count()
			si_respuesta_34[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		pregunta35 = collections.OrderedDict()
		for obj in CHOICE_SI_NO:
			conteo = filtro.filter(estadoactual__pregunta35=obj[0],year=y).count()
			pregunta35[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		si_respuesta_35 = collections.OrderedDict()
		for obj in CHOICE_35_SI:
			conteo = filtro.filter(estadoactual__si_respuesta_35__contains=obj[0],year=y).count()
			si_respuesta_35[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		pregunta38 = collections.OrderedDict()
		for obj in CHOICE_38:
			conteo = filtro.filter(estadoactual__pregunta38__contains=obj[0],year=y).count()
			pregunta38[obj[1]] = saca_porcentajes(conteo,encuestas,False)

		pregunta39 = collections.OrderedDict()
		for obj in CHOICE_39:
			conteo = filtro.filter(estadoactual__pregunta39__contains=obj[0],year=y).count()
			pregunta39[obj[1]] = saca_porcentajes(conteo,encuestas,False)


		year[y] = (encuestas,pregunta34,si_respuesta_34,pregunta35,si_respuesta_35,pregunta38,pregunta39)

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