# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('violencia_juvenil', '0002_auto_20151201_1625'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='encuestador',
            options={'verbose_name': 'Encuestador', 'verbose_name_plural': 'Encuestadores'},
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='latitud',
            field=models.FloatField(null=True, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='longitud',
            field=models.FloatField(null=True, editable=False, blank=True),
        ),
    ]
