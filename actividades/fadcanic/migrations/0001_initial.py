# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import datetime
from django.conf import settings
import actividades.utils


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EjeTransversal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Ejes transversales',
            },
        ),
        migrations.CreateModel(
            name='Organizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250)),
                ('nombre_corto', models.CharField(help_text=b'Pueden ser siglas', max_length=15)),
                ('contacto', models.CharField(max_length=200, verbose_name=b'Persona de contacto')),
                ('telefono', models.CharField(default=b'', max_length=12, blank=True)),
                ('direccion', models.CharField(default=b'', max_length=300, blank=True)),
                ('web', models.URLField(default=b'www.example.com', verbose_name=b'Sitio web', blank=True)),
                ('historia', models.TextField(default=b'', blank=True)),
                ('logo', sorl.thumbnail.fields.ImageField(null=True, upload_to=actividades.utils.get_file_path, blank=True)),
                ('last_register', models.DateTimeField(default=datetime.datetime(2015, 6, 12, 20, 35, 41, 745250), editable=False)),
                ('admin', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Organizaciones',
                'permissions': (('view_programa', 'Puede ver salidas por programa'),),
            },
        ),
        migrations.CreateModel(
            name='ResultadoPrograma',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_corto', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'Resultado de programa',
                'verbose_name_plural': 'Resultados de programa',
            },
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Tema de actividad',
                'verbose_name_plural': 'Temas de actividad',
            },
        ),
        migrations.CreateModel(
            name='TipoActividad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Tipo de actividad',
                'verbose_name_plural': 'Tipos de actividad',
            },
        ),
    ]
