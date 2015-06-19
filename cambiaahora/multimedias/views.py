# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView
from cambiaahora.multimedias.models import *

# Create your views here.
class MultimediaView(TemplateView):
    template_name = "cambiaahora/multimedia/multimedia.html"

    def get_context_data(self, **kwargs):
        context = super(MultimediaView, self).get_context_data(**kwargs)
        context['documentales'] = Documentales.objects.filter(aprobacion=2).order_by('-fecha')[:2]
        context['videos'] = Videos.objects.filter(aprobacion=2)[:2]
        context['fotos'] = Fotos.objects.filter(aprobacion=2)[:2]

        return context