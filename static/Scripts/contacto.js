var datosUsuario = ""
ValidarSoloNumeros()
ValidarContenido()

function ValidarContenido(){
    var configuracionPagina = document.getElementById("configuracionPagina"),
        accion = document.getElementById("pAccion").innerHTML,
        cuerpo = document.querySelector("body"),
        botonEnviar = document.getElementById("btnEnviarCt")
    datosUsuario = ObtenerDatosUsuario()
    botonEnviar.addEventListener("click",EnviarFormularioContacto)
    if(accion == "enviado" || accion=="fallido"){
        if(accion == "enviado"){
            window.alert("Su mensaje ha sido enviado correctamente, \n gracias por utilizar nuestros servicios, \n pronto nos pondremos en contacto con usted")
        }else{
            let mensajeError = document.getElementById("pMensajeError").innerHTML
            window.alert("Ha ocurrido un error: \n" +  mensajeError + "\n" + "su mensaje no se envió, \n por favor intente nuevamente")
        }   
    }
    cuerpo.removeChild(configuracionPagina)
}

function ValidarSoloNumeros(){
    var input = document.getElementById("txtTelefonoCt")
    input.addEventListener('keydown', function(event) {
    if ((event.keyCode < 48 || event.keyCode > 57) && (event.keyCode < 96 || event.keyCode > 105) && event.keyCode !== 190 && event.keyCode !== 110 && event.keyCode !== 8 && event.keyCode !== 9) {
        event.preventDefault();
    }
    })
}

function ObtenerDatosUsuario(){
    let datos = new Map(), 
        nombreUsuario = document.getElementById("pNombreUsuario").getAttribute("data-nombre_usuario")
    if(nombreUsuario!=""){
        let nombresUsuario = document.getElementById("pNombreUsuario").getAttribute("data-nombres_usuario"),
            apellidosUsuario = document.getElementById("pNombreUsuario").getAttribute("data-apellidos_usuario"),
            correoUsuario = document.getElementById("pNombreUsuario").getAttribute("data-correo_usuario"),
            telefonoUsuario = document.getElementById("pNombreUsuario").getAttribute("data-telefono_usuario"),
            direccionUsuario = document.getElementById("pNombreUsuario").getAttribute("data-direccion_usuario"),
            detallesDireccionUsuario = document.getElementById("pNombreUsuario").getAttribute("data-detalles_direccion_usuario"),
            barrioUsuario = document.getElementById("pNombreUsuario").getAttribute("data-barrio_usuario")
        datos.set("nombreUsuario",nombreUsuario)
        datos.set("nombresUsuario",nombresUsuario)
        datos.set("apellidosUsuario",apellidosUsuario)
        datos.set("correoUsuario",correoUsuario)
        datos.set("telefonoUsuario",telefonoUsuario)
        datos.set("direccionUsuario",direccionUsuario)
        datos.set("detallesDireccionUsuario",detallesDireccionUsuario)
        datos.set("barrioUsuario",barrioUsuario)
        let txtNombres = document.getElementById("txtNombreCt"),
            txtApellidos = document.getElementById("txtApellidoCt"),
            txtCorreo = document.getElementById("txtCorreoCt"),
            txtTelefono = document.getElementById("txtTelefonoCt")
        txtNombres.setAttribute("readonly","")
        txtApellidos.setAttribute("readonly","")
        txtCorreo.setAttribute("readonly","")
        txtTelefono.setAttribute("readonly","")
        txtNombres.value = nombresUsuario
        txtApellidos.value = apellidosUsuario
        txtCorreo.value = correoUsuario
        txtTelefono.value = telefonoUsuario
    }else{
        let vacio = ""
        datos.set("nombreUsuario",vacio)
        datos.set("nombresUsuario",vacio)
        datos.set("apellidosUsuario",vacio)
        datos.set("correoUsuario",vacio)
        datos.set("telefonoUsuario",vacio)
        datos.set("direccionUsuario",vacio)
        datos.set("detallesDireccionUsuario",vacio)
        datos.set("barrioUsuario",vacio)
    }
    let seccionUsuario = document.querySelector("#configuracionUsuario"),
        cuerpo = document.querySelector("body")
    cuerpo.removeChild(seccionUsuario)
    return datos
}

function EnviarFormularioContacto(){
    var nombre = document.getElementById("txtNombreCt"),
        apellido = document.getElementById("txtApellidoCt"),
        correo = document.getElementById("txtCorreoCt"),
        telefono = document.getElementById("txtTelefonoCt"),
        tipoMensaje = document.getElementById("SlctTipoCt"),
        mensaje = document.getElementById("txtMensajeCt"),
        terminosCondiciones = document.getElementById("chkTerminosCt"),
        formulario = document.getElementById("formContacto"),
        alerta = "No fue posible enviar su mensaje, revise los conflictos: \n",
        permitirEnvio = true

    if (nombre.value == ""){
        alerta = alerta + "▪ El campo de nombres no debe estar vacío \n"
        permitirEnvio = false
    }else{
        if(datosUsuario.get("nombresUsuario")!=""){
            if(nombre.value != datosUsuario.get("nombresUsuario")){
                alerta = alerta + "▪ El campo de nombres ha sido alterado y no coincide con la información del usuario \n"
                permitirEnvio = false
            }
        }
    }

    if (apellido.value == ""){
        alerta = alerta + "▪ El campo de apellidos no debe estar vacío \n"
        permitirEnvio = false
    }else{
        if(datosUsuario.get("apellidosUsuario")!=""){
            if(apellido.value != datosUsuario.get("apellidosUsuario")){
                alerta = alerta + "▪ El campo de apellidos ha sido alterado y no coincide con la información del usuario \n"
                permitirEnvio = false
            }
        }
    }

    if (correo.value == ""){
        alerta = alerta + "▪ El campo de correo no debe estar vacío \n"
        permitirEnvio = false
    }else{
        let expresionRegular = /^\w+([\.-]?\w+)*@[\w-]+(\.[\w-]+)*\.\w{2,}$/ 
        if(!expresionRegular.test(correo.value)){
            alerta = alerta + "▪ El correo no tiene formato válido (nombreusuario@servidor.dominio) \n"
            permitirEnvio = false
        }
        if(datosUsuario.get("correoUsuario")!=""){
            if(correo.value != datosUsuario.get("correoUsuario")){
                alerta = alerta + "▪ El campo de correo ha sido alterado y no coincide con la información del usuario \n"
                permitirEnvio = false
            }
        }
    }

    if(telefono.value == "" ){
        alerta = alerta + "▪ El campo de teléfono no debe estar vacío \n"
        permitirEnvio = false
    }else{
        let expresionRegular = /^\d{7,10}$/
        if(!expresionRegular.test(telefono.value)){
            alerta = alerta + "▪ El teléfono no tiene formato válido(Mínimo 7 digitos, máximo 10 y solo números)\n"
            permitirEnvio = false
        }
        if(datosUsuario.get("telefonoUsuario")!=""){
            if(telefono.value != datosUsuario.get("telefonoUsuario")){
                alerta = alerta + "▪ El campo de teléfono ha sido alterado y no coincide con la información del usuario \n"
                permitirEnvio = false
            }
        }
    }

    if(tipoMensaje.value == "" ){
        alerta = alerta + "▪ Seleccione un tipo de mensaje \n"
        permitirEnvio = false
    }

    if(mensaje.value == "" ){
        alerta = alerta + "▪ El campo de mensaje no debe estar vacío \n"
        permitirEnvio = false
    }

    if(!terminosCondiciones.checked){
        alerta = alerta + "▪ Acepte tanto los términos y condiciones como la política de tratamiento de datos \n"
        permitirEnvio = false
    }

    if(permitirEnvio == false){
        window.alert(alerta)
    }else{
        formulario.submit()
    }
}

