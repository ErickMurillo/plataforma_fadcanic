# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multimedias', '0003_auto_20150618_2255'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subiraudios',
            options={'ordering': ('-titulo',), 'verbose_name': 'Subir audio', 'verbose_name_plural': 'Subir audios'},
        ),
    ]
