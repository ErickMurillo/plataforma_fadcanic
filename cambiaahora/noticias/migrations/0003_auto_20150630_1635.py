# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0002_auto_20150619_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='slug',
            field=models.SlugField(max_length=450, editable=False),
        ),
    ]
