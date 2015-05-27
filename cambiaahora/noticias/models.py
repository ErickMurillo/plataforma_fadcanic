# -*- coding: utf-8 -*-
from django.db import models
from sorl.thumbnail import ImageField
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from cambiaahora.utils import get_file_path
from django.contrib.auth.models import User

# Create your models here.
CHOICE_APROBACION = (
                        (1,'Borrador'),
                        (2, 'Aprobado'),
                    )
CHOICE_IDIOMA = (
                        (1,'Español'),
                        (2, 'Ingles'),
                    )

class Noticias(models.Model):
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(editable=False)
    fecha = models.DateField()
    foto = ImageField('Foto principal', upload_to=get_file_path, blank=True, null=True)
    url = models.URLField('url del video como portada', blank=True, null=True)
    texto = RichTextField(blank=True, null=True)
    aprobacion = models.IntegerField(choices=CHOICE_APROBACION, default='1')
    idioma = models.IntegerField(choices=CHOICE_IDIOMA, default='1')

    user = models.ForeignKey(User)

    fileDir = 'noticias/'

    def save(self, *args, **kwargs):
        self.slug = (slugify(self.titulo))
        super(Noticias, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s' % (self.titulo)

    class Meta:
        verbose_name='Noticia'
        verbose_name_plural='Noticias'
    