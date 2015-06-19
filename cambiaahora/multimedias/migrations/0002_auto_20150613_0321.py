# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('multimedias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subirfotos',
            name='foto',
            field=sorl.thumbnail.fields.ImageField(upload_to=b'', verbose_name='Foto'),
        ),
    ]
