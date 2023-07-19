from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from datetime import datetime,timedelta
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from Apps.persona.models import Identidad,ClientePersona,Colaborador
from Apps.contacto.models import RegistroContacto,TipoMensaje,TipoUsuario
from Apps.servicio.models import MunicipioServicio,GrupoBeneficiario,Servicio
from Apps.pedido.models import Pedido,PrestacionServicio,TipoEspacio,Agenda,Factura,MedioPago
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
import calendar
import json
from django.utils import timezone
from django.db.models import Q
import requests
from django.http import HttpResponse

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('mostrar_inicio')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def formatear_fecha(fecha):
    meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
    dias = {"Monday": "Lunes", "Tuesday": "Martes", "Wednesday": "Miércoles", "Thursday": "Jueves", "Friday": "Viernes", "Saturday": "Sábado", "Sunday": "Domingo"}
    dia_descriptivo = dias[fecha.strftime("%A")]
    dia = fecha.day
    mes = meses[fecha.month - 1]
    anio = fecha.year
    fecha_con_formato = "{}, {} de {} del {}".format(dia_descriptivo, dia, mes, anio)
    return(fecha_con_formato)

def verificar_sesion(request):
    if request.user.is_authenticated:
        return request.session['username']
    else:
        return ""
    
def obtener_datos_usuario(diccionario):
    if(diccionario["nombre_usuario"]!=""):
        usuario = User.objects.get(username=diccionario["nombre_usuario"])
        identidad = Identidad.objects.get(usuario=usuario)
        diccionario["perm_adm_usuario"] = usuario.is_staff
        diccionario["nombres_usuario"] = usuario.first_name
        diccionario["apellidos_usuario"] = usuario.last_name
        diccionario["correo_usuario"] = usuario.email
        diccionario["telefono_usuario"] = identidad.telefono_1
        diccionario["municipio_usuario"] = identidad.municipio
        diccionario["direccion_usuario"] = identidad.direccion
        diccionario["detalles_direccion_usuario"] = identidad.detalles_direccion
        diccionario["barrio_usuario"] = identidad.barrio
    else:
        vacio = ""
        diccionario["perm_adm_usuario"] = vacio
        diccionario["nombres_usuario"] = vacio
        diccionario["apellidos_usuario"] = vacio
        diccionario["correo_usuario"] = vacio
        diccionario["telefono_usuario"] = vacio
        diccionario["municipio_usuario"] = vacio
        diccionario["direccion_usuario"] = vacio
        diccionario["detalles_direccion_usuario"] = vacio
        diccionario["barrio_usuario"] = vacio
    return diccionario

def obtener_datos_fecha(diccionario):
    hoy = datetime.now()
    meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
    equivalente_dias = {"Monday": "1", "Tuesday": "2", "Wednesday": "3", "Thursday": "4", "Friday": "5", "Saturday": "6", "Sunday": "7"}
    mes = meses[hoy.month-1]
    anio = hoy.year
    mes_siguiente = meses[hoy.month]
    primera_fecha = datetime(hoy.year, hoy.month,1)
    dia_comienzo_mes = equivalente_dias[primera_fecha.strftime("%A")]
    numero_dias_mes = calendar.monthrange(hoy.year, hoy.month)[1]
    dia_actual = hoy.day

    if(mes == "Diciembre"):
        anio_siguiente = hoy.year + 1
        numero_dias_mes_siguiente = calendar.monthrange(hoy.year+1, 1)[1]
        primera_fecha_siguiente = datetime(hoy.year+1, 1,1)
    else:
        anio_siguiente = anio
        numero_dias_mes_siguiente = calendar.monthrange(hoy.year, hoy.month+1)[1]
        primera_fecha_siguiente = datetime(hoy.year, hoy.month+1, 1)
    dia_comienzo_mes_siguiente = equivalente_dias[primera_fecha_siguiente.strftime("%A")]

    diccionario["mes"] = mes
    diccionario["anio"] = anio
    diccionario["mes_siguiente"] =  mes_siguiente
    diccionario["anio_siguiente"] =  anio_siguiente
    diccionario["numero_dias_mes"] =  numero_dias_mes
    diccionario["numero_dias_mes_siguiente"] =  numero_dias_mes_siguiente
    diccionario["dia_comienzo_mes"] =  dia_comienzo_mes
    diccionario["dia_comienzo_mes_siguiente"] =  dia_comienzo_mes_siguiente
    diccionario["dia_actual"] =  dia_actual
    return diccionario

def mostrar_sitio_administrativo(request):
    if request.user.is_authenticated:
        return redirect("/administracion")
    else:
        return redirect("/ingreso/?next=/administracion")

def mostrar_inicio(request):
    diccionario = {
        "pagina": "inicio",
        "complemento_titulo": "",
        "nombre_usuario": verificar_sesion(request)
    }
    diccionario = obtener_datos_usuario(diccionario)
    return render(request, "index.html",diccionario)

def mostrar_inicio_2(request):
    diccionario = {
        "pagina": "inicio",
        "complemento_titulo": "",
        "nombre_usuario": verificar_sesion(request)
    }
    diccionario = obtener_datos_usuario(diccionario)
    return render(request, "index_2.html",diccionario)

@unauthenticated_user
def mostrar_ingreso(request):
    diccionario = {
        "pagina": "ingreso",
        "complemento_titulo": "- Ingreso",
        "nombre_usuario": verificar_sesion(request),
        "accion": "inicio"
    }
    if(request.POST):
        usuarios = User.objects.all()
        encontrado = False
        valido = False
        correo = request.POST["nmCorreoIng"]
        pase = request.POST["nmPaseIng"]
        next_url = request.POST['nmNextIng']
        nombre_usuario = ""
        for usuario in usuarios:
            if(usuario.email == correo):
                encontrado = True
                nombre_usuario = usuario.username
                sesion_usuario = authenticate(request, username=nombre_usuario, password=pase)
                if sesion_usuario is not None:
                    login(request, sesion_usuario)
                    request.session['username'] = nombre_usuario
                    valido = True
                    diccionario["nombre_usuario"] = usuario.username
                break
        if(encontrado == False):
            diccionario["accion"] = "errorUsuario"
            return render(request,"index.html",diccionario)
        else:
            if(valido == False):
                diccionario["accion"] = "errorPase"
                return render(request,"index.html",diccionario)
            else:
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect("mostrar_inicio")
    else:
        return render(request,"index.html",diccionario)
        
@unauthenticated_user
def mostrar_registro(request):
    diccionario = {
        "pagina": "registro",
        "complemento_titulo": "- Registro",
        "nombre_usuario": verificar_sesion(request),
        "accion": "inicio"
    }
    if(request.POST):
        try:
            nombres = request.POST["nmNombresReg"]
            apellidos = request.POST["nmApellidosReg"]
            correo = request.POST["nmCorreoReg"]
            telefono = request.POST["nmTelefonoReg"]
            municipio_ = request.POST["nmMunicipioReg"]
            direccion_ = request.POST["nmDireccionReg"]
            detalles_direccion_ = request.POST["nmDetallesDireccion"]
            barrio_ = request.POST["nmBarrioReg"]
            pase = request.POST["nmPaseReg"]
            confirmacion_pase = request.POST["nmPaseConfReg"]
            if(nombres!= "" and apellidos!= "" and telefono!="" and municipio_!="" and direccion_!=""  
               and barrio_!="" and pase!="" and confirmacion_pase!="" and correo!=""):
                if User.objects.filter(email=correo).exists():
                    diccionario["accion"] = "fallido"
                    diccionario["mensaje_error"] = "El usuario ya está registrado en la base de datos"
                else:
                    if(pase==confirmacion_pase):
                        nuevo_usuario = User.objects.create_user(username=correo, email=correo, password=pase)
                        nuevo_usuario.first_name = nombres
                        nuevo_usuario.last_name = apellidos
                        nuevo_usuario.save()
                        municipio_ = MunicipioServicio.objects.get(id=municipio_)
                        grupo_ = GrupoBeneficiario.objects.get(id=2)
                        nueva_identidad = Identidad.objects.create(usuario=nuevo_usuario,telefono_1=telefono,municipio=municipio_,grupo=grupo_,
                                                                   direccion=direccion_,detalles_direccion=detalles_direccion_,barrio=barrio_)
                        
                        nueva_identidad.save()
                        nuevo_cliente_persona = ClientePersona.objects.create(identidad=nueva_identidad)
                        nuevo_cliente_persona.save()
                        diccionario["accion"] = "creado"
                    else:
                        diccionario["accion"] = "fallido"
                        diccionario["mensaje_error"] = "La contraseña y la confirmación no coinciden"
            else:
                diccionario["accion"] = "fallido"
                diccionario["mensaje_error"] = "Hay campos vacíos"
        except Exception as error:
            diccionario["accion"] = "fallido"
            diccionario["mensaje_error"] = str(error)
        return render(request,"index.html",diccionario)
    else:
        return render(request,"index.html",diccionario)

def mostrar_recuperacion_acceso(request):
    diccionario = {
        "pagina": "recuperacion_acceso",
        "complemento_titulo": "- Recuperación de acceso",
        "nombre_usuario": verificar_sesion(request),
        "accion": "inicio"
    }
    if(request.POST):
        try:
            correo = request.POST["nmCorreoRec"]
            usuario = User.objects.get(username=correo)
            token = default_token_generator.make_token(usuario)
            usuario.forgot_password_token = token
            usuario.save()
            uid = urlsafe_base64_encode(force_bytes(usuario.pk))
            reset_url = request.build_absolute_uri(reverse('restablecimiento_pase', kwargs={'uidb64': uid, 'token': token}))
            asunto = "T.I Biolimpieza [Servicio de recuperación de acceso]"
            valor_mensaje = "Para restablecer su contraseña, haga clic en este enlace: " + reset_url
            remitente = settings.EMAIL_HOST_USER
            destinatario = [correo]
            send_mail(asunto,valor_mensaje,remitente,destinatario,fail_silently= False)
            diccionario["accion"] = "enviado"
        except Exception as error:
            diccionario["accion"] = "fallido"
            diccionario["mensaje_error"] = str(error)
        return render(request, "index.html", diccionario)
    else:
        if(diccionario["nombre_usuario"]==""):       
            return render(request, "index.html", diccionario)
        else:
            return redirect("mostrar_inicio")

def  mostrar_restablecimiento_pase(request, uidb64, token):
    diccionario = {
        "pagina": "restablecimiento_pase",
        "complemento_titulo": "- Restablecimiento de contraseña",
        "nombre_usuario": verificar_sesion(request),
        "accion": "inicio"
    }
    try:
        uid = str(urlsafe_base64_decode(uidb64), 'utf-8')
        usuario = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        usuario = None
        diccionario["accion"] = "fallido"
        diccionario["mensaje_error"] = "error de identificación de usuario"
    if usuario is not None and default_token_generator.check_token(usuario, token):
        if(request.POST):
            try:
                pase = request.POST["nmPaseRestablec"]
                confirmacion_pase = request.POST["nmConfirmPaseRestablec"]
                if(pase!="" and confirmacion_pase!="" and pase==confirmacion_pase):
                    usuario.set_password(pase)
                    usuario.forgot_password_token = None
                    usuario.save()
                    usuario = authenticate(username=usuario.username, password=pase)
                    login(request, usuario)
                    request.session['username'] = usuario.get_username()
                    asunto = "T.I Biolimpieza [Servicio de recuperación de acceso]"
                    valor_mensaje = "Se ha cambiado la contraseña de su cuenta en Biolimpieza. Si no ha sido usted, póngase en contacto con nosotros"
                    remitente = settings.EMAIL_HOST_USER
                    destinatario = [usuario.email]
                    send_mail(asunto,valor_mensaje,remitente,destinatario,fail_silently= False)
                    return redirect('mostrar_inicio')
                else:
                    diccionario["accion"] = "fallido"
                    diccionario["mensaje_error"] = "La contraseña no coincide con la confirmación"
            except Exception as error:
                diccionario["accion"] = "fallido"
                diccionario["mensaje_error"] = str(error)
    else:
        diccionario["accion"] = "fallido"
        diccionario["mensaje_error"] = "error de token o de identificación de usuario"
    return render(request, "index.html", diccionario)

@login_required(login_url='/ingreso/')
def mostrar_gestion_datos(request):
    diccionario = {
        "pagina": "gestion_datos",
        "complemento_titulo": "- Gestión de datos",
        "nombre_usuario": verificar_sesion(request),
        "accion": "inicio"
    }
    diccionario = obtener_datos_usuario(diccionario)
    if(request.POST):
        cambios_a_realizar = ["NO","NO","OK"]
        try:
            usuario_ = User.objects.get(username=diccionario["nombre_usuario"])
            pase_actual = request.POST["nmPaseGestDatos"]
            if(pase_actual is not None and usuario_ is not None and usuario_.check_password(pase_actual)):
                nombres = request.POST["nmNombresGestDatos"]
                apellidos = request.POST["nmApellidosGestDatos"]
                correo = request.POST["nmCorreoGestDatos"]
                telefono = request.POST["nmTelefonoGestDatos"]
                municipio = request.POST["nmMunicipioGestDatos"]
                direccion = request.POST["nmDireccionGestDatos"]
                detalles_direccion = request.POST["nmDetallesDireccionGestDatos"]
                barrio = request.POST["nmBarrioGestDatos"]
                nuevo_pase = request.POST["nmNuevoPaseGestDatos"]
                confirm_nuevo_pase = request.POST["nmNuevoPaseConfGestDatos"]
                if(nuevo_pase!="" and confirm_nuevo_pase!=""):
                    if(nuevo_pase==confirm_nuevo_pase):
                        cambios_a_realizar[0]="SI"
                    else:
                        cambios_a_realizar[2]="ER"
                        diccionario["accion"] = "fallido"
                        diccionario["mensaje_error"] = "La nueva contraseña no coincide con la confirmación"
                if(nombres and apellidos and correo and telefono and municipio and direccion and barrio and cambios_a_realizar[2]=="OK"):
                    cambios_a_realizar[1]="SI"
                    identidad_ = Identidad.objects.get(usuario=usuario_)
                    destinatario = [usuario_.email]
                    usuario_.first_name = nombres
                    usuario_.last_name = apellidos
                    usuario_.username = correo
                    usuario_.email = correo
                    identidad_.telefono_1 = telefono
                    municipio_= MunicipioServicio.objects.get(id=municipio)
                    identidad_.municipio = municipio_
                    identidad_.direccion = direccion
                    identidad_.detalles_direccion = detalles_direccion
                    identidad_.barrio = barrio
                    if(cambios_a_realizar[0]=="SI" and cambios_a_realizar[2]=="OK"):
                        usuario_.set_password(nuevo_pase)
                    usuario_.save()
                    identidad_.save()
                    diccionario["accion"] = "actualizado"
                    asunto = "T.I Biolimpieza [Servicio de actualización de datos]"
                    if(cambios_a_realizar[0]=="SI" and cambios_a_realizar[2]=="OK"):
                        valor_mensaje = "Se ha cambiado la contraseña de su cuenta en Biolimpieza. Si no ha sido usted, póngase en contacto con nosotros"
                    else:
                        if(cambios_a_realizar[1]=="SI" and cambios_a_realizar[2]=="OK"):
                            valor_mensaje = "Se ha actualizado la información de su cuenta en Biolimpieza. Si no ha sido usted, póngase en contacto con nosotros"
                    if (cambios_a_realizar[2]=="OK"):
                        remitente = settings.EMAIL_HOST_USER
                        send_mail(asunto,valor_mensaje,remitente,destinatario,fail_silently= False)
            else:
                cambios_a_realizar[2]="ER"
                diccionario["accion"] = "fallido"
                diccionario["mensaje_error"] = "Error de autenticación"   
        except Exception as error:
            cambios_a_realizar[2]="ER"
            diccionario["accion"] = "fallido"
            diccionario["mensaje_error"] = str(error)  
    return render(request, "index.html", diccionario)

@login_required(login_url='/ingreso/')
def mostrar_eliminar_cuenta(request):
    diccionario = {
        "pagina": "eliminacion_cuenta",
        "complemento_titulo": "- Eliminación de cuenta",
        "nombre_usuario": verificar_sesion(request),
        "accion": "inicio"
    }
    diccionario = obtener_datos_usuario(diccionario)
    if(request.POST):
        try:
            pase = request.POST["nmPaseEliminacionCuenta"]
            comentarios = request.POST["nmTxtAreaEliminacionCuenta"]
            usuario_ = User.objects.get(username=diccionario["nombre_usuario"])
            if(usuario_.check_password(pase)):
                tipo_usuario_ = TipoUsuario.objects.get(id=2)
                emisor = Identidad.objects.get(usuario=usuario_)
                cliente = ClientePersona.objects.get(identidad=emisor)
                nombre_solicitante = usuario_.get_full_name()
                correo_solicitante = usuario_.email
                tel_solicitante = emisor.telefono_1
                municip_solicitante = emisor.municipio.nombre
                fecha_radicacion = datetime.now()
                fecha = formatear_fecha(fecha_radicacion)
                valor_mensaje = '''
                SOLICITUD PARA ELIMINACIÓN DE CUENTA
    
                DATOS DE LA PERSONA SOLICITANTE
                -----------------------------------
                Código ID del cliente: %s
                Código ID de identificación: %s
                Nombre: %s
                Correo electrónico: %s
                Teléfono: %s
                Municipio: %s
                Comentarios del usuario: %s

                Fecha de solicitud: %s
                '''%(cliente.id,emisor.id,nombre_solicitante,correo_solicitante,tel_solicitante,municip_solicitante,
                     comentarios,fecha)
                
                mensaje_ = '''
                Cordial saludo,

                El cliente %s
                Solicita la eliminación de su cuenta, identificada con ID de cliente %s, ID de Identificación %s y
                con usuario %s.

                comentarios adicionales del cliente: 
                %s
                '''%(nombre_solicitante,cliente.id,emisor.id,usuario_.email,comentarios)
                nuevo_registro_contacto = RegistroContacto(
                    remitente = emisor,
                    tipo_mensaje = TipoMensaje.objects.get(id=1),
                    mensaje = mensaje_,
                    tipo_usuario = tipo_usuario_)
                nuevo_registro_contacto.save()
                usuario_.is_active = False
                usuario_.save()
                return redirect("cerrar_sesion")
            else:
                diccionario["mensaje_error"] = "La contraseña es incorrecta"
                return render(request, "index.html",diccionario)
        except Exception as error:
            diccionario["accion"] = "fallido"
            diccionario["mensaje_error"] = str(error)
            return render(request, "index.html",diccionario)
    else:
        return render(request, "index.html",diccionario)

def mostrar_contacto(request):
    diccionario = {
        "pagina": "contacto",
        "complemento_titulo": "- Contacto",
        "nombre_usuario": verificar_sesion(request),
        "accion": "inicio"
    }
    diccionario = obtener_datos_usuario(diccionario)
    if(request.POST):
        try:
            nombres = request.POST["nmNombreCt"]
            apellidos = request.POST["nmApellidoCt"]
            correo = request.POST["nmCorreoCt"]
            telefono = request.POST["nmTelefonoCt"]
            tipo_mensaje_ = int(request.POST["nmTipoCt"])
            mensaje_ = request.POST["nmMensajeCt"]
            fecha_radicacion = datetime.now()

            tipo_mensaje_ = TipoMensaje.objects.get(id=tipo_mensaje_)
            enviar_mensaje = True
            if(diccionario["nombre_usuario"]!=""):
                tipo_usuario_ = TipoUsuario.objects.get(id=2)
                usuario_ = User.objects.get(username=diccionario["nombre_usuario"])
                emisor = Identidad.objects.get(usuario=usuario_)
                if(nombres!=usuario_.first_name or apellidos!=usuario_.last_name or correo!=usuario_.email or telefono!=emisor.telefono_1):
                    enviar_mensaje = False
                    diccionario["accion"] = "fallido"
                    diccionario["mensaje_error"] = "Los datos entregados no coinciden con los del usuario"
            else:
                tipo_usuario_ = TipoUsuario.objects.get(id=1)
                nombre_usuario = "pqrsf_" + str(fecha_radicacion) + "_" + str(User.objects.count())
                nuevo_usuario_PQRSF = User(
                    username=nombre_usuario,
                    password=".admpqrsf",
                    email=correo,
                    first_name=nombres,
                    last_name = apellidos)
                nuevo_usuario_PQRSF.save()
                municipio_ = MunicipioServicio.objects.get(id=1)
                grupo_beneficiario = GrupoBeneficiario.objects.get(id=3)
                nueva_identidad_pqrsf = Identidad(
                    usuario = nuevo_usuario_PQRSF,
                    telefono_1 = telefono,
                    municipio = municipio_,
                    grupo = grupo_beneficiario)
                nueva_identidad_pqrsf.save()
                emisor = nueva_identidad_pqrsf
            if(enviar_mensaje==True):
                nuevo_registro_contacto = RegistroContacto(
                    remitente = emisor,
                    tipo_mensaje = tipo_mensaje_,
                    mensaje = mensaje_,
                    tipo_usuario = tipo_usuario_)
                nuevo_registro_contacto.save()
                fecha = formatear_fecha(fecha_radicacion)
                asunto = "T.I Biolimpieza [Servicio de Contacto] - " + nombres + " " + apellidos
                remitente = settings.EMAIL_HOST_USER
                #destinatario = "biolimpiezahogarescologicos@gmail.com"
                destinatario = ["danisantamaria97@gmail.com"]
            
                valor_mensaje = '''
                Remitente: %s %s
                Correo electrónico: %s
                Teléfono: %s
                Tipo de mensaje: %s
                Fecha: %s

                Mensaje: %s
                '''%(nombres,apellidos,correo,telefono,tipo_mensaje_,fecha,mensaje_)
                
                #send_mail(asunto,valor_mensaje,remitente,destinatario)
                diccionario["accion"] = "enviado"
        except Exception as error:
            diccionario["accion"] = "fallido"
            diccionario["mensaje_error"] = str(error)
    return render(request, "index.html",diccionario)

@login_required(login_url='/ingreso/')
def mostrar_cotizacion_brigada(request):
    diccionario = {
        "pagina": "brigada",
        "complemento_titulo": "- Brigada",
        "nombre_usuario": verificar_sesion(request),
        "accion": "inicio"
    }
    diccionario = obtener_datos_usuario(diccionario)
    if(request.POST): 
        if(diccionario["nombre_usuario"]!=""):
            try:
                tipo_cliente_receptor = request.POST["nmPersonaCtzBrigada"]
                nombre = request.POST["nmNombreCtzBrigada"]
                apellido = request.POST["nmApellidoCtzBrigada"]
                correo = request.POST["nmCorreoCtzBrigada"]
                telefono = request.POST["nmTelefonoCtzBrigada"]
                municipio = request.POST["nmMunicipioCtzBrigada"]
                tipo_espacio_ = request.POST["nmTipoEspacio"]
                direccion_ = request.POST["nmDireccion"]
                detalles_direccion_ = request.POST["nmDetallesDireccion"]
                barrio_ = request.POST["nmBarrio"]
                metros_cuadrados_espacio_ = request.POST["nmMetrosEspacioCtzBrigada"]
                numero_puestos_trabajo_ = request.POST["nmNroPuestosTrabajoCtzBrigada"]
                numero_cocinetas_ = request.POST["nmNroCocinetasCtzBrigada"]
                numero_banios_ = request.POST["nmNroBanosCtzBrigada"]

                fecha_hoy = datetime.now()
                fecha = formatear_fecha(fecha_hoy)

                usuario_cotizante = User.objects.get(username=diccionario["nombre_usuario"])
                identidad_cotizante = Identidad.objects.get(usuario=usuario_cotizante)
                cliente_cotizante_ = ClientePersona.objects.get(identidad=identidad_cotizante)
                nuevo_pedido = Pedido.objects.create(cliente_cotizante=cliente_cotizante_)
                nuevo_pedido.save()
                nombre_municipio = MunicipioServicio.objects.get(id=municipio).nombre
                municipio_ = MunicipioServicio.objects.get(id=municipio)

                if(tipo_cliente_receptor=="2"):
                    #tipo_usuario_ = TipoUsuario.objects.get(id=1)
                    nombre_usuario = "clt_" + str(datetime.now().date()) + "_" + str(User.objects.count())
                    nuevo_usuario_CLT = User.objects.create_user(
                        username=nombre_usuario,
                        password=".admclt",
                        email=correo,
                        first_name=nombre,
                        last_name = apellido)
                    nuevo_usuario_CLT.save()
                    grupo_beneficiario = GrupoBeneficiario.objects.get(id=3)
                    nueva_identidad_CLT = Identidad.objects.create(
                        usuario = nuevo_usuario_CLT,
                        telefono_1 = telefono,
                        municipio = municipio_,
                        direccion = direccion_,
                        detalles_direccion = detalles_direccion_,
                        barrio = barrio_,
                        grupo = grupo_beneficiario)
                    nueva_identidad_CLT.save()
                    nuevo_cliente_persona = ClientePersona.objects.create(identidad=nueva_identidad_CLT)
                    nuevo_cliente_persona.save()
                    cliente_receptor_ = nuevo_cliente_persona
                else:
                    cliente_receptor_ = cliente_cotizante_

                switch_case = {
                    "Hogar": 2,
                    "Oficina": 3,
                    "Edificio": 4,
                    "Bodega": 5,
                    "Local": 6,
                }
                id_tipo_espacio = switch_case[tipo_espacio_]
                espacio_ = TipoEspacio.objects.get(id=id_tipo_espacio)

                nueva_prestacion_servicio = PrestacionServicio.objects.create(
                    pedido = nuevo_pedido,
                    cliente_receptor = cliente_receptor_,
                    servicio = Servicio.objects.get(id=3),
                    municipio = municipio_,
                    direccion = cliente_receptor_.identidad.direccion,
                    detalles_direccion = cliente_receptor_.identidad.detalles_direccion,
                    barrio = cliente_receptor_.identidad.barrio,
                    jornada = "completa",
                    tipo_espacio = espacio_,
                    metros_cuadrados_espacio = metros_cuadrados_espacio_,
                    numero_puestos_trabajo = numero_puestos_trabajo_,
                    numero_cocinetas = numero_cocinetas_,
                    numero_banos = numero_banios_
                )
                nueva_prestacion_servicio.save()
                asunto = "T.I Biolimpieza [Cotización Brigada] -" + " " + nombre + " " + apellido
                remitente = settings.EMAIL_HOST_USER
                #destinatario = "biolimpiezahogarescologicos@gmail.com"
                destinatario = ["danisantamaria97@gmail.com"]
            
                direccion_completa = direccion_ + " " + detalles_direccion_
                valor_mensaje = '''
                SOLICITUD PARA SERVICIO DE BRIGADA
        
                DATOS DE LA PERSONA COTIZANTE
                -----------------------------------
                Nombre: %s %s
                Correo electrónico: %s
                Teléfono: %s
                Municipio: %s

                DATOS DE PERSONA QUE RECIBE SERVICIO
                ------------------------------------
                Nombre: %s %s
                Correo electrónico: %s
                Teléfono: %s
                Municipio: %s
                Dirección: %s
                Barrio: %s

                DETALLES DEL LUGAR Y SERVICIO
                ------------------------------------
                Tipo de espacio: %s
                Metros cuadrados del espacio: %s
                Número de puestos de trabajo: %s
                Número de cocinetas: %s
                Número de baños: %s
                Fecha de solicitud: %s
                '''%(usuario_cotizante.first_name,usuario_cotizante.last_name,usuario_cotizante.email,identidad_cotizante.telefono_1,
                    identidad_cotizante.municipio.nombre,nombre,apellido,correo,telefono,nombre_municipio,
                    direccion_completa,barrio_,tipo_espacio_,metros_cuadrados_espacio_,numero_puestos_trabajo_,numero_cocinetas_,numero_banios_,fecha)
                
                send_mail(asunto,valor_mensaje,remitente,destinatario)
                diccionario["accion"] = "enviado"
            except Exception as error:
                diccionario["accion"] = "fallido"
                diccionario["mensaje_error"] = str(error)
        else:
            diccionario["accion"] = "fallido"
            diccionario["mensaje_error"] = "Error de autenticación"
        return render(request, "index.html", diccionario)
    else:
        return render(request, "index.html", diccionario)

def mostrar_no_encontrada(request,valor):
    diccionario = {
        "pagina": "no_encontrada",
        "complemento_titulo": "- error 404",
        "nombre_usuario": verificar_sesion(request)
    }
    diccionario = obtener_datos_usuario(diccionario)
    return render(request, "index.html",diccionario)

def mostrar_colaboradoras(request):
    diccionario = {
        "pagina": "colaboradoras",
        "complemento_titulo": "- Colaboradoras",
        "nombre_usuario": verificar_sesion(request)
    }
    diccionario = obtener_datos_usuario(diccionario)
    diccionario ["colaboradoras"] = Colaborador.objects.filter(estado="activo",autoriza_imagen_publica=True,fotografia__isnull=False).exclude(fotografia='')
    return render(request, "index.html",diccionario)

@login_required(login_url='/ingreso/')
def mostrar_datos_reserva(request,servicio):
   diccionario = {
        "pagina": "datosReserva",
        "complemento_titulo": "- Reserva de servicio",
        "nombre_usuario": verificar_sesion(request)
    }
   if(request.POST):
        if(diccionario["nombre_usuario"]!=""):
            try:
                tipo_cliente_receptor = request.POST["nmPersonaDtsReserva"]
                nombres = request.POST["nmNombresDtsReserva"]
                apellidos = request.POST["nmApellidosDtsReserva"]
                correo = request.POST["nmCorreoDtsReserva"]
                telefono = request.POST["nmTelefonoDtsReserva"]
                municipio = request.POST["nmMunicipioDtsReserva"]
                direccion_ = request.POST["nmDireccionDtsReserva"]
                detalles_direccion_ = request.POST["nmDetallesDireccionDtsReserva"]
                barrio_ = request.POST["nmDetallesDireccionDtsReserva"]
                id_servicio = int(request.POST["nmServicioDtsReserva"])

                usuario_cotizante = User.objects.get(username=diccionario["nombre_usuario"])
                identidad_cotizante = Identidad.objects.get(usuario=usuario_cotizante)
                cliente_cotizante_ = ClientePersona.objects.get(identidad=identidad_cotizante)
                nuevo_pedido = Pedido.objects.create(cliente_cotizante=cliente_cotizante_)
                nuevo_pedido.save()
                municipio_ = MunicipioServicio.objects.get(id=municipio)
                
                if(tipo_cliente_receptor=="2"):
                    nombre_usuario = "clt_" + str(datetime.now().date()) + "_" + str(User.objects.count())
                    nuevo_usuario_CLT = User.objects.create_user(
                        username=nombre_usuario,
                        password=".admclt",
                        email=correo,
                        first_name=nombres,
                        last_name = apellidos)
                    nuevo_usuario_CLT.save()
                    grupo_beneficiario = GrupoBeneficiario.objects.get(id=3)
                    nueva_identidad_CLT = Identidad.objects.create(
                        usuario = nuevo_usuario_CLT,
                        telefono_1 = telefono,
                        municipio = municipio_,
                        direccion = direccion_,
                        detalles_direccion = detalles_direccion_,
                        barrio = barrio_,
                        grupo = grupo_beneficiario)
                    nueva_identidad_CLT.save()
                    nuevo_cliente_persona = ClientePersona.objects.create(identidad=nueva_identidad_CLT)
                    nuevo_cliente_persona.save()
                    cliente_receptor_ = nuevo_cliente_persona
                else:
                    cliente_receptor_ = cliente_cotizante_
                return redirect("mostrar_agenda",id_servicio,nuevo_pedido.id,cliente_receptor_.id)
            except Exception as error:
                print("error 1")
                diccionario["mensaje_error"] = str(error)
                return render(request, "index.html", diccionario)
        else:
            print("error 2")
            diccionario["mensaje_error"] = "Error de autenticación"
            return render(request, "index.html", diccionario)
   else:
        if not(servicio == "hogar" or servicio == "oficina"):
            return redirect("mostrar_inicio")
        else:
            if(servicio=="hogar"):
                diccionario["servicio_reserva"] = 1
            else:
                diccionario["servicio_reserva"] = 2
        diccionario = obtener_datos_usuario(diccionario)
        if(diccionario["nombre_usuario"]!=""):       
            return render(request, "index.html", diccionario)
        else:
            return redirect("ingreso")
  
@login_required(login_url='/ingreso/')
def mostrar_agenda(request,cod_serv,cod_pedido,cod_receptor):
    colaboradoras = Colaborador.objects.filter(categoria="asignable",estado="activo",autoriza_imagen_publica=True,fotografia__isnull=False).exclude(fotografia='')
    agendas = Agenda.objects.filter(fecha__gte=timezone.now().date())
    servicio_ = Servicio.objects.get(id=cod_serv)
    precio_jornada_am = servicio_.precio_jornada_am
    precio_jornada_pm = servicio_.precio_jornada_pm
    precio_jornada_completa = servicio_.precio_jornada_completa
    diccionario = {
        "pagina": "agenda",
        "complemento_titulo": "- Agenda de servicio",
        "nombre_usuario": verificar_sesion(request),
        "colaboradoras": colaboradoras,
        "agendas" : agendas,
        "cod_servicio": cod_serv,
        "cod_pedido": cod_pedido,
        "cod_receptor": cod_receptor,
        "precio_jornada_am": precio_jornada_am,
        "precio_jornada_pm": precio_jornada_pm,
        "precio_jornada_completa": precio_jornada_completa
    }
    diccionario = obtener_datos_usuario(diccionario)
    diccionario = obtener_datos_fecha(diccionario)
    if(request.POST):
        try:
            valor_a_pagar = int(request.POST["nmTotalPagarPasarela"])
            cantidad_prestac_serv = request.POST["nmCantidadServiciosPasarela"]
            codigo_servicio = int(request.POST["nmCodServicioPasarela"])
            codigo_pedido = int(request.POST["nmCodPedidoPasarela"])
            codigo_receptor = int(request.POST["nmCodReceptorPasarela"])
            prestaciones_servicio = request.POST["nmJsonPasarela"]
            json_prestac_servicio = json.loads(prestaciones_servicio)

            pedido_ = Pedido.objects.get(id=codigo_pedido)
            medio_pago_ = MedioPago.objects.get(id=3)
            cliente_receptor_ = ClientePersona.objects.get(id=codigo_receptor)
            municipio_ = cliente_receptor_.identidad.municipio
            direccion_ = cliente_receptor_.identidad.direccion
            detalles_direc = cliente_receptor_.identidad.detalles_direccion
            barrio_ = cliente_receptor_.identidad.barrio
            if(codigo_servicio==1):
                tipo_espacio_ = TipoEspacio.objects.get(id=2)
            else:
                tipo_espacio_ = TipoEspacio.objects.get(id=3)

            factura = Factura.objects.create(
                pedido = pedido_,
                valor = valor_a_pagar,
                medio_pago = medio_pago_,
                estado = "pendiente_pago"
            )
            factura.save()
            for elemento in json_prestac_servicio:
                id_colaboradora = int(elemento["colaboradora"])
                colaboradora_ = Colaborador.objects.get(id=id_colaboradora)
                prestacion_servicio_ = PrestacionServicio.objects.create(
                    pedido = pedido_,
                    cliente_receptor = cliente_receptor_,
                    servicio = servicio_,
                    municipio = municipio_,
                    direccion = direccion_,
                    detalles_direccion = detalles_direc,
                    barrio = barrio_,
                    jornada = elemento["jornada"],
                    estado = "pendiente_confirmacion",
                    tipo_espacio = tipo_espacio_,
                )
                prestacion_servicio_.save()

                agenda = Agenda.objects.create(
                    fecha = elemento["fecha"],
                    prestacion_servicio = prestacion_servicio_,
                    colaborador = colaboradora_
                )
                agenda.save()
            return redirect("mostar_pasarela_pagos",factura.id)
        except Exception as error:
            diccionario["mensaje_error"] = str(error)
            return render(request, "index.html",diccionario)
    else:   
        return render(request, "index.html",diccionario)

@login_required(login_url='/ingreso/')
def mostrar_agenda_admin(request):
    diccionario = {
        "pagina": "agenda_admin",
        "complemento_titulo": "- Agenda de servicio",
        "nombre_usuario": verificar_sesion(request),
        "accion": "inicio"
    }
    if(request.POST):
        try:
            fecha_seleccionada = request.POST["nmBusqFecha"]
            fecha_seleccionada = datetime.strptime(fecha_seleccionada, '%Y-%m-%d').date()
            diccionario["agenda"] = Agenda.objects.filter(fecha = fecha_seleccionada)
            diccionario["fecha_seleccionada"] = str(fecha_seleccionada)
        except Exception as error:
            diccionario["agenda"] = None
            diccionario["mensaje_error"] = str(error)
    else:
        diccionario["agenda"] = Agenda.objects.filter(fecha=datetime.now().date())
        diccionario["fecha_seleccionada"] = str(datetime.strptime(str(datetime.now().date()),'%Y-%m-%d').date())
    diccionario = obtener_datos_usuario(diccionario)
    diccionario = obtener_datos_fecha(diccionario)
    diccionario["prestaciones_servicio"] = PrestacionServicio.objects.filter(Q(estado="abierto") | Q(estado="pendiente_reprogramacion"))
    diccionario["colaboradoras"] = Colaborador.objects.filter(Q(categoria="asignable") & Q(estado="activo") | Q(estado="limitado"))
    return render(request, "index.html",diccionario)

@login_required(login_url='/ingreso/')
def asignar_agenda_admin(request):
    diccionario = {
        "pagina": "agenda_admin",
        "complemento_titulo": "- Agenda de servicio",
        "nombre_usuario": verificar_sesion(request),
        "accion": "inicio"
    }
    if(request.POST):
        try:
            fecha_aplicacion = request.POST["nmFechaAsignacion"]
            id_prestacion_serv = request.POST["nmSlcPrestacionServicioAsignacion"]
            id_profesional = request.POST["nmSlcColaboradoraAsignacion"]
            fecha_seleccionada = datetime.strptime(fecha_aplicacion, '%Y-%m-%d').date()
            diccionario["agenda"] = Agenda.objects.filter(fecha = fecha_seleccionada)
            diccionario["fecha_seleccionada"] = str(fecha_seleccionada)
            diccionario = obtener_datos_usuario(diccionario)
            diccionario = obtener_datos_fecha(diccionario)

            prestacion_serv = PrestacionServicio.objects.get(id=id_prestacion_serv)
            profesional = Colaborador.objects.get(id=id_profesional)
            resultado = Agenda.objects.filter(fecha=fecha_aplicacion,colaborador=profesional).first()

            if(datetime.now().date()<=fecha_seleccionada):
                if(resultado is not None):
                    if(resultado.prestacion_servicio.jornada=="completa" or resultado.prestacion_servicio.jornada==prestacion_serv.jornada):
                        diccionario["mensaje_error"] = profesional.identidad.usuario.get_full_name() + " ya tiene la jornada ocupada para la fecha seleccionada"
                        diccionario["accion"] = "fallido"
                    else:
                        if(prestacion_serv.jornada=="completa"):
                            diccionario["mensaje_error"] = profesional.identidad.usuario.get_full_name() + " solo tiene media jornada disponible para la fecha seleccionada"
                            diccionario["accion"] = "fallido"
                        else:
                            agenda = Agenda(fecha=fecha_seleccionada,prestacion_servicio=prestacion_serv,colaborador=profesional)
                            agenda.save()
                            diccionario["accion"] = "agendado"
                else:
                    agenda = Agenda(fecha=fecha_seleccionada,prestacion_servicio=prestacion_serv,colaborador=profesional)
                    agenda.save()
                    diccionario["accion"] = "agendado"
            else: 
                diccionario["accion"] = "fallido"
                diccionario["mensaje_error"] = "la fecha seleccionada es anterior a la fecha actual"
        except Exception as error:
            diccionario["accion"] = "fallido"
            diccionario["agenda"] = None
            diccionario["mensaje_error"] = str(error)
    return render(request,"index.html",diccionario)

def mostrar_politica_tratamiento_datos(request):
    diccionario = {
        "pagina": "politica_tratamiento_datos",
        "complemento_titulo": "- Política de tratamiento de datos",
        "nombre_usuario": verificar_sesion(request)
    }
    diccionario = obtener_datos_usuario(diccionario)
    return render(request, "index.html",diccionario)

def mostrar_terminos_condiciones(request):
    diccionario = {
        "pagina": "terminos_condiciones",
        "complemento_titulo": "- Términos y condiciones",
        "nombre_usuario": verificar_sesion(request)
    }
    diccionario = obtener_datos_usuario(diccionario)
    return render(request, "index.html",diccionario)

def mostrar_conocenos(request):
    diccionario = {
        "pagina": "conocenos",
        "complemento_titulo": "- Conócenos",
        "nombre_usuario": verificar_sesion(request)
    }
    diccionario = obtener_datos_usuario(diccionario)
    return render(request, "index.html",diccionario)

@login_required(login_url='/ingreso/')
def cerrar_sesion(request):
    nombre_usuario = verificar_sesion(request)
    if(nombre_usuario!=""):
        logout(request)
    return redirect("mostrar_inicio")

@login_required(login_url='/ingreso/')
def mostrar_pasarela_pago(request,cod_factura):
    diccionario = {
        "pagina": "pasarela",
        "complemento_titulo": "- Pasarela de pago",
        "nombre_usuario": verificar_sesion(request)
    }
    diccionario = obtener_datos_usuario(diccionario)
    factura = Factura.objects.get(id=cod_factura)
    valor_a_pagar = factura.valor
    diccionario["valor_a_pagar"] = valor_a_pagar
    diccionario["numero_factura"] = factura.id
    return render(request,"index.html",diccionario)

@login_required(login_url='/ingreso/')
def mostrar_gestion_pedidos(request):
    diccionario = {
        "pagina": "gestion_pedidos",
        "complemento_titulo": "- Gestión de pedidos",
        "nombre_usuario": verificar_sesion(request),
        "accion": "inicio"
    }
    diccionario = obtener_datos_usuario(diccionario)
    diccionario = obtener_datos_fecha(diccionario)
    usuario_ = User.objects.get(username=diccionario["correo_usuario"])
    identidad_ = Identidad.objects.get(usuario=usuario_)
    cliente_ = ClientePersona.objects.get(identidad=identidad_)
    if(request.POST):
        try:
            fecha_seleccionada = request.POST["nmBusqFecha"]
            fecha_seleccionada = datetime.strptime(fecha_seleccionada, '%Y-%m-%d').date()
            diccionario["correo_usuario"]
            diccionario["agenda"] = Agenda.objects.filter(fecha = fecha_seleccionada, prestacion_servicio__pedido__cliente_cotizante=cliente_)
            diccionario["fecha_seleccionada"] = str(fecha_seleccionada)
        except Exception as error:
            diccionario["agenda"] = None
            diccionario["mensaje_error"] = str(error)
    else:
        diccionario["agenda"] = Agenda.objects.filter(fecha=datetime.now().date(), prestacion_servicio__pedido__cliente_cotizante=cliente_)
        diccionario["fecha_seleccionada"] = str(datetime.strptime(str(datetime.now().date()),'%Y-%m-%d').date())
    diccionario["prestaciones_servicio"] = PrestacionServicio.objects.filter(pedido__cliente_cotizante = cliente_)
    diccionario["colaboradoras"] = Colaborador.objects.filter(Q(categoria="asignable") & Q(estado="activo"))
    return render(request, "index.html",diccionario)

@login_required(login_url='/ingreso/')
def asignar_agenda_cliente(request):
    diccionario = {
        "pagina": "gestion_pedidos",
        "complemento_titulo": "- Gestión de pedidos",
        "nombre_usuario": verificar_sesion(request),
        "accion": "inicio"
    }
    if(request.POST):
        try:
            fecha_aplicacion = request.POST["nmFechaAsignacion"]
            id_prestacion_serv = request.POST["nmSlcPrestacionServicioAsignacion"]
            id_profesional = request.POST["nmSlcColaboradoraAsignacion"]
            fecha_seleccionada = datetime.strptime(fecha_aplicacion, '%Y-%m-%d').date()
            diccionario["agenda"] = Agenda.objects.filter(fecha = fecha_seleccionada)
            diccionario["fecha_seleccionada"] = str(fecha_seleccionada)
            diccionario = obtener_datos_usuario(diccionario)
            diccionario = obtener_datos_fecha(diccionario)

            prestacion_serv = PrestacionServicio.objects.get(id=id_prestacion_serv)
            profesional = Colaborador.objects.get(id=id_profesional)
            resultado = Agenda.objects.filter(fecha=fecha_aplicacion,colaborador=profesional).first()

            if(datetime.now().date()<=fecha_seleccionada):
                if(resultado is not None):
                    if(resultado.prestacion_servicio.jornada=="completa" or resultado.prestacion_servicio.jornada==prestacion_serv.jornada):
                        diccionario["mensaje_error"] = profesional.identidad.usuario.get_full_name() + " ya tiene la jornada ocupada para la fecha seleccionada"
                        diccionario["accion"] = "fallido"
                    else:
                        if(prestacion_serv.jornada=="completa"):
                            diccionario["mensaje_error"] = profesional.identidad.usuario.get_full_name() + " solo tiene media jornada disponible para la fecha seleccionada"
                            diccionario["accion"] = "fallido"
                        else:
                            agenda = Agenda(fecha=fecha_seleccionada,prestacion_servicio=prestacion_serv,colaborador=profesional)
                            agenda.save()
                            diccionario["accion"] = "agendado"
                else:
                    agenda = Agenda(fecha=fecha_seleccionada,prestacion_servicio=prestacion_serv,colaborador=profesional)
                    agenda.save()
                    diccionario["accion"] = "agendado"
            else: 
                diccionario["accion"] = "fallido"
                diccionario["mensaje_error"] = "la fecha seleccionada es anterior a la fecha actual"
        except Exception as error:
            diccionario["accion"] = "fallido"
            diccionario["agenda"] = None
            diccionario["mensaje_error"] = str(error)
    return render(request,"index.html",diccionario)


def crear_fuente_pago(session_id, token, customer_email):
    url = "https://api.wompi.sv/v1/payment_sources"
    payload = {
        "session_id": session_id,
        "type": "CARD",
        "token": token,
        "customer_email": customer_email
    }

    headers = {
        "Authorization": "prv_prod_n9VZMSmkeBmhaASKUpk7ns3FzOyUdK8i",
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        payment_source_id = response.json()["id"]
        # Realiza acciones adicionales con el ID de la fuente de pago
        return payment_source_id
    else:
        # Maneja errores y muestra mensajes adecuados
        return None

def crear_transaccion(request):
    diccionario = {
        "nombre_usuario": verificar_sesion(request)
    }
    diccionario = obtener_datos_usuario(diccionario)
    session_id_front = request.POST["nmidSession"]
    session_id = session_id_front
    token = "eyJhbGciOiJIUzI1NiJ9.eyJjb250cmFjdF9pZCI6NDEsInBlcm1hbGluayI6Imh0dHBzOi8vd29tcGkuY29tL2Fzc2V0cy9kb3dubG9hZGJsZS9UQy1Vc3Vhcmlvcy1Db2xvbWJpYS5wZGYiLCJmaWxlX2hhc2giOiJiZjcyMmFjZDExYzRjMzQzMTVjMDg1NWIyMmIyOGI5OSIsImppdCI6IjE2ODkwOTg3MzEtNjE1ODEiLCJlbWFpbCI6IiIsImV4cCI6MTY4OTEwMjMzMX0.TZd2VWvBSoxCCR5XJMbGdC3CsPRmzWKIj8AWZHMM7Es"
    correo_cliente = diccionario["correo_usuario"]
    id_fuente_de_pago = crear_fuente_pago(session_id,token,correo_cliente)
    if id_fuente_de_pago is not None:
        # Realiza acciones adicionales si la fuente de pago se creó correctamente
        return HttpResponse("Fuente de pago creada exitosamente.")
    else:
        # Maneja errores y muestra mensajes adecuados
        return HttpResponse("Error al crear la fuente de pago.")
    
def mostrar_pasarela_pay_pal(request):
    return render(request,"pasarelaPago_paypal.html")

def actualizar_estado_prestac_serv(request,id_factura):
    factura = Factura.objects.get(id=id_factura)
    factura.estado = "pagado"
    factura.save()
    pedido_ = factura.pedido
    pedido_.estado = "confirmado"
    pedido_.save()
    prestac_servicio = PrestacionServicio.objects.filter(pedido=pedido_)
    for elemento in prestac_servicio:
        elemento.estado = "abierto"
        elemento.save()
    return redirect('mostrar_inicio')