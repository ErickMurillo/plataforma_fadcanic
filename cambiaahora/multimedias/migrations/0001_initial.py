# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250, verbose_name='Nombre')),
                ('aprobacion', models.IntegerField(default=b'1', verbose_name='Aprobaci\xf3n', choices=[(1, 'Borrador'), (2, 'Aprobado')])),
                ('idioma', models.IntegerField(default=b'1', verbose_name='Idioma', choices=[(1, 'Espa\xf1ol'), (2, 'English')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Audio',
                'verbose_name_plural': 'Audios',
            },
        ),
        migrations.CreateModel(
            name='Documentales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250, verbose_name='Nombre')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('descripcion', models.TextField(verbose_name='Descripci\xf3n')),
                ('aprobacion', models.IntegerField(default=b'1', verbose_name='Aprobaci\xf3n', choices=[(1, 'Borrador'), (2, 'Aprobado')])),
                ('idioma', models.IntegerField(default=b'1', verbose_name='Idioma', choices=[(1, 'Espa\xf1ol'), (2, 'English')])),
                ('categoria', models.ForeignKey(verbose_name='Categoria', to='noticias.Categoria')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Documentale',
                'verbose_name_plural': 'Documentales',
            },
        ),
        migrations.CreateModel(
            name='Fotos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250, verbose_name='Nombre')),
                ('aprobacion', models.IntegerField(default=b'1', verbose_name='Aprobaci\xf3n', choices=[(1, 'Borrador'), (2, 'Aprobado')])),
                ('idioma', models.IntegerField(default=b'1', verbose_name='Idioma', choices=[(1, 'Espa\xf1ol'), (2, 'English')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Foto',
                'verbose_name_plural': 'Fotos',
            },
        ),
        migrations.CreateModel(
            name='SubirAudios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=250, verbose_name='Titulo')),
                ('audio', models.FileField(upload_to=b'', verbose_name='Audio')),
                ('audios', models.ForeignKey(to='multimedias.Audios')),
            ],
            options={
                'verbose_name': 'Subir audio',
                'verbose_name_plural': 'Subir audios',
            },
        ),
        migrations.CreateModel(
            name='SubirDocumentales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=250, verbose_name='Titulo')),
                ('video', models.URLField(verbose_name='Video')),
                ('documental', models.ForeignKey(to='multimedias.Documentales')),
            ],
            options={
                'verbose_name': 'Subir documento',
                'verbose_name_plural': 'Subir documentos',
            },
        ),
        migrations.CreateModel(
            name='SubirFotos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=250, verbose_name='Titulo')),
                ('foto', models.FileField(upload_to=b'', verbose_name='Foto')),
                ('fotos', models.ForeignKey(to='multimedias.Fotos')),
            ],
            options={
                'verbose_name': 'Subir foto',
                'verbose_name_plural': 'Subir fotos',
            },
        ),
        migrations.CreateModel(
            name='SubirVideos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=250, verbose_name='Titulo')),
                ('video', models.URLField(verbose_name='Video')),
            ],
            options={
                'verbose_name': 'Subir video',
                'verbose_name_plural': 'Subir videos',
            },
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250, verbose_name='Nombre')),
                ('aprobacion', models.IntegerField(default=b'1', verbose_name='Aprobaci\xf3n', choices=[(1, 'Borrador'), (2, 'Aprobado')])),
                ('idioma', models.IntegerField(default=b'1', verbose_name='Idioma', choices=[(1, 'Espa\xf1ol'), (2, 'English')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
        ),
        migrations.AddField(
            model_name='subirvideos',
            name='videos',
            field=models.ForeignKey(to='multimedias.Videos'),
        ),
    ]
