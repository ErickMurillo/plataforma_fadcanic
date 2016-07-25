# -*- coding: UTF-8 -*-
from django.db import models
from models import *
from django import forms

TIPO_CHOICES = (('','Todos'),(1,'Comité municipal de prevención de violencia'),(2,'Comité comunal'),
					(3,'Diplomado de promotoría'),(4,'Diplomado de comunicación'),
					(5,'Acción docente'),(6,'Comité comunal y municipal'),(7,'Acción masiva'),
					(8,'Debate escolar'))

class OrganizacionConsulta(forms.Form):
    def __init__(self, *args, **kwargs):
        super(OrganizacionConsulta, self).__init__(*args, **kwargs)
        self.fields['tipo'] = forms.ChoiceField(label=u'Tipo de organizaciones',choices=TIPO_CHOICES,required=False)
