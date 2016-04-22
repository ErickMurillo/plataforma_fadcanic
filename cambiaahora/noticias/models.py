# -*- coding: utf-8 -*-
from django.db import models
from sorl.thumbnail import ImageField
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from cambiaahora.utils import get_file_path
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.
CHOICE_APROBACION = (
                        (1, _(u'Borrador')),
                        (2, _(u'Aprobado')),
                    )
CHOICE_IDIOMA = (
                        (1, _(u'Español')),
                        (2, _(u'English')),
                    )
class Categoria(models.Model):
    nombre = models.CharField(max_length=250)

    def __unicode__(self):
        return self.nombre

class Noticias(models.Model):
    titulo = models.CharField(_(u'Titulo'),max_length=450)
    slug = models.SlugField(editable=False, max_length=450)
    fecha = models.DateField(_(u'Fecha'))
    foto = ImageField(_(u'Foto principal'), upload_to=get_file_path, blank=True, null=True)
    url = models.URLField(_(u'url del video como portada'), blank=True, null=True)
    texto = RichTextField(_(u'Texto'),blank=True, null=True)
    aprobacion = models.IntegerField(choices=CHOICE_APROBACION, default='1', verbose_name=_(u'Aprobación'))
    idioma = models.IntegerField(choices=CHOICE_IDIOMA, default='1',verbose_name=_(u'Idioma'))
    categoria = models.ForeignKey(Categoria, verbose_name=_(u'Categoria'))

    user = models.ForeignKey(User)

    fileDir = 'noticias/'

    def save(self, *args, **kwargs):
        self.slug = (slugify(self.titulo))
        super(Noticias, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s' % (self.titulo)

    class Meta:
        verbose_name= _(u'Noticia')
        verbose_name_plural= _(u'Noticias')

class NoticiasAudios(models.Model):
    audios = models.ForeignKey(Noticias)
    titulo = models.CharField(_(u'Titulo'),max_length=250)
    audio = models.FileField(_(u'Audio'),)

    fileDir = 'subirNoticiasAudios/'

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name=_(u'Subir audio')
        verbose_name_plural=_(u'Subir audios')
        ordering = ('-titulo', )

class NoticiasAdjuntos(models.Model):
    adjuntos = models.ForeignKey(Noticias)
    titulo = models.CharField(_(u'Titulo'),max_length=250)
    archivo = models.FileField(upload_to=get_file_path)

    fileDir = 'subirNoticiasAdjuntos/'

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name=_(u'Subir adjuntos')
        verbose_name_plural=_(u'Subir adjuntos')
        ordering = ('-titulo', )
