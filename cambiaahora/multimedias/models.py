# -*- coding: utf-8 -*-
from django.db import models
from cambiaahora.utils import get_file_path
from django.contrib.auth.models import User
from cambiaahora.noticias.models import CHOICE_APROBACION, CHOICE_IDIOMA, Categoria
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField

# Create your models here.

class Videos(models.Model):
    nombre = models.CharField(_(u'Nombre'), max_length=250)
    aprobacion = models.IntegerField(choices=CHOICE_APROBACION, default='1', verbose_name=_(u'Aprobación'))
    idioma = models.IntegerField(choices=CHOICE_IDIOMA, default='1', verbose_name=_(u'Idioma'))

    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name=_(u'Video')
        verbose_name_plural=_(u'Videos')

class Audios(models.Model):
    nombre = models.CharField(_(u'Nombre'), max_length=250)
    aprobacion = models.IntegerField(choices=CHOICE_APROBACION, default='1', verbose_name=_(u'Aprobación'))
    idioma = models.IntegerField(choices=CHOICE_IDIOMA, default='1', verbose_name=_(u'Idioma'))

    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name=_(u'Audio')
        verbose_name_plural=_(u'Audios')

class Fotos(models.Model):
    nombre = models.CharField(_(u'Nombre'), max_length=250)
    aprobacion = models.IntegerField(choices=CHOICE_APROBACION, default='1', verbose_name=_(u'Aprobación'))
    idioma = models.IntegerField(choices=CHOICE_IDIOMA, default='1', verbose_name=_(u'Idioma'))

    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name=_(u'Foto')
        verbose_name_plural=_(u'Fotos')
<<<<<<< HEAD
=======

class Documentales(models.Model):
    nombre = models.CharField(_(u'Nombre'), max_length=250)
    fecha = models.DateField(_(u'Fecha'))
    categoria = models.ForeignKey(Categoria, verbose_name=_(u'Categoria'))
    descripcion = models.TextField(_(u'Descripción'))
    aprobacion = models.IntegerField(choices=CHOICE_APROBACION, default='1', verbose_name=_(u'Aprobación'))
    idioma = models.IntegerField(choices=CHOICE_IDIOMA, default='1', verbose_name=_(u'Idioma'))

    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name=_(u'Documentale')
        verbose_name_plural=_(u'Documentales')
>>>>>>> d27e4dba33e0028aad23f3b729e6f194b26e2e33

#los Inlines de los videos, audios, fotos

class SubirVideos(models.Model):
    videos = models.ForeignKey(Videos)
    titulo = models.CharField(_(u'Titulo'),max_length=250)
    video = models.URLField(_(u'Video'),)

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name=_(u'Subir video')
        verbose_name_plural=_(u'Subir videos')

class SubirAudios(models.Model):
    audios = models.ForeignKey(Audios)
    titulo = models.CharField(_(u'Titulo'),max_length=250)
    audio = models.FileField(_(u'Audio'),)

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name=_(u'Subir audio')
        verbose_name_plural=_(u'Subir audios')

class SubirFotos(models.Model):
    fotos = models.ForeignKey(Fotos)
    titulo = models.CharField(_(u'Titulo'),max_length=250)
<<<<<<< HEAD
    foto = models.FileField(_(u'Foto'),)
=======
    foto = ImageField(_(u'Foto'),)

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name=_(u'Subir foto')
        verbose_name_plural=_(u'Subir fotos')

class SubirDocumentales(models.Model):
    documental = models.ForeignKey(Documentales)
    titulo = models.CharField(_(u'Titulo'),max_length=250)
    video = models.URLField(_(u'Video'))
>>>>>>> d27e4dba33e0028aad23f3b729e6f194b26e2e33

    def __unicode__(self):
        return self.titulo

    class Meta:
<<<<<<< HEAD
        verbose_name=_(u'Subir foto')
        verbose_name_plural=_(u'Subir fotos')
=======
        verbose_name=_(u'Subir documento')
        verbose_name_plural=_(u'Subir documentos')
>>>>>>> d27e4dba33e0028aad23f3b729e6f194b26e2e33
