# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0003_auto_20150630_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoticiasAudios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=250, verbose_name='Titulo')),
                ('audio', models.FileField(upload_to=b'', verbose_name='Audio')),
                ('audios', models.ForeignKey(to='noticias.Noticias')),
            ],
            options={
                'ordering': ('-titulo',),
                'verbose_name': 'Subir audio',
                'verbose_name_plural': 'Subir audios',
            },
        ),
    ]
