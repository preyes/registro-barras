# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django import forms
from barras.models import Codigo, Operador
from django.contrib.admin import widgets




MY_CHOICES = (
    ('None', '---Seleccione una quincena---'),
    ('1', 'Quincena 1'),
    ('2', 'Quincena 2'),
)
   

CHOICES_BANCO = (
    ('None', '---Seleccione Banco---'),
    ('banco cordoba', 'Banco Cordoba'),
    ('banco nacion', 'Banco Nacion'),
    ('correo','Correo'),
)

class ReportForm(forms.Form):        
    seccional = forms.CharField(widget = forms.TextInput())
    quincena  = forms.ChoiceField(choices=MY_CHOICES)
    
    fecha     = forms.DateField(widget=widgets.AdminDateWidget())
    
    
class CodigoForm(forms.ModelForm):
    quincena = forms.ChoiceField(choices=MY_CHOICES)
    banco    = forms.ChoiceField(choices=CHOICES_BANCO)
    fecha    = forms.DateField(widget=widgets.AdminDateWidget())   

    def clean_numero(self):
        dato = self.cleaned_data['numero']
        letras = len(dato)
        
        if letras != 26:
            raise forms.ValidationError("Codigo incorrecto")  
                             
            return self.cleaned_data['numero']
            
        else:            
            if Codigo.objects.filter(numero = dato):
                    raise forms.ValidationError('El codigo ya fue ingresado')
                    
                    return self.cleaned_data['numero'] 
                    
            return self.cleaned_data['numero'] 
            
        
          
    class Meta:
        model = Codigo
        exclude = ('seccional','boleta','monto') 	

   
    

        
