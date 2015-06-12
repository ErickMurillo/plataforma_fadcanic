# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion',
            name='descripcion1',
            field=models.CharField(max_length=450, null=True, verbose_name='Descripci\xf3n espa\xf1ol'),
        ),
        migrations.AddField(
            model_name='configuracion',
            name='descripcion2',
            field=models.CharField(max_length=450, null=True, verbose_name='Descripci\xf3n ingles'),
        ),
        migrations.AddField(
            model_name='configuracion',
            name='descripcion3',
            field=models.CharField(max_length=450, null=True, verbose_name='Descripci\xf3n miskitu'),
        ),
        migrations.AddField(
            model_name='configuracion',
            name='descripcion4',
            field=models.CharField(max_length=450, null=True, verbose_name='Descripci\xf3n otro'),
        ),
    ]
