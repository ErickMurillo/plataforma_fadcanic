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
            name='Testimonios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=250, verbose_name=b'Nombre')),
                ('slug', models.SlugField(editable=False)),
                ('foto', sorl.thumbnail.fields.ImageField(upload_to=cambiaahora.utils.get_file_path, null=True, verbose_name=b'Foto principal', blank=True)),
                ('fecha', models.DateField()),
                ('texto', ckeditor.fields.RichTextField()),
                ('aprobacion', models.IntegerField(default=b'1', choices=[(1, b'Borrador'), (2, b'Aprobado')])),
                ('idioma', models.IntegerField(default=b'1', choices=[(1, b'Espa\xc3\xb1ol'), (2, b'Ingles')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Testimonio',
                'verbose_name_plural': 'Testimonios',
            },
        ),
    ]
