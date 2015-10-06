from django.contrib import admin
from .models import Noticias, Categoria, NoticiasAudios
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from cambiaahora.utils import *

class InlineNoticiasAudios(admin.TabularInline):
    model = NoticiasAudios
    extra = 1

class NoticiasAdmin(admin.ModelAdmin):

    def queryset(self, request):
        if request.user.is_superuser:
            return Noticias.objects.all()
        return Noticias.objects.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        #guarda todos los objectos   
        obj.save()
        #envio de correo
        if not obj.user.is_superuser:
            try:
                subject, from_email, to = 'Nueva Noticia de Cambia ahora', 'noreply@cambiaahora.com', arreglo_mail
                text_content = "Una nueva noticia ha sido enviada, del usuario " + \
                                str(obj.user) + ', ' + \
                                ' Si decia revisarla dar clic al siguiente enlace' + \
                                ' http://www.cambiaahora.com/noticias/noticias/' + str(obj.id)
                html_content = "Una nueva noticia ha sido enviada, del usuario " + \
                                str(obj.user) + ', ' + \
                                ' Si decia revisarla dar clic al siguiente enlace' + \
                                ' http://www.cambiaahora.com/admin/noticias/noticias/' + str(obj.id)
                msg = EmailMultiAlternatives(subject, text_content, from_email, arreglo_mail)
                msg.attach_alternative(html_content, "text/html")
                msg.send()
            except:
                pass


    def get_form(self, request, obj=None, **kwargs): 
        if request.user.is_superuser: 
            self.exclude = () 
        else: 
            self.exclude = ('aprobacion',) 
        return super(NoticiasAdmin, self).get_form(request, obj=None, **kwargs)

    # exclude = ('user',)
    inlines = [InlineNoticiasAudios]
    list_display = ('titulo', 'fecha', 'aprobacion', 'idioma', 'user')
    list_filter = ('idioma', 'user', 'aprobacion')
    search_fields = ('titulo',)

# Register your models here.
admin.site.register(Noticias, NoticiasAdmin)
admin.site.register(Categoria)
