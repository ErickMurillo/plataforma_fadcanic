from django.contrib import admin
from .models import Noticias

class NoticiasAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'fecha', 'aprobacion', 'idioma', 'user')
	list_filter = ('idioma', 'user', 'aprobacion')
	search_fields = ('titulo',)
# Register your models here.
admin.site.register(Noticias, NoticiasAdmin)