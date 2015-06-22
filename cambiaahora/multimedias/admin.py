from django.contrib import admin
from .models import Videos, Audios, Fotos, Documentales, SubirVideos, SubirAudios, SubirFotos, SubirDocumentales

class InlineSubirVideos(admin.TabularInline):
	model = SubirVideos
	extra = 1

class InlineSubirAudios(admin.TabularInline):
	model = SubirAudios
	extra = 1

class InlineSubirFotos(admin.TabularInline):
	model = SubirFotos
	extra = 1

class InlineSubirDocumentos(admin.TabularInline):
	model = SubirDocumentales
	extra = 1

class VideosAdmin(admin.ModelAdmin):
	def queryset(self, request):
		if request.user.is_superuser:
			return Videos.objects.all()
		return Videos.objects.filter(user=request.user)

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		obj.save()

	exclude = ('user',)
	inlines = [InlineSubirVideos]

class AudiosAdmin(admin.ModelAdmin):
	def queryset(self, request):
		if request.user.is_superuser:
			return Audios.objects.all()
		return Audios.objects.filter(user=request.user)

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		obj.save()

	exclude = ('user',)
	inlines = [InlineSubirAudios]

class FotosAdmin(admin.ModelAdmin):
	def queryset(self, request):
		if request.user.is_superuser:
			return Fotos.objects.all()
		return Fotos.objects.filter(user=request.user)

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		obj.save()

	exclude = ('user',)
	inlines = [InlineSubirFotos]

class DocumentosAdmin(admin.ModelAdmin):
	def queryset(self, request):
		if request.user.is_superuser:
			return Documentales.objects.all()
		return Documentales.objects.filter(user=request.user)

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		obj.save()

	exclude = ('user',)
	inlines = [InlineSubirDocumentos]

# Register your models here.
admin.site.register(Videos, VideosAdmin)
admin.site.register(Audios, AudiosAdmin)
admin.site.register(Fotos, FotosAdmin)
admin.site.register(Documentales, DocumentosAdmin)
#los inlines
admin.site.register(SubirVideos)
admin.site.register(SubirAudios)
admin.site.register(SubirFotos)
admin.site.register(SubirDocumentales)