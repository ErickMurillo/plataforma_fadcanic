from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.
class IndexMapeo(TemplateView):
	template_name = "mapeo/index.html"

	def get_context_data(self, **kwargs):
		context = super(IndexMapeo, self).get_context_data(**kwargs)
		return context
