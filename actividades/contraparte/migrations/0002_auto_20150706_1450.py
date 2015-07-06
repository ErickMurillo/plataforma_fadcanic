# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contraparte', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actividad',
            name='adultos',
        ),
        migrations.RemoveField(
            model_name='actividad',
            name='estudiantes',
        ),
        migrations.RemoveField(
            model_name='actividad',
            name='jovenes',
        ),
        migrations.RemoveField(
            model_name='actividad',
            name='maestros',
        ),
        migrations.RemoveField(
            model_name='actividad',
            name='miembros',
        ),
        migrations.RemoveField(
            model_name='actividad',
            name='ninos',
        ),
        migrations.RemoveField(
            model_name='actividad',
            name='pobladores',
        ),
        migrations.RemoveField(
            model_name='actividad',
            name='tecnicos',
        ),
        migrations.AddField(
            model_name='actividad',
            name='comunitarios',
            field=models.IntegerField(default=b'0', verbose_name=b'Comunitarios/Pobladores'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='creole',
            field=models.IntegerField(default=b'0'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='docente',
            field=models.IntegerField(default=b'0'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='estudiante',
            field=models.IntegerField(default=b'0'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='extranjero',
            field=models.IntegerField(default=b'0'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='garifuna',
            field=models.IntegerField(default=b'0'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='mayagna',
            field=models.IntegerField(default=b'0'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='mayor_12',
            field=models.IntegerField(default=b'0', verbose_name=b'13 a 18 a\xc3\xb1os'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='mayor_18',
            field=models.IntegerField(default=b'0', verbose_name=b'19 a 30 a\xc3\xb1os'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='mayor_30',
            field=models.IntegerField(default=b'0', verbose_name=b'31 a m\xc3\xa1s a\xc3\xb1os'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='menor_12',
            field=models.IntegerField(default=b'0', verbose_name=b'Menor a 12 a\xc3\xb1os'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='mestizo',
            field=models.IntegerField(default=b'0'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='miskito',
            field=models.IntegerField(default=b'0'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='no_dato2',
            field=models.BooleanField(default=1, verbose_name=b'No hay datos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actividad',
            name='periodista',
            field=models.IntegerField(default=b'0', verbose_name=b'Periodista/comunicador'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='rama',
            field=models.IntegerField(default=b'0'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='representantes',
            field=models.IntegerField(default=b'0', verbose_name=b'Representantes de Organizaciones'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='ulwa',
            field=models.IntegerField(default=b'0'),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='autoridades',
            field=models.IntegerField(default=b'0', verbose_name=b'Autoridades comunitarias'),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='lideres',
            field=models.IntegerField(default=b'0', verbose_name=b'L\xc3\xadderes comunitarios'),
        ),
    ]
