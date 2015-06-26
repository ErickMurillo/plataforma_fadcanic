# -*- coding: utf-8 -*-
from django.db import models
from actividades.lugar.models import Departamento, Municipio
from smart_selects.db_fields import ChainedForeignKey
from multiselectfield import MultiSelectField

# Create your models here.

class Encuestador(models.Model):
    nombre = models.CharField('Nombre del recolector', max_length=250)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name='Encuestadores'

#a- Datos de Recoleccion

class Encuesta(models.Model):
    fecha = models.DateField()
    encuestador = models.ForeignKey(Encuestador)

    year = models.IntegerField(editable=False)

    def save(self):
        self.year = self.fecha.year
        super(Encuesta, self).save()

    def __unicode__(self):
        return self.encuestador.nombre

    class Meta:
        verbose_name_plural = 'Encuesta opinión violencia juvenil y abuso de drogas'


#b- Información del Entrevistado
CHOICE_SEXO = ((1,'Mujer'),(2,'Hombre'))
CHOICE_AREA = ((1,'Urbano'),(2,'Rural'))
CHOICE_HABITA = ((1,'Barrio'),(2,'Comunidad'))

class Etnias(models.Model):
    nombre = models.CharField(max_length=250)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name='Etnias'

class InformacionEntrevistado(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    edad = models.IntegerField()
    etnia = models.ForeignKey(Etnias)
    departamento = models.ForeignKey(Departamento)
    municipio = ChainedForeignKey(
                                Municipio,
                                chained_field="departamento", 
                                chained_model_field="departamento",
                                show_all=False, auto_choose=True,null=True, blank=True)
    residencia = models.IntegerField(choices=CHOICE_AREA)
    habita = models.IntegerField(choices=CHOICE_HABITA)


    def __unicode__(self):
        return self.etnia.nombre

    class Meta:
        verbose_name_plural = 'b-Información del Entrevistado'

#c- Nivel de escolaridad
CHOICE_ESCOLARIDAD = ((1,'No sabe leer'),(2,'Alfabeto'),
                      (3,'Primaria completa'),(4,'Primaria incompleta'),
                      (5,'Secundaria completa'),(6,'Secundaria incompleta'),
                      (7,'Técnico'),(8,'Universitario'))

CHOICE_CIVIL = ((1,'Soltero/Soltera'),(2,'Casado/casada'),
                      (3,'Unión de hecho estable'),(4,'Divorciado/divorciada'),
                      (5,'Viudo/viuda'))

CHOICE_SI_NO = ((1,'Si'),(2,'No'))

class Escolaridad(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    escolaridad = models.IntegerField(choices=CHOICE_ESCOLARIDAD)
    civil = models.IntegerField(choices=CHOICE_CIVIL)
    varones = models.IntegerField()
    mujeres = models.IntegerField()


    def __unicode__(self):
        return self.

    class Meta:
        verbose_name_plural = 'Nivel de escolaridad'

#f- Favor indicar

class ParticipaOrganizacion(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    participado = models.IntegerField(choices=CHOICE_SI_NO)

    def __unicode__(self):
        return u'%s' % (str(self.get_participado_display))

    class Meta:
        verbose_name_plural = 'participa o ha participado en alguna orga. que previene la violencia juvenil y abuso de drogas?'

CHOICE_RESPUESTA_SI = ((1, 'Promotor/Promotora'),
                       (2, 'Asistiendo a charlas que se brinda'),
                       (3, 'Apoyando a otras persona de la comunidad'),
                       (4, 'Organizando actividades'),
                       )
class RespuetaSi(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    respuesta = MultiSelectField(choices=CHOICE_RESPUESTA_SI)

    class Meta:
        verbose_name_plural = 'Indique en cuales tipos de organizaciones'

#I- Conocimiento sobre los temas de violencia y abuso de drogas
CHOICE_VIOLENCIA = ((1, 'Actos violentos realizados por jóvenes'),
                    (2, 'Acción que afecta negativamente a otra persona'),
                    (3, 'Daños físicos (golpes, gritos)'),
                    (4, 'Daños psicológicos (descalificaciones, burlas, insultos)'),
                    (5, 'Todas las anteriores'),
                )

CHOICE_ABUSO_DROGA = ((1, 'Problema de salud pública'),
                    (2, 'Uso de cualquier tipo de droga ilícita'),
                    (3, 'Consumo de droga'),
                    (4, 'No responde'),
                )

CHOICE_TIPO_VIOLENCIA = ((1, 'Violencia hacia las mujeres'),
                    (2, 'Violencia hacia personas con opciones sexual diferente'),
                    (3, 'Acoso sexual'),
                    (4, 'Abuso sexual'),
                    (4, 'Abuso sexual'),
                    (4, 'Abuso sexual'),
                    (4, 'Abuso sexual'),
                )

class Conocimiento(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    FIELDNAME = models.IntegerField()

    def __unicode__(self):
        return self.

    class Meta:
        verbose_name_plural = ''