from django.shortcuts import render
from .models import Temas, Biblioteca
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request,template='biblioteca/index.html',slug=None):
	temas = Temas.objects.all()
	ultimas_guias = Biblioteca.objects.all().order_by('-fecha')[:6]

	return render(request, template, locals())

def buscar(request, template='biblioteca/index.html'):

	return render(request, template, locals())

def detalle_guia(request,template='biblioteca/detalle.html',slug=None):
	temas = Temas.objects.all()
	la_guia = get_object_or_404(Biblioteca, slug=slug)

	return render(request, template, locals())
