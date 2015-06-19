# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='titulo',
            field=models.CharField(max_length=450, verbose_name='Titulo'),
        ),
    ]
