from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.
class IndexMapeo(TemplateView):
	template_name = "mapeo/index.html"

	def get_context_data(self, **kwargs):
		context = super(IndexMapeo, self).get_context_data(**kwargs)
		list_municipio = Organizaciones.objects.values_list('municipio', flat=True).distinct('municipio')
		lista = []
		for x in list_municipio:
			municipio = Municipio.objects.filter(id=x)
			organizaciones = Organizaciones.objects.filter(municipio=x)
			for y in municipio:
				lista.append((y,float(y.latitud),float(y.longitud),organizaciones))
		context['municipios'] = lista
		return context

class DetailOrg(DetailView):
	template_name = "mapeo/detalle.html"
	model = Organizaciones

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
	if request.method == 'POST':
		mensaje = None
		form = OrganizacionConsulta(request.POST)
		if form.is_valid():
			request.session['tipo'] = form.cleaned_data['tipo']

			mensaje = "Todas las variables estan correctamente :)"
			request.session['activo'] = True
			centinela = 1

			tipo = request.session['tipo']
			list_municipio = Organizaciones.objects.filter(tipo=tipo).values_list('municipio', flat=True).distinct('municipio')
			lista = []
			for x in list_municipio:
				municipio = Municipio.objects.filter(id=x)
				organizaciones = Organizaciones.objects.filter(municipio=x,tipo=tipo)
				for y in municipio:
					lista.append((y,float(y.latitud),float(y.longitud),organizaciones))
			municipios = lista

		else:
			centinela = 0

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