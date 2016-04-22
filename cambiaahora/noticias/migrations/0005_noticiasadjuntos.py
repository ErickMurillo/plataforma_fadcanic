# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cambiaahora.utils


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0004_noticiasaudios'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoticiasAdjuntos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=250, verbose_name='Titulo')),
                ('archivo', models.FileField(upload_to=cambiaahora.utils.get_file_path)),
                ('adjuntos', models.ForeignKey(to='noticias.Noticias')),
            ],
            options={
                'ordering': ('-titulo',),
                'verbose_name': 'Subir adjuntos',
                'verbose_name_plural': 'Subir adjuntos',
            },
        ),
    ]
