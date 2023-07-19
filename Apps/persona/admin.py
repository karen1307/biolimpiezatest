from django.contrib import admin
from .models import *

class IdentidadAdmin(admin.ModelAdmin):
    list_filter = ("grupo",)
    search_fields = ("usuario",)

    def get_usuario_first_name(self, obj):
        return obj.usuario.first_name
    
    def get_usuario_last_name(self, obj):
        return obj.usuario.last_name

    get_usuario_first_name.short_description = "Nombre"
    get_usuario_last_name.short_description = "Apellido"
    list_display = ("usuario", "get_usuario_first_name","get_usuario_last_name", "grupo", "telefono_1", "direccion")

class ClientePersonaAdmin(admin.ModelAdmin):
    def get_usuario_username(self, obj):
        return obj.identidad.usuario.username
    
    def get_usuario_first_name(self, obj):
        return obj.identidad.usuario.first_name
    
    def get_usuario_last_name(self, obj):
        return obj.identidad.usuario.last_name
    
    def get_usuario_group(self, obj):
        return obj.identidad.grupo
    
    def get_usuario_direction(self, obj):
        return obj.identidad.direccion
    
    def get_usuario_tel(self, obj):
        return obj.identidad.telefono_1
    
    def get_usuario_city(self, obj):
        return obj.identidad.municipio.nombre

    get_usuario_username.short_description = "Usuario"
    get_usuario_first_name.short_description = "Nombre"
    get_usuario_last_name.short_description = "Apellido"
    get_usuario_group.short_description = "Grupo"
    get_usuario_direction.short_description = "Dirección"
    get_usuario_tel.short_description = "Teléfono"
    get_usuario_city.short_description = "Ciudad"

    list_display = ("get_usuario_username", "get_usuario_first_name","get_usuario_last_name", 
                    "get_usuario_group", "get_usuario_direction","get_usuario_tel","get_usuario_city") 
    search_fields = ("identidad__usuario__username","identidad__usuario__first_name","identidad__usuario__last_name",
                     "identidad__telefono_1","identidad__direccion","identidad__municipio__nombre")
    
class ColaboradorAdmin(admin.ModelAdmin):
    def get_usuario_username(self, obj):
        return obj.identidad.usuario.username
    
    def get_usuario_first_name(self, obj):
        return obj.identidad.usuario.first_name
    
    def get_usuario_last_name(self, obj):
        return obj.identidad.usuario.last_name
    
    def get_usuario_direction(self, obj):
        return obj.identidad.direccion
    
    def get_usuario_tel(self, obj):
        return obj.identidad.telefono_1
    
    def get_usuario_state(self, obj):
        return obj.identidad.municipio.nombre

    get_usuario_username.short_description = "Usuario"
    get_usuario_first_name.short_description = "Nombre"
    get_usuario_last_name.short_description = "Apellido"
    get_usuario_direction.short_description = "Dirección"
    get_usuario_tel.short_description = "Teléfono"

    list_display = ("get_usuario_username", "get_usuario_first_name","get_usuario_last_name", 
                    "get_usuario_direction","get_usuario_tel","estado","rol") 
    search_fields = ("identidad__usuario__username","identidad__usuario__first_name","identidad__usuario__last_name",
                     "identidad__telefono_1","identidad__direccion","estado")
    
class AdministradorAdmin(admin.ModelAdmin):
    def get_usuario_username(self, obj):
        return obj.identidad.usuario.username
    
    def get_usuario_first_name(self, obj):
        return obj.identidad.usuario.first_name
    
    def get_usuario_last_name(self, obj):
        return obj.identidad.usuario.last_name
    
    def get_usuario_direction(self, obj):
        return obj.identidad.direccion
    
    def get_usuario_tel(self, obj):
        return obj.identidad.telefono_1
    
    def get_usuario_state(self, obj):
        return obj.identidad.municipio.nombre

    get_usuario_username.short_description = "Usuario"
    get_usuario_first_name.short_description = "Nombre"
    get_usuario_last_name.short_description = "Apellido"
    get_usuario_direction.short_description = "Dirección"
    get_usuario_tel.short_description = "Teléfono"

    list_display = ("get_usuario_username", "get_usuario_first_name","get_usuario_last_name", 
                    "get_usuario_direction","get_usuario_tel","rol") 
    search_fields = ("identidad__usuario__username","identidad__usuario__first_name","identidad__usuario__last_name",
                     "identidad__telefono_1","identidad__direccion","rol")

admin.site.register(ARL)
admin.site.register(EPS)
admin.site.register(FondoPension)
admin.site.register(FondoCesantias)
admin.site.register(CajaCompensacion)
admin.site.register(RolPersona)
admin.site.register(TipoIdentificacion)
admin.site.register(Identidad,IdentidadAdmin)
admin.site.register(ClientePersona, ClientePersonaAdmin)
admin.site.register(ClienteEmpresa)
admin.site.register(Colaborador,ColaboradorAdmin)
admin.site.register(Administrador, AdministradorAdmin)
