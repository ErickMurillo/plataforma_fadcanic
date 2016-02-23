# -*- coding: utf-8 -*-
from django import forms
from django.forms.widgets import RadioSelect
from fadcanic.models import *
from contraparte.models import *
from formutils.forms import FormFKAutoFill    
from lugar.models import *
from utils import * 

MONTH_CHOICES = (('', 'Mes'),
				 (1, 'Enero'), (2, 'Febrero'),
				 (3, 'Marzo'), (4, 'Abril'),
				 (5, 'Mayo'), (6, 'Junio'),
				 (7, 'Julio'), (8, 'Agosto'),
				 (9, 'Septiembre'), (10, 'Octubre'),
				 (11, 'Noviembre'), (12, 'Diciembre'))

ANIOS_CHOICE = (('', u'Año'), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018,2018), (2019,2019))

class ProyectoForm(FormFKAutoFill):
	#validar que el usuario solo pueda ver su organizacion.
	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request', None)
		super(ProyectoForm, self).__init__(*args, **kwargs)
		# if not self.request.user.has_perm('fadcanic.view_programa') or not self.request.user.is_superuser:                    
		#     self.fields['organizacion'].queryset = Organizacion.objects.filter(admin=self.request.user)
	
		self.fields['organizacion'] = forms.ModelChoiceField(queryset=Organizacion.objects.all(),required=True, 
											  widget=forms.Select(attrs={'class':'form-large'}))
		self.fields['proyecto'] = forms.ModelChoiceField(queryset=Proyecto.objects.all(), required=True,
										  widget=forms.Select(attrs={'class':'form-large'}))
		self.fields['resultado'] = forms.ModelMultipleChoiceField(queryset=Resultado.objects.all(), required=True)
		self.fields['fecha_inicio'] = forms.DateField(required=True, widget=forms.TextInput(attrs={'style':'width: 320px'}))
		self.fields['fecha_fin'] = forms.DateField(required=True, widget=forms.TextInput(attrs={'style':'width: 320px'}))

		#query municipios--------------------------------------
		foo = Actividad.objects.all().order_by('municipio__nombre').distinct().values_list('municipio__id', flat=True)
		#------------------------------------------------------
		self.fields['municipio'] = forms.ModelMultipleChoiceField(queryset=Municipio.objects.filter(id__in=foo),
									 required=False)
		
	class Foo:
		config = [{'on_change': {'field': 'organizacion'},
				   'fill': {'field': 'proyecto', 'model': 'Proyecto', 'app_label': 'contraparte'},
				   'values': {'filter': 'organizacion', 'regress': 'id,nombre'}},
				  {'on_change': {'field': 'proyecto'},
				   'fill': {'field': 'resultado', 'model': 'Resultado', 'app_label': 'contraparte'},
				   'values': {'filter': 'proyecto', 'regress': 'id,nombre_corto'}},
				  ]

class ProgramaForm(forms.Form):
	organizaciones = forms.ModelMultipleChoiceField(queryset=Organizacion.objects.all(), widget=forms.SelectMultiple(attrs={'style':'width: 320px'})) 
	proyectos = forms.ModelMultipleChoiceField(queryset=Proyecto.objects.all(), required=False, widget=forms.SelectMultiple(attrs={'style':'width: 320px'}))
	resultado = forms.ModelChoiceField(queryset=ResultadoPrograma.objects.all().exclude(id=8), empty_label='Todos los resultados',
									   widget=forms.Select(attrs={'class':'form-large'}), required=False)
	fecha_inicio = forms.DateField(required=False)
	fecha_fin = forms.DateField(required=False) 

#--- parametros para creacion del form de cruces ----
first_class = {'tipo_actividad': ['tipo_actividad'], 
			   'tema_actividad': ['tema_actividad'], 
			   'ejes_transversales': ['ejes_transversales']}

participantes = {'participantes_por_sexo': ['hombres', 'mujeres'],
				 'participantes_por_edad': ['menor_12', 'mayor_12', 'mayor_18', 'mayor_30'],
				 'participantes_por_etnia': ['creole', 'miskito', 'ulwa','rama', 'mestizo',
											 'mayagna', 'garifuna','extranjero'],
				 'participantes_por_tipo': ['estudiante', 'docente', 'periodista',
											'lideres', 'representantes', 'comunitarios']}

evaluacion = {'importancia_del_tema': 'relevancia',
			  'efectividad_de_la_accion': 'efectividad',
			  'grado_de_aprendizaje': 'aprendizaje',
			  'nivel_de_apropiacion': 'empoderamiento',
			  'nivel_de_participacion': 'participacion'}

evaluacion_m = {'importancia_del_tema': 'relevancia_m',
			  'efectividad_de_la_accion': 'efectividad_m',
			  'grado_de_aprendizaje': 'aprendizaje_m',
			  'nivel_de_apropiacion': 'empoderamiento_m',
			  'nivel_de_participacion': 'participacion_m'}

class SubFiltroForm(forms.Form):  
	def __init__(self, *args, **kwargs):
		super(SubFiltroForm, self).__init__(*args, **kwargs)  
		self.fields['main_var'] = forms.ChoiceField(choices=to_choices(first_class.keys()))
		self.fields['participantes'] = forms.ChoiceField(choices=to_choices(participantes.keys()),
										  required=False)
		self.fields['evaluacion'] = forms.ChoiceField(choices=to_choices(evaluacion.keys()),
									   required=False)
		self.fields['eval_tipo'] = forms.ChoiceField(choices=((1, 'Hombres'), (2, 'Mujeres')), 
									  widget=RadioSelect(attrs={'class':'nobutton'}),initial=1)
		self.fields['total'] = forms.BooleanField(required=False, label=u"Ver totales")
		self.fields['bar_graph'] = forms.BooleanField(required=False, label=u"Gráfico de barras")
		self.fields['pie_graph'] = forms.BooleanField(required=False, label=u"Gráfico de pastel")
	
	def clean(self):
		cleaned_data = self.cleaned_data
		participantes = cleaned_data.get("participantes")
		evaluacion = cleaned_data.get("evaluacion")
		recursos = cleaned_data.get("recursos")

		if not participantes and not evaluacion and not recursos:              
			#validando que se marque una segunda variable         
			raise forms.ValidationError("Debes elegir al menos una segunda variable "
						"a cruzar. Ejm: Participantes o Evaluacion o Recursos")
			
		if (participantes and evaluacion) or (participantes and recursos) or (evaluacion and recursos):
			#validando que solo se elija una segunda variable         
			raise forms.ValidationError("Solo puede seleccionar una segunda variable")                            
		
		return cleaned_data

class PanelForm(forms.Form):
	fecha_inicio = forms.DateField(required=False)
	fecha_fin = forms.DateField(required=False) 
