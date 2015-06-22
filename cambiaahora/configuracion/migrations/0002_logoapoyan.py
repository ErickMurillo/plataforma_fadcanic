# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
from django.conf import settings
import cambiaahora.utils


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('configuracion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogoApoyan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250, verbose_name='siglas organizmo')),
                ('foto', sorl.thumbnail.fields.ImageField(upload_to=cambiaahora.utils.get_file_path, null=True, verbose_name='Foto', blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Logo apoyan',
                'verbose_name_plural': 'Logo apoyan',
            },
        ),
    ]
