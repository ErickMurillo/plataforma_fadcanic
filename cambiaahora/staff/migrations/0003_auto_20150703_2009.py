# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_auto_20150619_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='fecha',
            field=models.DateField(null=True, verbose_name='Fecha de nacimiento', blank=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='profesion',
            field=models.CharField(max_length=250, null=True, verbose_name='Profesi\xf3n', blank=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='texto',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Texto', blank=True),
        ),
    ]
