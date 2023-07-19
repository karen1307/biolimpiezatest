from django.db import models
from django.contrib.auth.models import User
from Apps.servicio.models import MunicipioServicio, GrupoBeneficiario
from django.core.validators import FileExtensionValidator
from datetime import datetime

class ARL(models.Model):
    nombre = models.CharField(max_length=50)
    observaciones = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "ARL"
        verbose_name_plural = "ARL"

    def __str__(self):
        return self.nombre
    
class EPS(models.Model):
    nombre = models.CharField(max_length=50)
    observaciones = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "EPS"
        verbose_name_plural = "EPS"

    def __str__(self):
        return self.nombre

class FondoPension(models.Model):
    nombre = models.CharField(max_length=50)
    observaciones = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Fondo de pensión"
        verbose_name_plural = "Fondos de pensión"

    def __str__(self):
        return self.nombre
    
class CajaCompensacion(models.Model):
    nombre = models.CharField(max_length=50)
    observaciones = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Caja de compensación"
        verbose_name_plural = "Cajas de compensación"

    def __str__(self):
        return self.nombre
    
class FondoCesantias(models.Model):
    nombre = models.CharField(max_length=50)
    observaciones = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Fondo de cesantías"
        verbose_name_plural = "Fondos de cesantías"

    def __str__(self):
        return self.nombre
    
class RolPersona(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"
        
    def __str__(self):
        return self.nombre

class TipoIdentificacion(models.Model):
    descripcion = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Tipo de identificación"
        verbose_name_plural = "Tipos de identificación"

    def __str__(self):
        return self.descripcion

class Identidad(models.Model):
    usuario = models.ForeignKey(User,unique=True,on_delete=models.RESTRICT)
    tipo_identificacion = models.ForeignKey(TipoIdentificacion,null=True, blank=True, on_delete=models.RESTRICT)
    identificacion = models.CharField(max_length=30, null=True, blank=True)
    telefono_1 = models.CharField(max_length=10, null=True, blank=True)
    telefono_2 = models.CharField(max_length=10, null=True, blank=True)
    municipio = models.ForeignKey(MunicipioServicio,on_delete=models.RESTRICT)
    direccion = models.CharField(max_length=50, null=True, blank=True)
    detalles_direccion = models.CharField(max_length=50, null=True, blank=True)
    barrio = models.CharField(max_length=50, null=True, blank=True)
    grupo = models.ForeignKey(GrupoBeneficiario,on_delete=models.RESTRICT)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Identidad"
        verbose_name_plural = "Identidades"

    def __str__(self):
        cadena = self.usuario.username + " - " + self.usuario.first_name + " " +self.usuario.last_name
        return cadena

class ClientePersona(models.Model):
    identidad = models.ForeignKey(Identidad,on_delete=models.RESTRICT,unique=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
       cadena = self.identidad.usuario.first_name + " " + self.identidad.usuario.last_name + " - " + self.identidad.usuario.email
       return cadena

class ClienteEmpresa(models.Model):
    identidad = models.ForeignKey(Identidad,on_delete=models.RESTRICT, unique=True)
    representante_legal = models.ForeignKey(ClientePersona,on_delete=models.RESTRICT)

    class Meta:
        verbose_name = "Cliente Empresa"
        verbose_name_plural = "Clientes Empresa"

    def __str__(self):
       cadena = self.identidad.usuario.first_name 
       return cadena

class Colaborador(models.Model):
    identidad = models.ForeignKey(Identidad,on_delete=models.RESTRICT)
    rol = models.ForeignKey(RolPersona,on_delete=models.RESTRICT)
    fecha_firma_contrato = models.DateTimeField(default=datetime.now())
    fotografia = models.ImageField(upload_to='colaboradoras/images', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])], null=True, blank=True)
    categoria = models.CharField(
        max_length = 30,
        choices = [
            ("asignable", "Asignable"),
            ("fijo", "Fijo")
        ],
        default = "asignable"
    )
    arl = models.ForeignKey(ARL,on_delete=models.RESTRICT)
    eps = models.ForeignKey(EPS,on_delete=models.RESTRICT)
    fondo_pension = models.ForeignKey(FondoPension,on_delete=models.RESTRICT)
    caja_compensacion = models.ForeignKey(CajaCompensacion,on_delete=models.RESTRICT)
    fondo_cesantias = models.ForeignKey(FondoCesantias,on_delete=models.RESTRICT)
    autoriza_imagen_publica = models.BooleanField()
    autorizacion_imagen_publica = models.FileField(upload_to='static/Documentos/autorizaciones_imagen_publica/', null=True, blank=True)
    fotografia = models.FileField(upload_to='static/Images/Colaboradoras/', null=True, blank=True)
    estado = models.CharField(
        max_length = 30,
        choices = [
            ("activo", "Activo"),
            ("suspendido", "Suspendido"),
            ("incapacitado", "Incapacitado"),
            ("en_vacaciones", "En vacaciones"),
            ("limitado", "Limitado"),
            ("inactivo", "Inactivo"),
        ],
        default = "activo"
    )

    class Meta:
        verbose_name = "Colaborador"
        verbose_name_plural = "Colaboradores"

    def __str__(self):
       cadena = self.identidad.usuario.username + ": " + self.identidad.usuario.first_name + " " + self.identidad.usuario.last_name
       return cadena
    
class Administrador(models.Model):
    identidad = models.ForeignKey(Identidad,on_delete=models.RESTRICT)
    rol = models.ForeignKey(RolPersona,on_delete=models.RESTRICT)

    class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"

    def __str__(self):
       cadena = self.identidad.usuario.username + ": " + self.identidad.usuario.first_name + " " + self.identidad.usuario.last_name
       return cadena
    


    



