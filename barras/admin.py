from django.contrib import admin
from barras.models import Codigo, Operador

class CodigoAdmin(admin.ModelAdmin):
   
    list_display = ('numero','seccional','boleta','monto','quincena','fecha','operador')
    search_fields = ('numero','seccional')
    
admin.site.register(Codigo, CodigoAdmin)

class AdminSite(admin.AdminSite):
      index_template = "qbe_index.html"
      
class OperadorAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido')
    
admin.site.register(Operador, OperadorAdmin)      

