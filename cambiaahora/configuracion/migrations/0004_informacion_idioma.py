# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0003_auto_20150622_0219'),
    ]

    operations = [
        migrations.AddField(
            model_name='informacion',
            name='idioma',
            field=models.IntegerField(default=b'1', verbose_name='Idioma', choices=[(1, 'Espa\xf1ol'), (2, 'English')]),
        ),
    ]
