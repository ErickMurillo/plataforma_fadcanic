# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields
from django.conf import settings
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fadcanic', '0002_auto_20150619_1927'),
        ('lugar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monitoreo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('resultados', ckeditor.fields.RichTextField(verbose_name=b'Resultados y/o logros de la actividad')),
                ('masculino', models.IntegerField()),
                ('femenino', models.IntegerField()),
                ('menor_12', models.IntegerField(verbose_name=b'Menor a 12 a\xc3\xb1os')),
                ('mayor_12', models.IntegerField(verbose_name=b'12 a 18 a\xc3\xb1os')),
                ('mayor_18', models.IntegerField(verbose_name=b'18 a 30 a\xc3\xb1os')),
                ('mayor_30', models.IntegerField(verbose_name=b'30 a m\xc3\xa1s a\xc3\xb1os')),
                ('creole', models.IntegerField()),
                ('miskito', models.IntegerField()),
                ('ulwa', models.IntegerField()),
                ('rama', models.IntegerField()),
                ('mestizo', models.IntegerField()),
                ('mayagna', models.IntegerField()),
                ('garifuna', models.IntegerField()),
                ('extranjero', models.IntegerField()),
                ('estudiante', models.IntegerField()),
                ('docente', models.IntegerField()),
                ('periodista', models.IntegerField(verbose_name=b'Periodista/comunicador')),
                ('lideres', models.IntegerField(verbose_name=b'L\xc3\xadderes comunitarios')),
                ('representantes', models.IntegerField(verbose_name=b'Representantes de Organizaciones')),
                ('autoridades', models.IntegerField(verbose_name=b'Autoridades comunitarias')),
                ('comunitarios', models.IntegerField(verbose_name=b'Comunitarios/Pobladores')),
                ('actividad', models.ForeignKey(to='fadcanic.TipoActividad')),
                ('comunidad', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'municipio', chained_field=b'municipio', blank=True, auto_choose=True, to='lugar.Comunidad', null=True)),
                ('eje', models.ForeignKey(to='fadcanic.EjeTransversal')),
                ('municipio', models.ForeignKey(to='lugar.Municipio')),
            ],
            options={
                'verbose_name': 'Monitoreo Actividad',
                'verbose_name_plural': 'Monitoreo Actividades',
            },
        ),
        migrations.CreateModel(
            name='Recolector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('cargo', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Datos persona que llena el registro',
                'verbose_name_plural': 'Datos persona que llena el registro',
            },
        ),
        migrations.AddField(
            model_name='monitoreo',
            name='recolector',
            field=models.ForeignKey(to='comunidad.Recolector'),
        ),
        migrations.AddField(
            model_name='monitoreo',
            name='resultado',
            field=models.ForeignKey(to='fadcanic.ResultadoPrograma'),
        ),
        migrations.AddField(
            model_name='monitoreo',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
