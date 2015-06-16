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
#los inlines
admin.site.register(SubirVideos)
admin.site.register(SubirAudios)
admin.site.register(SubirFotos)
admin.site.register(SubirDocumentales)