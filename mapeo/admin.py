# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *
from django.forms import SelectMultiple

#Register your models here.
class OrganizacionesAdmin(admin.ModelAdmin):
	filter_horizontal = ('cobertura','acciones_violencia','acciones_consumo_drogas','acciones_apoyo')
	fieldsets = [
			(None, {'fields' : ['tipo','nombre','persona_contacto','direccion','departamento','municipio','comunidad',
								('convencional','celular','correo'),('web','facebook','twitter'),('youtube','otro'),
								'cobertura',('masculino','femenino'),'integrantes',('mayor_13','mayor_19','mayor_30'),
								'acciones_violencia','acciones_consumo_drogas','acciones_apoyo'
								]}),
		]

	class Media:
		js = ('/static/mapeo/js/admin.js', ) 

admin.site.register(Organizaciones,OrganizacionesAdmin)
admin.site.register(Acciones_Violencia)
admin.site.register(Acciones_Consumo_Drogas)
admin.site.register(Acciones_Apoyo)