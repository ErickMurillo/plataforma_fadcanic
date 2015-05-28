# -*- coding: utf-8 -*-
from django.db import models
from sorl.thumbnail import ImageField
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from cambiaahora.utils import get_file_path
from django.contrib.auth.models import User

# Create your models here.

class Staff(models.Model):
	titulo = models.CharField('Nombre', max_length=250)
	slug = models.SlugField(editable=False)
	foto = ImageField('Foto principal', upload_to=get_file_path, blank=True, null=True)
	fecha = models.DateField('fecha de nacimiento')
	texto = RichTextField()
	profesion = models.CharField('Profesión', max_length=250)
	cargo = models.CharField(max_length=250)
	aprobacion = models.IntegerField(choices=CHOICE_APROBACION, default='1')
    idioma = models.IntegerField(choices=CHOICE_IDIOMA, default='1')

    user = models.ForeignKey(User)

    fileDir = 'staff/'

    def save(self, *args, **kwargs):
        self.slug = (slugify(self.titulo))
        super(Staff, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s' % (self.titulo)

    class Meta:
        verbose_name='Staff'
        verbose_name_plural='Staff'
