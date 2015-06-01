# -*- coding: utf-8 -*-
from django.db import models
from sorl.thumbnail import ImageField
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from cambiaahora.utils import get_file_path
from django.contrib.auth.models import User
from cambiaahora.noticias.models import CHOICE_APROBACION, CHOICE_IDIOMA
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Historias(models.Model):
    titulo = models.CharField(_('Titulo'), max_length=250)
    slug = models.SlugField(editable=False)
    foto = ImageField(_('Foto principal'), upload_to=get_file_path, blank=True, null=True)
    fecha = models.DateField(_('Fecha'))
    texto = RichTextField(_('Texto'))
    aprobacion = models.IntegerField(choices=CHOICE_APROBACION, default='1', verbose_name=_('Aprobación'))
    idioma = models.IntegerField(choices=CHOICE_IDIOMA, default='1', verbose_name=_('Idioma'))

    user = models.ForeignKey(User)

    fileDir = 'Historias/'

    def save(self, *args, **kwargs):
        self.slug = (slugify(self.titulo))
        super(Historias, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s' % (self.titulo)

    class Meta:
        verbose_name= _('Historia')
        verbose_name_plural= _('Historias')