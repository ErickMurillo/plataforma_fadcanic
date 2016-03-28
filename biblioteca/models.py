# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User
from cambiaahora.utils import *
from embed_video.fields import EmbedVideoField


# Create your models here.
class Temas(models.Model):
    """(Temas description)"""
    titulo = models.CharField(max_length=350)

    def __unicode__(self):
        return self.titulo



class Biblioteca(models.Model):
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, editable=False)
    tema = models.ForeignKey(Temas, blank=True, null=True)
    autor = models.CharField('Autores', max_length=250, null=True, blank=True)
    anio = models.CharField('Año', max_length=50, null=True, blank=True)
    descripcion = RichTextField('Descripción', null=True, blank=True)
    fecha = models.DateField(auto_now=True)
    portada = ImageField(upload_to=get_file_path, null=True, blank=True)
    palabras_claves = models.CharField(max_length=250, null=True, blank=True,
                                       help_text='Por favor separar las palabras claves con coma \
                                       ejemplo(\'violencia,programa\') ')

    user = models.ForeignKey(User)

    fileDir = 'BibliotecaPortadas/'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.titulo)
        return super(Biblioteca, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Biblioteca'
        verbose_name_plural = 'Bibliotecas'


class Documentales(models.Model):
    biblioteca = models.ForeignKey(Biblioteca)
    titulo = models.CharField(max_length=250)
    documental = EmbedVideoField(help_text="Agregar videos de Youtube y Vimeo")

    def __unicode__(self):
        return self.documental

    class Meta:
        verbose_name = "Documental"
        verbose_name_plural = "Documentales"


class Audios(models.Model):
    biblioteca = models.ForeignKey(Biblioteca)
    titulo = models.CharField(max_length=250)
    audio = models.FileField(upload_to=get_file_path)

    fileDir = 'BibliotecaAudios/'

    def __unicode__(self):
        return self.documental

    class Meta:
        verbose_name = "Audio"
        verbose_name_plural = "Audios"


class Adjuntos(models.Model):
    biblioteca = models.ForeignKey(Biblioteca)
    archivo = models.FileField(upload_to=get_file_path)

    fileDir = 'BibliotecaAdjuntos/'

    fileDir = 'BibliotecaArchivos/'

    class Meta:
        verbose_name = "PDF Adjunto"
        verbose_name_plural = "PDF Adjuntos"
