# -*- coding: utf-8 -*-
from django.db import models
from sorl.thumbnail import ImageField
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from cambiaahora.utils import get_file_path
from django.contrib.auth.models import User
from cambiaahora.noticias.models import CHOICE_APROBACION, CHOICE_IDIOMA

# Create your models here.

class Historias(models.Model):
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(editable=False)
    foto = ImageField('Foto principal', upload_to=get_file_path, blank=True, null=True)
    fecha = models.DateField()
    texto = RichTextField()
    aprobacion = models.IntegerField(choices=CHOICE_APROBACION, default='1')
    idioma = models.IntegerField(choices=CHOICE_IDIOMA, default='1')

    user = models.ForeignKey(User)

    fileDir = 'Historias/'

    def save(self, *args, **kwargs):
        self.slug = (slugify(self.titulo))
        super(Historias, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s' % (self.titulo)

    class Meta:
        verbose_name='Historia'
        verbose_name_plural='Historias'