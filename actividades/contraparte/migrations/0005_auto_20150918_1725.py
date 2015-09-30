# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapeo', '0001_initial'),
        ('contraparte', '0004_auto_20150826_1711'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='precedencia_participantes',
            options={'verbose_name': 'Procedencia de los participantes', 'verbose_name_plural': 'Procedencia de los participantes'},
        ),
        migrations.AddField(
            model_name='actividad',
            name='comite',
            field=models.ForeignKey(verbose_name=b'Comit\xc3\xa9 comunal que organiza la actividad', blank=True, to='mapeo.Organizaciones', null=True),
        ),
        migrations.AddField(
            model_name='actividad',
            name='tipo',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'Persona'), (2, b'Comit\xc3\xa9 comunal')]),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='persona_organiza',
            field=models.ForeignKey(verbose_name='Persona que organiza la actividad', blank=True, to='contraparte.Organizador', null=True),
        ),
    ]
