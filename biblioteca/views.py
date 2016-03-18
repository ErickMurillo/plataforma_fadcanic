from django.shortcuts import render

# Create your views here.
def index(request,template='biblioteca/index.html',slug=None):
	return render(request, template, locals())
	
def bdetalle(request,template='biblioteca/detalle.html',slug=None):
	return render(request, template, locals())