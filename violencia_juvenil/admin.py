from django.contrib import admin
from .models import *

class InformacionInline(admin.StackedInline):
    model = InformacionEntrevistado
    fields = (('sexo','residencia','habita'),('edad','etnia','departamento','municipio'))
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
                ('pregunta13'))
    extra = 1
    max_num = 1

class ActitudInline(admin.StackedInline):
    model = Actitud
    fields = (('pregunta14','pregunta15'),('pregunta16','pregunta17'),
                ('pregunta18','pregunta19'),('pregunta20'))
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
                ('pregunta29','pregunta30'),('pregunta31','pregunta32'),
                ('pregunta33','pregunta34'),('pregunta35','pregunta36'),
                ('pregunta37','pregunta38'))
    extra = 1
    max_num = 1

class EstadoActualInline(admin.StackedInline):
    model = EstadoActual
    fields = (('pregunta40','pregunta41'),('pregunta42','si_respuesta_42'),
                ('pregunta43','si_respuesta_43'),('pregunta44','pregunta45'))
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

    class Media:
        css = {
            "all": ("/static/cambiaahora/css/my_styles_admin.css",)
        }
        #js = ("my_code.js",)


# Register your models here.
admin.site.register(Encuesta, EncuestaAdmin)
admin.site.register(Encuestador)
