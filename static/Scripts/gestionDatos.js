var datosUsuario = ObtenerDatosUsuario()
ValidarSoloNumeros()
ValidarContenido()

function ValidarContenido(){
    var configuracionPagina = document.getElementById("configuracionPagina"),
        accion = document.getElementById("pAccion").innerHTML,
        cuerpo = document.querySelector("body")
    if(accion == "actualizado" || accion=="fallido"){
        if(accion == "actualizado"){
            window.alert("Sus datos se han actualizado correctamente, \n gracias por utilizar nuestros servicios, \n")
        }else{
            let mensajeError = document.getElementById("pMensajeError").innerHTML
            window.alert("Ha ocurrido un error al actualizar sus datos: \n" +  mensajeError + "\n" + "Por favor intente nuevamente")
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
            municipioUsuario = document.getElementById("pNombreUsuario").getAttribute("data-municipio_usuario"),
            direccionUsuario = document.getElementById("pNombreUsuario").getAttribute("data-direccion_usuario"),
            detallesDireccionUsuario = document.getElementById("pNombreUsuario").getAttribute("data-detalles_direccion_usuario"),
            barrioUsuario = document.getElementById("pNombreUsuario").getAttribute("data-barrio_usuario")
        datos.set("nombreUsuario",nombreUsuario)
        datos.set("nombresUsuario",nombresUsuario)
        datos.set("apellidosUsuario",apellidosUsuario)
        datos.set("correoUsuario",correoUsuario)
        datos.set("telefonoUsuario",telefonoUsuario)
        datos.set("municipioUsuario",municipioUsuario)
        datos.set("direccionUsuario",direccionUsuario)
        datos.set("detallesDireccionUsuario",detallesDireccionUsuario)
        datos.set("barrioUsuario",barrioUsuario)

        let txtNombres = document.getElementById("txtNombreGestDatos"),
            txtApellidos = document.getElementById("txtApellidoGestDatos"),
            txtCorreo = document.getElementById("txtCorreoGestDatos"),
            txtTelefono = document.getElementById("txtTelefonoGestDatos"),
            slcMunicipio = document.getElementById("slcMunicipioGestDatos"),
            slcMunicipios = slcMunicipio.querySelectorAll("option"),
            txtDireccion = document.getElementById("txtDireccionGestDatos"),
            txtDetallesDireccion = document.getElementById("txtDetallesDireccionGestDatos"),
            txtBarrio = document.getElementById("txtBarrioGestDatos"),
            txtNuevoPase = document.getElementById("txtNuevoPaseGestDatos"),
            txtConfirmacionNuevoPase = document.getElementById("chkActualizarPaseGestDatos")
        txtNombres.value = datos.get("nombresUsuario")
        txtApellidos.value = datos.get("apellidosUsuario")
        txtCorreo.value = datos.get("correoUsuario")
        txtTelefono.value = datos.get("telefonoUsuario")
        txtDireccion.value = datos.get("direccionUsuario")
        txtDetallesDireccion.value = datos.get("detallesDireccionUsuario")
        txtBarrio.value = datos.get("barrioUsuario")
        txtConfirmacionNuevoPase.checked = true
        for(let i=1; i<slcMunicipios.length;i++){
            if(slcMunicipios[i].innerHTML==datos.get("municipioUsuario")){
                slcMunicipio.selectedIndex = i
                break
            }
        }
    }else{
        let vacio = ""
        datos.set("nombreUsuario",vacio)
        datos.set("nombresUsuario",vacio)
        datos.set("apellidosUsuario",vacio)
        datos.set("correoUsuario",vacio)
        datos.set("telefonoUsuario",vacio)
        datos.set("direccionUsuario",vacio)
        datos.set("municipioUsuario",vacio)
        datos.set("detallesDireccionUsuario",vacio)
        datos.set("barrioUsuario",vacio)
    }
    cuerpo.removeChild(seccionUsuario)
    return datos
}

function ValidarSoloNumeros(){
    var input = document.getElementById("txtTelefonoGestDatos")
    input.addEventListener('keydown', function(event) {
    if ((event.keyCode < 48 || event.keyCode > 57) && (event.keyCode < 96 || event.keyCode > 105) && event.keyCode !== 190 && event.keyCode !== 110 && event.keyCode !== 8 && event.keyCode !== 9) {
        event.preventDefault();
    }
    })
}

function verificarControladorCambioPase(){
    var checkCambioPase = document.getElementById("chkActualizarPaseGestDatos"),
        txtNuevoPase = document.getElementById("txtNuevoPaseGestDatos"),
        txtConfirmacionNuevoPase = document.getElementById("txtNuevoPaseConfGestDatos")

    if(checkCambioPase.checked){
        txtNuevoPase.classList.remove("inactivo")
        txtConfirmacionNuevoPase.classList.remove("inactivo")
    }else{
        txtNuevoPase.value = ""
        txtConfirmacionNuevoPase.value = ""
        txtNuevoPase.classList.add("inactivo")
        txtConfirmacionNuevoPase.classList.add("inactivo")
    }
}

function ActualizarDatos(){
    var nombres = document.getElementById("txtNombreGestDatos"),
        apellidos = document.getElementById("txtApellidoGestDatos"),
        correo = document.getElementById("txtCorreoGestDatos"),
        telefono = document.getElementById("txtTelefonoGestDatos"),
        municipio = document.getElementById("slcMunicipioGestDatos"),
        direccion = document.getElementById("txtDireccionGestDatos"),
        barrio = document.getElementById("txtBarrioGestDatos"),
        pase = document.getElementById("txtPaseGestDatos"),
        nuevoPase = document.getElementById("txtNuevoPaseGestDatos"),
        confirmacionNuevoPase = document.getElementById("txtNuevoPaseConfGestDatos"),
        cambioPase = document.getElementById("chkActualizarPaseGestDatos"),
        formulario = document.getElementById("formGestionDatos"),
        alerta = "No fue posible actualizar sus datos, revise los conflictos: \n",
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

    if(pase.value==""){
        alerta = alerta + "▪ El campo de contraseña no debe estar vacío \n"
        permitirEnvio = false
    }

    if(cambioPase.checked){
        
        if(nuevoPase.value==""){
            alerta = alerta + "▪ Ha elegido actualizar su contraseña, por lo tanto, el campo de nueva contraseña no debe estar vacío \n"
            permitirEnvio = false
        }

        if(confirmacionNuevoPase.value==""){
            alerta = alerta + "▪ Ha elegido actualizar su contraseña, por lo tanto, el campo de confirmación no debe estar vacío \n"
            permitirEnvio = false
        }

        if(nuevoPase.value!=confirmacionNuevoPase.value){
            alerta = alerta + "▪ La nueva contraseña y su confirmación no coinciden \n"
            permitirEnvio = false
        }
    }
    
    if(permitirEnvio == false){
        window.alert(alerta)
    }else{
        formulario.submit()
    }
}

function PantallaEliminarDatos(){
    window.location.href = "/gestionarmisdatos/eliminarcuenta/";
}