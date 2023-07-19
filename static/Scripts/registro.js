var datosUsuario = ObtenerDatosUsuario()
ValidarSoloNumeros()
ValidarContenido()

function ValidarContenido(){
    var configuracionPagina = document.getElementById("configuracionPagina"),
        accion = document.getElementById("pAccion").innerHTML,
        cuerpo = document.querySelector("body")
    if(accion == "creado" || accion=="fallido"){
        if(accion == "creado"){
            window.alert("Su usuario ha sido creado correctamente")
        }else{
            let mensajeError = document.getElementById("pMensajeError").innerHTML
            window.alert("Ha ocurrido un error, \n" +  mensajeError + "\n" + "para crear su usuario, \n por favor intente nuevamente")
        }   
    }
    cuerpo.removeChild(configuracionPagina)
}

function ObtenerDatosUsuario(){
    let datos = new Map(), 
        nombreUsuario = document.getElementById("pNombreUsuario").getAttribute("data-nombre_usuario"),
        cuerpo = document.querySelector("body"),
        seccionUsuario = document.querySelector("#configuracionUsuario")
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
    cuerpo.removeChild(seccionUsuario)
    return datos
}

function ValidarSoloNumeros(){
    var input = document.getElementById("txtTelefonoReg")
    input.addEventListener('keydown', function(event) {
    if ((event.keyCode < 48 || event.keyCode > 57) && (event.keyCode < 96 || event.keyCode > 105) && event.keyCode !== 190 && event.keyCode !== 110 && event.keyCode !== 8 && event.keyCode !== 9) {
        event.preventDefault();
    }
    })
}

function EnviarFormularioRegistro(){
    var nombres = document.getElementById("txtNombreReg"),
        apellidos = document.getElementById("txtApellidoReg"),
        correo = document.getElementById("txtCorreoReg"),
        telefono = document.getElementById("txtTelefonoReg"),
        municipio = document.getElementById("slcMunicipioReg"),
        direccion = document.getElementById("txtDireccionReg"),
        barrio = document.getElementById("txtBarrioReg"),
        pase = document.getElementById("txtPaseReg"),
        confirmacionPase = document.getElementById("txtPaseConfReg"),
        terminosCondiciones = document.getElementById("chkTerminosReg"),
        formulario = document.getElementById("formRegistro"),
        alerta = "No fue posible crear su usuario, revise los conflictos: \n",
        permitirEnvio = true

    if (nombres.value == ""){
        alerta = alerta + "▪ El campo de nombres no debe estar vacío \n"
        permitirEnvio = false
    }

    if (apellidos.value == ""){
        alerta = alerta + "▪ El campo de apellidos no debe estar vacío \n"
        permitirEnvio = false
    }

    if (correo.value == ""){
        alerta = alerta + "▪ El campo de correo no debe estar vacío \n"
        permitirEnvio = false
    }else{
        let expresionRegular = /^\w+([\.-]?\w+)*@[\w-]+(\.[\w-]+)*\.\w{2,}$/ 
        if(!expresionRegular.test(correo.value)){
            alerta = alerta + "▪ El correo no tiene formato válido (nombresusuario@servidor.dominio) \n"
            permitirEnvio = false
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
    }

    if(municipio.value == "" ){
        alerta = alerta + "▪ Seleccione su municipio de residencia \n"
        permitirEnvio = false
    }

    if(direccion.value == "" ){
        alerta = alerta + "▪ El campo de dirección no debe estar vacía \n"
        permitirEnvio = false
    }

    if(barrio.value == "" ){
        alerta = alerta + "▪ El campo de barrio no debe estar vacío \n"
        permitirEnvio = false
    }

    if (pase.value == ""){
        alerta = alerta + "▪ Asigne una contraseña a su cuenta \n"
        permitirEnvio = false
    }

    if (confirmacionPase.value == ""){
        alerta = alerta + "▪ Confirme su contraseña \n"
        permitirEnvio = false
    }

    if(pase.value != confirmacionPase.value){
        alerta = alerta + "▪ La contraseña y su confirmación no coinciden \n"
        permitirEnvio = false
    }

    if(!terminosCondiciones.checked){
        alerta = alerta + "▪ Acepte los términos y condiciones \n"
        permitirEnvio = false
    }

    if(permitirEnvio == false){
        window.alert(alerta)
    }else{
        formulario.submit()
    }
}

