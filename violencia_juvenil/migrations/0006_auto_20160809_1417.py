# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('violencia_juvenil', '0005_auto_20160106_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicas',
            name='pregunta22',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=11, null=True, verbose_name=b'22-\xc2\xbfQu\xc3\xa9 hace usted para prevenir la violencia juvenil y abuso de droga?', choices=[(b'a', b'Participo de actividades de prevenci\xc3\xb3n en mi lugar'), (b'b', b'Evito discusi\xc3\xb3n o acciones que generen violencia'), (b'c', b'Doy m\xc3\xa1s cari\xc3\xb1o y menos golpes a las j\xc3\xb3venes'), (b'd', b'Estoy organizada/o en mi comunidad'), (b'e', b'No hago nada'), (b'f', b'No s\xc3\xa9 que hacer')]),
        ),
    ]
