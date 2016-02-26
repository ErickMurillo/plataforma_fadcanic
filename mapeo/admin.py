# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *
from django.forms import SelectMultiple

#Register your models here.

class Info_Organizaciones_Inline(admin.TabularInline):
    model = Info_Organizaciones
    extra = 1

class OrganizacionesAdmin(admin.ModelAdmin):
	filter_horizontal = ('cobertura','acciones_violencia','acciones_consumo_drogas','acciones_apoyo')
	fieldsets = [
			(None, {'fields' : ['tipo','nombre','foto','persona_contacto','direccion','departamento','municipio','comunidad',
								#('convencional_1','celular_1','correo'),('web','facebook','twitter'),('youtube','otro'),
								'correo',
								'cobertura',('masculino','femenino'),'integrantes',('mayor_13','mayor_19','mayor_30'),
								'cantidad_org'
								]}),
		]

	inlines = [Info_Organizaciones_Inline]
		
	list_display = ['nombre','tipo']
	list_filter = ['tipo']
	search_fields = ['nombre',]

	class Media:
		js = ('/static/mapeo/js/admin.js', ) 

admin.site.register(Organizaciones,OrganizacionesAdmin)
# admin.site.register(Acciones_Violencia)
# admin.site.register(Acciones_Consumo_Drogas)
# admin.site.register(Acciones_Apoyo)
