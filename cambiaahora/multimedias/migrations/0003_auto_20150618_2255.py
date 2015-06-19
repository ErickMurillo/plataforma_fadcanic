# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import cambiaahora.utils
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('multimedias', '0002_auto_20150613_0321'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documentales',
            options={'verbose_name': 'Documentales', 'verbose_name_plural': 'Documentales'},
        ),
        migrations.AddField(
            model_name='audios',
            name='descripcion',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Descripci\xf3n', blank=True),
        ),
        migrations.AddField(
            model_name='audios',
            name='foto',
            field=sorl.thumbnail.fields.ImageField(upload_to=cambiaahora.utils.get_file_path, null=True, verbose_name='Foto', blank=True),
        ),
        migrations.AddField(
            model_name='documentales',
            name='foto',
            field=sorl.thumbnail.fields.ImageField(upload_to=cambiaahora.utils.get_file_path, null=True, verbose_name='Foto', blank=True),
        ),
        migrations.AddField(
            model_name='fotos',
            name='descripcion',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Descripci\xf3n', blank=True),
        ),
        migrations.AddField(
            model_name='videos',
            name='descripcion',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Descripci\xf3n', blank=True),
        ),
        migrations.AddField(
            model_name='videos',
            name='foto',
            field=sorl.thumbnail.fields.ImageField(upload_to=cambiaahora.utils.get_file_path, null=True, verbose_name='Foto', blank=True),
        ),
    ]
