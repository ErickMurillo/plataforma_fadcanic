# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0004_informacion_idioma'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logoapoyan',
            options={'ordering': ['-id'], 'verbose_name': 'Logo apoyan', 'verbose_name_plural': 'Logo apoyan'},
        ),
        migrations.AlterField(
            model_name='informacion',
            name='acciones',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='informacion',
            name='objetivos',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='informacion',
            name='territorios',
            field=models.TextField(),
        ),
    ]
