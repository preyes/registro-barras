from barras.models import Codigo
from barras.forms import CodigoForm, ReportForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from django.core.context_processors import csrf
from django.db.models import Q, Avg, Count, Max, Sum

def index(request):

    return render_to_response('index.html', context_instance = RequestContext(request))
 

def guardar_codigo(request):
  #  a = Dato()
    info_guardada = False
    num = 0
    
    if request.method == 'POST':
        formulario = CodigoForm(request.POST)
        
        if formulario.is_valid():
            
            info_guardada = True  # Define si se guardo el codigo. 
                 
            data = formulario.cleaned_data            
            form = formulario.save(commit=False)
            
            quincena = int(formulario.cleaned_data['quincena'])
            form.seccional = form.numero[6:13]
            form.boleta = form.numero[13:20]
            form.monto = form.numero[20:25]
               
            formulario.save()
            
           
            var = {'formulario':formulario, 'info':info_guardada, 'seccional':form.seccional, 
                    'boleta':form.boleta, 'monto':form.monto,'quincena':quincena
                    }
                    
            return render_to_response('lector.html', var, context_instance = RequestContext(request))
            
    else:
        formulario = CodigoForm()
    
    #variable = {'formulario':formulario, 'info':info_guardada}  
            
    return render_to_response('lector.html',{'formulario':formulario, 'info':info_guardada,}, context_instance = RequestContext(request))
    
    
def report_view(request):
     #   if request.method == 'POST':
      #      formulario = ReportForm(request.POST)
            
       #     if formulario is_valid()
        
        
        
         
        total = Codigo.objects.all()
        
        monto = []
        
        for i in total
            
        
        
       
        consulta = Codigo.objects.filter(seccional = '0001805').aggregate(contador_boleta=Count('numero'))

        
        consulta = Codigo.objects.annotate(contador_boleta=Count('monto')).values('seccional', 'contador_boleta')
        

        x = {'total':total, 'consulta':consulta}               
           
        return render_to_response('reporte.html', x, context_instance = RequestContext(request))


    
