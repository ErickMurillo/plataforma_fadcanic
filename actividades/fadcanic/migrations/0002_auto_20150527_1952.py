# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fadcanic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizacion',
            name='last_register',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 27, 19, 52, 11, 797655), editable=False),
        ),
    ]
