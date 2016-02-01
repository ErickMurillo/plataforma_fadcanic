# -*- coding: UTF-8 -*-
from django.db import models
from models import *
from django import forms

def fecha_choice():
    years = []
    for en in Encuesta.objects.order_by('year').values_list('year', flat=True):
        years.append((en,en))
    return list(sorted(set(years)))

class ViolenciaConsulta(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ViolenciaConsulta, self).__init__(*args, **kwargs)
        self.fields['year'] = forms.ChoiceField(label=u'Año',choices=fecha_choice(),required=False)