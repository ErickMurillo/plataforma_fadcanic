# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contraparte', '0002_auto_20150706_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='aprobacion',
            field=models.IntegerField(default=b'1', verbose_name=b'Aprobaci\xc3\xb3n', choices=[(1, b'Borrador'), (2, b'Aprobado')]),
        ),
        migrations.AddField(
            model_name='actividad',
            name='dificultades',
            field=models.TextField(default=b'', verbose_name=b'Dificultades', blank=True),
        ),
        migrations.AddField(
            model_name='actividad',
            name='logros',
            field=models.TextField(default=b'', verbose_name=b'Logros', blank=True),
        ),
        migrations.AddField(
            model_name='actividad',
            name='objetivo_actividad',
            field=models.CharField(max_length=400, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='actividad',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='actividad',
            name='acuerdos',
            field=models.TextField(default=b'', verbose_name=b'Acuerdos', blank=True),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='aprendizaje',
            field=models.IntegerField(blank=True, null=True, verbose_name='Grado de aprendizaje', choices=[(99, 'No aplica'), (1, 'Muy bueno'), (2, 'Bueno'), (3, 'Regular'), (4, 'Malo'), (5, 'Muy malo')]),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='aprendizaje_m',
            field=models.IntegerField(blank=True, null=True, verbose_name='Grado de aprendizaje', choices=[(99, 'No aplica'), (1, 'Muy bueno'), (2, 'Bueno'), (3, 'Regular'), (4, 'Malo'), (5, 'Muy malo')]),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='comentarios',
            field=models.TextField(default=b'', verbose_name=b'Descripci\xc3\xb3n de la Actividad', blank=True),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='efectividad',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Efectividad de la acci\xc3\xb3n', choices=[(99, 'No aplica'), (1, 'Muy bueno'), (2, 'Bueno'), (3, 'Regular'), (4, 'Malo'), (5, 'Muy malo')]),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='efectividad_m',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Efectividad de la acci\xc3\xb3n', choices=[(99, 'No aplica'), (1, 'Muy bueno'), (2, 'Bueno'), (3, 'Regular'), (4, 'Malo'), (5, 'Muy malo')]),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='empoderamiento',
            field=models.IntegerField(blank=True, null=True, verbose_name='Nivel de apropiaci\xf3n', choices=[(99, 'No aplica'), (1, 'Muy bueno'), (2, 'Bueno'), (3, 'Regular'), (4, 'Malo'), (5, 'Muy malo')]),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='empoderamiento_m',
            field=models.IntegerField(blank=True, null=True, verbose_name='Nivel de apropiaci\xf3n', choices=[(99, 'No aplica'), (1, 'Muy bueno'), (2, 'Bueno'), (3, 'Regular'), (4, 'Malo'), (5, 'Muy malo')]),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='participacion',
            field=models.IntegerField(blank=True, null=True, verbose_name='Nivel de participaci\xf3n', choices=[(99, 'No aplica'), (1, 'Muy bueno'), (2, 'Bueno'), (3, 'Regular'), (4, 'Malo'), (5, 'Muy malo')]),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='participacion_m',
            field=models.IntegerField(blank=True, null=True, verbose_name='Nivel de participaci\xf3n', choices=[(99, 'No aplica'), (1, 'Muy bueno'), (2, 'Bueno'), (3, 'Regular'), (4, 'Malo'), (5, 'Muy malo')]),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='relevancia',
            field=models.IntegerField(blank=True, null=True, verbose_name='Importancia del tema/acci\xf3n', choices=[(99, 'No aplica'), (1, 'Muy bueno'), (2, 'Bueno'), (3, 'Regular'), (4, 'Malo'), (5, 'Muy malo')]),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='relevancia_m',
            field=models.IntegerField(blank=True, null=True, verbose_name='Importancia del tema/acci\xf3n', choices=[(99, 'No aplica'), (1, 'Muy bueno'), (2, 'Bueno'), (3, 'Regular'), (4, 'Malo'), (5, 'Muy malo')]),
        ),
    ]
