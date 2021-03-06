# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect, HttpResponseForbidden
from actividades.contraparte.views import checkParams
from actividades.forms import *
from django.contrib.auth.decorators import login_required

#@login_required
def filtro_programa(request):
    if not request.user.has_perm('fadcanic.view_programa'):
        error = '''<h1>Acceso restringido. Redirigiendo en 3 segundos.</h1>
        <script>setTimeout("window.location='/actividades/'",3000)</script>'''
        return HttpResponseForbidden(error)
    
    params = {}
    filtro = {}
    if request.method == 'POST':
        form = ProgramaForm(request.POST)
        if form.is_valid():
            params['organizacion__id__in'] = form.cleaned_data['organizaciones'].values_list('id', flat=True)
            try:            
                params['proyecto__id__in'] = form.cleaned_data['proyectos'].values_list('id', flat=True)
            except:
                params['proyecto__id__in'] = None

            # adding all results option
            result_foo = form.cleaned_data.get('resultado', None)
            if result_foo:
                params['resultado__aporta_a__id'] = result_foo.id

            params['fecha__range'] = (form.cleaned_data['fecha_inicio'], form.cleaned_data['fecha_fin'])
            
            #guardando los filtros seleccionados para pintarlos en plantilla
            filtro['organizacion'] = form.cleaned_data['organizaciones']
            filtro['proyecto'] = form.cleaned_data['proyectos']
            filtro['fecha_inicio'] = form.cleaned_data['fecha_inicio']
            filtro['fecha_fin'] = form.cleaned_data['fecha_fin']
            filtro['salida'] = 'Por programa'

            filtro['resultado'] = result_foo.nombre_corto if result_foo else 'Todos los resultados'
            
            params = checkParams(params)
            request.session['filtro'] = filtro
            request.session['params'] = params             
            
            return HttpResponseRedirect('/actividades/variables/')            
    else:
        form = ProgramaForm()
    return render_to_response('actividades/filtro_programa.html', RequestContext(request, locals()))