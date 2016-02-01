# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lugar', '0001_initial'),
        ('violencia_juvenil', '0003_auto_20151201_2011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='informacionentrevistado',
            name='municipio',
        ),
        migrations.AddField(
            model_name='informacionentrevistado',
            name='municipio1',
            field=models.ForeignKey(default=1, verbose_name=b'Municipio', to='lugar.Municipio'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='escolaridad',
            name='cantidad',
            field=models.IntegerField(choices=[(1, b'1 a 3'), (2, b'4 a 6'), (3, b'6 a m\xc3\xa1s'), (4, b'Ninguno')]),
        ),
    ]
