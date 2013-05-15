#encoding:utf-8

from django.db import models
from django.contrib import admin
from django.db.models import ForeignKey

# Create your models here.



class Codigo(models.Model):
    
    numero = models.CharField (max_length= 30)
    seccional = models.CharField(max_length=30)
    boleta = models.CharField(max_length=30)
    monto = models.IntegerField(max_length=30)
    quincena = models.IntegerField()
    fecha = models.DateField()
    operador = models.ForeignKey('Operador')

    
    def __unicode__(self):
        return self.numero
        
class Operador(models.Model):

    nombre = models.CharField (max_length=30)
    apellido = models.CharField (max_length=30)


    def __unicode__(self):
        return self.nombre 
        


