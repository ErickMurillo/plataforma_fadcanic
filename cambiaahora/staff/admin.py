from django.contrib import admin
from .models import Staff

class StaffAdmin(admin.ModelAdmin):
	def queryset(self, request):
		if request.user.is_superuser:
			return Staff.objects.all()
		return Staff.objects.filter(user=request.user)

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		obj.save()

	exclude = ('user',)
	list_display = ('titulo', 'profesion', 'cargo', 'fecha', 'idioma')
	list_filter = ('idioma', 'user', 'aprobacion')
	search_fields = ('titulo',)
# Register your models here.
admin.site.register(Staff, StaffAdmin)