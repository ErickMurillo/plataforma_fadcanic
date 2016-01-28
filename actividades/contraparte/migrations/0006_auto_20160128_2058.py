# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import actividades.thumbs
import cambiaahora.utils


class Migration(migrations.Migration):

    dependencies = [
        ('contraparte', '0005_auto_20150918_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='foto1',
            field=actividades.thumbs.ImageWithThumbsField(null=True, upload_to=cambiaahora.utils.get_file_path, blank=True),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='foto2',
            field=actividades.thumbs.ImageWithThumbsField(null=True, upload_to=cambiaahora.utils.get_file_path, blank=True),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='foto3',
            field=actividades.thumbs.ImageWithThumbsField(null=True, upload_to=cambiaahora.utils.get_file_path, blank=True),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='tipo',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'Persona'), (2, b'Acci\xc3\xb3n comit\xc3\xa9 comunal'), (3, b'Acci\xc3\xb3n municipal de prevenci\xc3\xb3n de violencia'), (4, b'Acci\xc3\xb3n diplomado de promotor\xc3\xada'), (5, b'Acci\xc3\xb3n diplomado de comunicaci\xc3\xb3n')]),
        ),
    ]
