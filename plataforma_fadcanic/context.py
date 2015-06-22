# -*- coding: utf-8 -*-

from cambiaahora.configuracion.models import LogoApoyan
from cambiaahora.staff.models import Staff

def globales(request):
    logos = LogoApoyan.objects.all()
    equipo = Staff.objects.all()
   
    return {'logos':logos, 'equipo':equipo}