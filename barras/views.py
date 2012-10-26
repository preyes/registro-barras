from barras.models import Codigo #, Dato
from forms import CodigoForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from django.core.context_processors import csrf


def guardar_codigo(request):
  #  a = Dato()
    info_guardada = False
    num = 0
    
    if request.method == 'POST':
        formulario = CodigoForm(request.POST)
        
        if formulario.is_valid():
            num = num + 1
            info_guardada = True  # Define si se guardo el codigo. 
                 
            data = formulario.cleaned_data
            form = formulario.save(commit=False)
            
            quincena = int(formulario.cleaned_data['quincena'])
            seccional = form.numero[0:10]
            boleta = form.numero[10:20]
            monto = form.numero[20:26]
            
            formulario.save()
            
            
            var = {'formulario':formulario, 'info':info_guardada, 'seccional':seccional, 'boleta':boleta, 'monto':monto,'quincena':quincena, 'num':num}
            return render_to_response('lector.html', var, context_instance = RequestContext(request))
            
    else:
        formulario = CodigoForm()
    
    #variable = {'formulario':formulario, 'info':info_guardada}  
            
    return render_to_response('lector.html',{'formulario':formulario, 'info':info_guardada,}, context_instance = RequestContext(request))
    
    
    

    
