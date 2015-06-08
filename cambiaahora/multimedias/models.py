# -*- coding: utf-8 -*-
from django.db import models
from cambiaahora.utils import get_file_path
from django.contrib.auth.models import User
from cambiaahora.noticias.models import CHOICE_APROBACION, CHOICE_IDIOMA
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Videos(models.Model):
    nombre = models.CharField(_('Nombre'), max_length=250)
    aprobacion = models.IntegerField(choices=CHOICE_APROBACION, default='1', verbose_name=_('Aprobación'))
    idioma = models.IntegerField(choices=CHOICE_IDIOMA, default='1', verbose_name=_('Idioma'))

    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name=_('Video')
        verbose_name_plural=_('Videos')

class Audios(models.Model):
    nombre = models.CharField(_('Nombre'), max_length=250)
    aprobacion = models.IntegerField(choices=CHOICE_APROBACION, default='1', verbose_name=_('Aprobación'))
    idioma = models.IntegerField(choices=CHOICE_IDIOMA, default='1', verbose_name=_('Idioma'))

    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name=_('Audio')
        verbose_name_plural=_('Audios')

class Fotos(models.Model):
    nombre = models.CharField(_('Nombre'), max_length=250)
    aprobacion = models.IntegerField(choices=CHOICE_APROBACION, default='1', verbose_name=_('Aprobación'))
    idioma = models.IntegerField(choices=CHOICE_IDIOMA, default='1', verbose_name=_('Idioma'))

    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name=_('Foto')
        verbose_name_plural=_('Fotos')

#los Inlines de los videos, audios, fotos

class SubirVideos(models.Model):
    videos = models.ForeignKey(Videos)
    titulo = models.CharField(_('Titulo'),max_length=250)
    video = models.URLField(_('Video'),)

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name=_('Subir video')
        verbose_name_plural=_('Subir videos')

class SubirAudios(models.Model):
    audios = models.ForeignKey(Audios)
    titulo = models.CharField(_('Titulo'),max_length=250)
    audio = models.FileField(_('Audio'),)

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name=_('Subir audio')
        verbose_name_plural=_('Subir audios')

class SubirFotos(models.Model):
    fotos = models.ForeignKey(Fotos)
    titulo = models.CharField(_('Titulo'),max_length=250)
    foto = models.FileField(_('Foto'),)

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name=_('Subir foto')
        verbose_name_plural=_('Subir fotos')