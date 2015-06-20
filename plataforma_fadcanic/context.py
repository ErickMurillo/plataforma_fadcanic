# -*- coding: utf-8 -*-

from cambiaahora.configuracion.models import LogoApoyan

def globales(request):
    logos = LogoApoyan.objects.all()
   
    return {'logos':logos}