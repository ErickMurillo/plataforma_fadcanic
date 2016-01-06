from django.contrib import admin
from .models import *
from import_export.admin import ImportExportActionModelAdmin

class InformacionInline(admin.TabularInline):
    model = InformacionEntrevistado
    fields = (('sexo','edad','etnia'),('departamento','municipio'))
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

class ConocimientoInline(admin.StackedInline):
    model = Conocimiento
    fields = (('pregunta1','pregunta2'),('pregunta3','pregunta4'),
                ('pregunta5','pregunta6'),('pregunta7','pregunta8'),
                ('pregunta9','pregunta10'),('pregunta11','pregunta12'),
                ('pregunta13','pregunta14'))
    extra = 1
    max_num = 1

class ActitudInline(admin.StackedInline):
    model = Actitud
    fields = (('pregunta15','pregunta16'),('pregunta17','pregunta18'),
                ('pregunta19','pregunta20'))
    extra = 1
    max_num = 1

class PracticasInline(admin.StackedInline):
    model = Practicas
    fields = (('pregunta21','pregunta22'),('pregunta23','pregunta24'),
            )
    extra = 1
    max_num = 1

class PercepcionInline(admin.StackedInline):
    model = Percepcion
    fields = (('pregunta25','pregunta26'),('pregunta27','pregunta28'),
                ('pregunta29_1','pregunta30'),('pregunta31','pregunta32_1'),
                ('pregunta33',))
    extra = 1
    max_num = 1

class EstadoActualInline(admin.StackedInline):
    model = EstadoActual
    fields = (('pregunta34','si_respuesta_34'),('pregunta35','si_respuesta_35'),
                ('pregunta36','pregunta37'),('pregunta38','pregunta39'))
    extra = 1
    max_num = 1

#ImportExportActionModelAdmin
class EncuestaAdmin(ImportExportActionModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    exclude = ('user',)
    fields = (('fecha','grupos'),('encuestador',))
    inlines = [InformacionInline,EscolaridadInline,ParticipaOrganizacionInline,
                RespuetaSiInline,ConocimientoInline,ActitudInline,PracticasInline,
                PercepcionInline,EstadoActualInline]
    list_display = ('fecha','grupos','encuestador')

    class Media:
        css = {
            "all": ("/static/cambiaahora/css/my_styles_admin.css",)
        }
        #js = ("my_code.js",)


# Register your models here.
admin.site.register(Encuesta, EncuestaAdmin)

class EncuestadorAdmin(ImportExportActionModelAdmin):
    model = Encuestador

admin.site.register(Encuestador,EncuestadorAdmin)
# admin.site.register(Encuestador)

#export import
class InformacionAdmin(ImportExportActionModelAdmin):
    model = InformacionEntrevistado

class EscolaridadAdmin(ImportExportActionModelAdmin):
    model = Escolaridad

class ParticipaOrganizacionAdmin(ImportExportActionModelAdmin):
    model = ParticipaOrganizacion

class RespuetaSiAdmin(ImportExportActionModelAdmin):
    model = RespuetaSi

class ConocimientoAdmin(ImportExportActionModelAdmin):
    model = Conocimiento

class ActitudAdmin(ImportExportActionModelAdmin):
    model = Actitud

class PracticasAdmin(ImportExportActionModelAdmin):
    model = Practicas

class PercepcionAdmin(ImportExportActionModelAdmin):
    model = Percepcion

class EstadoActualAdmin(ImportExportActionModelAdmin):
    model = EstadoActual

admin.site.register(InformacionEntrevistado,InformacionAdmin)
admin.site.register(Escolaridad,EscolaridadAdmin)
admin.site.register(ParticipaOrganizacion,ParticipaOrganizacionAdmin)
admin.site.register(RespuetaSi,RespuetaSiAdmin)
admin.site.register(Conocimiento,ConocimientoAdmin) 
admin.site.register(Actitud,ActitudAdmin) 
admin.site.register(Practicas,PracticasAdmin)
admin.site.register(Percepcion,PercepcionAdmin)
admin.site.register(EstadoActual,EstadoActualAdmin)