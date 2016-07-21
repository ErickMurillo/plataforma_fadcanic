# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0004_adjuntos_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='adjuntos',
            name='portada',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=b'BibliotecaPortada/', blank=True),
        ),
    ]
