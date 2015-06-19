# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
from django.conf import settings
import cambiaahora.utils
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Historias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=250, verbose_name='Titulo')),
                ('slug', models.SlugField(editable=False)),
                ('foto', sorl.thumbnail.fields.ImageField(upload_to=cambiaahora.utils.get_file_path, null=True, verbose_name='Foto principal', blank=True)),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('texto', ckeditor.fields.RichTextField(verbose_name='Texto')),
                ('aprobacion', models.IntegerField(default=b'1', verbose_name='Aprobaci\xf3n', choices=[(1, 'Borrador'), (2, 'Aprobado')])),
                ('idioma', models.IntegerField(default=b'1', verbose_name='Idioma', choices=[(1, 'Espa\xf1ol'), (2, 'English')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Historia',
                'verbose_name_plural': 'Historias',
            },
        ),
    ]
