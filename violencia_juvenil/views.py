from django.shortcuts import render
from .models import *
from .forms import *

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
					etnia[x[1]] = count_etnia
				#fin salidas---------

			except:
				pass
	else:
		form = ViolenciaConsulta()
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
					count_etnia = InformacionEntrevistado.objects.filter(encuesta__year=year,etnia=x[0]).count()
					etnia[x[1]] = count_etnia
			#fin salidas---------

			del request.session['tipo']
		except:
			pass

	return render(request, template, locals())