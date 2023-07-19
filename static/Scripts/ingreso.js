ValidarContenido()

function ValidarContenido(){
    var configuracionUsuario = document.getElementById("configuracionUsuario"),
        configuracionPagina =  document.getElementById("configuracionPagina"),
        accion = document.getElementById("pAccion").innerHTML,
        cuerpo = document.querySelector("body")
    if(accion=="creado"){
        window.alert("Su usuario ha sido creado correctamente, \n ya puede iniciar sesión, \n gracias por utilizar nuestros servicios")
    }else{
        if(accion!="inicio"){
            if (accion=="errorUsuario"){
                window.alert("El usuario indicado no está registrado en la base de datos")
            }else{
                if(accion=="errorPase"){
                    window.alert("La contraseña es incorrecta")
                }
            } 
        }
    }
    cuerpo.removeChild(configuracionUsuario)
    cuerpo.removeChild(configuracionPagina)
}

function IniciarSesion(){
    var correo = document.getElementById("txtCorreoIng"),
        pase = document.getElementById("txtPaseIng"),
        formulario = document.getElementById("formIngreso"),
        alerta = "No es posible iniciar sesión, revise los conflictos: \n",
        permitirIngreso = true

    if(correo.value == ""){
        alerta = alerta + "▪ El campo de correo no debe estar vacío \n"
        permitirIngreso = false
    }else{
        let expresionRegular = /^\w+([\.-]?\w+)*@[\w-]+(\.[\w-]+)*\.\w{2,}$/ 
        if(!expresionRegular.test(correo.value)){
            alerta = alerta + "▪ El correo no tiene formato válido (nombresusuario@servidor.dominio) \n"
            permitirEnvio = false
        }
    }

    if(pase.value == ""){
        alerta = alerta + "▪ El campo de contraseña no debe estar vacío \n"
        permitirIngreso = false
    }

    if(permitirIngreso == false){
        window.alert(alerta)
    }else{
        formulario.submit()
    }
}