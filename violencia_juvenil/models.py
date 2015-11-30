# -*- coding: utf-8 -*-
from django.db import models
from actividades.lugar.models import Departamento, Municipio
from smart_selects.db_fields import ChainedForeignKey
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

# Create your models here.

class Encuestador(models.Model):
    nombre = models.CharField('Nombre del recolector', max_length=250)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name='Encuestadores'

#a- Datos de Recoleccion
GRUPOS_CHOICES = ((1,'Adolescente o Joven'),
                 (2,'Comité comunal'),
                 (3,'Diplomado/Promotoría'),
                 (4,'Diplomado/comunicación'),
                 (5,'Poblador general +30'))

class Encuesta(models.Model):
    fecha = models.DateField()
    grupos = models.IntegerField(choices=GRUPOS_CHOICES)
    encuestador = models.ForeignKey(Encuestador)
    latitud = models.FloatField(editable=False)
    longitud = models.FloatField(editable=False)
    year = models.IntegerField(editable=False)
    user = models.ForeignKey(User)

    def save(self):
        self.year = self.fecha.year
        super(Encuesta, self).save()

    def __unicode__(self):
        return self.encuestador.nombre

    class Meta:
        verbose_name_plural = 'Encuesta opinión violencia juvenil y abuso de drogas'


#b- Informacion del Entrevistado

CHOICE_SEXO = ((1,'Mujer'),(2,'Hombre'))
CHOICE_AREA = ((1,'Urbano'),(2,'Rural'))
CHOICE_HABITA = ((1,'Barrio'),(2,'Comunidad'))

class Etnias(models.Model):
    nombre = models.CharField(max_length=250)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name='Etnias'

EDAD_CHOICES = ((1,'13 a 18'),(2,'19 a 30'),(3,'30 a +'))

ETNIAS_CHOICES = ((1,'Mestiza'),(2,'Ulwa'),(3,'Miskitu'),(4,'Creole'))

class InformacionEntrevistado(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    edad = models.IntegerField(choices=EDAD_CHOICES)
    etnia = models.IntegerField(choices=ETNIAS_CHOICES)
    departamento = models.ForeignKey(Departamento)
    municipio = ChainedForeignKey(
                                Municipio,
                                chained_field="departamento", 
                                chained_model_field="departamento",
                                show_all=False, auto_choose=True,null=True, blank=True)
    # residencia = models.IntegerField(choices=CHOICE_AREA)
    # habita = models.IntegerField(choices=CHOICE_HABITA)
    sexo = models.IntegerField(choices=CHOICE_SEXO)

    # def __unicode__(self):
    #     return self.etnia.nombre

    class Meta:
        verbose_name_plural = 'Información del Entrevistado'

#c- Nivel de escolaridad
CHOICE_ESCOLARIDAD = ((1,'No sabe leer'),(2,'Alfabeto'),
                      (3,'Primaria completa'),(4,'Primaria incompleta'),
                      (5,'Secundaria completa'),(6,'Secundaria incompleta'),
                      (7,'Técnico'),(8,'Universitario a más'))

CHOICE_CIVIL = ((1,'Soltero/Soltera'),(2,'Casado/casada'),
                      (3,'Unión de hecho estable'),(4,'Divorciado/divorciada'),
                      (5,'Viudo/viuda'))

CHOICE_SI_NO = ((1,'Si'),(2,'No'))

CANTIDAD_HIJOS_CHOICES = ((1,'1 a 3'),(2,'4 a 6'),(3,'6 a más'))

class Escolaridad(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    escolaridad = models.IntegerField(choices=CHOICE_ESCOLARIDAD)
    civil = models.IntegerField(choices=CHOICE_CIVIL)
    hijos = models.IntegerField(choices=CHOICE_SI_NO)
    cantidad = models.IntegerField(choices=CANTIDAD_HIJOS_CHOICES)
    # varones = models.IntegerField(default='0')
    # mujeres = models.IntegerField(default='0')

    def __unicode__(self):
       return u'%s' % (str(self.get_escolaridad_display())

    class Meta:
        verbose_name_plural = 'Nivel de escolaridad'

#f- Favor indicar
class ParticipaOrganizacion(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    participado = models.IntegerField(choices=CHOICE_SI_NO)

    def __unicode__(self):
        return u'%s' % (str(self.get_participado_display))

    class Meta:
        verbose_name_plural = 'Participa o ha participado en alguna orga. que previene la violencia juvenil y abuso de drogas?'

CHOICE_RESPUESTA_SI = (('a', 'Promotor/Promotora'),
                       ('b', 'Asistiendo a charlas que se brinda'),
                       ('c', 'Apoyando a otras persona de la comunidad'),
                       ('d', 'Organizando actividades'),
                       )
class RespuetaSi(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    respuesta = MultiSelectField(choices=CHOICE_RESPUESTA_SI)

    class Meta:
        verbose_name_plural = 'Indique en cuales tipos de organizaciones'

#I- Conocimiento sobre los temas de violencia y abuso de drogas
CHOICE_VIOLENCIA_1 = (('a', 'Actos violentos realizados por jóvenes'),
                    ('b', 'Daños físicos y psicológicos realizado por adultos a los jóvenes'),
                    ('c', 'Problema social que daña tanto a las víctimas como a los victimarios'),
                    ('d', 'Todas las anteriores'),
                    ('e', 'NS/NR'),
                )

CHOICE_ABUSO_DROGA_2 = (('a', 'Problema de salud pública'),
                        ('b', 'Uso de cualquier tipo de droga ilícita/ilegal'),
                        ('c', 'Consumo de todo tipo de químicos '),
                        ('d', 'NS/NR'),
                    )

CHOICE_TIPO_VIOLENCIA_3 = (('a', 'Violencia hacia las mujeres'),
                        ('b', 'Violencia intrafamiliar '),
                        ('c', 'Violencia hacia personas con opciones sexuales diferentes'),
                        ('d', 'Acoso sexual'),
                        ('e', 'Abuso sexual'),
                        ('f', 'Violencia en la escuela'),
                        ('g', 'Aumento de expendios de drogas'),
                        ('h', 'Aumento de jóvenes adictos'),
                        ('i', 'Pleito entre pandillas'),
                        ('j', 'Conflictos étnicos y territoriales'),
                        ('k', 'NS/NR')
                    )

CHOICE_LUGARES_4 = (('a', 'En el hogar y las familias'),
                        ('b', 'En la escuela (dentro y alrededor de ellas)'),
                        ('c', 'En las calles o espacios abiertos'),
                        ('d', 'En los centros de trabajo'),
                        ('e', 'En instituciones manejadas por el Estado'),
                        ('f', 'NS/NR')
                    )

CHOICE_JOVEN_VIOLENTO_5 = (('a', 'Nivel de pobreza en su familia'),
                        ('b', 'Sufrió maltrato físico y psicológico en el hogar'),
                        ('c', 'Falta de atención y consejos de su familia'),
                        ('d', 'Influencia de otros jóvenes con problemas'),
                        ('e', 'Falta de acceso a la educación'),
                        ('f', 'Falta de empleos y oportunidades'),
                        ('g', 'NS/NR'),
                    )

CHOICE_PERJUDICADOS_6 = (('a', 'La familia'),
                        ('b', 'Las personas de la comunidad o barrio'),
                        ('c', 'Las mujeres'),
                        ('d', 'Los hombres'),
                        ('e', 'Las y los jóvenes'),
                        ('f', 'Niñas y niños'),
                        ('g', 'La sociedad en general'),
                        ('h', 'NS/NR')
                    )

CHOICE_SOLUCIONES_7 = (('a', 'Prisión para los que ejercen violencia'),
                        ('b', 'Prisión para expendedores de droga'),
                        ('c', 'Prisión para consumidores  de drogas'),
                        ('d', 'Tomar la justicia por sus propias manos'),
                        ('e', 'Buscar ayuda psicológica'),
                        ('f', 'Brindar mayor nivel de información'),
                        ('g', 'Acompañar procesos de capacitación'),
                        ('h', 'Organizar a la comunidad y barrio'),
                        ('i', 'Mayor nivel de organización de la población y las instituciones'),
                    )

CHOICE_RESPONSABLES_8 = (('a', 'La Policía'),
                        ('b', 'Ministerio de Salud'),
                        ('c', 'Ministerio de Educación/Escuelas'),
                        ('d', 'Gobiernos municipales y locales'),
                        ('f', 'La comunidad'),
                        ('g', 'La familia'),
                        ('h', 'Las Iglesias'),
                        ('i', 'Organizaciones comunitarias'),
                        ('j', 'Organizaciones sin fin de lucro (ONG)'),
                    )

CHOICE_FEMINICIDIO_9 = (('a', 'Mujeres violentas contra los hombres'),
                        ('b', 'Cuando el hombre asesina a una mujer'),
                        ('c', 'Cuando el esposo, novio o familiar le quita la vida a una mujer'),
                        ('d', 'NS/NR'),
                    )

CHOICE_ABUSO_SEXUAL_10 = (('a', 'Actividad sexual entre dos o más personas sin consentimiento de una de ellas'),
                        ('b', 'Todo acto con fines sexuales hacia niñas, niños y adolescentes'),
                        ('c', 'Presionar a una pareja para tener relaciones sexuales'),
                        ('d', 'Relación sexual entre dos personas'),
                        ('e', 'NS/NR'),
                    )

CHOICE_LUGARES_11 = (('a', 'Casa'),
                    ('b', 'Escuela (dentro o fuera)'),
                    ('c', 'Calle'),
                    ('d', 'Comunidades rurales'),
                    ('e', 'En la ciudad'),
                    ('f', 'En la iglesia'),
                    ('g', 'NS/NR'),
            )

CHOICE_PREVENIR_ABUSO_12 = (('a', 'Denunciar al agreso'),
                    ('b', 'Apoyo moral y psicológico a la víctima'),
                    ('c', 'Promover campañas de sensibilización contra el AS'),
                    ('d', 'Mejor comunicación entre los miembros de la familia'),
                    ('e', 'Organizarnos en la comunidad'),
                    ('f', 'NS/NR'),
            )

CHOICE_SEGURIDAD_CIUDADA_13 = (('a', 'Vivir en paz y armonía'),
                    ('b', 'Prevención de los delitos'),
                    ('c', 'Más cárceles y mano dura contra los delincuentes'),
                    ('d', 'Erradicar la violencia de cualquier tipo'),
                    ('e', 'Un trabajo de la Policía nacional'),
                    ('f', 'NS/NR'),
            )

CHOICE_EDUCAR_NINOS_14 = (('a', 'Con la faja o con las manos'),
                    ('b', 'Mejor castigarles pero no pegarles'),
                    ('c', 'Hay que pegarles para que sepan respetar'),
                    ('d', 'Hablarles fuerte o gritarles pero no pegarles'),
                    ('e', 'NS/NR'),
            )

class Conocimiento(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    pregunta1 = MultiSelectField(choices=CHOICE_VIOLENCIA_1, verbose_name='1-¿Para Usted, que es Violencia Juvenil?')
    pregunta2 = MultiSelectField(choices=CHOICE_ABUSO_DROGA_2, verbose_name='2-¿Para usted, qué es el abuso de drogas?')
    pregunta3 = MultiSelectField(choices=CHOICE_TIPO_VIOLENCIA_3, verbose_name='3-¿Qué tipo violencia afecta más a tu comunidad?')
    pregunta4 = MultiSelectField(choices=CHOICE_LUGARES_4, verbose_name='4-¿Qué lugares considera que genera más violencia?')
    pregunta5 = MultiSelectField(choices=CHOICE_JOVEN_VIOLENTO_5, verbose_name='5-¿Qué lleva a un joven a ser violento?')
    pregunta6 = MultiSelectField(choices=CHOICE_PERJUDICADOS_6, verbose_name='6-¿Quiénes son los más perjudicados por la violencia juvenil y el abuso de drogas?')
    pregunta7 = MultiSelectField(choices=CHOICE_SOLUCIONES_7, verbose_name='7-¿Qué soluciones hay para prevenir la violencia juvenil?')
    pregunta8 = MultiSelectField(choices=CHOICE_RESPONSABLES_8, verbose_name='8-¿Quiénes deben ser los responsables de prevenir la violencia juvenil?')
    pregunta9 = MultiSelectField(choices=CHOICE_FEMINICIDIO_9, verbose_name='9-¿Qué entiende por femicidio?')
    pregunta10 = MultiSelectField(choices=CHOICE_ABUSO_SEXUAL_10, verbose_name='10-¿Qué es el abuso sexual?')
    pregunta11 = MultiSelectField(choices=CHOICE_LUGARES_11, verbose_name='11-¿En qué lugares ocurren más los abusos sexuales?')
    pregunta12 = MultiSelectField(choices=CHOICE_PREVENIR_ABUSO_12, verbose_name='12-¿Qué hacer para prevenir el abuso sexual?')
    pregunta13 = MultiSelectField(choices=CHOICE_SEGURIDAD_CIUDADA_13, verbose_name='13-¿Qué entiende por seguridad ciudadana?')
    pregunta14 = MultiSelectField(choices=CHOICE_EDUCAR_NINOS_14,verbose_name='14-¿Para educar a los niños y niñas se les debe pegar?')
    
    class Meta:
        verbose_name_plural = 'I-Conocimiento sobre los temas de violencia y abuso de drogas'

#II- Actitud sobre los temas de violencia y abuso de drogas.

CHOICE_VALORA_14 = (('a', 'Alta'),
                    ('b', 'Media'),
                    ('c', 'Baja'),
                    ('d', 'No responde'),
                    ('e', 'No sabe'),
            )

CHOICE_PERSONAS_15 = (('a', 'Son enfermos'),
                    ('b', 'Criminales/delincuentes'),
                    ('c', 'Personas que se equivocan'),
                    ('d', 'No cuentan con la educación suficiente'),
                    ('e', 'Fueron víctimas de violencia'),
                    ('f', 'Personas violentas de acuerdo a su Etnia'),
                    ('g', 'No responde'),
                    ('h', 'No sabe'),
            )

CHOICE_16 = (('a', 'Hay que brindarles ayuda'),
                    ('b', 'Es pasajero, no lo necesita'),
                    ('c', 'El/ella se lo busco'),
                    ('d', 'No responde'),
                    ('e', 'No sabe'),
            )

CHOICE_17 = (('a', 'Mayor orientación de la familia'),
                    ('b', 'Organizando a la comunidad'),
                    ('c', 'Mayores niveles de información'),
                    ('d', 'Acceso a la educación'),
                    ('e', 'Generando oportunidades de empleo'),
                    ('f', 'No responde'),
                    ('g', 'No sabe'),
            )

CHOICE_18 = (('a', 'Falta de información'),
                    ('b', 'Maltrato físico en el seno familiar'),
                    ('c', 'Carencia afectiva de la familia'),
                    ('d', 'Desintegración de la familia'),
                    ('e', 'Por el grupo étnico al que pertenece'),
                    ('f', 'Viene en la sangre (genes)'),
                    ('g', 'No sabe'),
            )

CHOICE_19 = (('a', 'Masoquismo'),
                    ('b', 'Porque le ama y cree que puede cambiar'),
                    ('c', 'No cuenta con apoyo para mantenerse'),
                    ('d', 'No recibió apoyo de las instituciones'),
                    ('e', 'No responde'),
                    ('f', 'No sabe'),
            )

CHOICE_20 = (('a', 'Falta de educación'),
                    ('b', 'Falta de información'),
                    ('c', 'La no protección de los padres a sus hijos/hijas'),
                    ('d', 'Falta de vigilancia policial en la ciudad'),
                    ('e', 'La comunidad sabe pero no denuncia'),
                    ('f', 'Por abuso de droga y alcohol'),
                    ('g', 'No responde'),
                    ('h', 'No sabe'),
            )

class Actitud(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    pregunta14 = MultiSelectField(choices=CHOICE_VALORA_14, verbose_name='14 -¿Cómo valora la situación de la violencia juvenil y abuso de drogas en su localidad?')
    pregunta15 = MultiSelectField(choices=CHOICE_PERSONAS_15, verbose_name='15- ¿Qué piensa usted de las personas violentas y abusadores de droga?')
    pregunta16 = MultiSelectField(choices=CHOICE_16, verbose_name='16- ¿Qué piensa de las personas víctimas de la violencia juvenil?')
    pregunta17 = MultiSelectField(choices=CHOICE_17, verbose_name='17- ¿Cómo prevenir la violencia juvenil y abuso de drogas?')
    pregunta18 = MultiSelectField(choices=CHOICE_18, verbose_name='18- ¿Cuáles cree usted son las principales causas de la violencia juvenil?')
    pregunta19 = MultiSelectField(choices=CHOICE_19, verbose_name='19- ¿Por qué crees que muchas mujeres después vivir violencia, perdonan a sus parejas o abusadores?')
    pregunta20 = MultiSelectField(choices=CHOICE_20, verbose_name='20- ¿Cuáles cree Usted son las causas de abuso sexual?')
   
    class Meta:
        verbose_name_plural = 'II-Actitud sobre los temas de violencia y abuso de drogas'

#III- Prácticas sobre el tema de violencia y abuso de drogas

CHOICE_21 = (('a', 'La defiendo, ejerciendo la fuerza'),
                    ('b', 'No hago nada'),
                    ('c', 'Hago denuncia a las autoridades'),
                    ('d', 'Lo denuncio con un familiar de la víctima'),
                    ('e', 'No responde'),
                    ('f', 'No sabe'),
            )

CHOICE_22 = (('a', 'Participo de actividades de prevención en mi lugar'),
                    ('b', 'Trato de informarme'),
                    ('c', 'Evito discusión o acciones que generé violencia'),
                    ('d', 'Protejo a mi familia'),
                    ('e', 'Hago denuncia pública'),
                    ('f', 'No hago nada'),
                    ('g', 'No sé que hacer'),
            )


CHOICE_23 = (('a', 'La defendería'),
                    ('b', 'Poner denuncia ante la Policía'),
                    ('c', 'No hago nada'),
                    ('d', 'Me alejo del problema'),
                    ('e', 'No responde'),
            )

CHOICE_24 = (('a', 'Mayor vigilancia policial'),
                    ('b', 'Generar oportunidades de empleo'),
                    ('c', 'Mayor acceso a la educación'),
                    ('d', 'Un sistema de justicia más beligerante'),
                    ('e', 'Mayor unión familiar'),
                    ('f', 'Mayor organización de la comunidad'),
                    ('g', 'No responde'),
                    ('h', 'No sabe'),
            )

class Practicas(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    pregunta21 = MultiSelectField(choices=CHOICE_21, verbose_name='21- ¿Qué harías si en tu presencia alguien es víctimade violencia juvenil?')
    pregunta22 = MultiSelectField(choices=CHOICE_22, verbose_name='22- ¿Qué hace usted para prevenir la violencia juvenil y abuso de droga?')
    pregunta23 = MultiSelectField(choices=CHOICE_23, verbose_name='23- ¿Qué harías si en tu presencia una mujer es víctima de violencia?')
    pregunta24 = MultiSelectField(choices=CHOICE_24, verbose_name='24- ¿Qué hacer para que los jóvenes no caigan en el problema de narcotráfico?')
   
    class Meta:
        verbose_name_plural = 'III-Prácticas sobre el tema de violencia y abuso de drogas'

#IV- Percepción sobre el tema de violencia y abuso de drogas

CHOICE_25 = (('a', 'Niñas, niños'),
                    ('b', 'Jóvenes (mujeres y hombres)'),
                    ('c', 'Mujeres'),
                    ('d', 'La familia'),
                    ('e', 'La persona violenta'),
                    ('f', 'La comunidad'),
                    ('g', 'El país'),
            )


CHOICE_26 = (('a', 'La familia'),
                    ('b', 'La Comunidad'),
                    ('c', 'El Estado'),
                    ('d', 'La Policía'),
                    ('e', 'Medios de Comunicación'),
                    ('f', 'Gobiernos Autónomos'),
                    ('g', 'Las Iglesias'),
                    ('h', 'ONGs'),
            )

CHOICE_27 = (('a', 'Familias pobres'),
                    ('b', 'Familias de clase media'),
                    ('c', 'Familias adineradas'),
                    ('d', 'Todas por igual'),
            )

CHOICE_28 = (('a', 'Educan a la población'),
                    ('b', 'Dan seguimiento a los casos'),
                    ('c', 'Revictimizan a las victimas'),
                    ('d', 'Brindan asistencia psicológica a la víctimas'),
                    ('e', 'No hacen nada'),
            )

CHOICE_29 = (('a', 'Porque no reciben tratamientos especializado'),
                    ('b', 'Faltan centros especializados'),
                    ('c', 'No reciben el apoyo de sus familias'),
                    ('d', 'Los marginans'),
                    ('e', 'La policía no actuá para apresarlos'),
                    ('f', 'Baja autoestima'),
            )

CHOICE_30 = (('a', 'Denunciar a las autoridades'),
                    ('b', 'Organizar promotores para la prevención'),
                    ('c', 'Campañas públicas abordando el tema'),
                    ('d', 'Campañas de información en escuelas'),
            )

CHOICE_32 = (('a', 'Educan a la población'),
                    ('b', 'Dan seguimiento a los casos'),
                    ('c', 'Revictimizan a las victimas'),
                    ('d', 'Brindan asistencia psicológica a la víctimas'),
                    ('e', 'No hacen nada'),
            )

CHOICE_34 = (('a', 'Varones adultos'),
                    ('b', 'Mujeres adultas'),
                    ('c', 'Varones jóvenes'),
                    ('d', 'Mujeres jóvenes'),
                    ('e', 'Varones adolescentes'),
                    ('f', 'Mujeres adolescentes'),
            )

CHOICE_35_37_38 = ((1, 'Si'),
                    (2, 'No'),
                    (3, 'No responde'),
            )

CHOICE_31_33_36 = ((1, 'Si'),
                    (2, 'No'),
                    (3, 'Es posible'),
                    (4, 'No responde'),
            )

class Percepcion(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    pregunta25 = MultiSelectField(choices=CHOICE_25, verbose_name='25-¿Quiénes son los más afectados por la violencia?')
    pregunta26 = MultiSelectField(choices=CHOICE_26, verbose_name='26- ¿Quiénes deben ser protagonistas de la prevención de la violencia juvenil y abuso de drogas?')
    pregunta27 = MultiSelectField(choices=CHOICE_27, verbose_name='27- ¿En que familias se da más frecuentemente el abuso sexual?')
    pregunta28 = MultiSelectField(choices=CHOICE_28, verbose_name='28- ¿Qué piensa del rol de las autoridades en la prevención de la violencia juvenil y abuso de drogas?')
    pregunta29 = MultiSelectField(choices=CHOICE_29, verbose_name='29- ¿Por qué los jóvenes que consumen droga se vuelven adictos?')
    pregunta30 = MultiSelectField(choices=CHOICE_30, verbose_name='30- ¿Para usted que acciones se puede hacer desde la comunidad para la prevención de la violencia juvenil y abuso de drogas?')
    pregunta31 = models.IntegerField(choices=CHOICE_31_33_36, verbose_name='31- ¿Cree Usted que la población se organizara para prevenir la violencia y abuso de drogas se disminuiría?')
    pregunta32 = MultiSelectField(choices=CHOICE_32, verbose_name='32- ¿Qué piensa del rol de las autoridades en la prevención de la violencia juvenil y abuso de drogas?')
    pregunta33 = models.IntegerField(choices=CHOICE_31_33_36, verbose_name='33- ¿Consideras usted que los piropos constituyen una forma de violencia?')
    pregunta34 = MultiSelectField(choices=CHOICE_34, verbose_name='34- ¿Quiénes consideras que son más violentos?')
    pregunta35 = models.IntegerField(choices=CHOICE_35_37_38, verbose_name='35- ¿Cree usted que el narcotráfico es un problema?')
    pregunta36 = models.IntegerField(choices=CHOICE_31_33_36, verbose_name='36- ¿Cree usted que el narcotráfico ayuda a las comunidades?')
    pregunta37 = models.IntegerField(choices=CHOICE_35_37_38, verbose_name='37- ¿Crees que Nicaragua es un país seguro?')
    pregunta38 = models.IntegerField(choices=CHOICE_35_37_38, verbose_name='38- ¿Crees que tu comunidad/barrio es seguro (a)?')


    class Meta:
        verbose_name_plural = 'IV-Percepción sobre el tema de violencia y abuso de drogas'

#Estado actual sobre sobre el tema de violencia y abuso de drogas

CHOICE_40_41 = ((1, 'No es un problema'),
            (2, 'Es un problema'),
            (3, 'Es un problema grave'),
            )

CHOICE_42 = ((1, 'Si'),
            (2, 'No'),
            (3, 'No sabe'),
            )

class Acciones(models.Model):
    accion = models.CharField(max_length=250)

    def __unicode__(self):
        return self.accion

CHOICE_43 = ((1, 'Si'),
            (2, 'No'),
            )

class LugaresComunidad(models.Model):
    lugar = models.CharField(max_length=250)

    def __unicode__(self):
        return self.lugar

CHOICE_44 = (('a', 'Atención psicológica'),
            ('b', 'Atención Jurídica'),
            ('c', 'Atención médica'),
            ('d', 'Acompañamiento de los casos'),
            ('e', 'Desconoce'),
        )

CHOICE_45 = (('a', 'Viaja a otro municipio/comunidad'),
            ('b', 'Paga psicóloga o abogados particulares'),
            ('c', 'No hace nada'),
            ('d', 'No sabe'),
        )

class EstadoActual(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    pregunta40 = models.IntegerField(choices=CHOICE_40_41, verbose_name='40- ¿Usted considera que la violencia juvenil y abuso de drogas es un problema en su comunidad?')
    pregunta41 = models.IntegerField(choices=CHOICE_40_41, verbose_name='41- ¿Usted considera que la violencia juvenil y abuso de drogas es un problema del país?')
    pregunta42 = models.IntegerField(choices=CHOICE_42, verbose_name='42- ¿Sabe si la comunidad hace acciones comunitarias para la prevención de la violencia juvenil y abuso de drogas?')
    si_respuesta_42 = models.ManyToManyField(Acciones, blank=True, verbose_name='Si responde Si, favor mencione tipos de acción')
    pregunta43 = models.IntegerField(choices=CHOICE_43, verbose_name='43- ¿Sabe si hay lugares en esta comunidad que atienden a personas que vivieron la violencia juvenil y abuso de drogas?')
    si_respuesta_43 = models.ManyToManyField(LugaresComunidad, blank=True, verbose_name='Si responde SI favor mencione los lugares')
    pregunta44 = MultiSelectField(choices=CHOICE_44, verbose_name='44- ¿Usted sabe qué tipo de atención brindan en esos lugares?')
    pregunta45 = MultiSelectField(choices=CHOICE_45, verbose_name='45- ¿Si no hay ningún lugar en su comunidad donde se atiende a las personas víctimas violencia juvenil y abuso de drogas a dónde van para recibir atención?')


    class Meta:
        verbose_name_plural = 'V-Estado actual sobre sobre el tema de violencia y abuso de drogas'