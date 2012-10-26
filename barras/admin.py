from django.contrib import admin
from barras.models import Codigo

class CodigoAdmin(admin.ModelAdmin):
   
    list_display = ('numero','seccional','boleta','monto')
    search_fields = ('numero','seccional')
    

#admin.site.register(Dato, DatoAdmin)
admin.site.register(Codigo, CodigoAdmin)

