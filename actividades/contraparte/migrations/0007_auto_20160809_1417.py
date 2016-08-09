# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contraparte', '0006_auto_20160128_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='tipo',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'Persona'), (2, b'Acci\xc3\xb3n comit\xc3\xa9 comunal'), (3, b'Acci\xc3\xb3n municipal de prevenci\xc3\xb3n de violencia'), (4, b'Acci\xc3\xb3n diplomado de promotor\xc3\xada'), (5, b'Acci\xc3\xb3n diplomado de comunicaci\xc3\xb3n'), (6, b'Acci\xc3\xb3n docente'), (7, b'Comit\xc3\xa9 comunal y municipal'), (8, b'Acci\xc3\xb3n masiva'), (9, b'Debate escolar')]),
        ),
    ]
