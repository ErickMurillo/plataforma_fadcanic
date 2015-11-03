# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField
from actividades.lugar.models import *
from smart_selects.db_fields import ChainedForeignKey

class Acciones_Violencia(models.Model):
	nombre = models.CharField(max_length=200)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = "Acción en prevención de violencia"
		verbose_name_plural = "Acciones en prevención de violencia"

class Acciones_Consumo_Drogas(models.Model):
	nombre = models.CharField(max_length=200)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = "Acción en prevención de consumo de drogas"
		verbose_name_plural = "Acciones en prevención de consumo de drogas"

class Acciones_Apoyo(models.Model):
	nombre = models.CharField(max_length=200)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = "Acción de apoyo directo a la Campaña"
		verbose_name_plural = "Acciones de apoyo directo a la Campaña"

TIPO_CHOICES = (
		(1,'Organización que apoya y participa con la Campaña'),
		(2,'Comité comunal'),
		(3,'Diplomado de promotoría'),
		(4,'Diplomado de comunicación'),
	)

class Organizaciones(models.Model):
	tipo =  models.IntegerField(choices=TIPO_CHOICES)
	nombre = models.CharField(max_length=200)
	persona_contacto = models.CharField(max_length=200,verbose_name='Persona de contacto (Opcional)',blank=True,null=True)
	direccion = models.CharField(max_length=400,blank=True,null=True)
	departamento = models.ForeignKey(Departamento)
	municipio = ChainedForeignKey(
								Municipio,
								chained_field="departamento",
								chained_model_field="departamento",
								show_all=False, auto_choose=True)
	comunidad = ChainedForeignKey(
								Comunidad,
								chained_field="municipio",
								chained_model_field="municipio",
								show_all=False, auto_choose=True,blank=True,null=True)
	convencional = models.IntegerField(blank=True,null=True)
	celular = models.IntegerField(blank=True,null=True)
	correo = models.EmailField(blank=True,null=True)
	web = models.URLField(blank=True,null=True)
	facebook = models.URLField(blank=True,null=True)
	twitter = models.URLField(blank=True,null=True)
	youtube = models.URLField(blank=True,null=True)
	otro = models.URLField(blank=True,null=True)
	cobertura = models.ManyToManyField(Municipio,related_name='Cobertura',blank=True)

	masculino = models.IntegerField(null=True,blank=True,verbose_name='Cantidad de integrantes masculinos')
	femenino = models.IntegerField(null=True,blank=True,verbose_name='Cantidad de integrantes femeninos')

	integrantes = RichTextField('Nombre de los integrantes',blank=True,null=True)
	
	#edades
	mayor_13 = models.IntegerField('Edades de integrantes de 13 a 18 años',null=True,blank=True)
	mayor_19 = models.IntegerField('Edades de integrantes de 19 a 30 años',null=True,blank=True)
	mayor_30 = models.IntegerField('Edades de integrantes de 31 a más años',null=True,blank=True)
	###########
	acciones_violencia = models.ManyToManyField(Acciones_Violencia,blank=True)
	acciones_consumo_drogas = models.ManyToManyField(Acciones_Consumo_Drogas,blank=True)
	acciones_apoyo = models.ManyToManyField(Acciones_Apoyo,blank=True)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = "Organización"
		verbose_name_plural = "Organizaciones"
