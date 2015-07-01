from django.contrib import admin
from .models import *

class InformacionInline(admin.TabularInline):
    model = InformacionEntrevistado
    #fields = ((),)
    extra = 1
    max_num = 1

class EscolaridadInline(admin.TabularInline):
    model = Escolaridad
    extra = 1
    max_num = 1

class ParticipaOrganizacionInline(admin.TabularInline):
    model = ParticipaOrganizacion
    extra = 1
    max_num = 1

class RespuetaSiInline(admin.TabularInline):
    model = RespuetaSi
    extra = 1
    max_num = 1

class ConocimientoInline(admin.TabularInline):
    model = Conocimiento
    extra = 1
    max_num = 1

class ActitudInline(admin.TabularInline):
    model = Actitud
    extra = 1
    max_num = 1

class PracticasInline(admin.TabularInline):
    model = Practicas
    extra = 1
    max_num = 1

class PercepcionInline(admin.TabularInline):
    model = Percepcion
    extra = 1
    max_num = 1

class EstadoActualInline(admin.TabularInline):
    model = EstadoActual
    extra = 1
    max_num = 1

class EncuestaAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    exclude = ('user',)
    fields = (('fecha','encuestador'),)
    inlines = [InformacionInline,EscolaridadInline,ParticipaOrganizacionInline,
                RespuetaSiInline,ConocimientoInline,ActitudInline,PracticasInline,
                PercepcionInline,EstadoActualInline]
    list_display = ('fecha', 'encuestador')


# Register your models here.
admin.site.register(Encuesta, EncuestaAdmin)
admin.site.register(Encuestador)
