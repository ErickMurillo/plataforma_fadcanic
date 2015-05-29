# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Audios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250)),
                ('aprobacion', models.IntegerField(default=b'1', choices=[(1, b'Borrador'), (2, b'Aprobado')])),
                ('idioma', models.IntegerField(default=b'1', choices=[(1, b'Espa\xc3\xb1ol'), (2, b'Ingles')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Audio',
                'verbose_name_plural': 'Audios',
            },
        ),
        migrations.CreateModel(
            name='Fotos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250)),
                ('aprobacion', models.IntegerField(default=b'1', choices=[(1, b'Borrador'), (2, b'Aprobado')])),
                ('idioma', models.IntegerField(default=b'1', choices=[(1, b'Espa\xc3\xb1ol'), (2, b'Ingles')])),
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
                ('titulo', models.CharField(max_length=250)),
                ('audio', models.FileField(upload_to=b'')),
                ('audios', models.ForeignKey(to='multimedias.Audios')),
            ],
            options={
                'verbose_name': 'Subir audio',
                'verbose_name_plural': 'Subir audios',
            },
        ),
        migrations.CreateModel(
            name='SubirFotos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=250)),
                ('foto', models.FileField(upload_to=b'')),
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
                ('titulo', models.CharField(max_length=250)),
                ('video', models.URLField()),
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
                ('nombre', models.CharField(max_length=250)),
                ('aprobacion', models.IntegerField(default=b'1', choices=[(1, b'Borrador'), (2, b'Aprobado')])),
                ('idioma', models.IntegerField(default=b'1', choices=[(1, b'Espa\xc3\xb1ol'), (2, b'Ingles')])),
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
