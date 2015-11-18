from django.shortcuts import render
from .models import *
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