from django.contrib import admin
from .models import *

class ServicioAdmin(admin.ModelAdmin):
    list_display =("nombre","estado","precio_jornada_am","precio_jornada_pm","precio_jornada_completa","precio_hora_adicional")
    list_filter = ("tipo_equipo", "estado")
    search_fields = ("nombre",)

class MunicipioServicioAdmin(admin.ModelAdmin):
    list_display =("nombre","zona_ubicacion","costo_transporte","estado")
    list_filter = ("zona_ubicacion", "estado")
    search_fields = ("nombre","zona_ubicacion")

class BonoAdmin(admin.ModelAdmin):
    list_display =("nombre","descripcion","servicio","fecha_inicio","fecha_fin","jornada","grupo")
    list_filter = ("servicio", "grupo")
    search_fields = ("nombre","descripcion")
    
admin.site.register(GrupoBeneficiario)
admin.site.register(EstadoServicio)
admin.site.register(Bono,BonoAdmin)
admin.site.register(MunicipioServicio,MunicipioServicioAdmin)
admin.site.register(Servicio,ServicioAdmin)
