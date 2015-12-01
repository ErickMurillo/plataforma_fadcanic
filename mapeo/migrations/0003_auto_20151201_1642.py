# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapeo', '0002_auto_20151117_1648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizaciones',
            name='celular',
        ),
        migrations.RemoveField(
            model_name='organizaciones',
            name='convencional',
        ),
        migrations.AddField(
            model_name='organizaciones',
            name='celular_1',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='organizaciones',
            name='convencional_1',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
