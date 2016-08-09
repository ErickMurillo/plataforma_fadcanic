# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapeo', '0005_auto_20160225_1600'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='info_organizaciones',
            options={'verbose_name': 'Organizaci\xf3n', 'verbose_name_plural': 'Organizaciones'},
        ),
        migrations.AlterField(
            model_name='organizaciones',
            name='tipo',
            field=models.IntegerField(choices=[(1, b'Comit\xc3\xa9 municipal de prevenci\xc3\xb3n de violencia'), (2, b'Comit\xc3\xa9 comunal'), (3, b'Diplomado de promotor\xc3\xada'), (4, b'Diplomado de comunicaci\xc3\xb3n'), (5, b'Acci\xc3\xb3n docente'), (6, b'Comit\xc3\xa9 comunal y municipal'), (7, b'Acci\xc3\xb3n masiva'), (8, b'Debate escolar')]),
        ),
    ]
