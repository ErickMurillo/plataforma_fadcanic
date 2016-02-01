# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('violencia_juvenil', '0004_auto_20160105_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actitud',
            name='pregunta15',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=11, null=True, verbose_name=b'14-\xc2\xbfQu\xc3\xa9 piensa de las personas consumidoras de droga?', choices=[(b'a', b'Son enfermos'), (b'b', b'Personas que necesitan apoyo de su familia y la sociedad'), (b'c', b'No cuentan con la educaci\xc3\xb3n suficiente'), (b'd', b'Fueron v\xc3\xadctimas de violencia'), (b'e', b'Deben estar aislados de los dem\xc3\xa1s '), (b'f', b'NS/NR')]),
        ),
        migrations.AlterField(
            model_name='actitud',
            name='pregunta16',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=11, null=True, verbose_name=b'16-\xc2\xbfQu\xc3\xa9 piensa de los j\xc3\xb3venes violentos?', choices=[(b'a', b'Criminales/delincuentes'), (b'b', b'Es rebeld\xc3\xada luego se le pasar\xc3\xa1'), (b'c', b'Ojo por ojo contra ellos'), (b'd', b'Necesitan m\xc3\xa1s apoyo de su familia y la sociedad'), (b'e', b'Darles apoyo con empleo y educaci\xc3\xb3n'), (b'f', b'NS/NR')]),
        ),
        migrations.AlterField(
            model_name='actitud',
            name='pregunta17',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=13, null=True, verbose_name=b'17-\xc2\xbfC\xc3\xb3mo prevenir la violencia juvenil y el abuso de drogas?', choices=[(b'a', b'Mayor orientaci\xc3\xb3n de la familia'), (b'b', b'Organizando a la comunidad'), (b'c', b'M\xc3\xa1s empleo y educaci\xc3\xb3n'), (b'd', b'M\xc3\xa1s terapias y consejos con las familias y los j\xc3\xb3venes'), (b'e', b'Disminuir la violencia presentada en los medios de comunicaci\xc3\xb3n'), (b'f', b'Hacer m\xc3\xa1s centros de rehabilitaci\xc3\xb3n'), (b'g', b'NS/NR')]),
        ),
        migrations.AlterField(
            model_name='actitud',
            name='pregunta18',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=13, null=True, verbose_name=b'18-\xc2\xbfCu\xc3\xa1les son las principales causas de la violencia juvenil?', choices=[(b'a', b'Se criaron en la calle'), (b'b', b'Sus madres y padres no les inculcaron buenos valores'), (b'c', b'Carencia de afecto en la familia'), (b'd', b'Fueron ni\xc3\xb1os que vivieron violencia en sus casas'), (b'e', b'Por el grupo \xc3\xa9tnico al que pertenece'), (b'f', b'Viene en la sangre (genes)'), (b'g', b'NS/NR')]),
        ),
        migrations.AlterField(
            model_name='actitud',
            name='pregunta19',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=15, null=True, verbose_name=b'19-\xc2\xbfPor qu\xc3\xa9 muchas mujeres despu\xc3\xa9s vivir violencia, perdonan a sus parejas o abusadores?', choices=[(b'a', b'Masoquismo'), (b'b', b'Tiene dependencia emocional hacia \xc3\xa9l'), (b'c', b'Porque lo ama y cree que puede cambiar'), (b'd', b'No cuenta con apoyo para mantenerse econ\xc3\xb3micamente '), (b'e', b'No recibi\xc3\xb3 apoyo de las instituciones'), (b'f', b'La gente le aconseja que lo perdone'), (b'g', b'Est\xc3\xa1 en el ciclo de la violencia'), (b'h', b'NS/NR')]),
        ),
        migrations.AlterField(
            model_name='actitud',
            name='pregunta20',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=17, null=True, verbose_name=b'20-\xc2\xbfCu\xc3\xa1les crees son las causas de abuso sexual?', choices=[(b'a', b'Falta de informaci\xc3\xb3n de madres, padres o tutores'), (b'b', b'Las madres, padres o tutores no protegen ni informan a sus hijos/hijas'), (b'c', b'Falta de vigilancia policial en la ciudad'), (b'd', b'La comunidad sabe, pero no denuncia'), (b'e', b'Por consumo de droga y alcohol'), (b'f', b'Los ni\xc3\xb1os y ni\xc3\xb1as no se saben cuidar'), (b'g', b'Por el machismo y abuso de poder de los hombres'), (b'h', b'Por el machismo y abuso de poder de las mujeres'), (b'i', b'NS/NR')]),
        ),
        migrations.AlterField(
            model_name='conocimiento',
            name='pregunta1',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=9, null=True, verbose_name=b'1-\xc2\xbfPara Usted, que es Violencia Juvenil?', choices=[(b'a', b'Actos violentos realizados por j\xc3\xb3venes'), (b'b', b'Da\xc3\xb1os f\xc3\xadsicos y psicol\xc3\xb3gicos realizado por adultos a los j\xc3\xb3venes'), (b'c', b'Problema social que da\xc3\xb1a tanto a las v\xc3\xadctimas como a los victimarios'), (b'd', b'Todas las anteriores'), (b'e', b'NS/NR')]),
        ),
        migrations.AlterField(
            model_name='conocimiento',
            name='pregunta10',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=9, null=True, verbose_name=b'10-\xc2\xbfQu\xc3\xa9 es el abuso sexual?', choices=[(b'a', b'Actividad sexual entre dos o m\xc3\xa1s personas sin consentimiento de una de ellas'), (b'b', b'Todo acto con fines sexuales hacia ni\xc3\xb1as, ni\xc3\xb1os y adolescentes'), (b'c', b'Presionar a una pareja para tener relaciones sexuales'), (b'd', b'Relaci\xc3\xb3n sexual entre dos personas'), (b'e', b'NS/NR')]),
        ),
        migrations.AlterField(
            model_name='conocimiento',
            name='pregunta11',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=13, null=True, verbose_name=b'11-\xc2\xbfEn qu\xc3\xa9 lugares ocurren m\xc3\xa1s los abusos sexuales?', choices=[(b'a', b'Casa'), (b'b', b'Escuela (dentro o fuera)'), (b'c', b'Calle'), (b'd', b'Comunidades rurales'), (b'e', b'En la ciudad'), (b'f', b'En la iglesia'), (b'g', b'NS/NR')]),
        ),
        migrations.AlterField(
            model_name='conocimiento',
            name='pregunta12',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=11, null=True, verbose_name=b'12-\xc2\xbfQu\xc3\xa9 hacer para prevenir el abuso sexual?', choices=[(b'a', b'Denunciar al agreso'), (b'b', b'Apoyo moral y psicol\xc3\xb3gico a la v\xc3\xadctima'), (b'c', b'Promover campa\xc3\xb1as de sensibilizaci\xc3\xb3n contra el AS'), (b'd', b'Mejor comunicaci\xc3\xb3n entre los miembros de la familia'), (b'e', b'Organizarnos en la comunidad'), (b'f', b'NS/NR')]),
        ),
        migrations.AlterField(
            model_name='conocimiento',
            name='pregunta13',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=11, null=True, verbose_name=b'13-\xc2\xbfQu\xc3\xa9 entiende por seguridad ciudadana?', choices=[(b'a', b'Vivir en paz y armon\xc3\xada'), (b'b', b'Prevenci\xc3\xb3n de los delitos'), (b'c', b'M\xc3\xa1s c\xc3\xa1rceles y mano dura contra los delincuentes'), (b'd', b'Erradicar la violencia de cualquier tipo'), (b'e', b'Un trabajo de la Polic\xc3\xada nacional'), (b'f', b'NS/NR')]),
        ),
        migrations.AlterField(
            model_name='conocimiento',
            name='pregunta14',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=9, null=True, verbose_name=b'14-\xc2\xbfPara educar a los ni\xc3\xb1os y ni\xc3\xb1as se les debe pegar?', choices=[(b'a', b'Con la faja o con las manos'), (b'b', b'Mejor castigarles pero no pegarles'), (b'c', b'Hay que pegarles para que sepan respetar'), (b'd', b'Hablarles fuerte o gritarles pero no pegarles'), (b'e', b'NS/NR')]),
        ),
        migrations.AlterField(
            model_name='conocimiento',
            name='pregunta2',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=7, null=True, verbose_name=b'2-\xc2\xbfPara usted, qu\xc3\xa9 es el abuso de drogas?', choices=[(b'a', b'Problema de salud p\xc3\xbablica'), (b'b', b'Uso de cualquier tipo de droga il\xc3\xadcita/ilegal'), (b'c', b'Consumo de todo tipo de qu\xc3\xadmicos '), (b'd', b'NS/NR')]),
        ),
        migrations.AlterField(
            model_name='conocimiento',
            name='pregunta3',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=21, null=True, verbose_name=b'3-\xc2\xbfQu\xc3\xa9 tipo violencia afecta m\xc3\xa1s a tu comunidad?', choices=[(b'a', b'Violencia hacia las mujeres'), (b'b', b'Violencia intrafamiliar '), (b'c', b'Violencia hacia personas con opciones sexuales diferentes'), (b'd', b'Acoso sexual'), (b'e', b'Abuso sexual'), (b'f', b'Violencia en la escuela'), (b'g', b'Aumento de expendios de drogas'), (b'h', b'Aumento de j\xc3\xb3venes adictos'), (b'i', b'Pleito entre pandillas'), (b'j', b'Conflictos \xc3\xa9tnicos y territoriales'), (b'k', b'NS/NR')]),
        ),
        migrations.AlterField(
            model_name='conocimiento',
            name='pregunta4',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=11, null=True, verbose_name=b'4-\xc2\xbfQu\xc3\xa9 lugares considera que genera m\xc3\xa1s violencia?', choices=[(b'a', b'En el hogar y las familias'), (b'b', b'En la escuela (dentro y alrededor de ellas)'), (b'c', b'En las calles o espacios abiertos'), (b'd', b'En los centros de trabajo'), (b'e', b'En instituciones manejadas por el Estado'), (b'f', b'NS/NR')]),
        ),
        migrations.AlterField(
            model_name='conocimiento',
            name='pregunta5',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=13, null=True, verbose_name=b'5-\xc2\xbfQu\xc3\xa9 lleva a un joven a ser violento?', choices=[(b'a', b'Nivel de pobreza en su familia'), (b'b', b'Sufri\xc3\xb3 maltrato f\xc3\xadsico y psicol\xc3\xb3gico en el hogar'), (b'c', b'Falta de atenci\xc3\xb3n y consejos de su familia'), (b'd', b'Influencia de otros j\xc3\xb3venes con problemas'), (b'e', b'Falta de acceso a la educaci\xc3\xb3n'), (b'f', b'Falta de empleos y oportunidades'), (b'g', b'NS/NR')]),
        ),
        migrations.AlterField(
            model_name='conocimiento',
            name='pregunta6',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=15, null=True, verbose_name=b'6-\xc2\xbfQui\xc3\xa9nes son los m\xc3\xa1s perjudicados por la violencia juvenil y el abuso de drogas?', choices=[(b'a', b'La familia'), (b'b', b'Las personas de la comunidad o barrio'), (b'c', b'Las mujeres'), (b'd', b'Los hombres'), (b'e', b'Las y los j\xc3\xb3venes'), (b'f', b'Ni\xc3\xb1as y ni\xc3\xb1os'), (b'g', b'La sociedad en general'), (b'h', b'NS/NR')]),
        ),
        migrations.AlterField(
            model_name='conocimiento',
            name='pregunta7',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=17, null=True, verbose_name=b'7-\xc2\xbfQu\xc3\xa9 soluciones hay para prevenir la violencia juvenil?', choices=[(b'a', b'Prisi\xc3\xb3n para los que ejercen violencia'), (b'b', b'Prisi\xc3\xb3n para expendedores de droga'), (b'c', b'Prisi\xc3\xb3n para consumidores  de drogas'), (b'd', b'Tomar la justicia por sus propias manos'), (b'e', b'Buscar ayuda psicol\xc3\xb3gica'), (b'f', b'Brindar mayor nivel de informaci\xc3\xb3n'), (b'g', b'Acompa\xc3\xb1ar procesos de capacitaci\xc3\xb3n'), (b'h', b'Organizar a la comunidad y barrio'), (b'i', b'Mayor nivel de organizaci\xc3\xb3n de la poblaci\xc3\xb3n y las instituciones')]),
        ),
        migrations.AlterField(
            model_name='conocimiento',
            name='pregunta8',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=17, null=True, verbose_name=b'8-\xc2\xbfQui\xc3\xa9nes deben ser los responsables de prevenir la violencia juvenil?', choices=[(b'a', b'La Polic\xc3\xada'), (b'b', b'Ministerio de Salud'), (b'c', b'Ministerio de Educaci\xc3\xb3n/Escuelas'), (b'd', b'Gobiernos municipales y locales'), (b'f', b'La comunidad'), (b'g', b'La familia'), (b'h', b'Las Iglesias'), (b'i', b'Organizaciones comunitarias'), (b'j', b'Organizaciones sin fin de lucro (ONG)')]),
        ),
        migrations.AlterField(
            model_name='conocimiento',
            name='pregunta9',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=7, null=True, verbose_name=b'9-\xc2\xbfQu\xc3\xa9 entiende por femicidio?', choices=[(b'a', b'Mujeres violentas contra los hombres'), (b'b', b'Cuando el hombre asesina a una mujer'), (b'c', b'Cuando el esposo, novio o familiar le quita la vida a una mujer'), (b'd', b'NS/NR')]),
        ),
        migrations.AlterField(
            model_name='estadoactual',
            name='pregunta34',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'34-\xc2\xbfHa participado en acciones comunitarias para prevenir la violencia juvenil y el abuso de drogas?', choices=[(1, b'Si'), (2, b'No')]),
        ),
        migrations.AlterField(
            model_name='estadoactual',
            name='pregunta35',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'35- \xc2\xbfExisten lugares en tu comunidad para atender a personas que vivieron la violencia juvenil y el abuso de drogas?', choices=[(1, b'Si'), (2, b'No')]),
        ),
        migrations.AlterField(
            model_name='estadoactual',
            name='pregunta36',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=7, null=True, verbose_name=b'36-Si no hay lugares en la comunidad, \xc2\xbfd\xc3\xb3nde se atienden las v\xc3\xadctimas?', choices=[(b'a', b'Viaja a otro municipio/comunidad'), (b'b', b'Paga psic\xc3\xb3loga o abogados particulares'), (b'c', b'No hace nada'), (b'd', b'NS/NR')]),
        ),
        migrations.AlterField(
            model_name='estadoactual',
            name='pregunta37',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'37-\xc2\xbfHa escuchado de la Campa\xc3\xb1a: Cambia ahora solo hazlo?', choices=[(1, b'Si'), (2, b'No'), (3, b'NS/NR')]),
        ),
        migrations.AlterField(
            model_name='estadoactual',
            name='pregunta38',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=11, null=True, verbose_name=b'38-\xc2\xbfDe qu\xc3\xa9 temas trata la campa\xc3\xb1a?', choices=[(b'a', b'Prevenci\xc3\xb3n de violencia'), (b'b', b'Prevenci\xc3\xb3n de consumo de drogas'), (b'c', b'Contra la violencia hacia las mujeres'), (b'd', b'Diversi\xc3\xb3n y deporte en la juventud'), (b'e', b'Medio ambiente'), (b'f', b'NS/NR')]),
        ),
        migrations.AlterField(
            model_name='estadoactual',
            name='pregunta39',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=11, null=True, verbose_name=b'39-\xc2\xbfQu\xc3\xa9 producto ha visto de la Campa\xc3\xb1a?', choices=[(b'a', b'Historias de radio'), (b'b', b'Historias en la televisi\xc3\xb3n (documentales)'), (b'c', b'Cuaderno informativo'), (b'd', b'Actividades en los colegios'), (b'e', b'Video foros en los barrios'), (b'f', b'NS/NR')]),
        ),
        migrations.AlterField(
            model_name='percepcion',
            name='pregunta25',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=13, null=True, verbose_name=b'25-\xc2\xbfEn que familias se da m\xc3\xa1s frecuentemente el abuso sexual?', choices=[(b'a', b'Familias pobres'), (b'b', b'Familias de clase media'), (b'c', b'Familias adineradas'), (b'd', b'Donde no escuchan a las ni\xc3\xb1as y ni\xc3\xb1os'), (b'e', b'Donde no se interesan por el bienestar de las ni\xc3\xb1as y ni\xc3\xb1os'), (b'f', b'Todas por igual'), (b'g', b'NS/NR')]),
        ),
        migrations.AlterField(
            model_name='percepcion',
            name='pregunta26',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=13, null=True, verbose_name=b'26-\xc2\xbfQu\xc3\xa9 piensa del rol de las autoridades en la prevenci\xc3\xb3n de la violencia juvenil y abuso de drogas?', choices=[(b'a', b'Educan a la poblaci\xc3\xb3n'), (b'b', b'Dan seguimiento a los casos'), (b'c', b'Revictimizan'), (b'd', b'Brindan asistencia psicol\xc3\xb3gica a la v\xc3\xadctimas'), (b'e', b'No hacen nada'), (b'f', b'Hacen muy poco'), (b'g', b'NS/NR')]),
        ),
        migrations.AlterField(
            model_name='percepcion',
            name='pregunta27',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=13, null=True, verbose_name=b'27-\xc2\xbfQu\xc3\xa9 lleva a un joven a consumir drogas?', choices=[(b'a', b'Porque no reciben tratamientos especializado'), (b'b', b'Faltan centros especializados'), (b'c', b'No reciben el apoyo de sus familias'), (b'd', b'Los marginan'), (b'e', b'La Polic\xc3\xada no act\xc3\xbaa para apresarlos'), (b'f', b'Baja autoestima'), (b'g', b'NS/NR')]),
        ),
        migrations.AlterField(
            model_name='percepcion',
            name='pregunta28',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=9, null=True, verbose_name=b'28-\xc2\xbfQu\xc3\xa9 acciones hacer desde la comunidad para la prevenci\xc3\xb3n de la violencia juvenil y el abuso de drogas?', choices=[(b'a', b'Denunciar ante las autoridades'), (b'b', b'Organizar promotores para la prevenci\xc3\xb3n'), (b'c', b'Campa\xc3\xb1as p\xc3\xbablicas abordando el tema'), (b'd', b'Campa\xc3\xb1as de informaci\xc3\xb3n en escuelas'), (b'e', b'NS/NR')]),
        ),
        migrations.AlterField(
            model_name='percepcion',
            name='pregunta29_1',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'29-\xc2\xbfPara usted el piropo es una forma de violencia?', choices=[(1, b'Si'), (2, b'No'), (3, b'Es posible'), (4, b'NS/NR')]),
        ),
        migrations.AlterField(
            model_name='percepcion',
            name='pregunta30',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=13, null=True, verbose_name=b'30-\xc2\xbfQui\xc3\xa9nes considera que son m\xc3\xa1s violentos?', choices=[(b'a', b'Hombres adultos'), (b'b', b'Mujeres adultas'), (b'c', b'Hombres j\xc3\xb3venes'), (b'd', b'Mujeres j\xc3\xb3venes'), (b'e', b'Hombres adolescentes'), (b'f', b'Mujeres adolescentes'), (b'g', b'NS/NR')]),
        ),
        migrations.AlterField(
            model_name='percepcion',
            name='pregunta31',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=7, null=True, verbose_name=b'31-\xc2\xbfQu\xc3\xa9 opina del narcotr\xc3\xa1fico?', choices=[(b'a', b'Ayuda a la econom\xc3\xada de la comunidad'), (b'b', b'Da\xc3\xb1a a la juventud'), (b'c', b'Genera m\xc3\xa1s violencia'), (b'd', b'NS/NR')]),
        ),
        migrations.AlterField(
            model_name='percepcion',
            name='pregunta32_1',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'32-\xc2\xbfCree que Nicaragua es un pa\xc3\xads seguro?', choices=[(1, b'Si'), (2, b'No'), (3, b'Relativamente s\xc3\xad'), (4, b'NS/NR')]),
        ),
        migrations.AlterField(
            model_name='percepcion',
            name='pregunta33',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'33-\xc2\xbfCree que tu comunidad es segura?', choices=[(1, b'Si'), (2, b'No'), (3, b'Relativamente s\xc3\xad'), (4, b'NS/NR')]),
        ),
        migrations.AlterField(
            model_name='practicas',
            name='pregunta21',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=9, null=True, verbose_name=b'21-\xc2\xbfQu\xc3\xa9 har\xc3\xadas si en tu presencia alguien es v\xc3\xadctima de violencia juvenil?', choices=[(b'a', b'La defiendo, ejerciendo la fuerza'), (b'b', b'No hago nada'), (b'c', b'Hago denuncia a las autoridades'), (b'd', b'Tratar de convencer al joven de no ejercer violencia contra la v\xc3\xadctima'), (b'e', b'NS/NR')]),
        ),
        migrations.AlterField(
            model_name='practicas',
            name='pregunta22',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=11, null=True, verbose_name=b'22-Qu\xc3\xa9 hace usted para prevenir la violencia juvenil y abuso de droga?', choices=[(b'a', b'Participo de actividades de prevenci\xc3\xb3n en mi lugar'), (b'b', b'Evito discusi\xc3\xb3n o acciones que generen violencia'), (b'c', b'Doy m\xc3\xa1s cari\xc3\xb1o y menos golpes a las j\xc3\xb3venes'), (b'd', b'Estoy organizada/o en mi comunidad'), (b'e', b'No hago nada'), (b'f', b'No s\xc3\xa9 que hacer')]),
        ),
        migrations.AlterField(
            model_name='practicas',
            name='pregunta23',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=11, null=True, verbose_name=b'23-\xc2\xbfQu\xc3\xa9 har\xc3\xada si ve que una mujer est\xc3\xa1 siendo violentada?', choices=[(b'a', b'La defender\xc3\xada'), (b'b', b'Poner denuncia ante la Polic\xc3\xada'), (b'c', b'No hago nada'), (b'd', b'Llamo a los medios de comunicaci\xc3\xb3n '), (b'e', b'La aconsejar\xc3\xada despu\xc3\xa9s'), (b'f', b'NS/NR')]),
        ),
        migrations.AlterField(
            model_name='practicas',
            name='pregunta24',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=13, null=True, verbose_name=b'24-\xc2\xbfQu\xc3\xa9 hacer para que los j\xc3\xb3venes no se conviertan en expendedores de droga?', choices=[(b'a', b'Mayor vigilancia policial'), (b'b', b'Generar oportunidades de empleo'), (b'c', b'Mayor acceso a la educaci\xc3\xb3n'), (b'd', b'Un sistema de justicia m\xc3\xa1s beligerante'), (b'e', b'Mayor uni\xc3\xb3n familiar'), (b'f', b'Mayor organizaci\xc3\xb3n de la comunidad'), (b'g', b'NS/NR')]),
        ),
    ]
