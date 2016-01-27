# -*- coding: UTF-8 -*-
from django.db import models
from models import *
from django import forms

def fecha_choice():
    years = []
    for en in Encuesta.objects.order_by('year').values_list('year', flat=True):
        years.append((en,en))
    return list(sorted(set(years)))

def departamentos():   
    foo = Encuesta.objects.all().order_by('informacionentrevistado__municipio1__departamento__nombre').distinct().values_list('informacionentrevistado__municipio1__departamento__id', flat=True)
    return Departamento.objects.filter(id__in=foo)

class ViolenciaConsulta(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ViolenciaConsulta, self).__init__(*args, **kwargs)
        self.fields['year'] = forms.MultipleChoiceField(label=u'Año',choices=fecha_choice(),required=True)
        self.fields['grupos'] = forms.MultipleChoiceField(label=u'Grupos',choices=GRUPOS_CHOICES,required=False)
        self.fields['sexo'] = forms.ChoiceField(label=u'Sexo',choices=CHOICE_SEXO,required=False)
        self.fields['edad'] = forms.MultipleChoiceField(label=u'Edad',choices=EDAD_CHOICES,required=False)
        self.fields['etnia'] = forms.MultipleChoiceField(label=u'Etnia',choices=ETNIAS_CHOICES,required=False)
        self.fields['departamento'] = forms.ModelMultipleChoiceField(queryset=departamentos(), required=False,
        															 label=u'Departamentos')
        self.fields['municipio'] = forms.ModelMultipleChoiceField(queryset=Municipio.objects.all().order_by('nombre'), 
        															required=False, label='Municipios')