# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0003_auto_20160422_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='adjuntos',
            name='titulo',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
    ]
