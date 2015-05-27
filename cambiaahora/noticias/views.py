from django.shortcuts import render

# Create your views here.

def index(request, template="cambiaahora/index.html"):
	return render(request, template, locals())