# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import cambiaahora.utils


class Migration(migrations.Migration):

    dependencies = [
        ('mapeo', '0003_auto_20151201_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizaciones',
            name='foto',
            field=sorl.thumbnail.fields.ImageField(upload_to=cambiaahora.utils.get_file_path, null=True, verbose_name=b'Foto', blank=True),
        ),
        migrations.AlterField(
            model_name='organizaciones',
            name='celular_1',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Celular', blank=True),
        ),
        migrations.AlterField(
            model_name='organizaciones',
            name='convencional_1',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Convencional', blank=True),
        ),
        migrations.AlterField(
            model_name='organizaciones',
            name='tipo',
            field=models.IntegerField(choices=[(1, b'Comit\xc3\xa9 municipal de prevenci\xc3\xb3n de violencia'), (2, b'Comit\xc3\xa9 comunal'), (3, b'Diplomado de promotor\xc3\xada'), (4, b'Diplomado de comunicaci\xc3\xb3n')]),
        ),
    ]
