from django.db import models
from datetime import datetime,timedelta
from django.contrib.auth.models import User
from Apps.persona.models import Identidad

class TipoMensaje(models.Model):
    descripcion = models.CharField(max_length=30)
    prioridad = models.CharField(
        max_length=20,
        choices= [
            ("Alta", "Alta"),
            ("Media", "Media"),
            ("Baja", "Baja")
        ]
    )

    class Meta:
        verbose_name = "Tipo de mensaje"
        verbose_name_plural = "Tipos de mensaje"

    def __str__(self):
        return self.descripcion
    
class TipoUsuario(models.Model):
    descripcion = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Tipo de usuario"
        verbose_name_plural = "Tipos de usuario"

    def __str__(self):
        return self.descripcion

class EstadoRegistroContacto(models.Model):
    descripcion = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Estado de registro de contacto"
        verbose_name_plural = "Estados de registro de contacto"

    def __str__(self):
        return self.descripcion

class RegistroContacto(models.Model):
    remitente = models.ForeignKey(Identidad, related_name="remitente",on_delete=models.CASCADE)
    tipo_mensaje = models.ForeignKey(TipoMensaje,on_delete=models.RESTRICT)
    mensaje = models.TextField()
    fecha_radicacion = models.DateTimeField(default=datetime.now())
    fecha_vencimiento = models.DateTimeField(default=datetime.now()+timedelta(15))
    tipo_usuario = models.ForeignKey(TipoUsuario,on_delete=models.RESTRICT)
    estado = models.ForeignKey(EstadoRegistroContacto,default=1,on_delete=models.RESTRICT)
    fecha_respuesta = models.DateTimeField(null=True,blank=True)
    respuesta = models.TextField(null=True,blank=True)
    responsable_respuesta = models.ForeignKey(Identidad,related_name="responsable",default=3,null=True,blank=True,on_delete=models.SET_NULL)
    
    class Meta:
        verbose_name = "Registro de contacto"
        verbose_name_plural = "Registros de contacto"
    
    def __str__(self):
        cadena = self.tipo_mensaje.descripcion + " - " + self.remitente.usuario.first_name + " " + self.remitente.usuario.last_name + " - " + self.estado.descripcion
        return cadena

