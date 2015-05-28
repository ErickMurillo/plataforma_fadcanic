from django.db import models

# Create your models here.

class Videos(models.Model):
	nombre = models.CharField(max_length=250)
	aprobacion = models.IntegerField(choices=CHOICE_APROBACION, default='1')
    idioma = models.IntegerField(choices=CHOICE_IDIOMA, default='1')

    user = models.ForeignKey(User)

	def __str__(self):
		return self.nombre

class Audios(models.Model):
	nombre = models.CharField(max_length=250)
	aprobacion = models.IntegerField(choices=CHOICE_APROBACION, default='1')
    idioma = models.IntegerField(choices=CHOICE_IDIOMA, default='1')

    user = models.ForeignKey(User)

	def __str__(self):
		return self.nombre

class Fotos(models.Model):
	nombre = models.CharField(max_length=250)
	aprobacion = models.IntegerField(choices=CHOICE_APROBACION, default='1')
    idioma = models.IntegerField(choices=CHOICE_IDIOMA, default='1')

    user = models.ForeignKey(User)

	def __str__(self):
		return self.nombre

#los Inlines de los videos, audios, fotos

class SubirVideos(models.Model):
	video = models.ForeignKey(Videos)
	titulo = models.CharField(max_length=250)
	video = models.URLField()

class SubirAudios(models.Model):
	audio = models.ForeignKey(Audios)
	titulo = models.CharField(max_length=250)
	audio = models.FileField()

class SubirFotos(models.Model):
	foto = models.ForeignKey(Fotos)
	titulo = models.CharField(max_length=250)
	foto = models.FileField()