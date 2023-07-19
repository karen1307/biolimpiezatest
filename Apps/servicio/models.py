from django.db import models
from datetime import datetime

class GrupoBeneficiario(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    class Meta:
        verbose_name = "Grupo de beneficiarios"
        verbose_name_plural = "Grupos de beneficiarios"

    def __str__(self):
        return self.nombre

class EstadoServicio(models.Model):
    descripcion = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Estado de servicio"
        verbose_name_plural = "Estados de servicio"

    def __str__(self):
        return self.descripcion

class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    precio_jornada_am = models.IntegerField()
    precio_jornada_pm = models.IntegerField()
    precio_jornada_completa = models.IntegerField()
    precio_hora_adicional = models.IntegerField()
    descripcion = models.TextField()
    estado = models.ForeignKey(EstadoServicio,on_delete=models.RESTRICT)
    fecha_registro = models.DateTimeField(datetime.now())
    tipo_equipo = models.CharField(
        max_length = 50,
        choices = [
            ("individual", "Individual (1 colaborador)"),
            ("colectivo", "Colectivo (Más de 1 colaborador)")
        ]
    )

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.nombre

class Bono(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    codigo = models.CharField(max_length=10, unique=True)
    fecha_inicio =  models.DateTimeField()
    fecha_fin = models.DateTimeField()
    servicio = models.ForeignKey(Servicio,on_delete=models.CASCADE)
    porcentaje_descuento = models.IntegerField()
    jornada = models.CharField(
        max_length = 50,
        choices = [
            ("completa", "Completa"),
            ("media_am", "Media en la mañana"),
            ("media_pm", "Media en la tarde"),
            ("todas","Todas")
        ]
    )
    grupo = models.ForeignKey(GrupoBeneficiario,on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Bono"
        verbose_name_plural = "Bonos"

    def __str__(self):
        return self.nombre
    
class MunicipioServicio(models.Model):
    nombre = models.CharField(max_length=50)
    zona_ubicacion = models.CharField(
        max_length = 20,
        choices = [
            ("centro", "Zona centro"),
            ("norte", "Zona norte"),
            ("sur", "Zona sur"),
            ("oriental", "Zona oriental"),
            ("occidental", "Zona occidental")
        ]
    )
    costo_transporte = models.IntegerField()
    estado = models.ForeignKey(EstadoServicio,on_delete=models.RESTRICT)

    class Meta:
        verbose_name = "Municipio en servicio"
        verbose_name_plural = "Municipios en servicio"

    def __str__(self):
        return self.nombre

