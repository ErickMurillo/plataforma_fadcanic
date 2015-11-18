# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapeo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizaciones',
            name='slug',
            field=models.SlugField(default=1, max_length=450, editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='organizaciones',
            name='tipo',
            field=models.IntegerField(choices=[(1, b'Organizaci\xc3\xb3n que apoya y participa con la Campa\xc3\xb1a'), (2, b'Comit\xc3\xa9 comunal'), (3, b'Diplomado de promotor\xc3\xada'), (4, b'Diplomado de comunicaci\xc3\xb3n')]),
        ),
    ]
