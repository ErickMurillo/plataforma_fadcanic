from django.db import models
from sorl.thumbnail import ImageField
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

# Create your models here.

class Noticias(models.Model):
	titulo = models.CharField(max_length=250)
	fecha = models.DateField()
	foto = ImageField('Foto principal', upload_to=get_file_path, blank=True, null=True)
	url = models.URLField(blank=True, null=True)
	texto = RichTextField(blank=True, null=True)
	