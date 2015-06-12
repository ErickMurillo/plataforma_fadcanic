from django.contrib import admin
from .models import Videos, Audios, Fotos, Documentales, SubirVideos, SubirAudios, SubirFotos, SubirDocumentales

class InlineSubirVideos(admin.TabularInline):
	model = SubirVideos

class InlineSubirAudios(admin.TabularInline):
	model = SubirAudios

class InlineSubirFotos(admin.TabularInline):
	model = SubirFotos

class InlineSubirDocumentos(admin.TabularInline):
	model = SubirDocumentales

class VideosAdmin(admin.ModelAdmin):
	inlines = [InlineSubirVideos]

class AudiosAdmin(admin.ModelAdmin):
	inlines = [InlineSubirAudios]

class FotosAdmin(admin.ModelAdmin):
	inlines = [InlineSubirFotos]

class DocumentosAdmin(admin.ModelAdmin):
	inlines = [InlineSubirDocumentos]

# Register your models here.
admin.site.register(Videos, VideosAdmin)
admin.site.register(Audios, AudiosAdmin)
admin.site.register(Fotos, FotosAdmin)
admin.site.register(Documentales, DocumentosAdmin)