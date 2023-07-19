ValidarContenido()

function ValidarContenido(){
    var configuracionPagina = document.getElementById("configuracionPagina"),
        configuracionUsuario = document.getElementById("configuracionUsuario"),
        accion = document.getElementById("pAccion").innerHTML,
        cuerpo = document.querySelector("body")
    if(accion == "enviado" || accion=="fallido"){
        if(accion == "enviado"){
            window.alert("Se ha enviado un enlace de recuperación a su correo electrónico")
        }else{
            let mensajeError = document.getElementById("pMensajeError").innerHTML
            window.alert("Ha ocurrido un error: \n" +  mensajeError + "\n" + "no se pudo generar enlace de recuperación, \n por favor intente nuevamente")
        }   
    }
    cuerpo.removeChild(configuracionPagina)
    cuerpo.removeChild(configuracionUsuario)
}

function EnviarFormularioRecuperacion(){
    var correo = document.getElementById("txtCorreoRec"),
        formulario = document.getElementById("formRecuperacionAcceso"),
        alerta = "No fue posible enviar un enlace de recuperación, revise los conflictos: \n",
        permitirEnvio = true

    if (correo.value == ""){
        alerta = alerta + "▪ El campo de correo no debe estar vacío \n"
        permitirEnvio = false
    }else{
        let expresionRegular = /^\w+([\.-]?\w+)*@[\w-]+(\.[\w-]+)*\.\w{2,}$/ 
        if(!expresionRegular.test(correo.value)){
            alerta = alerta + "▪ El correo no tiene formato válido (nombreusuario@servidor.dominio) \n"
            permitirEnvio = false
        }
    }

    if(permitirEnvio == false){
        window.alert(alerta)
    }else{
        formulario.submit()
    }
}