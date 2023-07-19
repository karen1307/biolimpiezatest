ValidarContenido()

function ValidarContenido(){
    var configuracionPagina = document.getElementById("configuracionPagina"),
        configuracionUsuario = document.getElementById("configuracionUsuario"),
        accion = document.getElementById("pAccion").innerHTML,
        cuerpo = document.querySelector("body")
    if(accion=="fallido"){
        let mensajeError = document.getElementById("pMensajeError").innerHTML
        window.alert("Ha ocurrido un error: \n" +  mensajeError + "\n" + "no se pudo asignar una nueva contraseña, \n por favor intente nuevamente")
    }
    cuerpo.removeChild(configuracionPagina)
    cuerpo.removeChild(configuracionUsuario)
}

function EnviarFormularioRestablecimientoPase(){
    var pase = document.getElementById("txtPaseRestablec"),
        confirmacionPase = document.getElementById("txtConfirmPaseRestablec"),
        formulario = document.getElementById("formRestablecimientoPase"),
        alerta = "No fue posible restablecer su contraseña, revise los conflictos: \n",
        permitirEnvio = true

    if(pase.value==""){
        alerta = alerta + "▪ El campo de contraseña no debe estar vacío \n"
        permitirEnvio = false
    }

    if(confirmacionPase.value==""){
        alerta = alerta + "▪ El campo de confirmación de contraseña no debe estar vacío \n"
        permitirEnvio = false
    }

    if(pase.value!=confirmacionPase.value){
        alerta = alerta + "▪ Los campos contraseña y confirmación no coinciden \n"
        permitirEnvio = false
    }

    if(permitirEnvio == false){
        window.alert(alerta)
    }else{
        formulario.submit()
    }
    
}