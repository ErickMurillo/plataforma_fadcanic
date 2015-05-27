# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticias',
            name='aprobacion',
            field=models.IntegerField(default=b'1', choices=[(1, b'Borrador'), (2, b'Aprobado')]),
        ),
        migrations.AddField(
            model_name='noticias',
            name='idioma',
            field=models.IntegerField(default=b'1', choices=[(1, b'Espa\xc3\xb1ol'), (2, b'Ingles')]),
        ),
    ]
