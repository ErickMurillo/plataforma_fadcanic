# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from actividades.thumbs import ImageWithThumbsField
from actividades.utils import get_file_path
import datetime
from sorl.thumbnail import ImageField

class ResultadoPrograma(models.Model):   
    nombre_corto = models.CharField(max_length=50)
    descripcion = models.TextField()
    
    def __unicode__(self):
        return '%s' % self.nombre_corto
    
    class Meta:
        verbose_name = 'Resultado de programa'
        verbose_name_plural = 'Resultados de programa'
        
class Organizacion(models.Model):
    admin = models.ForeignKey(User)
    nombre = models.CharField(max_length=250)
    nombre_corto = models.CharField(max_length=15, help_text='Pueden ser siglas')
    contacto = models.CharField(max_length=200, verbose_name='Persona de contacto')
    telefono = models.CharField(max_length=12, blank=True, default='')
    direccion = models.CharField(max_length=300, blank=True, default='')
    web = models.URLField(verbose_name='Sitio web', blank=True, default='www.example.com')
    historia = models.TextField(blank=True, default='')      
    logo = ImageField(upload_to=get_file_path,blank=True, null=True)
    last_register = models.DateTimeField(editable=False, default=datetime.datetime.now)
    
    fileDir = 'logos/'
    
    def __unicode__(self):
        return u'%s' % self.nombre_corto
    
    class Meta:
        verbose_name_plural = 'Organizaciones'
        permissions = (
            ("view_programa", "Puede ver salidas por programa"),            
        )
        
class Generica(models.Model):
    nombre = models.CharField(max_length=150)
    
    def __unicode__(self):
        return u'%s' % self.nombre
    
    class Meta:
        abstract = True

class TipoActividad(Generica):
    
    class Meta:
        verbose_name = 'Tipo de actividad'
        verbose_name_plural = 'Tipos de actividad'

class Tema(Generica):
    
    class Meta:
        verbose_name = 'Tema de actividad'
        verbose_name_plural = 'Temas de actividad'
        
class EjeTransversal(Generica):
    
    class Meta:
        verbose_name_plural = 'Ejes transversales'