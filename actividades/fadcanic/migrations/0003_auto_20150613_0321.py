# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fadcanic', '0002_auto_20150527_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizacion',
            name='last_register',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 3, 21, 14, 521088), editable=False),
        ),
    ]
