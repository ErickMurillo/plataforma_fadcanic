from django.contrib import admin
from .models import Noticias

class NoticiasAdmin(admin.ModelAdmin):
	pass

# Register your models here.
admin.site.register(Noticias, NoticiasAdmin)