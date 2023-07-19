var datosUsuario = ObtenerDatosUsuario()
ValidarSoloNumeros()
ValidarContenido()

function ValidarContenido(){
    var configuracionPagina = document.getElementById("configuracionPagina"),
        accion = document.getElementById("pAccion").innerHTML,
        cuerpo = document.querySelector("body")
        mensajeError = document.getElementById("pMensajeError").innerHTML
    if(accion == "fallido" ){
        window.alert("Ha ocurrido un error: \n" +  mensajeError + "\n" + "su mensaje no se envió, \n por favor intente nuevamente")
    }
    cuerpo.removeChild(configuracionPagina)
}

function ValidarSoloNumeros(){
    var input = document.getElementById("txtTelefonoDtsReserva")
    input.addEventListener('keydown', function(event) {
    if ((event.keyCode < 48 || event.keyCode > 57) && (event.keyCode < 96 || event.keyCode > 105) && event.keyCode !== 190 && event.keyCode !== 110 && event.keyCode !== 8 && event.keyCode !== 9) {
        event.preventDefault();
    }
    })
}

function ObtenerDatosUsuario(){
    let datos = new Map(), 
        nombreUsuario = document.getElementById("pNombreUsuario").getAttribute("data-nombre_usuario"),
        selectorDatos = document.getElementById("slcPersonaDtsReserva").querySelectorAll("option"),
        confUsuario = document.getElementById("configuracionUsuario"),
        cuerpo = document.querySelector("body")

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
        selectorDatos[0].setAttribute("selected","")
        let txtNombres = document.getElementById("txtNombreDtsReserva"),
            txtApellidos = document.getElementById("txtApellidoDtsReserva"),
            txtCorreo = document.getElementById("txtCorreoDtsReserva"),
            txtTelefono = document.getElementById("txtTelefonoDtsReserva"),
            slcMunicipio = document.getElementById("slcMunicipioDtsReserva"),
            slcMunicipios = slcMunicipio.querySelectorAll("option"),
            txtDireccion = document.getElementById("txtDireccionDtsReserva"),
            txtDetallesDireccion = document.getElementById("txtDetallesDireccionDtsReserva"),
            txtBarrio = document.getElementById("txtBarrioDtsReserva")
        txtNombres.disabled = true
        txtApellidos.disabled = true
        txtCorreo.disabled = true
        txtTelefono.disabled = true
        slcMunicipio.disabled = true
        txtDireccion.disabled = true
        txtDetallesDireccion.disabled = true
        txtBarrio.disabled = true
        txtNombres.value = nombresUsuario
        txtApellidos.value = apellidosUsuario
        txtCorreo.value = correoUsuario
        txtTelefono.value = telefonoUsuario
        txtDireccion.value = direccionUsuario
        txtDetallesDireccion.value = detallesDireccionUsuario
        txtBarrio.value = barrioUsuario
        for(let i=1; i<slcMunicipios.length;i++){
            if(slcMunicipios[i].innerHTML==datos.get("municipioUsuario")){
                slcMunicipio.selectedIndex = i
                break
            }
        }
    }else{
        let vacio = "",
            slcMunicipio = document.getElementById("slcMunicipioDtsReserva"),
            slcMunicipios = slcMunicipio.querySelectorAll("option")
        datos.set("nombreUsuario",vacio)
        datos.set("nombresUsuario",vacio)
        datos.set("apellidosUsuario",vacio)
        datos.set("correoUsuario",vacio)
        datos.set("telefonoUsuario",vacio)
        datos.set("direccionUsuario",vacio)
        datos.set("detallesDireccionUsuario",vacio)
        datos.set("barrioUsuario",vacio)
        slcMunicipio.selectedIndex = 0
        selectorDatos[2].innerHTML = "Mí, sin cuenta"
        selectorDatos[2].setAttribute("selected","")
        for(let i=0; i<selectorDatos.length-1; i++){
            selectorDatos[i].setAttribute("disabled","")
        }
    }
    cuerpo.removeChild(confUsuario)
    return datos
}

function SeleccionarTipoRelleno(){
    var selectorTipoRelleno = document.getElementById("slcPersonaDtsReserva")
        index_seleccionado = selectorTipoRelleno.selectedIndex
    switch(index_seleccionado){
        case 0:
            RellenarDatosUsuario()
            break
        case 1:
            RellenarDatosUsuario()
            var direccion_usuario = document.getElementById("txtDireccionDtsReserva"),
                detallesDireccionUsuario = document.getElementById("txtDetallesDireccionDtsReserva"),
                barrio_usuario = document.getElementById("txtBarrioDtsReserva"),
                slcMunicipio = document.getElementById("slcMunicipioDtsReserva")
            slcMunicipio.disabled = false
            direccion_usuario.disabled = false
            detallesDireccionUsuario.disabled = false
            barrio_usuario.disabled = false
            slcMunicipio.selectedIndex = 0
            direccion_usuario.value = "" 
            detallesDireccionUsuario.value = ""
            barrio_usuario.value = ""
            break
        case 2:
            let formulario = document.getElementById("formDatosReserva")
            formulario.reset()
            selectorTipoRelleno.selectedIndex = 2
            let txtNombres = document.getElementById("txtNombreDtsReserva"),
                txtApellidos = document.getElementById("txtApellidoDtsReserva"),
                txtCorreo = document.getElementById("txtCorreoDtsReserva"),
                txtTelefono = document.getElementById("txtTelefonoDtsReserva"),
                txtDireccion = document.getElementById("txtDireccionDtsReserva"),
                txtDetallesDireccion = document.getElementById("txtDetallesDireccionDtsReserva"),
                txtBarrio = document.getElementById("txtBarrioDtsReserva")
            txtNombres.disabled = false
            txtApellidos.disabled = false
            txtCorreo.disabled = false
            txtTelefono.disabled = false
            slcMunicipio.disabled = false
            txtDireccion.disabled = false
            txtDetallesDireccion.disabled = false
            txtBarrio.disabled = false
            break
    }
}

function RellenarDatosUsuario(){
    let txtNombres = document.getElementById("txtNombreDtsReserva"),
        txtApellidos = document.getElementById("txtApellidoDtsReserva"),
        txtCorreo = document.getElementById("txtCorreoDtsReserva"),
        txtTelefono = document.getElementById("txtTelefonoDtsReserva"),
        slcMunicipio = document.getElementById("slcMunicipioDtsReserva"),
        slcMunicipios = slcMunicipio.querySelectorAll("option"),
        txtDireccion = document.getElementById("txtDireccionDtsReserva"),
        txtDetallesDireccion = document.getElementById("txtDetallesDireccionDtsReserva"),
        txtBarrio = document.getElementById("txtBarrioDtsReserva")
    txtNombres.disabled = true
    txtApellidos.disabled = true
    txtCorreo.disabled = true
    txtTelefono.disabled = true
    slcMunicipio.disabled = true
    txtDireccion.disabled = true
    txtDetallesDireccion.disabled = true
    txtBarrio.disabled = true
    txtNombres.value = datosUsuario.get("nombresUsuario")
    txtApellidos.value = datosUsuario.get("apellidosUsuario")
    txtCorreo.value = datosUsuario.get("correoUsuario")
    txtTelefono.value = datosUsuario.get("telefonoUsuario")
    txtDireccion.value = datosUsuario.get("direccionUsuario")
    txtDetallesDireccion.value = datosUsuario.get("detallesDireccionUsuario")
    txtBarrio.value = datosUsuario.get("barrioUsuario")
    for(let i=1; i<slcMunicipios.length;i++){
        if(slcMunicipios[i].innerHTML==datosUsuario.get("municipioUsuario")){
            slcMunicipio.selectedIndex = i
            break
        }
    }
}

function EnviarFormularioDatosReserva(){
    var personaQueRecibeServicio = document.getElementById("slcPersonaDtsReserva"),
        nombre = document.getElementById("txtNombreDtsReserva"),
        apellido = document.getElementById("txtApellidoDtsReserva"),
        correo =  document.getElementById("txtCorreoDtsReserva"),
        telefono = document.getElementById("txtTelefonoDtsReserva"),
        municipio = document.getElementById("slcMunicipioDtsReserva"),
        direccion = document.getElementById("txtDireccionDtsReserva"),
        detalles_direccion = document.getElementById("txtDetallesDireccionDtsReserva"),
        barrio = document.getElementById("txtBarrioDtsReserva"),
        terminosCondiciones = document.getElementById("chkTerminosDtsReserva"),
        idServicio = document.getElementById("txtServicioDtsReserva"),
        formulario = document.getElementById("formDatosReserva"),
        alerta = "No es posible continuar con la reserva del servicio, revise los conflictos: \n",
        permitirEnvio = true

    if (nombre.value == ""){
        alerta = alerta + "▪ El campo de nombres no debe estar vacío \n"
        permitirEnvio = false
    }else{
        if((personaQueRecibeServicio == 0 || personaQueRecibeServicio == 1) && nombre.value != datosUsuario.get("nombresUsuario")){
            alerta = alerta + "▪ El campo de nombres ha sido alterado y no coincide con la información del usuario \n"
            permitirEnvio = false
        }
    }

    if (apellido.value == ""){
        alerta = alerta + "▪ El campo de apellidos no debe estar vacío \n"
        permitirEnvio = false
    }else{
        if((personaQueRecibeServicio == 0 || personaQueRecibeServicio == 1) && apellido.value != datosUsuario.get("apellidosUsuario")){
            alerta = alerta + "▪ El campo de apellidos ha sido alterado y no coincide con la información del usuario \n"
            permitirEnvio = false
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
        if((personaQueRecibeServicio == 0 || personaQueRecibeServicio == 1) && correo.value != datosUsuario.get("correoUsuario")){
            alerta = alerta + "▪ El campo de correo ha sido alterado y no coincide con la información del usuario \n"
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
        if((personaQueRecibeServicio == 0 || personaQueRecibeServicio == 1) && telefono.value != datosUsuario.get("telefonoUsuario")){
            alerta = alerta + "▪ El campo de teléfono ha sido alterado y no coincide con la información del usuario \n"
            permitirEnvio = false
        }
    }

    if(municipio.value == ""){
        alerta = alerta + "▪ Seleccione un municipio \n"
        permitirEnvio = false
    }

    if(direccion.value == ""){
        alerta = alerta + "▪ El campo de dirección no debe estar vacío \n"
        permitirEnvio = false
    }else{
        if(personaQueRecibeServicio == 0 && direccion.value != datosUsuario.get("direccionUsuario")){
            alerta = alerta + "▪ El campo de dirección ha sido alterado y no coincide con la información del usuario \n"
            permitirEnvio = false
        }
    }

    if(barrio.value == ""){
        alerta = alerta + "▪ El campo de barrio no debe estar vacío \n"
        permitirEnvio = false
    }else{
        if(personaQueRecibeServicio == 0 && barrio.value != datosUsuario.get("barrioUsuario")){
            alerta = alerta + "▪ El campo de barrio ha sido alterado y no coincide con la información del usuario \n"
            permitirEnvio = false
        }
    }

    if(!terminosCondiciones.checked){
        alerta = alerta + "▪ Acepte tanto los términos y condiciones como la política de tratamiento de datos \n"
        permitirEnvio = false
    }

    if(idServicio == ""){
        alerta = alerta + "▪ El campo de id de servicio no debe estar vacío \n"
        permitirEnvio = false
    }

    if(permitirEnvio == false){
        window.alert(alerta)
    }else{
        //window.location.href = "/agenda/"
        if(idServicio.value=="1"){
            formulario.setAttribute("action","/reserva/limpieza/hogar")
        }else{
            formulario.setAttribute("action","/reserva/limpieza/oficina")
        }
        nombre.disabled = false
        apellido.disabled = false
        correo.disabled = false
        telefono.disabled = false
        municipio.disabled = false
        direccion.disabled = false
        detalles_direccion.disabled = false
        barrio.disabled = false
        formulario.submit()
    }
    
}

