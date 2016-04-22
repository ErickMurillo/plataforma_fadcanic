# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_auto_20160328_2122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='temas',
            options={'verbose_name_plural': 'Temas'},
        ),
        migrations.AddField(
            model_name='biblioteca',
            name='tipo_documento',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'Documento para biblioteca'), (2, b'Informe privado')]),
        ),
        migrations.AlterField(
            model_name='biblioteca',
            name='descripcion',
            field=ckeditor.fields.RichTextField(null=True, verbose_name=b'Sinopsis', blank=True),
        ),
    ]
