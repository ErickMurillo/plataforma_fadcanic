# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
from django.conf import settings
import cambiaahora.utils
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=250, verbose_name=b'Nombre')),
                ('slug', models.SlugField(editable=False)),
                ('foto', sorl.thumbnail.fields.ImageField(upload_to=cambiaahora.utils.get_file_path, null=True, verbose_name=b'Foto principal', blank=True)),
                ('fecha', models.DateField(verbose_name=b'fecha de nacimiento')),
                ('texto', ckeditor.fields.RichTextField()),
                ('profesion', models.CharField(max_length=250, verbose_name=b'Profesi\xc3\xb3n')),
                ('cargo', models.CharField(max_length=250)),
                ('aprobacion', models.IntegerField(default=b'1', choices=[(1, b'Borrador'), (2, b'Aprobado')])),
                ('idioma', models.IntegerField(default=b'1', choices=[(1, b'Espa\xc3\xb1ol'), (2, b'Ingles')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Staff',
                'verbose_name_plural': 'Staff',
            },
        ),
    ]
