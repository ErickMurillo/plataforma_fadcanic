# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
from django.conf import settings
import cambiaahora.utils


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('foto', sorl.thumbnail.fields.ImageField(upload_to=cambiaahora.utils.get_file_path, null=True, verbose_name='Foto', blank=True)),
                ('titulo1', models.CharField(max_length=250, verbose_name='Titulo espa\xf1ol')),
                ('titulo2', models.CharField(max_length=250, verbose_name='Titulo ingles')),
                ('titulo3', models.CharField(max_length=250, verbose_name='Titulo miskitu')),
                ('titulo4', models.CharField(max_length=250, verbose_name='Titulo otro')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Configuraci\xf3n',
                'verbose_name_plural': 'Configuraciones',
            },
        ),
    ]
