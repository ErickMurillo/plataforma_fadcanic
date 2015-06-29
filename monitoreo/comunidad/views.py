# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from .models import *
from django.db.models import Sum


# Create your views here.
class MonitoreoView(TemplateView):
    template_name = "monitoreo_actividades/index.html"

    def get_context_data(self, **kwargs):
        context = super(MonitoreoView, self).get_context_data(**kwargs)
        context['masculino'] = Monitoreo.objects.all().aggregate(Sum('masculino'))
        context['femenino'] = Monitoreo.objects.all().aggregate(Sum('femenino'))

        for x in Municipio.objects.all():
        	conteo_actividades = Monitoreo.objects.filter(municipio=x)
        return context
