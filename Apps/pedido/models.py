from django.db import models
from Apps.persona.models import ClientePersona,Colaborador
from Apps.servicio.models import Servicio,MunicipioServicio
from datetime import datetime
from django.utils import timezone
    
class MedioPago(models.Model):
    nombre = models.CharField(max_length=30)
    estado = models.CharField(
        max_length = 30,
        choices = [
            ("activo", "Activo"),
            ("inactivo", "Inactivo")
        ],
        default = "activo"
    )
    nota = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Medio de pago"
        verbose_name_plural = "Medios de pago"

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    cliente_cotizante = models.ForeignKey(ClientePersona,default=20,on_delete=models.SET_DEFAULT)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    estado = models.CharField(
        max_length = 50,
        choices = [
            ("pendiente_cotizacion", "Pendiente de cotización"),
            ("cotizado", "Cotizado"),
            ("confirmado", "Confirmado"),
            ("cancelado", "Cancelado")
        ],
        default="pendiente_cotizacion"
    )

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def __str__(self):
        cadena = str(self.id) + " - " + self.cliente_cotizante.identidad.usuario.username + " - " + self.cliente_cotizante.identidad.usuario.get_full_name()
        return (cadena)
    
class TipoEspacio(models.Model):
    descripcion = models.CharField(max_length=30)
    nota = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Tipo de espacio"
        verbose_name_plural = "Tipos de espacio"

    def __str__(self):
        return self.descripcion

class PrestacionServicio(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cliente_receptor = models.ForeignKey(ClientePersona,default=3,on_delete=models.SET_DEFAULT)
    servicio = models.ForeignKey(Servicio,on_delete=models.RESTRICT)
    municipio = models.ForeignKey(MunicipioServicio, on_delete=models.RESTRICT)
    direccion = models.CharField(max_length=50, null=True, blank=True)
    detalles_direccion = models.CharField(max_length=50, null=True, blank=True)
    barrio = models.CharField(max_length=50, null=True, blank=True)
    jornada = models.CharField(
        max_length = 50,
        choices = [
            ("completa", "Completa"),
            ("media_am", "Media en la mañana"),
            ("media_pm", "Media en la tarde")
        ]
    )
    fecha_aplicacion = models.DateTimeField(default=datetime.now(), null=True, blank=True)
    estado = models.CharField(
        max_length = 50,
        choices = [
            ("abierto", "Abierto"),
            ("aplicado", "Aplicado"),
            ("cancelado", "Cancelado"),
            ("pendiente_confirmacion", "Pendiente de confirmación"),
            ("pendiente_reprogramacion", "Pendiente de reprog. de fecha"),
            ("cerrado", "Cerrado")
        ],
        default="pendiente_confirmacion"
    )
    tipo_espacio = models.ForeignKey(TipoEspacio, on_delete=models.RESTRICT)
    metros_cuadrados_espacio = models.IntegerField(default=0)
    numero_puestos_trabajo = models.IntegerField(default=0)
    numero_cocinetas = models.IntegerField(default=0)
    numero_banos = models.IntegerField(default=0, verbose_name="Número de baños")
    profesionales_asignados = models.ManyToManyField(Colaborador, null=True, blank=True)

    class Meta:
        verbose_name = "Prestación de servicio"
        verbose_name_plural = "Prestaciones de servicio"

    def __str__(self):
        cadena = str (self.id) + " - pedido[" + str(self.pedido.id) + "] - " + self.estado + " - " + str(self.fecha_aplicacion.strftime("%Y-%m-%d"))
        return cadena

class Factura(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.RESTRICT)
    fecha_generacion = models.DateTimeField(default=datetime.now())
    fecha_pago = models.DateTimeField(null=True, blank=True)
    valor = models.IntegerField(default=0)
    medio_pago = models.ForeignKey(MedioPago, null=True, blank=True, on_delete=models.RESTRICT)
    estado = models.CharField(
        max_length = 30,
        choices = [
            ("pagado", "Pagado"),
            ("pendiente_pago", "Pendiente de pago")
        ],
        default = "pendiente_pago"
    )

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"

    def __str__(self):
        cadena = self.pedido.cliente_cotizante.identidad.usuario.username + " - " + str(self.fecha_generacion)
        return cadena
    
class Agenda(models.Model):
    fecha = models.DateField(default=timezone.now(), blank=False, null=False)
    prestacion_servicio = models.ForeignKey(
        PrestacionServicio,
        blank=False,
        null=False,
        on_delete=models.CASCADE
    )
    colaborador = models.ForeignKey(
        Colaborador,
        blank=False,
        null=False,
        default=20,
        on_delete=models.SET_DEFAULT,
        related_name="colaborador"
    )

    class Meta:
        verbose_name = "Agenda"
        verbose_name_plural = "Agendas"

    def __str__(self):
        cadena = str(self.id) + " - " + str(self.fecha.strftime("%Y-%m-%d"))
        return cadena

