# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('lugar', '0001_initial'),
        ('contraparte', '0003_auto_20150820_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Precedencia_Participantes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('conteo', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Procedencia de los participantes',
            },
        ),
        migrations.AlterField(
            model_name='actividad',
            name='aprendizaje',
            field=models.IntegerField(blank=True, null=True, verbose_name='Grado de aprendizaje', choices=[(99, 'No aplica'), (1, 'Muy bueno (90-100%)'), (2, 'Bueno (60-80%)'), (3, 'Regular (50%)'), (4, 'Malo (menor al 30%)')]),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='aprendizaje_m',
            field=models.IntegerField(blank=True, null=True, verbose_name='Grado de aprendizaje', choices=[(99, 'No aplica'), (1, 'Muy bueno (90-100%)'), (2, 'Bueno (60-80%)'), (3, 'Regular (50%)'), (4, 'Malo (menor al 30%)')]),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='efectividad',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Efectividad de la acci\xc3\xb3n', choices=[(99, 'No aplica'), (1, 'Muy bueno (90-100%)'), (2, 'Bueno (60-80%)'), (3, 'Regular (50%)'), (4, 'Malo (menor al 30%)')]),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='efectividad_m',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Efectividad de la acci\xc3\xb3n', choices=[(99, 'No aplica'), (1, 'Muy bueno (90-100%)'), (2, 'Bueno (60-80%)'), (3, 'Regular (50%)'), (4, 'Malo (menor al 30%)')]),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='empoderamiento',
            field=models.IntegerField(blank=True, null=True, verbose_name='Nivel de apropiaci\xf3n', choices=[(99, 'No aplica'), (1, 'Muy bueno (90-100%)'), (2, 'Bueno (60-80%)'), (3, 'Regular (50%)'), (4, 'Malo (menor al 30%)')]),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='empoderamiento_m',
            field=models.IntegerField(blank=True, null=True, verbose_name='Nivel de apropiaci\xf3n', choices=[(99, 'No aplica'), (1, 'Muy bueno (90-100%)'), (2, 'Bueno (60-80%)'), (3, 'Regular (50%)'), (4, 'Malo (menor al 30%)')]),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='objetivo_actividad',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='participacion',
            field=models.IntegerField(blank=True, null=True, verbose_name='Nivel de participaci\xf3n', choices=[(99, 'No aplica'), (1, 'Muy bueno (90-100%)'), (2, 'Bueno (60-80%)'), (3, 'Regular (50%)'), (4, 'Malo (menor al 30%)')]),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='participacion_m',
            field=models.IntegerField(blank=True, null=True, verbose_name='Nivel de participaci\xf3n', choices=[(99, 'No aplica'), (1, 'Muy bueno (90-100%)'), (2, 'Bueno (60-80%)'), (3, 'Regular (50%)'), (4, 'Malo (menor al 30%)')]),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='relevancia',
            field=models.IntegerField(blank=True, null=True, verbose_name='Importancia del tema/acci\xf3n', choices=[(99, 'No aplica'), (1, 'Muy bueno (90-100%)'), (2, 'Bueno (60-80%)'), (3, 'Regular (50%)'), (4, 'Malo (menor al 30%)')]),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='relevancia_m',
            field=models.IntegerField(blank=True, null=True, verbose_name='Importancia del tema/acci\xf3n', choices=[(99, 'No aplica'), (1, 'Muy bueno (90-100%)'), (2, 'Bueno (60-80%)'), (3, 'Regular (50%)'), (4, 'Malo (menor al 30%)')]),
        ),
        migrations.AddField(
            model_name='precedencia_participantes',
            name='actividad',
            field=models.ForeignKey(to='contraparte.Actividad'),
        ),
        migrations.AddField(
            model_name='precedencia_participantes',
            name='comunidad',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'municipio', chained_field=b'municipio', auto_choose=True, to='lugar.Comunidad'),
        ),
        migrations.AddField(
            model_name='precedencia_participantes',
            name='municipio',
            field=models.ForeignKey(to='lugar.Municipio'),
        ),
    ]
