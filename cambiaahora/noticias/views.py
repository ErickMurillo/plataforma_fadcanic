# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from .models import Noticias
# Create your views here.

class IndexView(TemplateView):
    template_name = "cambiaahora/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['latest_news'] = Noticias.objects.filter(aprobacion=2).order_by('-fecha')[:3]

        return context

#Listar las Noticias
class ListNewsView(ListView):
    model = Noticias
    queryset = Noticias.objects.order_by('-fecha')
    paginate_by = 10

class DetailNewsView(DetailView):
	model = Noticias

