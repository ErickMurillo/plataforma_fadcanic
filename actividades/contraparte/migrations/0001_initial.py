# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields
import actividades.thumbs
from django.conf import settings
import actividades.utils


class Migration(migrations.Migration):

    dependencies = [
        ('fadcanic', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lugar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_actividad', models.CharField(max_length=150)),
                ('fecha', models.DateTimeField()),
                ('hombres', models.IntegerField(default=0)),
                ('mujeres', models.IntegerField(default=0)),
                ('no_dato', models.BooleanField(verbose_name=b'No hay datos')),
                ('adultos', models.IntegerField(default=0, verbose_name='Adultos/as')),
                ('jovenes', models.IntegerField(default=0, verbose_name='J\xf3venes')),
                ('ninos', models.IntegerField(default=0, verbose_name='Ni\xf1os/as')),
                ('no_dato1', models.BooleanField(verbose_name=b'No hay datos')),
                ('autoridades', models.IntegerField(default=0, verbose_name='Autoridades p\xfablicas')),
                ('maestros', models.IntegerField(default=0)),
                ('lideres', models.IntegerField(default=0, verbose_name='Lideres/zas Comunitarios')),
                ('pobladores', models.IntegerField(default=0, verbose_name='Pobladores/as')),
                ('estudiantes', models.IntegerField(default=0)),
                ('miembros', models.IntegerField(default=0, verbose_name='Miembros de organizaciones comunitarias')),
                ('tecnicos', models.IntegerField(default=0, verbose_name='T\xe9cnicas/os de Organizaciones Copartes de FADCANIC')),
                ('relevancia', models.IntegerField(verbose_name='Importancia del tema/acci\xf3n', choices=[(99, 'No aplica'), (1, 'Muy bueno'), (2, 'Bueno'), (3, 'Regular'), (4, 'Malo'), (5, 'Muy malo')])),
                ('efectividad', models.IntegerField(verbose_name=b'Efectividad de la acci\xc3\xb3n', choices=[(99, 'No aplica'), (1, 'Muy bueno'), (2, 'Bueno'), (3, 'Regular'), (4, 'Malo'), (5, 'Muy malo')])),
                ('aprendizaje', models.IntegerField(verbose_name='Grado de aprendizaje', choices=[(99, 'No aplica'), (1, 'Muy bueno'), (2, 'Bueno'), (3, 'Regular'), (4, 'Malo'), (5, 'Muy malo')])),
                ('empoderamiento', models.IntegerField(verbose_name='Nivel de apropiaci\xf3n', choices=[(99, 'No aplica'), (1, 'Muy bueno'), (2, 'Bueno'), (3, 'Regular'), (4, 'Malo'), (5, 'Muy malo')])),
                ('participacion', models.IntegerField(verbose_name='Nivel de participaci\xf3n', choices=[(99, 'No aplica'), (1, 'Muy bueno'), (2, 'Bueno'), (3, 'Regular'), (4, 'Malo'), (5, 'Muy malo')])),
                ('relevancia_m', models.IntegerField(verbose_name='Importancia del tema/acci\xf3n', choices=[(99, 'No aplica'), (1, 'Muy bueno'), (2, 'Bueno'), (3, 'Regular'), (4, 'Malo'), (5, 'Muy malo')])),
                ('efectividad_m', models.IntegerField(verbose_name=b'Efectividad de la acci\xc3\xb3n', choices=[(99, 'No aplica'), (1, 'Muy bueno'), (2, 'Bueno'), (3, 'Regular'), (4, 'Malo'), (5, 'Muy malo')])),
                ('aprendizaje_m', models.IntegerField(verbose_name='Grado de aprendizaje', choices=[(99, 'No aplica'), (1, 'Muy bueno'), (2, 'Bueno'), (3, 'Regular'), (4, 'Malo'), (5, 'Muy malo')])),
                ('empoderamiento_m', models.IntegerField(verbose_name='Nivel de apropiaci\xf3n', choices=[(99, 'No aplica'), (1, 'Muy bueno'), (2, 'Bueno'), (3, 'Regular'), (4, 'Malo'), (5, 'Muy malo')])),
                ('participacion_m', models.IntegerField(verbose_name='Nivel de participaci\xf3n', choices=[(99, 'No aplica'), (1, 'Muy bueno'), (2, 'Bueno'), (3, 'Regular'), (4, 'Malo'), (5, 'Muy malo')])),
                ('comentarios', models.TextField(default=b'', blank=True)),
                ('acuerdos', models.TextField(default=b'', blank=True)),
                ('foto1', actividades.thumbs.ImageWithThumbsField(null=True, upload_to=actividades.utils.get_file_path, blank=True)),
                ('foto2', actividades.thumbs.ImageWithThumbsField(null=True, upload_to=actividades.utils.get_file_path, blank=True)),
                ('foto3', actividades.thumbs.ImageWithThumbsField(null=True, upload_to=actividades.utils.get_file_path, blank=True)),
                ('video', models.CharField(default=b'', max_length=300, blank=True)),
                ('mes', models.IntegerField(editable=False)),
                ('year', models.IntegerField(editable=False)),
                ('comunidad', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'municipio', chained_field=b'municipio', auto_choose=True, to='lugar.Comunidad')),
                ('ejes_transversales', models.ForeignKey(to='fadcanic.EjeTransversal')),
                ('municipio', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'proyecto', chained_field=b'proyecto', auto_choose=True, to='lugar.Municipio')),
                ('organizacion', models.ForeignKey(to='fadcanic.Organizacion')),
            ],
            options={
                'verbose_name_plural': 'Actividades',
            },
        ),
        migrations.CreateModel(
            name='Organizador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Organizadores',
            },
        ),
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('time', models.TimeField(null=True, blank=True)),
                ('params', models.TextField()),
                ('comment', models.TextField(default=b'', blank=True)),
                ('file', models.BooleanField()),
                ('bar_img', models.URLField(null=True, blank=True)),
                ('pie1_img', models.URLField(null=True, blank=True)),
                ('pie2_img', models.URLField(null=True, blank=True)),
                ('html_table', models.TextField(default=b'', blank=True)),
                ('bar_chart', models.TextField(default=b'', blank=True)),
                ('pie_chart_one', models.TextField(default=b'', blank=True)),
                ('pie_chart_two', models.TextField(default=b'', blank=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'Salida',
                'verbose_name_plural': 'Salidas',
            },
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250)),
                ('codigo', models.CharField(max_length=20)),
                ('inicio', models.DateField()),
                ('finalizacion', models.DateField()),
                ('monto_fadcanic', models.IntegerField()),
                ('monto_contrapartida', models.IntegerField()),
                ('contacto', models.CharField(max_length=100, verbose_name=b'Persona de contacto')),
                ('aporta_fadcanic', models.IntegerField(verbose_name='Aporta a Fadcanic', choices=[(1, 'Si'), (2, 'No')])),
                ('municipios', models.ManyToManyField(to='lugar.Municipio')),
                ('organizacion', models.ForeignKey(to='fadcanic.Organizacion')),
            ],
            options={
                'verbose_name_plural': 'Proyectos',
            },
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_corto', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('aporta_a', models.ForeignKey(to='fadcanic.ResultadoPrograma')),
                ('proyecto', models.ForeignKey(to='contraparte.Proyecto')),
            ],
            options={
                'verbose_name': 'Resultado del proyecto',
                'verbose_name_plural': 'Resultados del proyecto',
            },
        ),
        migrations.AddField(
            model_name='actividad',
            name='persona_organiza',
            field=models.ForeignKey(verbose_name='Persona que organiza la actividad', to='contraparte.Organizador'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='proyecto',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'organizacion', chained_field=b'organizacion', auto_choose=True, to='contraparte.Proyecto'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='resultado',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, to='contraparte.Resultado', chained_model_field=b'proyecto', chained_field=b'proyecto', verbose_name='Resultado al que aporta'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='tema_actividad',
            field=models.ForeignKey(to='fadcanic.Tema'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='tipo_actividad',
            field=models.ForeignKey(to='fadcanic.TipoActividad'),
        ),
    ]
