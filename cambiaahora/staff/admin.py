from django.contrib import admin
from .models import Staff

class StaffAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'profesion', 'cargo', 'fecha', 'idioma')
	list_filter = ('idioma', 'user', 'aprobacion')
	search_fields = ('titulo',)
# Register your models here.
admin.site.register(Staff, StaffAdmin)