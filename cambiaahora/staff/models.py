# -*- coding: utf-8 -*-
from django.db import models
from sorl.thumbnail import ImageField
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from cambiaahora.utils import get_file_path
from django.contrib.auth.models import User
from cambiaahora.noticias.models import CHOICE_APROBACION, CHOICE_IDIOMA
from django.utils.translation import ugettext as _
from datetime import date
# Create your models here.

class Staff(models.Model):
    titulo = models.CharField(_(u'Nombre'), max_length=250)
    slug = models.SlugField(editable=False)
    foto = ImageField(_(u'Foto principal'), upload_to=get_file_path, blank=True, null=True)
    fecha = models.DateField(_(u'Fecha de nacimiento'), blank=True, null=True)
    texto = RichTextField(_(u'Texto'), blank=True, null=True)
    profesion = models.CharField(_(u'Profesión'), max_length=250, blank=True, null=True)
    cargo = models.CharField(_(u'Cargo/Puesto'),max_length=250)
    aprobacion = models.IntegerField(choices=CHOICE_APROBACION, default='1', verbose_name=_(u'Aprobación'))
    idioma = models.IntegerField(choices=CHOICE_IDIOMA, default='1', verbose_name=_(u'Idioma'))

    user = models.ForeignKey(User)

    fileDir = 'staff/'

    def save(self, *args, **kwargs):
        self.slug = (slugify(self.titulo))
        super(Staff, self).save(*args, **kwargs)



    def calculate_age(self):
        days_in_year = 365.2425
        age = int((date.today() - self.fecha).days / days_in_year)  
        return age

        def __unicode__(self):
            return u'%s' % (self.titulo)

    class Meta:
        verbose_name=_(u'Staff')
        verbose_name_plural=_(u'Staff')
