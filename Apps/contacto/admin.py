from django.contrib import admin
from .models import *

class RegistroContactoAdmin(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = list(self.readonly_fields)
        readonly_fields.append("remitente")
        readonly_fields.append("tipo_mensaje")   
        readonly_fields.append("mensaje")   
        readonly_fields.append("fecha_radicacion")   
        readonly_fields.append("fecha_vencimiento")   
        readonly_fields.append("tipo_usuario")      
        if obj and obj.estado == EstadoRegistroContacto.objects.get(id=5):
            readonly_fields.append("estado")
            readonly_fields.append("fecha_respuesta")
            readonly_fields.append("respuesta")
            readonly_fields.append("responsable_respuesta")
        return readonly_fields
    
    def save_model(self, request, obj, form, change):
        estado_actual = obj.estado
        estado_cerrado = EstadoRegistroContacto.objects.get(id=5)

        if estado_actual == EstadoRegistroContacto.objects.get(id=4) or estado_actual ==EstadoRegistroContacto.objects.get(id=2) :
            obj.estado = estado_cerrado
            obj.save()
        super().save_model(request, obj, form, change)
     
    list_display =("tipo_mensaje","fecha_radicacion","fecha_vencimiento","estado")
    list_filter = ("tipo_mensaje","fecha_radicacion","fecha_vencimiento","estado")
    search_fields = ("remitente",)
    fields = ("remitente", "tipo_mensaje","mensaje","fecha_radicacion", "fecha_vencimiento", "tipo_usuario","estado","fecha_respuesta","respuesta","responsable_respuesta")

admin.site.register(TipoMensaje)
admin.site.register(TipoUsuario)
admin.site.register(EstadoRegistroContacto)
admin.site.register(RegistroContacto,RegistroContactoAdmin)
