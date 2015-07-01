# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields
import smart_selects.db_fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lugar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acciones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('accion', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Actitud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pregunta14', multiselectfield.db.fields.MultiSelectField(max_length=9, verbose_name=b'14 -\xc2\xbfC\xc3\xb3mo valora la situaci\xc3\xb3n de la violencia juvenil y abuso de drogas en su localidad?', choices=[(1, b'Alta'), (2, b'Media'), (3, b'Baja'), (4, b'No responde'), (5, b'No sabe')])),
                ('pregunta15', multiselectfield.db.fields.MultiSelectField(max_length=15, verbose_name=b'15- \xc2\xbfQu\xc3\xa9 piensa usted de las personas violentas y abusadores de droga?', choices=[(1, b'Son enfermos'), (2, b'Criminales/delincuentes'), (3, b'Personas que se equivocan'), (4, b'No cuentan con la educaci\xc3\xb3n suficiente'), (5, b'Fueron v\xc3\xadctimas de violencia'), (6, b'Personas violentas de acuerdo a su Etnia'), (7, b'No responde'), (8, b'No sabe')])),
                ('pregunta16', multiselectfield.db.fields.MultiSelectField(max_length=9, verbose_name=b'16- \xc2\xbfQu\xc3\xa9 piensa de las personas v\xc3\xadctimas de la violencia juvenil?', choices=[(1, b'Hay que brindarles ayuda'), (2, b'Es pasajero, no lo necesita'), (3, b'El/ella se lo busco'), (4, b'No responde'), (5, b'No sabe')])),
                ('pregunta17', multiselectfield.db.fields.MultiSelectField(max_length=13, verbose_name=b'17- \xc2\xbfC\xc3\xb3mo prevenir la violencia juvenil y abuso de drogas?', choices=[(1, b'Mayor orientaci\xc3\xb3n de la familia'), (2, b'Organizando a la comunidad'), (3, b'Mayores niveles de informaci\xc3\xb3n'), (4, b'Acceso a la educaci\xc3\xb3n'), (5, b'Generando oportunidades de empleo'), (6, b'No responde'), (7, b'No sabe')])),
                ('pregunta18', multiselectfield.db.fields.MultiSelectField(max_length=13, verbose_name=b'18- \xc2\xbfCu\xc3\xa1les cree usted son las principales causas de la violencia juvenil?', choices=[(1, b'Falta de informaci\xc3\xb3n'), (2, b'Maltrato f\xc3\xadsico en el seno familiar'), (3, b'Carencia afectiva de la familia'), (4, b'Desintegraci\xc3\xb3n de la familia'), (5, b'Por el grupo \xc3\xa9tnico al que pertenece'), (6, b'Viene en la sangre (genes)'), (7, b'No sabe')])),
                ('pregunta19', multiselectfield.db.fields.MultiSelectField(max_length=11, verbose_name=b'19- \xc2\xbfPor qu\xc3\xa9 crees que muchas mujeres despu\xc3\xa9s vivir violencia, perdonan a sus parejas o abusadores?', choices=[(1, b'Masoquismo'), (2, b'Porque le ama y cree que puede cambiar'), (3, b'No cuenta con apoyo para mantenerse'), (4, b'No recibi\xc3\xb3 apoyo de las instituciones'), (5, b'No responde'), (6, b'No sabe')])),
                ('pregunta20', multiselectfield.db.fields.MultiSelectField(max_length=15, verbose_name=b'20- \xc2\xbfCu\xc3\xa1les cree Usted son las causas de abuso sexual?', choices=[(1, b'Falta de educaci\xc3\xb3n'), (2, b'Falta de informaci\xc3\xb3n'), (3, b'La no protecci\xc3\xb3n de los padres a sus hijos/hijas'), (4, b'Falta de vigilancia policial en la ciudad'), (5, b'La comunidad sabe pero no denuncia'), (6, b'Por abuso de droga y alcohol'), (7, b'No responde'), (8, b'No sabe')])),
            ],
            options={
                'verbose_name_plural': 'II-Actitud sobre los temas de violencia y abuso de drogas',
            },
        ),
        migrations.CreateModel(
            name='Conocimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pregunta1', multiselectfield.db.fields.MultiSelectField(max_length=9, verbose_name=b'1-\xc2\xbfPara Usted que es Violencia Juvenil?', choices=[(1, b'Actos violentos realizados por j\xc3\xb3venes'), (2, b'Acci\xc3\xb3n que afecta negativamente a otra persona'), (3, b'Da\xc3\xb1os f\xc3\xadsicos (golpes, gritos)'), (4, b'Da\xc3\xb1os psicol\xc3\xb3gicos (descalificaciones, burlas, insultos)'), (5, b'Todas las anteriores')])),
                ('pregunta2', multiselectfield.db.fields.MultiSelectField(max_length=7, verbose_name=b'2-\xc2\xbfQu\xc3\xa9 es abuso de drogas para usted?', choices=[(1, b'Problema de salud p\xc3\xbablica'), (2, b'Uso de cualquier tipo de droga il\xc3\xadcita'), (3, b'Consumo de droga'), (4, b'No responde')])),
                ('pregunta3', multiselectfield.db.fields.MultiSelectField(max_length=20, verbose_name=b'3-\xc2\xbfQu\xc3\xa9 tipo violencia afecta m\xc3\xa1s a tu comunidad?', choices=[(1, b'Violencia hacia las mujeres'), (2, b'Violencia hacia personas con opciones sexual diferente'), (3, b'Acoso sexual'), (4, b'Abuso sexual'), (5, b'Violencia en la escuela'), (6, b'Aumento de expendio de drogas'), (7, b'Aumento del consumo de drogas'), (8, b'Pleito entre pandillas'), (9, b'Aumento del grupos delictivos'), (10, b'Conflictos \xc3\xa9tnicos')])),
                ('pregunta4', multiselectfield.db.fields.MultiSelectField(max_length=9, verbose_name=b'4-\xc2\xbfQue\xcc\x81 lugares considera usted que genera m\xc3\xa1s violencia?', choices=[(1, b'En el hogar'), (2, b'En la escuela (dentro y alrededor de ellas)'), (3, b'En las calles o espacios abiertos'), (4, b'En los centros de trabajo'), (5, b'En instituciones manejadas por el Estado')])),
                ('pregunta5', multiselectfield.db.fields.MultiSelectField(max_length=13, verbose_name=b'5-\xc2\xbfQu\xc3\xa9 es lo que conlleva a un joven a ser violento y consuma drogas?', choices=[(1, b'Nivel de pobreza en su familia'), (2, b'Sufri\xc3\xb3 maltrato f\xc3\xadsico y psicolo\xcc\x81gico en el hogar'), (3, b'Falta de atenci\xc3\xb3n de su familia'), (4, b'Experiment\xc3\xb3 con drogas'), (5, b'Falta de acceso a la educaci\xc3\xb3n'), (6, b'Participaci\xc3\xb3n en pandillas juveniles'), (7, b'No responde')])),
                ('pregunta6', multiselectfield.db.fields.MultiSelectField(max_length=13, verbose_name=b'6-\xc2\xbfQui\xc3\xa9nes son los m\xc3\xa1s perjudicados por la violencia juvenil y abuso de drogas?', choices=[(1, b'La familia'), (2, b'Las personas de la comunidad o barrio'), (3, b'Las mujeres'), (4, b'Los hombres'), (5, b'Las y los j\xc3\xb3venes'), (6, b'Nin\xcc\x83as y ni\xc3\xb1os'), (7, b'La sociedad en general')])),
                ('pregunta7', multiselectfield.db.fields.MultiSelectField(max_length=17, verbose_name=b'7-\xc2\xbfQu\xc3\xa9 soluciones ve Usted para prevenir la violencia juvenil?', choices=[(1, b'Prisi\xc3\xb3n para los que ejercen violencia'), (2, b'Prisi\xc3\xb3n para los expendedores de droga'), (3, b'Prisi\xc3\xb3n para los que consumen drogas'), (4, b'Tomar la justicia por sus propias manos'), (5, b'Buscar ayuda psicol\xc3\xb3gica'), (6, b'Brindar mayor nivel de informaci\xc3\xb3n sobre el tema'), (7, b'Acompa\xc3\xb1ar procesos de capacitaci\xc3\xb3n sobre los temas'), (8, b'Organizar a la comunidad y barrio'), (9, b'Mayor nivel de organizacio\xcc\x81n de la poblaci\xc3\xb3n y las instituciones para prevenir delitos')])),
                ('pregunta8', multiselectfield.db.fields.MultiSelectField(max_length=17, verbose_name=b'8-\xc2\xbfQui\xc3\xa9nes son los responsables de aportar a la prevenci\xc3\xb3n de la violencia juvenil?', choices=[(1, b'La Polic\xc3\xada'), (2, b'Ministerio de Salud'), (3, b'Ministerio de Educaci\xc3\xb3n/Escuelas'), (4, b'Gobiernos municipales y locales'), (5, b'La comunidad'), (6, b'La familia'), (7, b'Las Iglesias'), (8, b'Organizaciones comunitarias'), (9, b'Organizaciones sin fin de lucro (ONG)')])),
                ('pregunta9', multiselectfield.db.fields.MultiSelectField(max_length=9, verbose_name=b'9-\xc2\xbfQu\xc3\xa9 entiendes por feminicidio?', choices=[(1, b'Es un delito'), (2, b'Cuando el hombre asesina a una mujer'), (3, b'No es un delito'), (4, b'No sabe'), (5, b'No responde')])),
                ('pregunta10', multiselectfield.db.fields.MultiSelectField(max_length=9, verbose_name=b'10-\xc2\xbfQu\xc3\xa9 es el abuso sexual?', choices=[(1, b'Actividad sexual entre dos o ma\xcc\x81s personas sin consentimiento de una persona'), (2, b'Acto sexual que se ejerce bajo presi\xc3\xb3n'), (3, b'Relaci\xc3\xb3n sexual entre dos personas'), (4, b'No sabe'), (5, b'No responde')])),
                ('pregunta11', multiselectfield.db.fields.MultiSelectField(max_length=15, verbose_name=b'11-\xc2\xbfEn qu\xc3\xa9 lugares ocurren m\xc3\xa1s el abuso sexual?', choices=[(1, b'Casa'), (2, b'Escuela (dentro o fuera)'), (3, b'Calle'), (4, b'Comunidades rurales'), (5, b'En la ciudad'), (6, b'En la iglesia'), (7, b'No sabe'), (8, b'No responde')])),
                ('pregunta12', multiselectfield.db.fields.MultiSelectField(max_length=11, verbose_name=b'12-\xc2\xbfQu\xc3\xa9 hacer para prevenir el abuso sexual?', choices=[(1, b'Denunciar al agreso'), (2, b'Apoyo moral y psicol\xc3\xb3gico a la v\xc3\xadctima'), (3, b'Promover campa\xc3\xb1as de sensibilizaci\xc3\xb3n contra el AS'), (4, b'Mejor comunicaci\xc3\xb3n entre los miembros de la familia'), (5, b'No sabe'), (6, b'No responde')])),
                ('pregunta13', multiselectfield.db.fields.MultiSelectField(max_length=13, verbose_name=b'13-\xc2\xbfQu\xc3\xa9 entiendes por seguridad ciudadana?', choices=[(1, b'Derecho a vivir con paz'), (2, b'Prevenci\xc3\xb3n de los delitos'), (3, b'Derecho a vivir en un ambiente pacifico'), (4, b'Erradicar la violencia de cualquier tipo'), (5, b'Falta contra las personas y sus bienes'), (6, b'No responde'), (7, b'No sabe')])),
            ],
            options={
                'verbose_name_plural': 'I-Conocimiento sobre los temas de violencia y abuso de drogas',
            },
        ),
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('year', models.IntegerField(editable=False)),
            ],
            options={
                'verbose_name_plural': 'Encuesta opini\xf3n violencia juvenil y abuso de drogas',
            },
        ),
        migrations.CreateModel(
            name='Encuestador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250, verbose_name=b'Nombre del recolector')),
            ],
            options={
                'verbose_name': 'Encuestadores',
            },
        ),
        migrations.CreateModel(
            name='Escolaridad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('escolaridad', models.IntegerField(choices=[(1, b'No sabe leer'), (2, b'Alfabeto'), (3, b'Primaria completa'), (4, b'Primaria incompleta'), (5, b'Secundaria completa'), (6, b'Secundaria incompleta'), (7, b'T\xc3\xa9cnico'), (8, b'Universitario')])),
                ('civil', models.IntegerField(choices=[(1, b'Soltero/Soltera'), (2, b'Casado/casada'), (3, b'Uni\xc3\xb3n de hecho estable'), (4, b'Divorciado/divorciada'), (5, b'Viudo/viuda')])),
                ('varones', models.IntegerField(default=b'0')),
                ('mujeres', models.IntegerField(default=b'0')),
                ('encuesta', models.ForeignKey(to='violencia_juvenil.Encuesta')),
            ],
            options={
                'verbose_name_plural': 'Nivel de escolaridad',
            },
        ),
        migrations.CreateModel(
            name='EstadoActual',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pregunta40', models.IntegerField(verbose_name=b'40- \xc2\xbfUsted considera que la violencia juvenil y abuso de drogas es un problema en su comunidad?', choices=[(1, b'No es un problema'), (2, b'Es un problema'), (3, b'Es un problema grave')])),
                ('pregunta41', models.IntegerField(verbose_name=b'41- \xc2\xbfUsted considera que la violencia juvenil y abuso de drogas es un problema del pa\xc3\xads?', choices=[(1, b'No es un problema'), (2, b'Es un problema'), (3, b'Es un problema grave')])),
                ('pregunta42', models.IntegerField(verbose_name=b'42- \xc2\xbfSabe si la comunidad hace acciones comunitarias para la prevenci\xc3\xb3n de la violencia juvenil y abuso de drogas?', choices=[(1, b'Si'), (2, b'No'), (3, b'No sabe')])),
                ('pregunta43', models.IntegerField(verbose_name=b'43- \xc2\xbfSabe si hay lugares en esta comunidad que atienden a personas que vivieron la violencia juvenil y abuso de drogas?', choices=[(1, b'Si'), (2, b'No')])),
                ('pregunta44', multiselectfield.db.fields.MultiSelectField(max_length=9, verbose_name=b'44- \xc2\xbfUsted sabe qu\xc3\xa9 tipo de atenci\xc3\xb3n brindan en esos lugares?', choices=[(1, b'Atenci\xc3\xb3n psicol\xc3\xb3gica'), (2, b'Atenci\xc3\xb3n Jur\xc3\xaddica'), (3, b'Atenci\xc3\xb3n m\xc3\xa9dica'), (4, b'Acompa\xc3\xb1amiento de los casos'), (5, b'Desconoce')])),
                ('pregunta45', multiselectfield.db.fields.MultiSelectField(max_length=7, verbose_name=b'45- \xc2\xbfSi no hay ning\xc3\xban lugar en su comunidad donde se atiende a las personas v\xc3\xadctimas violencia juvenil y abuso de drogas a d\xc3\xb3nde van para recibir atenci\xc3\xb3n?', choices=[(1, b'Viaja a otro municipio/comunidad'), (2, b'Paga psic\xc3\xb3loga o abogados particulares'), (3, b'No hace nada'), (4, b'No sabe')])),
                ('encuesta', models.ForeignKey(to='violencia_juvenil.Encuesta')),
                ('si_respuesta_42', models.ManyToManyField(to='violencia_juvenil.Acciones', verbose_name=b'Si responde Si, favor mencione tipos de acci\xc3\xb3n', blank=True)),
            ],
            options={
                'verbose_name_plural': 'V-Estado actual sobre sobre el tema de violencia y abuso de drogas',
            },
        ),
        migrations.CreateModel(
            name='Etnias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Etnias',
            },
        ),
        migrations.CreateModel(
            name='InformacionEntrevistado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('edad', models.IntegerField()),
                ('residencia', models.IntegerField(choices=[(1, b'Urbano'), (2, b'Rural')])),
                ('habita', models.IntegerField(choices=[(1, b'Barrio'), (2, b'Comunidad')])),
                ('sexo', models.IntegerField(choices=[(1, b'Mujer'), (2, b'Hombre')])),
                ('departamento', models.ForeignKey(to='lugar.Departamento')),
                ('encuesta', models.ForeignKey(to='violencia_juvenil.Encuesta')),
                ('etnia', models.ForeignKey(to='violencia_juvenil.Etnias')),
                ('municipio', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'departamento', chained_field=b'departamento', blank=True, auto_choose=True, to='lugar.Municipio', null=True)),
            ],
            options={
                'verbose_name_plural': 'Informaci\xf3n del Entrevistado',
            },
        ),
        migrations.CreateModel(
            name='LugaresComunidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lugar', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ParticipaOrganizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('participado', models.IntegerField(choices=[(1, b'Si'), (2, b'No')])),
                ('encuesta', models.ForeignKey(to='violencia_juvenil.Encuesta')),
            ],
            options={
                'verbose_name_plural': 'participa o ha participado en alguna orga. que previene la violencia juvenil y abuso de drogas?',
            },
        ),
        migrations.CreateModel(
            name='Percepcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pregunta25', multiselectfield.db.fields.MultiSelectField(max_length=13, verbose_name=b'25-\xc2\xbfQui\xc3\xa9nes son los m\xc3\xa1s afectados por la violencia?', choices=[(1, b'Ni\xc3\xb1as, ni\xc3\xb1os'), (2, b'J\xc3\xb3venes (mujeres y hombres)'), (3, b'Mujeres'), (4, b'La familia'), (5, b'La persona violenta'), (6, b'La comunidad'), (7, b'El pa\xc3\xads')])),
                ('pregunta26', multiselectfield.db.fields.MultiSelectField(max_length=15, verbose_name=b'26- \xc2\xbfQui\xc3\xa9nes deben ser protagonistas de la prevenci\xc3\xb3n de la violencia juvenil y abuso de drogas?', choices=[(1, b'La familia'), (2, b'La Comunidad'), (3, b'El Estado'), (4, b'La Polic\xc3\xada'), (5, b'Medios de Comunicaci\xc3\xb3n'), (6, b'Gobiernos Aut\xc3\xb3nomos'), (7, b'Las Iglesias'), (8, b'ONGs')])),
                ('pregunta27', multiselectfield.db.fields.MultiSelectField(max_length=7, verbose_name=b'27- \xc2\xbfEn que familias se da m\xc3\xa1s frecuentemente el abuso sexual?', choices=[(1, b'Familias pobres'), (2, b'Familias de clase media'), (3, b'Familias adineradas'), (4, b'Todas por igual')])),
                ('pregunta28', multiselectfield.db.fields.MultiSelectField(max_length=9, verbose_name=b'28- \xc2\xbfQu\xc3\xa9 piensa del rol de las autoridades en la prevenci\xc3\xb3n de la violencia juvenil y abuso de drogas?', choices=[(1, b'Educan a la poblaci\xc3\xb3n'), (2, b'Dan seguimiento a los casos'), (3, b'Revictimizan a las victimas'), (4, b'Brindan asistencia psicol\xc3\xb3gica a la v\xc3\xadctimas'), (5, b'No hacen nada')])),
                ('pregunta29', multiselectfield.db.fields.MultiSelectField(max_length=11, verbose_name=b'29- \xc2\xbfPor qu\xc3\xa9 los j\xc3\xb3venes que consumen droga se vuelven adictos?', choices=[(1, b'Porque no reciben tratamientos especializado'), (2, b'Faltan centros especializados'), (3, b'No reciben el apoyo de sus familias'), (4, b'Los marginans'), (5, b'La polic\xc3\xada no actu\xc3\xa1 para apresarlos'), (6, b'Baja autoestima')])),
                ('pregunta30', multiselectfield.db.fields.MultiSelectField(max_length=7, verbose_name=b'30- \xc2\xbfPara usted que acciones se puede hacer desde la comunidad para la prevenci\xc3\xb3n de la violencia juvenil y abuso de drogas?', choices=[(1, b'Denunciar a las autoridades'), (2, b'Organizar promotores para la prevenci\xc3\xb3n'), (3, b'Campa\xc3\xb1as p\xc3\xbablicas abordando el tema'), (4, b'Campa\xc3\xb1as de informaci\xc3\xb3n en escuelas')])),
                ('pregunta31', models.IntegerField(verbose_name=b'31- \xc2\xbfCree Usted que la poblaci\xc3\xb3n se organizara para prevenir la violencia y abuso de drogas se disminuir\xc3\xada?', choices=[(1, b'Si'), (2, b'No'), (3, b'Es posible'), (4, b'No responde')])),
                ('pregunta32', multiselectfield.db.fields.MultiSelectField(max_length=9, verbose_name=b'32- \xc2\xbfQu\xc3\xa9 piensa del rol de las autoridades en la prevenci\xc3\xb3n de la violencia juvenil y abuso de drogas?', choices=[(1, b'Educan a la poblaci\xc3\xb3n'), (2, b'Dan seguimiento a los casos'), (3, b'Revictimizan a las victimas'), (4, b'Brindan asistencia psicol\xc3\xb3gica a la v\xc3\xadctimas'), (5, b'No hacen nada')])),
                ('pregunta33', models.IntegerField(verbose_name=b'33- \xc2\xbfConsideras usted que los piropos constituyen una forma de violencia?', choices=[(1, b'Si'), (2, b'No'), (3, b'Es posible'), (4, b'No responde')])),
                ('pregunta34', multiselectfield.db.fields.MultiSelectField(max_length=11, verbose_name=b'34- \xc2\xbfQui\xc3\xa9nes consideras que son m\xc3\xa1s violentos?', choices=[(1, b'Varones adultos'), (2, b'Mujeres adultas'), (3, b'Varones j\xc3\xb3venes'), (4, b'Mujeres j\xc3\xb3venes'), (5, b'Varones adolescentes'), (6, b'Mujeres adolescentes')])),
                ('pregunta35', models.IntegerField(verbose_name=b'35- \xc2\xbfCree usted que el narcotr\xc3\xa1fico es un problema?', choices=[(1, b'Si'), (2, b'No'), (3, b'No responde')])),
                ('pregunta36', models.IntegerField(verbose_name=b'36- \xc2\xbfCree usted que el narcotr\xc3\xa1fico ayuda a las comunidades?', choices=[(1, b'Si'), (2, b'No'), (3, b'Es posible'), (4, b'No responde')])),
                ('pregunta37', models.IntegerField(verbose_name=b'37- \xc2\xbfCrees que Nicaragua es un pa\xc3\xads seguro?', choices=[(1, b'Si'), (2, b'No'), (3, b'No responde')])),
                ('pregunta38', models.IntegerField(verbose_name=b'38- \xc2\xbfCrees que tu comunidad/barrio es seguro (a)?', choices=[(1, b'Si'), (2, b'No'), (3, b'No responde')])),
                ('encuesta', models.ForeignKey(to='violencia_juvenil.Encuesta')),
            ],
            options={
                'verbose_name_plural': 'IV-Percepci\xf3n sobre el tema de violencia y abuso de drogas',
            },
        ),
        migrations.CreateModel(
            name='Practicas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pregunta21', multiselectfield.db.fields.MultiSelectField(max_length=11, verbose_name=b'21- \xc2\xbfQu\xc3\xa9 har\xc3\xadas si en tu presencia alguien es v\xc3\xadctimade violencia juvenil?', choices=[(1, b'La defiendo, ejerciendo la fuerza'), (2, b'No hago nada'), (3, b'Hago denuncia a las autoridades'), (4, b'Lo denuncio con un familiar de la v\xc3\xadctima'), (5, b'No responde'), (6, b'No sabe')])),
                ('pregunta22', multiselectfield.db.fields.MultiSelectField(max_length=13, verbose_name=b'22- \xc2\xbfQu\xc3\xa9 hace usted para prevenir la violencia juvenil y abuso de droga?', choices=[(1, b'Participo de actividades de prevenci\xc3\xb3n en mi lugar'), (2, b'Trato de informarme'), (3, b'Evito discusi\xc3\xb3n o acciones que gener\xc3\xa9 violencia'), (4, b'Protejo a mi familia'), (5, b'Hago denuncia p\xc3\xbablica'), (6, b'No hago nada'), (7, b'No s\xc3\xa9 que hacer')])),
                ('pregunta23', multiselectfield.db.fields.MultiSelectField(max_length=9, verbose_name=b'23- \xc2\xbfQu\xc3\xa9 har\xc3\xadas si en tu presencia una mujer es v\xc3\xadctima de violencia?', choices=[(1, b'La defender\xc3\xada'), (2, b'Poner denuncia ante la Polic\xc3\xada'), (3, b'No hago nada'), (4, b'Me alejo del problema'), (5, b'No responde')])),
                ('pregunta24', multiselectfield.db.fields.MultiSelectField(max_length=15, verbose_name=b'24- \xc2\xbfQu\xc3\xa9 hacer para que los j\xc3\xb3venes no caigan en el problema de narcotr\xc3\xa1fico?', choices=[(1, b'Mayor vigilancia policial'), (2, b'Generar oportunidades de empleo'), (3, b'Mayor acceso a la educaci\xc3\xb3n'), (4, b'Un sistema de justicia m\xc3\xa1s beligerante'), (5, b'Mayor uni\xc3\xb3n familiar'), (6, b'Mayor organizaci\xc3\xb3n de la comunidad'), (7, b'No responde'), (8, b'No sabe')])),
                ('encuesta', models.ForeignKey(to='violencia_juvenil.Encuesta')),
            ],
            options={
                'verbose_name_plural': 'III-Pr\xe1cticas sobre el tema de violencia y abuso de drogas',
            },
        ),
        migrations.CreateModel(
            name='RespuetaSi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('respuesta', multiselectfield.db.fields.MultiSelectField(max_length=7, choices=[(1, b'Promotor/Promotora'), (2, b'Asistiendo a charlas que se brinda'), (3, b'Apoyando a otras persona de la comunidad'), (4, b'Organizando actividades')])),
                ('encuesta', models.ForeignKey(to='violencia_juvenil.Encuesta')),
            ],
            options={
                'verbose_name_plural': 'Indique en cuales tipos de organizaciones',
            },
        ),
        migrations.AddField(
            model_name='estadoactual',
            name='si_respuesta_43',
            field=models.ManyToManyField(to='violencia_juvenil.LugaresComunidad', verbose_name=b'Si responde SI favor mencione los lugares', blank=True),
        ),
        migrations.AddField(
            model_name='encuesta',
            name='encuestador',
            field=models.ForeignKey(to='violencia_juvenil.Encuestador'),
        ),
        migrations.AddField(
            model_name='encuesta',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='conocimiento',
            name='encuesta',
            field=models.ForeignKey(to='violencia_juvenil.Encuesta'),
        ),
        migrations.AddField(
            model_name='actitud',
            name='encuesta',
            field=models.ForeignKey(to='violencia_juvenil.Encuesta'),
        ),
    ]
