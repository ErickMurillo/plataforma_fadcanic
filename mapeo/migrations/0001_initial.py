# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lugar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acciones_Apoyo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Acci\xf3n de apoyo directo a la Campa\xf1a',
                'verbose_name_plural': 'Acciones de apoyo directo a la Campa\xf1a',
            },
        ),
        migrations.CreateModel(
            name='Acciones_Consumo_Drogas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Acci\xf3n en prevenci\xf3n de consumo de drogas',
                'verbose_name_plural': 'Acciones en prevenci\xf3n de consumo de drogas',
            },
        ),
        migrations.CreateModel(
            name='Acciones_Violencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Acci\xf3n en prevenci\xf3n de violencia',
                'verbose_name_plural': 'Acciones en prevenci\xf3n de violencia',
            },
        ),
        migrations.CreateModel(
            name='Organizaciones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.IntegerField(choices=[(1, b'Organizaci\xc3\xb3n que apoya y participa con la Campa\xc3\xb1a'), (2, b'Comit\xc3\xa9 comunal')])),
                ('nombre', models.CharField(max_length=200)),
                ('persona_contacto', models.CharField(max_length=200, null=True, verbose_name=b'Persona de contacto (Opcional)', blank=True)),
                ('direccion', models.CharField(max_length=400, null=True, blank=True)),
                ('convencional', models.IntegerField(null=True, blank=True)),
                ('celular', models.IntegerField(null=True, blank=True)),
                ('correo', models.EmailField(max_length=254, null=True, blank=True)),
                ('web', models.URLField(null=True, blank=True)),
                ('facebook', models.URLField(null=True, blank=True)),
                ('twitter', models.URLField(null=True, blank=True)),
                ('youtube', models.URLField(null=True, blank=True)),
                ('otro', models.URLField(null=True, blank=True)),
                ('masculino', models.IntegerField(null=True, verbose_name=b'Cantidad de integrantes masculinos', blank=True)),
                ('femenino', models.IntegerField(null=True, verbose_name=b'Cantidad de integrantes femeninos', blank=True)),
                ('integrantes', ckeditor.fields.RichTextField(null=True, verbose_name=b'Nombre de los integrantes', blank=True)),
                ('mayor_13', models.IntegerField(null=True, verbose_name=b'Edades de integrantes de 13 a 18 a\xc3\xb1os', blank=True)),
                ('mayor_19', models.IntegerField(null=True, verbose_name=b'Edades de integrantes de 19 a 30 a\xc3\xb1os', blank=True)),
                ('mayor_30', models.IntegerField(null=True, verbose_name=b'Edades de integrantes de 31 a m\xc3\xa1s a\xc3\xb1os', blank=True)),
                ('acciones_apoyo', models.ManyToManyField(to='mapeo.Acciones_Apoyo', blank=True)),
                ('acciones_consumo_drogas', models.ManyToManyField(to='mapeo.Acciones_Consumo_Drogas', blank=True)),
                ('acciones_violencia', models.ManyToManyField(to='mapeo.Acciones_Violencia', blank=True)),
                ('cobertura', models.ManyToManyField(related_name='Cobertura', to='lugar.Municipio', blank=True)),
                ('comunidad', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'municipio', chained_field=b'municipio', blank=True, auto_choose=True, to='lugar.Comunidad', null=True)),
                ('departamento', models.ForeignKey(to='lugar.Departamento')),
                ('municipio', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'departamento', chained_field=b'departamento', auto_choose=True, to='lugar.Municipio')),
            ],
            options={
                'verbose_name': 'Organizaci\xf3n',
                'verbose_name_plural': 'Organizaciones',
            },
        ),
    ]
