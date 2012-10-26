#encoding:utf-8

from django.db import models
from django.contrib import admin


# Create your models here.
        

class Seccional(models.Model):
	seccional = models.IntegerField ()
	localidad = models.CharField (max_length=50)
	departamento = models.CharField (max_length=50)
	responsable = models.CharField (max_length=50)
	encargado = models.CharField (max_length=50)
	telefono = models.IntegerField ()
	telefono2 = models.IntegerField ()
	Fax = models.IntegerField ()
	mail= models.CharField (max_length=50)
	regcabecera = models.IntegerField ()
	tipo = models.CharField (max_length=50)
	 
	def __unicode__(self):
		return "%i" % self.seccional

class Pedido(models.Model):
	seccional = models.ManyToManyField(Seccional)
	fecha = models.DateTimeField (auto_now = False)
	desde = models.IntegerField()
	hasta = models.IntegerField()
	cantidad = models.IntegerField()
	descripcion = models.TextField()

	def __unicode__(self):
		return "%i" % self.cantidad


class Consulta(models.Model):
	fecha = models.DateTimeField (auto_now = False)
	sccional= models.ManyToManyField(Seccional)
	persona_atendida = models.CharField (max_length=50)
	comentarios = models.TextField()
	def __unicode__(self):
		return self.nombre


	
	
	

