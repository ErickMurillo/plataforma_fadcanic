from django.contrib import admin
from .models import Configuracion, LogoApoyan, Informacion
# Register your models here.

class ConfigAdmin(admin.ModelAdmin):
	def queryset(self, request):
		if request.user.is_superuser:
			return Configuracion.objects.all()
		return Configuracion.objects.filter(user=request.user)

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		obj.save()

	exclude = ('user',)

class LogoApoyanAdmin(admin.ModelAdmin):
	def queryset(self, request):
		if request.user.is_superuser:
			return LogoApoyan.objects.all()
		return LogoApoyan.objects.filter(user=request.user)

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		obj.save()

	exclude = ('user',)

class InformacionAdmin(admin.ModelAdmin):
	def queryset(self, request):
		if request.user.is_superuser:
			return Informacion.objects.all()
		return Informacion.objects.filter(user=request.user)

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		obj.save()

	exclude = ('user',)

admin.site.register(Configuracion, ConfigAdmin)
admin.site.register(LogoApoyan, LogoApoyanAdmin)
admin.site.register(Informacion, InformacionAdmin)