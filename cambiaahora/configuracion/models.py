# -*- coding: utf-8 -*-

from django.db import models
from sorl.thumbnail import ImageField
from cambiaahora.utils import get_file_path
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from cambiaahora.noticias.models import CHOICE_IDIOMA

# Create your models here.

class Configuracion(models.Model):
    foto = ImageField(_(u'Foto'), upload_to=get_file_path, blank=True, null=True)
    titulo1 = models.CharField(_(u'Titulo español'), max_length=250)
    descripcion1 = models.CharField(_(u'Descripción español'), max_length=450, null=True)
    titulo2 = models.CharField(_(u'Titulo ingles'),max_length=250)
    descripcion2 = models.CharField(_(u'Descripción ingles'),max_length=450, null=True)
    titulo3 = models.CharField(_(u'Titulo miskitu'),max_length=250)
    descripcion3 = models.CharField(_(u'Descripción miskitu'),max_length=450, null=True)
    titulo4 = models.CharField(_(u'Titulo otro'),max_length=250)
    descripcion4 = models.CharField(_(u'Descripción otro'),max_length=450, null=True)
    
    user = models.ForeignKey(User)
    
    fileDir = 'configuracion/'

    def __unicode__(self):
        return u'%s' % (self.titulo1)

    class Meta:
        verbose_name = _(u'Configuración')
        verbose_name_plural = _(u'Configuraciones')

class LogoApoyan(models.Model):
    nombre = models.CharField(_(u'siglas organismo'), max_length=250)
    foto = ImageField(_(u'Foto'), upload_to=get_file_path, blank=True, null=True)

    user = models.ForeignKey(User)
    
    fileDir = 'logoApoyan/'

    def __unicode__(self):
        return u'%s' % (self.nombre)

    class Meta:
        verbose_name = _(u'Logo apoyan')
        verbose_name_plural = _(u'Logo apoyan')

class Informacion(models.Model):
    foto = ImageField(_(u'Foto principal'), upload_to=get_file_path, blank=True, null=True)
    idioma = models.IntegerField(choices=CHOICE_IDIOMA, default='1',verbose_name=_(u'Idioma'))
    objetivos = models.TextField()
    territorios = models.TextField()
    acciones = models.TextField()

    user = models.ForeignKey(User)
    
    fileDir = 'imagenInformacion/'

    def __unicode__(self):
        return u'%s' % (self.objetivos)

    class Meta:
        verbose_name = _(u'Información de la campaña')
        verbose_name_plural = _(u'Información de la campaña')



