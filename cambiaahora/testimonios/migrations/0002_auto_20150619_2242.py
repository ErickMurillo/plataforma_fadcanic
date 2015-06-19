# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimonios', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testimonios',
            options={'verbose_name': 'Opiniones', 'verbose_name_plural': 'Opiniones'},
        ),
    ]
