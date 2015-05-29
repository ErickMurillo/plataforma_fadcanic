# -*- coding: utf-8 -*-
from django.db import models
from cambiaahora.utils import get_file_path
from django.contrib.auth.models import User
from cambiaahora.noticias.models import CHOICE_APROBACION, CHOICE_IDIOMA

# Create your models here.

class Videos(models.Model):
    nombre = models.CharField(max_length=250)
    aprobacion = models.IntegerField(choices=CHOICE_APROBACION, default='1')
    idioma = models.IntegerField(choices=CHOICE_IDIOMA, default='1')

    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name='Video'
        verbose_name_plural='Videos'

class Audios(models.Model):
    nombre = models.CharField(max_length=250)
    aprobacion = models.IntegerField(choices=CHOICE_APROBACION, default='1')
    idioma = models.IntegerField(choices=CHOICE_IDIOMA, default='1')

    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name='Audio'
        verbose_name_plural='Audios'

class Fotos(models.Model):
    nombre = models.CharField(max_length=250)
    aprobacion = models.IntegerField(choices=CHOICE_APROBACION, default='1')
    idioma = models.IntegerField(choices=CHOICE_IDIOMA, default='1')

    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name='Foto'
        verbose_name_plural='Fotos'

#los Inlines de los videos, audios, fotos

class SubirVideos(models.Model):
    videos = models.ForeignKey(Videos)
    titulo = models.CharField(max_length=250)
    video = models.URLField()

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name='Subir video'
        verbose_name_plural='Subir videos'

class SubirAudios(models.Model):
    audios = models.ForeignKey(Audios)
    titulo = models.CharField(max_length=250)
    audio = models.FileField()

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name='Subir audio'
        verbose_name_plural='Subir audios'

class SubirFotos(models.Model):
    fotos = models.ForeignKey(Fotos)
    titulo = models.CharField(max_length=250)
    foto = models.FileField()

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name='Subir foto'
        verbose_name_plural='Subir fotos'