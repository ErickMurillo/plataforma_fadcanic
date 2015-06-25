# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *
from .forms import *

class MonotireoAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    exclude = ('user',)
    fieldsets = [
        (None, {'fields' : [('fecha','recolector'),('eje','resultado'),('municipio','comunidad'),
                            ('actividad',),('resultados',)]}),

        ('Categorización de participantes', {'fields' : [('masculino','femenino')]}),

        ('Por edad', {'fields' : [('menor_12','mayor_12','mayor_18','mayor_30')]}),

        ('Identidad étnica', {'fields' : [('creole','miskito','ulwa','rama'),
                                          ('mestizo','mayagna','garifuna','extranjero')]}),
        
        ('Tipos de actores', {'fields' : [('estudiante','docente','periodista','lideres'),
                                          ('representantes','autoridades','comunitarios')]}),
    ]
    form = MonitoreoForm
# Register your models here.
admin.site.register(Monitoreo, MonotireoAdmin)
admin.site.register(Recolector)