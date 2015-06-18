# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fadcanic', '0003_auto_20150613_0321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizacion',
            name='last_register',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 18, 22, 55, 28, 927201), editable=False),
        ),
    ]
