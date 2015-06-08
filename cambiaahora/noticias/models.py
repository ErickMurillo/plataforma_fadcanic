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
                        (1, _('Borrador')),
                        (2, _('Aprobado')),
                    )
CHOICE_IDIOMA = (
                        (1, _('Español')),
                        (2, _('Ingles')),
                    )

class Noticias(models.Model):
    titulo = models.CharField(_('Titulo'),max_length=250)
    slug = models.SlugField(editable=False)
    fecha = models.DateField(_('Fecha'))
    foto = ImageField(_('Foto principal'), upload_to=get_file_path, blank=True, null=True)
    url = models.URLField(_('url del video como portada'), blank=True, null=True)
    texto = RichTextField(_('Texto'),blank=True, null=True)
    aprobacion = models.IntegerField(choices=CHOICE_APROBACION, default='1', verbose_name=_('Aprobación'))
    idioma = models.IntegerField(choices=CHOICE_IDIOMA, default='1',verbose_name=_('Idioma'))

    user = models.ForeignKey(User)

    fileDir = 'noticias/'

    def save(self, *args, **kwargs):
        self.slug = (slugify(self.titulo))
        super(Noticias, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s' % (self.titulo)

    class Meta:
        verbose_name= _('Noticia')
        verbose_name_plural= _('Noticias')