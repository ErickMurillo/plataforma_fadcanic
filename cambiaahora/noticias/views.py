# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from .models import Noticias
from cambiaahora.historias.models import Historias
from cambiaahora.multimedias.models import *
from cambiaahora.testimonios.models import Testimonios
from cambiaahora.configuracion.models import Configuracion

# Create your views here.

class IndexView(TemplateView):
    template_name = "cambiaahora/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['ultimas_noticias'] = Noticias.objects.filter(aprobacion=2).order_by('-fecha')[:9]
        context['ultimas_historia'] = Historias.objects.filter(aprobacion=2).order_by('-fecha')[:3]
        context['ultimas_testimonios'] = Testimonios.objects.filter(aprobacion=2).order_by('-fecha')[:3]
        context['albunes'] = Fotos.objects.filter(aprobacion=2).order_by('-id')[:1]
        context['audios'] = Audios.objects.filter(aprobacion=2).order_by('id')[:3]
        context['videos'] = Videos.objects.filter(aprobacion=2).order_by('-id')[:3]
        context['documentales'] = Documentales.objects.filter(aprobacion=2).order_by('-fecha')[:3]
        context['config'] = Configuracion.objects.all()[:3]
        return context

#Listar las Noticias
class ListNewsView(ListView):
    template_name = "cambiaahora/noticias/noticias_list.html"
    model = Noticias
    queryset = Noticias.objects.filter(aprobacion=2).order_by('-fecha')
    paginate_by = 6

class DetailNewsView(DetailView):
    template_name = "cambiaahora/noticias/noticias_detail.html"
    model = Noticias

    def get_context_data(self, **kwargs):
        context = super(DetailNewsView, self).get_context_data(**kwargs)
        context['noticias_relacionadas'] = Noticias.objects.filter(aprobacion=2, categoria=self.object.categoria).exclude(id=self.object.id).order_by('-fecha')[:3]
        return context