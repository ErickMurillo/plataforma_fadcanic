# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import embed_video.fields
import cambiaahora.utils
import ckeditor.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Adjuntos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('archivo', models.FileField(upload_to=cambiaahora.utils.get_file_path)),
            ],
            options={
                'verbose_name': 'PDF Adjunto',
                'verbose_name_plural': 'PDF Adjuntos',
            },
        ),
        migrations.CreateModel(
            name='Audios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=250)),
                ('audio', models.FileField(upload_to=cambiaahora.utils.get_file_path)),
            ],
            options={
                'verbose_name': 'Audio',
                'verbose_name_plural': 'Audios',
            },
        ),
        migrations.CreateModel(
            name='Biblioteca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, editable=False)),
                ('autor', models.CharField(max_length=250, null=True, verbose_name=b'Autores', blank=True)),
                ('anio', models.CharField(max_length=50, null=True, verbose_name=b'A\xc3\xb1o', blank=True)),
                ('descripcion', ckeditor.fields.RichTextField(null=True, verbose_name=b'Descripci\xc3\xb3n', blank=True)),
                ('fecha', models.DateField(auto_now=True)),
                ('portada', sorl.thumbnail.fields.ImageField(null=True, upload_to=cambiaahora.utils.get_file_path, blank=True)),
                ('palabras_claves', models.CharField(help_text=b"Por favor separar las palabras claves con coma                                        ejemplo('violencia,programa') ", max_length=250, null=True, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Biblioteca',
                'verbose_name_plural': 'Bibliotecas',
            },
        ),
        migrations.CreateModel(
            name='Documentales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=250)),
                ('documental', embed_video.fields.EmbedVideoField(help_text=b'Agregar videos de Youtube y Vimeo')),
                ('biblioteca', models.ForeignKey(to='biblioteca.Biblioteca')),
            ],
            options={
                'verbose_name': 'Documental',
                'verbose_name_plural': 'Documentales',
            },
        ),
        migrations.AddField(
            model_name='audios',
            name='biblioteca',
            field=models.ForeignKey(to='biblioteca.Biblioteca'),
        ),
        migrations.AddField(
            model_name='adjuntos',
            name='biblioteca',
            field=models.ForeignKey(to='biblioteca.Biblioteca'),
        ),
    ]
