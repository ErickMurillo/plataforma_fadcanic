# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=350)),
            ],
        ),
        migrations.AddField(
            model_name='biblioteca',
            name='tema',
            field=models.ForeignKey(blank=True, to='biblioteca.Temas', null=True),
        ),
    ]
