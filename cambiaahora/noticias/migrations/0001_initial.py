# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import cambiaahora.utils
import ckeditor.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=250, verbose_name='Titulo')),
                ('slug', models.SlugField(editable=False)),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('foto', sorl.thumbnail.fields.ImageField(upload_to=cambiaahora.utils.get_file_path, null=True, verbose_name='Foto principal', blank=True)),
                ('url', models.URLField(null=True, verbose_name='url del video como portada', blank=True)),
                ('texto', ckeditor.fields.RichTextField(null=True, verbose_name='Texto', blank=True)),
                ('aprobacion', models.IntegerField(default=b'1', verbose_name='Aprobaci\xf3n', choices=[(1, 'Borrador'), (2, 'Aprobado')])),
                ('idioma', models.IntegerField(default=b'1', verbose_name='Idioma', choices=[(1, 'Espa\xf1ol'), (2, 'English')])),
                ('categoria', models.ForeignKey(verbose_name='Categoria', to='noticias.Categoria')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
            },
        ),
    ]
