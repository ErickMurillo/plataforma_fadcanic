# -*- coding: utf-8 -*-
from django.db import models
from actividades.lugar.models import Departamento, Municipio
from smart_selects.db_fields import ChainedForeignKey
from multiselectfield import MultiSelectField

# Create your models here.

class Encuestador(models.Model):
    nombre = models.CharField('Nombre del recolector', max_length=250)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name='Encuestadores'

#a- Datos de Recoleccion

class Encuesta(models.Model):
    fecha = models.DateField()
    encuestador = models.ForeignKey(Encuestador)

    year = models.IntegerField(editable=False)

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

class InformacionEntrevistado(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    edad = models.IntegerField()
    etnia = models.ForeignKey(Etnias)
    departamento = models.ForeignKey(Departamento)
    municipio = ChainedForeignKey(
                                Municipio,
                                chained_field="departamento", 
                                chained_model_field="departamento",
                                show_all=False, auto_choose=True,null=True, blank=True)
    residencia = models.IntegerField(choices=CHOICE_AREA)
    habita = models.IntegerField(choices=CHOICE_HABITA)


    def __unicode__(self):
        return self.etnia.nombre

    class Meta:
        verbose_name_plural = 'b-Información del Entrevistado'

#c- Nivel de escolaridad
CHOICE_ESCOLARIDAD = ((1,'No sabe leer'),(2,'Alfabeto'),
                      (3,'Primaria completa'),(4,'Primaria incompleta'),
                      (5,'Secundaria completa'),(6,'Secundaria incompleta'),
                      (7,'Técnico'),(8,'Universitario'))

CHOICE_CIVIL = ((1,'Soltero/Soltera'),(2,'Casado/casada'),
                      (3,'Unión de hecho estable'),(4,'Divorciado/divorciada'),
                      (5,'Viudo/viuda'))

CHOICE_SI_NO = ((1,'Si'),(2,'No'))

class Escolaridad(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    escolaridad = models.IntegerField(choices=CHOICE_ESCOLARIDAD)
    civil = models.IntegerField(choices=CHOICE_CIVIL)
    varones = models.IntegerField()
    mujeres = models.IntegerField()


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
        verbose_name_plural = 'participa o ha participado en alguna orga. que previene la violencia juvenil y abuso de drogas?'

CHOICE_RESPUESTA_SI = ((1, 'Promotor/Promotora'),
                       (2, 'Asistiendo a charlas que se brinda'),
                       (3, 'Apoyando a otras persona de la comunidad'),
                       (4, 'Organizando actividades'),
                       )
class RespuetaSi(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    respuesta = MultiSelectField(choices=CHOICE_RESPUESTA_SI)

    class Meta:
        verbose_name_plural = 'Indique en cuales tipos de organizaciones'

#I- Conocimiento sobre los temas de violencia y abuso de drogas
CHOICE_VIOLENCIA_1 = ((1, 'Actos violentos realizados por jóvenes'),
                    (2, 'Acción que afecta negativamente a otra persona'),
                    (3, 'Daños físicos (golpes, gritos)'),
                    (4, 'Daños psicológicos (descalificaciones, burlas, insultos)'),
                    (5, 'Todas las anteriores'),
                )

CHOICE_ABUSO_DROGA_2 = ((1, 'Problema de salud pública'),
                        (2, 'Uso de cualquier tipo de droga ilícita'),
                        (3, 'Consumo de droga'),
                        (4, 'No responde'),
                    )

CHOICE_TIPO_VIOLENCIA_3 = ((1, 'Violencia hacia las mujeres'),
                        (2, 'Violencia hacia personas con opciones sexual diferente'),
                        (3, 'Acoso sexual'),
                        (4, 'Abuso sexual'),
                        (5, 'Violencia en la escuela'),
                        (6, 'Aumento de expendio de drogas'),
                        (7, 'Aumento del consumo de drogas'),
                        (8, 'Pleito entre pandillas'),
                        (9, 'Aumento del grupos delictivos'),
                        (10, 'Conflictos étnicos'),
                    )

CHOICE_LUGARES_4 = ((1, 'En el hogar'),
                        (2, 'En la escuela (dentro y alrededor de ellas)'),
                        (3, 'En las calles o espacios abiertos'),
                        (4, 'En los centros de trabajo'),
                        (5, 'En instituciones manejadas por el Estado'),
                    )

CHOICE_JOVEN_VIOLENTO_5 = ((1, 'Nivel de pobreza en su familia'),
                        (2, 'Sufrió maltrato físico y psicológico en el hogar'),
                        (3, 'Falta de atención de su familia'),
                        (4, 'Experimentó con drogas'),
                        (5, 'Falta de acceso a la educación'),
                        (6, 'Participación en pandillas juveniles'),
                        (7, 'No responde'),
                    )

CHOICE_PERJUDICADOS_6 = ((1, 'La familia'),
                        (2, 'Las personas de la comunidad o barrio'),
                        (3, 'Las mujeres'),
                        (4, 'Los hombres'),
                        (5, 'Las y los jóvenes'),
                        (6, 'Niñas y niños'),
                        (7, 'La sociedad en general'),
                    )

CHOICE_SOLUCIONES_7 = ((1, 'Prisión para los que ejercen violencia'),
                        (2, 'Prisión para los expendedores de droga'),
                        (3, 'Prisión para los que consumen drogas'),
                        (4, 'Tomar la justicia por sus propias manos'),
                        (5, 'Buscar ayuda psicológica'),
                        (6, 'Brindar mayor nivel de información sobre el tema'),
                        (7, 'Acompañar procesos de capacitación sobre los temas'),
                        (8, 'Organizar a la comunidad y barrio'),
                        (9, 'Mayor nivel de organización de la población y las instituciones para prevenir delitos'),
                    )

CHOICE_RESPONSABLES_8 = ((1, 'La Policía'),
                        (2, 'Ministerio de Salud'),
                        (3, 'Ministerio de Educación/Escuelas'),
                        (4, 'Gobiernos municipales y locales'),
                        (5, 'La comunidad'),
                        (6, 'La familia'),
                        (7, 'Las Iglesias'),
                        (8, 'Organizaciones comunitarias'),
                        (9, 'Organizaciones sin fin de lucro (ONG)'),
                    )

CHOICE_FEMINICIDIO_9 = ((1, 'Es un delito'),
                        (2, 'Cuando el hombre asesina a una mujer'),
                        (3, 'No es un delito'),
                        (4, 'No sabe'),
                        (5, 'No responde'),
                    )

CHOICE_ABUSO_SEXUAL_10 = ((1, 'Actividad sexual entre dos o más personas sin consentimiento de una persona'),
                        (2, 'Acto sexual que se ejerce bajo presión'),
                        (3, 'Relación sexual entre dos personas'),
                        (4, 'No sabe'),
                        (5, 'No responde'),
                    )

CHOICE_LUGARES_11 = ((1, 'Casa'),
                    (2, 'Escuela (dentro o fuera)'),
                    (3, 'Calle'),
                    (4, 'Comunidades rurales')
                    (5, 'En la ciudad'),
                    (6, 'En la iglesia'),
                    (7, 'No sabe'),
                    (8, 'No responde'),
            )

CHOICE_PREVENIR_ABUSO_12 = ((1, 'Denunciar al agreso'),
                    (2, 'Apoyo moral y psicológico a la víctima'),
                    (3, 'Promover campañas de sensibilización contra el AS'),
                    (4, 'Mejor comunicación entre los miembros de la familia'),
                    (5, 'No sabe'),
                    (6, 'No responde'),
            )

CHOICE_SEGURIDAD_CIUDADA_13 = ((1, 'Derecho a vivir con paz'),
                    (2, 'Prevención de los delitos'),
                    (3, 'Derecho a vivir en un ambiente pacifico'),
                    (4, 'Erradicar la violencia de cualquier tipo'),
                    (5, 'Falta contra las personas y sus bienes'),
                    (6, 'No responde'),
                    (7, 'No sabe'),
            )


class Conocimiento(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    pregunta1 = models.IntegerField(choices=CHOICE_VIOLENCIA_1, verbose_name='1-¿Para Usted que es Violencia Juvenil?')
    pregunta2 = models.IntegerField(choices=CHOICE_ABUSO_DROGA_2, verbose_name='2-¿Qué es abuso de drogas para usted?')
    pregunta3 = models.IntegerField(choices=CHOICE_TIPO_VIOLENCIA_3, verbose_name='3-¿Qué tipo violencia afecta más a tu comunidad?')
    pregunta4 = models.IntegerField(choices=CHOICE_LUGARES_4, verbose_name='4-¿Qué lugares considera usted que genera más violencia?')
    pregunta5 = models.IntegerField(choices=CHOICE_JOVEN_VIOLENTO_5, verbose_name='5-¿Qué es lo que conlleva a un joven a ser violento y consuma drogas?')
    pregunta6 = models.IntegerField(choices=CHOICE_PERJUDICADOS_6, verbose_name='6-¿Quiénes son los más perjudicados por la violencia juvenil y abuso de drogas?')
    pregunta7 = models.IntegerField(choices=CHOICE_SOLUCIONES_7, verbose_name='7-¿Qué soluciones ve Usted para prevenir la violencia juvenil?')
    pregunta8 = models.IntegerField(choices=CHOICE_RESPONSABLES_8, verbose_name='8-¿Quiénes son los responsables de aportar a la prevención de la violencia juvenil?')
    pregunta9 = models.IntegerField(choices=CHOICE_FEMINICIDIO_9, verbose_name='9-¿Qué entiendes por feminicidio?')
    pregunta10 = models.IntegerField(choices=CHOICE_ABUSO_SEXUAL_10, verbose_name='10-¿Qué es el abuso sexual?')
    pregunta11 = models.IntegerField(choices=CHOICE_LUGARES_11, verbose_name='11-¿En qué lugares ocurren más el abuso sexual?')
    pregunta12 = models.IntegerField(choices=CHOICE_PREVENIR_ABUSO_12, verbose_name='12-¿Qué hacer para prevenir el abuso sexual?')
    pregunta13 = models.IntegerField(choices=CHOICE_SEGURIDAD_CIUDADA_13, verbose_name='13-¿Qué entiendes por seguridad ciudadana?')


    class Meta:
        verbose_name_plural = 'I-Conocimiento sobre los temas de violencia y abuso de drogas'

#II- Actitud sobre los temas de violencia y abuso de drogas. Favor marcar X donde corresponda.

CHOICE_VALORA_14 = ((1, 'Alta'),
                    (2, 'Media'),
                    (3, 'Baja'),
                    (4, 'No responde'),
                    (5, 'No sabe'),
            )

CHOICE_PERSONAS_15 = ((1, 'Son enfermos'),
                    (2, 'Criminales/delincuentes'),
                    (3, 'Personas que se equivocan'),
                    (4, 'No cuentan con la educación suficiente'),
                    (5, 'Fueron víctimas de violencia'),
                    (6, 'Personas violentas de acuerdo a su Etnia'),
                    (7, 'No responde'),
                    (8, 'No sabe'),
            )

CHOICE_16 = ((1, 'Hay que brindarles ayuda'),
                    (2, 'Es pasajero, no lo necesita'),
                    (3, 'El/ella se lo busco'),
                    (4, 'No responde'),
                    (5, 'No sabe'),
            )

CHOICE_17 = ((1, 'Mayor orientación de la familia'),
                    (2, 'Organizando a la comunidad'),
                    (3, 'Mayores niveles de información'),
                    (4, 'Acceso a la educación'),
                    (5, 'Generando oportunidades de empleo'),
                    (6, 'No responde'),
                    (7, 'No sabe'),
            )

CHOICE_18 = ((1, 'Falta de información'),
                    (2, 'Maltrato físico en el seno familiar'),
                    (3, 'Carencia afectiva de la familia'),
                    (4, 'Desintegración de la familia'),
                    (5, 'Por el grupo étnico al que pertenece'),
                    (6, 'Viene en la sangre (genes)'),
                    (7, 'No sabe'),
            )

CHOICE_19 = ((1, 'Masoquismo'),
                    (2, 'Porque le ama y cree que puede cambiar'),
                    (3, 'No cuenta con apoyo para mantenerse'),
                    (4, 'No recibió apoyo de las instituciones'),
                    (5, 'No responde'),
                    (6, 'No sabe'),
            )

CHOICE_20 = ((1, 'Falta de educación'),
                    (2, 'Falta de información'),
                    (3, 'La no protección de los padres a sus hijos/hijas'),
                    (4, 'Falta de vigilancia policial en la ciudad'),
                    (5, 'La comunidad sabe pero no denuncia'),
                    (6, 'Por abuso de droga y alcohol'),
                    (5, 'No responde'),
                    (6, 'No sabe'),
            )










