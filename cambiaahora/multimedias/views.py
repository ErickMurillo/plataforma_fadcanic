# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from cambiaahora.multimedias.models import *
from django.utils import translation

# Create your views here.

class MultimediaView(TemplateView):
    template_name = "cambiaahora/multimedia/multimedia.html"

    def get_context_data(self, **kwargs):
        context = super(MultimediaView, self).get_context_data(**kwargs)
        context['documentales'] = Documentales.objects.filter(aprobacion=2).order_by('-fecha')[:2]
        context['videos'] = Videos.objects.filter(aprobacion=2)[:2]
        context['fotos'] = Fotos.objects.filter(aprobacion=2)[:2]

        return context


class ListVideosView(ListView):
    template_name = "cambiaahora/multimedia/videos_list.html"
    model = Videos
    # paginate_by = 6

    def get_queryset(self):
        cur_language = translation.get_language()
        if cur_language == 'en':
            queryset = Videos.objects.filter(aprobacion=2,idioma=2).order_by('-id')
        else:
            queryset = Videos.objects.filter(aprobacion=2,idioma=1).order_by('-id')
        return queryset

class ListAudiosView(ListView):
    template_name = "cambiaahora/multimedia/audios_list.html"
    model = Audios
    # paginate_by = 6

    def get_queryset(self):
        cur_language = translation.get_language()
        if cur_language == 'en':
            queryset = Audios.objects.filter(aprobacion=2,idioma=2).order_by('-nombre')
        else:
            queryset = Audios.objects.filter(aprobacion=2,idioma=1).order_by('-nombre')
        return queryset

class ListFotosView(ListView):
    template_name = "cambiaahora/multimedia/fotos_list.html"
    model = Fotos
    # paginate_by = 6

    def get_queryset(self):
        cur_language = translation.get_language()
        if cur_language == 'en':
            queryset = Fotos.objects.filter(aprobacion=2,idioma=2).order_by('-id')
        else:
            queryset = Fotos.objects.filter(aprobacion=2,idioma=1).order_by('-id')
        return queryset


class ListDocumentalesView(ListView):
    template_name = "cambiaahora/multimedia/documentales_list.html"
    model = Documentales

    def get_queryset(self):
        cur_language = translation.get_language()
        if cur_language == 'en':
            queryset = Documentales.objects.filter(aprobacion=2,idioma=2).order_by('-fecha')
        else:
            queryset = Documentales.objects.filter(aprobacion=2,idioma=1).order_by('-fecha')
        return queryset

class DetailDocumentalView(DetailView):
    template_name = "cambiaahora/multimedia/documentales_detail.html"
    model = Documentales

class DetailVideosView(DetailView):
    template_name = "cambiaahora/multimedia/videos_detail.html"
    model = Videos

class DetailFotosView(DetailView):
    template_name = "cambiaahora/multimedia/fotos_detail.html"
    model = Fotos

class DetailAudiosView(DetailView):
    template_name = "cambiaahora/multimedia/audios_detail.html"
    model = Audios
