from django.contrib import admin
from .models import Noticias, Categoria
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

class NoticiasAdmin(admin.ModelAdmin):

    def queryset(self, request):
        if request.user.is_superuser:
            return Noticias.objects.all()
        return Noticias.objects.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        subject, from_email, to = 'Nueva Noticia de Cambia ahora', 'crocha09.09@gmail.com', 'crocha09.09@gmail.com'
        text_content = str(obj.texto)
        html_content = str(obj.texto)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        obj.save()

    # exclude = ('user',)
    list_display = ('titulo', 'fecha', 'aprobacion', 'idioma', 'user')
    list_filter = ('idioma', 'user', 'aprobacion')
    search_fields = ('titulo',)
# Register your models here.
admin.site.register(Noticias, NoticiasAdmin)
admin.site.register(Categoria)
