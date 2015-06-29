# -*- coding: UTF-8 -*-
from django.db import models
from models import *
from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError

class MonitoreoForm(ModelForm):

    class Meta:
        model = Monitoreo
        fields = ('masculino','femenino','menor_12','mayor_12','mayor_18','mayor_30','creole',
                    'miskito','ulwa','ulwa','rama','mestizo','mayagna','garifuna','extranjero',
                    'estudiante','docente','periodista','lideres','representantes','autoridades','comunitarios')

    def clean(self):
        masculino = self.cleaned_data.get('masculino')
        femenino = self.cleaned_data.get('femenino')
        menor_12 = self.cleaned_data.get('menor_12')
        mayor_12 = self.cleaned_data.get('mayor_12')
        mayor_18 = self.cleaned_data.get('mayor_18')
        mayor_30 = self.cleaned_data.get('mayor_30')
        creole = self.cleaned_data.get('creole')
        miskito = self.cleaned_data.get('miskito')
        ulwa = self.cleaned_data.get('ulwa')
        rama = self.cleaned_data.get('rama')
        mestizo = self.cleaned_data.get('mestizo')
        mayagna = self.cleaned_data.get('mayagna')
        garifuna = self.cleaned_data.get('garifuna')
        extranjero = self.cleaned_data.get('extranjero')
        estudiante = self.cleaned_data.get('estudiante')
        docente = self.cleaned_data.get('docente')
        periodista = self.cleaned_data.get('periodista')
        lideres = self.cleaned_data.get('lideres')
        representantes = self.cleaned_data.get('representantes')
        autoridades = self.cleaned_data.get('autoridades')
        comunitarios = self.cleaned_data.get('comunitarios')

        suma_total_participantes = (masculino + femenino)
        suma_rangos = (menor_12 + mayor_12 + mayor_18 + mayor_30)
        suma_identidad_etnica = (creole + miskito + ulwa + rama + mestizo + mayagna + garifuna + extranjero)
        suma_actores = (estudiante + docente + periodista + lideres + representantes + autoridades + comunitarios)

        if suma_total_participantes < suma_rangos:

            raise ValidationError("Sumatoria de rangos de edad mayor a el total de participantes")

        if suma_total_participantes > suma_rangos:

            raise ValidationError("Sumatoria de rangos de edad menor a el total de participantes")

        if suma_total_participantes < suma_identidad_etnica:

            raise ValidationError("Sumatoria de identidad étnica mayor a el total de participantes")

        if suma_total_participantes > suma_identidad_etnica:

            raise ValidationError("Sumatoria de identidad étnica menor a el total de participantes")

        if suma_total_participantes < suma_actores:

            raise ValidationError("Sumatoria de actores mayor a el total de participantes")

        if suma_total_participantes > suma_actores:

            raise ValidationError("Sumatoria de ractores menor a el total de participantes")

        return self.cleaned_data