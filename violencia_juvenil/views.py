from django.shortcuts import render
from .models import *
from .forms import *
import collections

# Create your views here.
def _queryset_filtrado(request):
	params = {}

	if request.session['year']:
		params['year'] = request.session['year']

	unvalid_keys = []
	for key in params:
		if not params[key]:
			unvalid_keys.append(key)

	for key in unvalid_keys:
		del params[key]

	return Encuesta.objects.filter(**params)

def index(request,template="violencia_juvenil/index.html"):
	if request.method == 'POST':
		form = ViolenciaConsulta(request.POST)
		if form.is_valid():
			request.session['year'] = form.cleaned_data['year']
			year = request.session['year']
			encuestas = Encuesta.objects.filter(year=year).count()
			try:
				#sexo----------------
				sexo = {}
				for x in CHOICE_SEXO:
					count_sexo = InformacionEntrevistado.objects.filter(encuesta__year=year,sexo=x[0]).count()
					sexo[x[1]] = count_sexo
				#edad----------------
				edad = {}
				for x in EDAD_CHOICES:
					count_edad = InformacionEntrevistado.objects.filter(encuesta__year=year,edad=x[0]).count()
					edad[x[1]] = count_edad
				#etnia---------------
				etnia = {}
				for x in ETNIAS_CHOICES:
					count_etnia = InformacionEntrevistado.objects.filter(encuesta__year=year,etnia=x[0]).count()
					etnia[x[1]] = saca_porcentajes(count_etnia,encuestas,False)

				#tab conocimiento--------------------------------------------------
				#preg 3
				pregunta3 = collections.OrderedDict()
				for obj in CHOICE_TIPO_VIOLENCIA_3:
					conteo = Conocimiento.objects.filter(pregunta3__contains=obj[0],encuesta__year=year).count()
					pregunta3[obj[1]] = saca_porcentajes(conteo,encuestas,False)

				#preg 4
				pregunta4 = collections.OrderedDict()
				for obj in CHOICE_LUGARES_4:
					conteo = Conocimiento.objects.filter(pregunta4__contains=obj[0],encuesta__year=year).count()
					pregunta4[obj[1]] = saca_porcentajes(conteo,encuestas,False)

				#preg 7
				pregunta7 = collections.OrderedDict()
				for obj in CHOICE_SOLUCIONES_7:
					conteo = Conocimiento.objects.filter(pregunta7__contains=obj[0],encuesta__year=year).count()
					pregunta7[obj[1]] = saca_porcentajes(conteo,encuestas,False)

				#preg 9
				pregunta9 = collections.OrderedDict()
				for obj in CHOICE_FEMINICIDIO_9:
					conteo = Conocimiento.objects.filter(pregunta9__contains=obj[0],encuesta__year=year).count()
					pregunta9[obj[1]] = saca_porcentajes(conteo,encuestas,False)

				#preg 13
				pregunta13 = collections.OrderedDict()
				for obj in CHOICE_SEGURIDAD_CIUDADA_13:
					conteo = Conocimiento.objects.filter(pregunta13__contains=obj[0],encuesta__year=year).count()
					pregunta13[obj[1]] = saca_porcentajes(conteo,encuestas,False)

				#tab actitud-------------------------------------------------------
				#preg 15
				pregunta15 = collections.OrderedDict()
				for obj in CHOICE_15:
					conteo = Actitud.objects.filter(pregunta15__contains=obj[0],encuesta__year=year).count()
					pregunta15[obj[1]] = saca_porcentajes(conteo,encuestas,False)

				#preg 19
				pregunta19 = collections.OrderedDict()
				for obj in CHOICE_19:
					conteo = Actitud.objects.filter(pregunta19__contains=obj[0],encuesta__year=year).count()
					pregunta19[obj[1]] = saca_porcentajes(conteo,encuestas,False)
					
				#tab practicas-------------------------------------------------------
				#preg 23
				pregunta23 = collections.OrderedDict()
				for obj in CHOICE_23:
					conteo = Practicas.objects.filter(pregunta23__contains=obj[0],encuesta__year=year).count()
					pregunta23[obj[1]] = saca_porcentajes(conteo,encuestas,False)
				
				#preg 24
				pregunta24 = collections.OrderedDict()
				for obj in CHOICE_24:
					conteo = Practicas.objects.filter(pregunta24__contains=obj[0],encuesta__year=year).count()
					pregunta24[obj[1]] = saca_porcentajes(conteo,encuestas,False)
				#fin salidas-------------------------------------------------------

			except:
				pass
	else:
		form = ViolenciaConsulta()
		encuestas = Encuesta.objects.count()
		try:
			#sexo----------------
			sexo = {}
			for x in CHOICE_SEXO:
				count_sexo = InformacionEntrevistado.objects.filter(sexo=x[0]).count()
				sexo[x[1]] = count_sexo
			#edad----------------
			edad = {}
			for x in EDAD_CHOICES:
				count_edad = InformacionEntrevistado.objects.filter(edad=x[0]).count()
				edad[x[1]] = count_edad
			#etnia---------------
			etnia = {}
			for x in ETNIAS_CHOICES:
				count_etnia = InformacionEntrevistado.objects.filter(etnia=x[0]).count()
				etnia[x[1]] = saca_porcentajes(count_etnia,encuestas,False)

			#tab conocimiento--------------------------------------------------
			#preg 3
			pregunta3 = collections.OrderedDict()
			for obj in CHOICE_TIPO_VIOLENCIA_3:
				conteo = Conocimiento.objects.filter(pregunta3__contains=obj[0]).count()
				pregunta3[obj[1]] = saca_porcentajes(conteo,encuestas,False)

			#preg 4
			pregunta4 = collections.OrderedDict()
			for obj in CHOICE_LUGARES_4:
				conteo = Conocimiento.objects.filter(pregunta4__contains=obj[0]).count()
				pregunta4[obj[1]] = saca_porcentajes(conteo,encuestas,False)

			#preg 7	
			pregunta7 = collections.OrderedDict()
			for obj in CHOICE_SOLUCIONES_7:
				conteo = Conocimiento.objects.filter(pregunta7__contains=obj[0]).count()
				pregunta7[obj[1]] = saca_porcentajes(conteo,encuestas,False)

			#preg 9
			pregunta9 = collections.OrderedDict()
			for obj in CHOICE_FEMINICIDIO_9:
				conteo = Conocimiento.objects.filter(pregunta9__contains=obj[0]).count()
				pregunta9[obj[1]] = saca_porcentajes(conteo,encuestas,False)

			#preg 13
			pregunta13 = collections.OrderedDict()
			for obj in CHOICE_SEGURIDAD_CIUDADA_13:
				conteo = Conocimiento.objects.filter(pregunta13__contains=obj[0]).count()
				pregunta13[obj[1]] = saca_porcentajes(conteo,encuestas,False)

			#tab actitud-------------------------------------------------------
			#preg 15
			pregunta15 = collections.OrderedDict()
			for obj in CHOICE_15:
				conteo = Actitud.objects.filter(pregunta15__contains=obj[0]).count()
				pregunta15[obj[1]] = saca_porcentajes(conteo,encuestas,False)
			
			#preg 19
			pregunta19 = collections.OrderedDict()
			for obj in CHOICE_19:
				conteo = Actitud.objects.filter(pregunta19__contains=obj[0]).count()
				pregunta19[obj[1]] = saca_porcentajes(conteo,encuestas,False)

			#tab practicas-------------------------------------------------------
			#preg 23
			pregunta23 = collections.OrderedDict()
			for obj in CHOICE_23:
				conteo = Practicas.objects.filter(pregunta23__contains=obj[0]).count()
				pregunta23[obj[1]] = saca_porcentajes(conteo,encuestas,False)
			
			#preg 24
			pregunta24 = collections.OrderedDict()
			for obj in CHOICE_24:
				conteo = Practicas.objects.filter(pregunta24__contains=obj[0]).count()
				pregunta24[obj[1]] = saca_porcentajes(conteo,encuestas,False)

			#fin salidas-------------------------------------------------------

			del request.session['tipo']
		except:
			pass

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