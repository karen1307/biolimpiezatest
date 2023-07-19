from django.contrib import admin
from .models import *

class PedidoAdmin(admin.ModelAdmin):
    def get_usuario_username(self, obj):
        return obj.cliente_cotizante.identidad.usuario.username
    
    def get_usuario_first_name(self, obj):
        return obj.cliente_cotizante.identidad.usuario.first_name
    
    def get_usuario_last_name(self, obj):
        return obj.cliente_cotizante.identidad.usuario.last_name
    
    def get_usuario_tel(self, obj):
        return obj.cliente_cotizante.identidad.telefono_1
    
    get_usuario_username.short_description = "Usuario"
    get_usuario_first_name.short_description = "Nombre"
    get_usuario_last_name.short_description = "Apellido"
    get_usuario_tel.short_description = "Teléfono"

    list_display = ("id","get_usuario_username", "get_usuario_first_name","get_usuario_last_name","get_usuario_tel","fecha_creacion","estado")
    search_fields = ("cliente_cotizante__identidad__usuario__username","cliente_cotizante__identidad__usuario__first_name",
                     "cliente_cotizante__identidad__usuario__last_name","estado","fecha_creacion")
    list_filter = ("estado","fecha_creacion")

class PrestacionServicioAdmin(admin.ModelAdmin):
    def get_id_pedido(self, obj):
        return obj.pedido.id
    
    def get_usuario_first_name(self, obj):
        return obj.cliente_receptor.identidad.usuario.first_name
    
    def get_usuario_last_name(self, obj):
        return obj.cliente_receptor.identidad.usuario.last_name
    
    def get_servicio(self, obj):
        return obj.servicio.nombre
    
    def get_municipio(self, obj):
        return obj.municipio.nombre
    
    get_id_pedido.short_description = "ID Pedido"
    get_usuario_first_name.short_description = "Nombre"
    get_usuario_last_name.short_description = "Apellido"
    get_servicio.short_description = "Servicio"
    get_municipio.short_description = "Municipio"

    list_display = ("id","get_id_pedido","get_usuario_first_name","get_usuario_last_name","get_servicio","get_municipio",
                    "direccion","barrio", "estado", "fecha_aplicacion","jornada")
    search_fields = ("cliente_receptor__identidad__usuario__first_name","cliente_receptor__identidad__usuario__last_name","estado",
                     "fecha_aplicacion", "municipio__nombre")
    list_filter = ("estado","fecha_aplicacion","jornada")

class FacturaAdmin(admin.ModelAdmin):
    def get_id_pedido(self, obj):
        return obj.pedido.id
    
    get_id_pedido.short_description = "ID Pedido"

    list_display = ("get_id_pedido","valor","estado","fecha_generacion", "fecha_pago")
    search_fields = ("pedido__id","estado","valor","fecha_generacion", "fecha_pago")
    list_filter = ("estado","fecha_generacion","fecha_pago")

class AgendaAdmin(admin.ModelAdmin): 
    def get_prestacion_servicio(self,obj):
        return str(obj.prestacion_servicio.id)
    get_prestacion_servicio.short_description = "prestacion_servicio"

    list_display = ("id","fecha","get_prestacion_servicio")
    search_fields = ("fecha",)
    list_filter = ("fecha",)
    
admin.site.register(MedioPago)
admin.site.register(Pedido,PedidoAdmin)
admin.site.register(TipoEspacio)
admin.site.register(PrestacionServicio,PrestacionServicioAdmin)
admin.site.register(Factura,FacturaAdmin)
admin.site.register(Agenda,AgendaAdmin)