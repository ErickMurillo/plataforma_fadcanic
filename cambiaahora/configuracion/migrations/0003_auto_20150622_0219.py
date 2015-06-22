# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import cambiaahora.utils
import ckeditor.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('configuracion', '0002_logoapoyan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Informacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('foto', sorl.thumbnail.fields.ImageField(upload_to=cambiaahora.utils.get_file_path, null=True, verbose_name='Foto principal', blank=True)),
                ('objetivos', ckeditor.fields.RichTextField()),
                ('territorios', ckeditor.fields.RichTextField()),
                ('acciones', ckeditor.fields.RichTextField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Informaci\xf3n de la campa\xf1a',
                'verbose_name_plural': 'Informaci\xf3n de la campa\xf1a',
            },
        ),
        migrations.AlterField(
            model_name='logoapoyan',
            name='nombre',
            field=models.CharField(max_length=250, verbose_name='siglas organismo'),
        ),
    ]
