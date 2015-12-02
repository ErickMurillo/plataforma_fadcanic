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
		verbose_name = 'Encuestador'
		verbose_name_plural = 'Encuestadores'

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
	latitud = models.FloatField(editable=False,null=True,blank=True)
	longitud = models.FloatField(editable=False,null=True,blank=True)
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
		return u'%s' % (str(self.get_escolaridad_display()))

	class Meta:
		verbose_name_plural = 'Nivel de escolaridad'

#f- Favor indicar
class ParticipaOrganizacion(models.Model):
	encuesta = models.ForeignKey(Encuesta)
	participado = models.IntegerField(choices=CHOICE_SI_NO)

	# def __unicode__(self):
	# 	return u'%s' % (str(self.get_participado_display))

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

CHOICE_15 = (('a', 'Son enfermos'),
					('b', 'Personas que necesitan apoyo de su familia y la sociedad'),
					('c', 'No cuentan con la educación suficiente'),
					('d', 'Fueron víctimas de violencia'),
					('e', 'Deben estar aislados de los demás '),
					('f', 'NS/NR'),
			)

CHOICE_16 = (('a', 'Criminales/delincuentes'),
					('b', 'Es rebeldía luego se le pasará'),
					('c', 'Ojo por ojo contra ellos'),
					('d', 'Necesitan más apoyo de su familia y la sociedad'),
					('e', 'Darles apoyo con empleo y educación'),
					('f','NS/NR'),
			)

CHOICE_17 = (('a', 'Mayor orientación de la familia'),
					('b', 'Organizando a la comunidad'),
					('c', 'Más empleo y educación'),
					('d', 'Más terapias y consejos con las familias y los jóvenes'),
					('e', 'Disminuir la violencia presentada en los medios de comunicación'),
					('f', 'Hacer más centros de rehabilitación'),
					('g', 'NS/NR'),
			)

CHOICE_18 = (('a', 'Se criaron en la calle'),
					('b', 'Sus madres y padres no les inculcaron buenos valores'),
					('c', 'Carencia de afecto en la familia'),
					('d', 'Fueron niños que vivieron violencia en sus casas'),
					('e', 'Por el grupo étnico al que pertenece'),
					('f', 'Viene en la sangre (genes)'),
					('g', 'NS/NR'),
			)

CHOICE_19 = (('a', 'Masoquismo'),
					('b', 'Tiene dependencia emocional hacia él'),
					('c', 'Porque lo ama y cree que puede cambiar'),
					('d', 'No cuenta con apoyo para mantenerse económicamente '),
					('e', 'No recibió apoyo de las instituciones'),
					('f', 'La gente le aconseja que lo perdone'),
					('g', 'Está en el ciclo de la violencia'),
					('h', 'NS/NR'),
			)

CHOICE_20 = (('a', 'Falta de información de madres, padres o tutores'),
					('b', 'Las madres, padres o tutores no protegen ni informan a sus hijos/hijas'),
					('c', 'Falta de vigilancia policial en la ciudad'),
					('d', 'La comunidad sabe, pero no denuncia'),
					('e', 'Por consumo de droga y alcohol'),
					('f', 'Los niños y niñas no se saben cuidar'),
					('g', 'Por el machismo y abuso de poder de los hombres'),
					('h', 'Por el machismo y abuso de poder de las mujeres'),
					('i', 'NS/NR'),
			)

class Actitud(models.Model):
	encuesta = models.ForeignKey(Encuesta)
	#pregunta14 = MultiSelectField(choices=CHOICE_VALORA_14, verbose_name='14 -¿Cómo valora la situación de la violencia juvenil y abuso de drogas en su localidad?')
	pregunta15 = MultiSelectField(choices=CHOICE_15, verbose_name='14-¿Qué piensa de las personas consumidoras de droga?')
	pregunta16 = MultiSelectField(choices=CHOICE_16, verbose_name='16-¿Qué piensa de los jóvenes violentos?')
	pregunta17 = MultiSelectField(choices=CHOICE_17, verbose_name='17-¿Cómo prevenir la violencia juvenil y el abuso de drogas?')
	pregunta18 = MultiSelectField(choices=CHOICE_18, verbose_name='18-¿Cuáles son las principales causas de la violencia juvenil?')
	pregunta19 = MultiSelectField(choices=CHOICE_19, verbose_name='19-¿Por qué muchas mujeres después vivir violencia, perdonan a sus parejas o abusadores?')
	pregunta20 = MultiSelectField(choices=CHOICE_20, verbose_name='20-¿Cuáles crees son las causas de abuso sexual?')
   
	class Meta:
		verbose_name_plural = 'II-Actitud sobre los temas de violencia y abuso de drogas'

#III- Prácticas sobre el tema de violencia y abuso de drogas

CHOICE_21 = (('a', 'La defiendo, ejerciendo la fuerza'),
					('b', 'No hago nada'),
					('c', 'Hago denuncia a las autoridades'),
					('d', 'Lo denuncio con un familiar de la víctima'),
					('e', 'NS/NR'),
			)

CHOICE_22 = (('a', 'Participo de actividades de prevención en mi lugar'),
					('b', 'Evito discusión o acciones que generen violencia'),
					('c', 'Doy más cariño y menos golpes a las jóvenes'),
					('d', 'Estoy organizada/o en mi comunidad'),
					('e', 'No hago nada'),
					('f', 'No sé que hacer'),
			)


CHOICE_23 = (('a', 'La defendería'),
					('b', 'Poner denuncia ante la Policía'),
					('c', 'No hago nada'),
					('d', 'Llamo a los medios de comunicación '),
					('e', 'La aconsejaría después'),
					('f', 'NS/NR'),
			)

CHOICE_24 = (('a', 'Mayor vigilancia policial'),
					('b', 'Generar oportunidades de empleo'),
					('c', 'Mayor acceso a la educación'),
					('d', 'Un sistema de justicia más beligerante'),
					('e', 'Mayor unión familiar'),
					('f', 'Mayor organización de la comunidad'),
					('g', 'NS/NR'),
			)

class Practicas(models.Model):
	encuesta = models.ForeignKey(Encuesta)
	pregunta21 = MultiSelectField(choices=CHOICE_21, verbose_name='21-¿Qué harías si en tu presencia alguien es víctima de violencia juvenil?')
	pregunta22 = MultiSelectField(choices=CHOICE_22, verbose_name='22-Qué hace usted para prevenir la violencia juvenil y abuso de droga?')
	pregunta23 = MultiSelectField(choices=CHOICE_23, verbose_name='23-¿Qué haría si ve que una mujer está siendo violentada?')
	pregunta24 = MultiSelectField(choices=CHOICE_24, verbose_name='24-¿Qué hacer para que los jóvenes no se conviertan en expendedores de droga?')
   
	class Meta:
		verbose_name_plural = 'III-Prácticas sobre el tema de violencia y abuso de drogas'

#IV- Percepción sobre el tema de violencia y abuso de drogas

CHOICE_25 = (('a', 'Familias pobres'),
					('b', 'Familias de clase media'),
					('c', 'Familias adineradas'),
					('d', 'Donde no escuchan a las niñas y niños'),
					('e', 'Donde no se interesan por el bienestar de las niñas y niños'),
					('f', 'Todas por igual'),
					('g', 'NS/NR'),
			)


CHOICE_26 = (('a', 'Educan a la población'),
					('b', 'Dan seguimiento a los casos'),
					('c', 'Revictimizan'),
					('d', 'Brindan asistencia psicológica a la víctimas'),
					('e', 'No hacen nada'),
					('f', 'Hacen muy poco'),
					('g', 'NS/NR'),
			)

CHOICE_27 = (('a', 'Porque no reciben tratamientos especializado'),
					('b', 'Faltan centros especializados'),
					('c', 'No reciben el apoyo de sus familias'),
					('d', 'Los marginan'),
					('e', 'La Policía no actúa para apresarlos'),
					('f', 'Baja autoestima'),
					('g', 'NS/NR'),
			)

CHOICE_28 = (('a', 'Denunciar ante las autoridades'),
					('b', 'Organizar promotores para la prevención'),
					('c', 'Campañas públicas abordando el tema'),
					('d', 'Campañas de información en escuelas'),
					('e', 'NS/NR'),
			)

CHOICE_29 = ((1, 'Si'),
					(2, 'No'),
					(3, 'Es posible'),
					(4, 'NS/NR'),
			)

CHOICE_30 = (('a', 'Hombres adultos'),
					('b', 'Mujeres adultas'),
					('c', 'Hombres jóvenes'),
					('d', 'Mujeres jóvenes'),
					('e', 'Hombres adolescentes'),
					('f', 'Mujeres adolescentes'),
					('g', 'NS/NR'),
			)

CHOICE_31 = (('a', 'Ayuda a la economía de la comunidad'),
					('b', 'Daña a la juventud'),
					('c', 'Genera más violencia'),
					('d', 'NS/NR'),
			)

CHOICE_32_33 = ((1, 'Si'),
					(2, 'No'),
					(3, 'Relativamente sí'),
					(4, 'NS/NR'),
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
	pregunta25 = MultiSelectField(choices=CHOICE_25, verbose_name='25-¿En que familias se da más frecuentemente el abuso sexual?')
	pregunta26 = MultiSelectField(choices=CHOICE_26, verbose_name='26-¿Qué piensa del rol de las autoridades en la prevención de la violencia juvenil y abuso de drogas?')
	pregunta27 = MultiSelectField(choices=CHOICE_27, verbose_name='27-¿Qué lleva a un joven a consumir drogas?')
	pregunta28 = MultiSelectField(choices=CHOICE_28, verbose_name='28-¿Qué acciones hacer desde la comunidad para la prevención de la violencia juvenil y el abuso de drogas?')
	#pregunta29 = models.IntegerField(choices=CHOICE_29, verbose_name='29-¿Para usted el piropo es una forma de violencia?')
	pregunta29_1 = models.IntegerField(choices=CHOICE_29, verbose_name='29-¿Para usted el piropo es una forma de violencia?')
	pregunta30 = MultiSelectField(choices=CHOICE_30, verbose_name='30-¿Quiénes considera que son más violentos?')
	pregunta31 = MultiSelectField(choices=CHOICE_31, verbose_name='31-¿Qué opina del narcotráfico?')
	#pregunta32 = models.IntegerField(choices=CHOICE_32_33, verbose_name='32-¿Cree que Nicaragua es un país seguro?')
	pregunta32_1 = models.IntegerField(choices=CHOICE_32_33, verbose_name='32-¿Cree que Nicaragua es un país seguro?')
	pregunta33 = models.IntegerField(choices=CHOICE_32_33, verbose_name='33-¿Cree que tu comunidad es segura?')
	# pregunta34 = MultiSelectField(choices=CHOICE_34, verbose_name='34- ¿Quiénes consideras que son más violentos?')
	# pregunta35 = models.IntegerField(choices=CHOICE_35_37_38, verbose_name='35- ¿Cree usted que el narcotráfico es un problema?')
	# pregunta36 = models.IntegerField(choices=CHOICE_31_33_36, verbose_name='36- ¿Cree usted que el narcotráfico ayuda a las comunidades?')
	# pregunta37 = models.IntegerField(choices=CHOICE_35_37_38, verbose_name='37- ¿Crees que Nicaragua es un país seguro?')
	# pregunta38 = models.IntegerField(choices=CHOICE_35_37_38, verbose_name='38- ¿Crees que tu comunidad/barrio es seguro (a)?')


	class Meta:
		verbose_name_plural = 'IV-Percepción sobre el tema de violencia y abuso de drogas'

#Estado actual sobre sobre el tema de violencia y abuso de drogas

class Acciones(models.Model):
	accion = models.CharField(max_length=250)

	def __unicode__(self):
		return self.accion


# class LugaresComunidad(models.Model):
#     lugar = models.CharField(max_length=250)

#     def __unicode__(self):
#         return self.lugar
#-----------------------------------------------
CHOICE_34_SI = (('a', 'CineForo/videoForo'),
			('b', 'Marchas municipales'),
			('c', 'Debates escolares'),
			('d', 'Talleres de reflexión'),
		)

CHOICE_35_SI = (('a', 'Centros de Salud'),
			('b', 'Ministerio Público'),
			('c', 'Policía'),
			('d', 'MiFamilia'),
			('e', 'Comisaría de La Mujer'),
			('f', 'Bufete Jurídico'),
			('g', 'Casa Comunal'),
			('h', 'ONG'),
		)

CHOICE_36 = (('a', 'Viaja a otro municipio/comunidad'),
			('b', 'Paga psicóloga o abogados particulares'),
			('c', 'No hace nada'),
			('d', 'NS/NR'),
		)

CHOICE_37 = ((1, 'Si'),
			(2, 'No'),
			(3, 'NS/NR'),
		)

CHOICE_38 = (('a', 'Prevención de violencia'),
			('b', 'Prevención de consumo de drogas'),
			('c', 'Contra la violencia hacia las mujeres'),
			('d', 'Diversión y deporte en la juventud'),
			('e', 'Medio ambiente'),
			('f', 'NS/NR'),
		)

CHOICE_39 = (('a', 'Historias de radio'),
			('b', 'Historias en la televisión (documentales)'),
			('c', 'Cuaderno informativo'),
			('d', 'Actividades en los colegios'),
			('e', 'Video foros en los barrios'),
			('f', 'NS/NR'),
		)

class EstadoActual(models.Model):
	encuesta = models.ForeignKey(Encuesta)
	pregunta34 = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='34-¿Ha participado en acciones comunitarias para prevenir la violencia juvenil y el abuso de drogas?')
	si_respuesta_34 = MultiSelectField(choices=CHOICE_34_SI, verbose_name='Si responde Si, mencione tipos de acción',blank=True,null=True)
	pregunta35 = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='35- ¿Existen lugares en tu comunidad para atender a personas que vivieron la violencia juvenil y el abuso de drogas?')
	si_respuesta_35 = MultiSelectField(choices=CHOICE_35_SI, blank=True,null=True, verbose_name='Si responde SI, mencione los lugares')
	pregunta36 = MultiSelectField(choices=CHOICE_36, verbose_name='36-Si no hay lugares en la comunidad, ¿dónde se atienden las víctimas?')
	pregunta37 = models.IntegerField(choices=CHOICE_37, verbose_name='37-¿Ha escuchado de la Campaña: Cambia ahora solo hazlo?')
	pregunta38 = MultiSelectField(choices=CHOICE_38, verbose_name='38-¿De qué temas trata la campaña?')
	pregunta39 = MultiSelectField(choices=CHOICE_39, verbose_name='39-¿Qué producto ha visto de la Campaña?')


	class Meta:
		verbose_name_plural = 'V-Estado actual sobre sobre el tema de violencia y abuso de drogas'