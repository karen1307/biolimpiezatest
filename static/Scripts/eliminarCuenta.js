ValidarContenido()

function ValidarContenido(){
    var configuracionUsuario = document.getElementById("configuracionUsuario"),
        configuracionPagina =  document.getElementById("configuracionPagina"),
        accion = document.getElementById("pAccion").innerHTML,
        cuerpo = document.querySelector("body")
    if(accion == "enviado" || accion=="fallido"){
        if(accion == "enviado"){
            window.alert("Su mensaje ha sido enviado correctamente, \n gracias por utilizar nuestros servicios, \n pronto nos pondremos en contacto con usted")
        }else{
            let mensajeError = document.getElementById("pMensajeError").innerHTML
            window.alert("Ha ocurrido un error: \n" +  mensajeError + "\n" + "su mensaje no se envió, \n por favor intente nuevamente")
        }   
    }
    cuerpo.removeChild(configuracionUsuario)
    cuerpo.removeChild(configuracionPagina)
}

function cancelarEliminacionCuenta(){
    window.location.href = "/";
}

function eliminarCuenta(){
    var pase = document.getElementById("txtPaseEliminacionCuenta"),
        formulario = document.getElementById("formEliminacionCuenta"),
        alerta = "No es posible solicitar la eliminación de su cuenta, revise los conflictos: \n",
        permitirEnvio = true

    if (pase.value == ""){
        alerta = alerta + "▪ El campo de contraseña no debe estar vacío \n"
        permitirEnvio = false
    }

    if(permitirEnvio == false){
        window.alert(alerta)
    }else{
        formulario.submit()
    }
}