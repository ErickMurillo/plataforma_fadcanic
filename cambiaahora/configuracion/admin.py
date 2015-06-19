from django.contrib import admin
from .models import Configuracion
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

admin.site.register(Configuracion, ConfigAdmin)