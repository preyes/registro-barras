#encoding:utf-8

from django.db import models
from django.contrib import admin

# Create your models here.

class Codigo(models.Model):
    
    numero = models.CharField (max_length= 30)
    seccional = models.CharField(max_length=30)
    boleta = models.CharField(max_length=30)
    monto = models.CharField(max_length=30)
    quincena = models.IntegerField()
    fecha = models.DateField()
    
    def __unicode__(self):
        return self.numero
    
#class Dato(models.Model):    
 #   seccional = models.CharField(max_length=30)
  #  boleta = models.CharField(max_length=30)
   # monto = models.CharField(max_length=30)


 
    #def __unicode__(self):
     #   return "%s %s" % (self.boleta)

