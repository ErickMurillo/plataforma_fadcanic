from django.contrib import admin
from django import forms
from .models import Historias
from django.contrib.flatpages.models import FlatPage
# Note: we are renaming the original Admin and Form as we import them!
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.forms import FlatpageForm as FlatpageFormOld

from ckeditor.widgets import CKEditorWidget
 
class FlatpageForm(FlatpageFormOld):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = FlatPage # this is not automatically inherited from FlatpageFormOld
        fields = '__all__'
 
 
class FlatPageAdmin(FlatPageAdminOld):
    form = FlatpageForm
 
class HistoriasAdmin(admin.ModelAdmin):
	def queryset(self, request):
		if request.user.is_superuser:
			return Historias.objects.all()
		return Historias.objects.filter(user=request.user)

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		obj.save()

	exclude = ('user',)
	list_display = ('titulo', 'fecha', 'aprobacion', 'idioma', 'user')
	list_filter = ('idioma', 'user', 'aprobacion')
	search_fields = ('titulo',)

# Register your models here.
#admin.site.register(Historias, HistoriasAdmin)
# We have to unregister the normal admin, and then reregister ours
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)