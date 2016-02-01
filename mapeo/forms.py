# -*- coding: UTF-8 -*-
from django.db import models
from models import *
from django import forms

class OrganizacionConsulta(forms.Form):
    def __init__(self, *args, **kwargs):
        super(OrganizacionConsulta, self).__init__(*args, **kwargs)
        self.fields['tipo'] = forms.ChoiceField(label=u'Tipo de organizaciones',choices=TIPO_CHOICES,required=False)