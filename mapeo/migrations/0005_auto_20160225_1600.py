# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapeo', '0004_auto_20160126_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info_Organizaciones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=50, null=True, verbose_name=b'Tel\xc3\xa9fono', blank=True)),
                ('correo', models.EmailField(max_length=254, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='organizaciones',
            name='cantidad_org',
            field=models.IntegerField(null=True, verbose_name=b'Cantidad de Organizaciones', blank=True),
        ),
        migrations.AddField(
            model_name='info_organizaciones',
            name='organizacion',
            field=models.ForeignKey(to='mapeo.Organizaciones'),
        ),
    ]
