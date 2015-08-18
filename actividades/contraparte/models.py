# -*- coding: utf-8 -*-
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from actividades.fadcanic.models import *
from actividades.lugar.models import *
from smart_selects.db_fields import ChainedForeignKey
from actividades.thumbs import ImageWithThumbsField
from actividades.utils import get_file_path
from actividades import short
import datetime
import urlparse, urllib, json, time

#from south.modelsinspector import add_introspection_rules
#add_introspection_rules([], ["^actividades\.thumbs\.ImageWithThumbsField"])

SI_NO = ((1, u'Si'), (2, u'No'))

class Proyecto(models.Model):
    organizacion = models.ForeignKey(Organizacion)
    nombre = models.CharField(max_length=250)
    codigo = models.CharField(max_length=20)
    inicio = models.DateField()
    finalizacion = models.DateField()
    monto_fadcanic = models.IntegerField()
    monto_contrapartida = models.IntegerField()
    contacto = models.CharField(max_length=100, verbose_name='Persona de contacto')
    aporta_fadcanic = models.IntegerField(choices=SI_NO, verbose_name=u'Aporta a Fadcanic')
    municipios = models.ManyToManyField(Municipio)    
    
    def __unicode__(self):
        return u'%s-%s' % (self.organizacion.nombre_corto, self.codigo)
    
    class Meta:
        verbose_name_plural = u'Proyectos'
        
class Resultado(models.Model):    
    nombre_corto = models.CharField(max_length=50)
    descripcion = models.TextField()
    aporta_a = models.ForeignKey(ResultadoPrograma)
    proyecto = models.ForeignKey(Proyecto)
    
    def __unicode__(self):
        return u'%s' % self.nombre_corto
    
    class Meta:
        verbose_name = u'Resultado del proyecto'
        verbose_name_plural = u'Resultados del proyecto' 
        
class Organizador(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return u'%s' % self.nombre
    
    class Meta:
        verbose_name_plural = u'Organizadores'
        
TIPO_ACTIVIDAD = ((1, u'Encuentro'), (2, u'Taller'),
                  (3, u'Cabildo'), (4, u'Reunión Comunitaria'),
                  (5, u'Campamento'), (6, u'Festival'),
                  (7, u'Feria'), (8, u'Gestión ante autoridades'),
                  (9, u'Diplomado'))

TEMA_ACTIVIDAD = ((1, u'Derechos Humanos'), (2, u'Empoderamiento'),
                  (3, u'Participación Cuidadana'), (4, u'Incidencia'),
                  (5, u'Marco Jurídico Nacional'), (6, u'Género'),
                  (7, u'Fortalecimiento de capacidades de la organización'))

EJES = ((1, u'Interculturalidad'), (2, u'Género'), 
        (3, u'Medio ambiente'), (4, u'Generacional'))

EVALUACION = ((99, u'No aplica'), (1, u'Muy bueno'), (2, u'Bueno'),
              (3, u'Regular'), (4, u'Malo'), (5, u'Muy malo'))

class Actividad(models.Model):
    organizacion = models.ForeignKey(Organizacion)
    proyecto = ChainedForeignKey(Proyecto, 
                                 chained_field="organizacion",
                                 chained_model_field="organizacion", 
                                 show_all=False,
                                 auto_choose=True)    
    persona_organiza = models.ForeignKey(Organizador, verbose_name=u'Persona que organiza la actividad')
    nombre_actividad = models.CharField(max_length=150)
    fecha = models.DateTimeField()
    municipio = ChainedForeignKey(Municipio, 
                                 chained_field="proyecto",
                                 chained_model_field="proyecto", 
                                 show_all=False,
                                 auto_choose=True)    
    comunidad = ChainedForeignKey(Comunidad, 
                                 chained_field="municipio",
                                 chained_model_field="municipio", 
                                 show_all=False,
                                 auto_choose=True)
    tipo_actividad = models.ForeignKey(TipoActividad)
    tema_actividad = models.ForeignKey(Tema)
    ejes_transversales = models.ForeignKey(EjeTransversal)
    #participantes por sexo
    hombres = models.IntegerField(default=0)
    mujeres = models.IntegerField(default=0)
    
    #participantes por edad
    # no_dato = models.BooleanField(verbose_name='No hay datos')
    # adultos = models.IntegerField(default=0, verbose_name=u'Adultos/as')
    # jovenes = models.IntegerField(default=0, verbose_name=u'Jóvenes')
    # ninos = models.IntegerField(default=0, verbose_name=u'Niños/as')
    #participantes por tipo
    # no_dato1 = models.BooleanField(verbose_name='No hay datos')
    # autoridades = models.IntegerField(default=0, verbose_name=u'Autoridades públicas')
    # maestros = models.IntegerField(default=0)
    # lideres = models.IntegerField(default=0, verbose_name=u'Lideres/zas Comunitarios')
    # pobladores = models.IntegerField(default=0, verbose_name=u'Pobladores/as')
    # estudiantes = models.IntegerField(default=0)
    # miembros = models.IntegerField(default=0, verbose_name=u'Miembros de organizaciones comunitarias')
    # tecnicos = models.IntegerField(default=0, verbose_name=u'Técnicas/os de Organizaciones Copartes de FADCANIC')

    #participantes por edad
    no_dato = models.BooleanField(verbose_name='No hay datos')
    menor_12 = models.IntegerField('Menor a 12 años',default='0')
    mayor_12 = models.IntegerField('13 a 18 años',default='0')
    mayor_18 = models.IntegerField('19 a 30 años',default='0')
    mayor_30 = models.IntegerField('31 a más años',default='0')
    #identidad etnica
    no_dato1 = models.BooleanField(verbose_name='No hay datos')
    creole = models.IntegerField(default='0')
    miskito = models.IntegerField(default='0')
    ulwa = models.IntegerField(default='0')
    rama = models.IntegerField(default='0')
    mestizo = models.IntegerField(default='0')
    mayagna = models.IntegerField(default='0')
    garifuna = models.IntegerField(default='0')
    extranjero = models.IntegerField(default='0')
    #tipos de actores
    no_dato2 = models.BooleanField(verbose_name='No hay datos')
    estudiante = models.IntegerField(default='0')
    docente = models.IntegerField(default='0')
    periodista = models.IntegerField('Periodista/comunicador',default='0')
    lideres = models.IntegerField('Líderes comunitarios',default='0')
    representantes = models.IntegerField('Representantes de Organizaciones',default='0')
    autoridades = models.IntegerField('Autoridades comunitarias',default='0')
    comunitarios = models.IntegerField('Comunitarios/Pobladores',default='0')
    resultado = ChainedForeignKey(Resultado, 
                                  chained_field="proyecto",
                                  chained_model_field="proyecto", 
                                  show_all=False,
                                  auto_choose=True,
                                  verbose_name=u'Resultado al que aporta')    
    #evaluaciones de hombres
    relevancia = models.IntegerField(choices=EVALUACION, verbose_name=u'Importancia del tema/acción')
    efectividad = models.IntegerField(choices=EVALUACION, verbose_name='Efectividad de la acción')
    aprendizaje = models.IntegerField(choices=EVALUACION, verbose_name=u'Grado de aprendizaje')
    empoderamiento = models.IntegerField(choices=EVALUACION, verbose_name=u'Nivel de apropiación')
    participacion = models.IntegerField(choices=EVALUACION, verbose_name=u'Nivel de participación')
    
    #evaluaciones de mujeres
    relevancia_m = models.IntegerField(choices=EVALUACION, verbose_name=u'Importancia del tema/acción')
    efectividad_m = models.IntegerField(choices=EVALUACION, verbose_name='Efectividad de la acción')
    aprendizaje_m = models.IntegerField(choices=EVALUACION, verbose_name=u'Grado de aprendizaje')
    empoderamiento_m = models.IntegerField(choices=EVALUACION, verbose_name=u'Nivel de apropiación')
    participacion_m = models.IntegerField(choices=EVALUACION, verbose_name=u'Nivel de participación')
    
    #recursos
    comentarios = models.TextField(blank=True, default='')
    acuerdos = models.TextField(blank=True, default='')
    #foto1 = models.ImageField(upload_to='fotos', blank=True, null=True)
    foto1 = ImageWithThumbsField(upload_to=get_file_path, sizes=((128, 96), (640, 480)), blank=True, null=True)   
    foto2 = ImageWithThumbsField(upload_to=get_file_path, sizes=((128, 96), (640, 480)), blank=True, null=True)
    foto3 = ImageWithThumbsField(upload_to=get_file_path, sizes=((128, 96), (640, 480)), blank=True, null=True)
    video = models.CharField(max_length=300, blank=True, default='')
    
    mes = models.IntegerField(editable=False)
    year = models.IntegerField(editable=False)    
    
    fileDir = 'fotos'
    
    def save(self, *args, **kwargs):
        #guardando fecha de ultima edición
        self.organizacion.last_register = datetime.datetime.now()
        self.organizacion.save()
        
        #obteniendo mes and year por motivos de filtros
        self.mes = self.fecha.month
        self.year = self.fecha.year
        super(Actividad, self).save(*args, **kwargs)
            
    def __unicode__(self):
        return u'%s - %s' % (self.nombre_actividad, self.fecha)
    
    def get_video_id(self):
        if self.video:            
            url_data = urlparse.urlparse(self.video)
            query = urlparse.parse_qs(url_data.query)
            return query["v"][0]
        return None                        
        
    def get_vthumb(self):
        id = self.get_video_id()
        if id:
            return '<img width="128" height="96" src="http://img.youtube.com/vi/%s/2.jpg" alt="thumb">' % id
        return ''
    
    def get_video(self):
        id = self.get_video_id()
        if id:
            return """http://www.youtube.com/embed/%s??showsearch=0&showinfo=0&iv_load_policy=3&autoplay=1""" % id
        return ''
    
    def clean(self):
        suma_base = self.hombres + self.mujeres
        #suma_edad = self.adultos + self.jovenes + self.ninos
        suma_edad = self.menor_12 + self.mayor_12 + self.mayor_18 + self.mayor_30
        #suma_tipo = self.autoridades + self.maestros + self.lideres + self.pobladores + self.estudiantes + self.miembros + self.tecnicos
        suma_tipo = self.estudiante + self.docente + self.periodista + self.lideres + self.representantes + self.autoridades + self.comunitarios
        suma_etnia = self.creole + self.miskito + self.ulwa + self.rama + self.mestizo + self.mayagna + self.garifuna + self.extranjero
        
        if not self.no_dato:
            if suma_base != suma_edad:
                raise ValidationError('La suma de los participantes por edad no concuerda')
            
        if not self.no_dato1:
            if suma_base != suma_tipo:
                raise ValidationError('La suma de los participantes por tipo no concuerda')

        if not self.no_dato2:
            if suma_base != suma_etnia:
                raise ValidationError('La suma de los participantes por identidad étnica no concuerda')
    
    class Meta:
        verbose_name_plural = u'Actividades' 
        
class Output(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)    
    params = models.TextField()
    comment = models.TextField(blank=True, default='')
    file = models.BooleanField()
    bar_img = models.URLField(blank=True, null=True)
    pie1_img = models.URLField(blank=True, null=True)
    pie2_img = models.URLField(blank=True, null=True)
    # nueva forma de guardar salida
    html_table = models.TextField(blank=True, default='')
    bar_chart = models.TextField(blank=True, default='') # bar chart params if exists
    pie_chart_one = models.TextField(blank=True, default='') # first pie chart params if exists
    pie_chart_two = models.TextField(blank=True, default='') # second pie chart params if exists    
    
    def _hash(self):
        if self.id:
            return short.encode_url(self.id)
        
    hash = property(_hash)
    
    class Meta:
        ordering = ['-id']
        verbose_name = u'Salida'
        verbose_name_plural = u'Salidas'
