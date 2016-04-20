from django.shortcuts import render
from .models import Temas, Biblioteca
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.
def index(request,template='biblioteca/index.html',slug=None):
	temas = Temas.objects.all()
	ultimas_guias = Biblioteca.objects.all().order_by('-fecha')[:6]

	return render(request, template, locals())

def buscar_guia(request, template='biblioteca/lista_guias.html'):

	buscar_palabra = request.GET.get('q')

	resultado = Biblioteca.objects.filter(Q(titulo__icontains=buscar_palabra) | Q(descripcion__icontains=buscar_palabra))

	return render(request, template, locals())

def buscar_tema(request, template='biblioteca/lista_guias.html', id=None):

	temas = Temas.objects.all()
	buscar_palabra = get_object_or_404(Temas,id=id)

	resultado = Biblioteca.objects.filter(tema=buscar_palabra)

	return render(request, template, locals())

def detalle_guia(request,template='biblioteca/detalle.html',slug=None):
	temas = Temas.objects.all()
	la_guia = get_object_or_404(Biblioteca, slug=slug)

	return render(request, template, locals())
