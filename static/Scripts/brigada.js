var datosUsuario = ObtenerDatosUsuario()
let boton = document.getElementById("botonesTipoEspacio").querySelector(".esp_activo")
SeleccionarTipoEspacio(boton)
ValidarSoloNumeros()
ValidarContenido()

function ValidarContenido(){
    var configuracionPagina = document.getElementById("configuracionPagina"),
        accion = document.getElementById("pAccion").innerHTML,
        cuerpo = document.querySelector("body")
    if(accion == "enviado" || accion=="fallido"){
        if(accion == "enviado"){
            window.alert("Sus datos para cotizar servicio de Brigada han sido enviados correctamente, \n pronto nos pondremos en contacto con usted, \n gracias por utilizar nuestros servicios")
        }else{
            let mensajeError = document.getElementById("pMensajeError").innerHTML
            window.alert("Ha ocurrido un error, \n" +  mensajeError + "\n" + "sus datos para cotizar servicio de Brigada no se enviaron, \n por favor intente nuevamente")
        }   
    }
    cuerpo.removeChild(configuracionPagina)
}

function SeleccionarTipoEspacio(boton){
    var botones = boton.parentNode.querySelectorAll("button"),
        txtEspacio = document.getElementById("txtEspacioCtzBrigada")
    for(let i=0; i<botones.length;i++){
        if(botones[i]==boton){
            botones[i].setAttribute("class","esp_activo")
            txtEspacio.value = botones[i].innerHTML
            txtEspacio.setAttribute("value",botones[i].innerHTML)
        }else{
            botones[i].setAttribute("class","esp_inactivo")
        }
    }
}

function ValidarSoloNumeros(){
    var input = document.getElementById("txtTelefonoCtzBrigada")
    input.addEventListener('keydown', function(event) {
    if ((event.keyCode < 48 || event.keyCode > 57) && (event.keyCode < 96 || event.keyCode > 105) && event.keyCode !== 190 && event.keyCode !== 110 && event.keyCode !== 8 && event.keyCode !== 9) {
        event.preventDefault();
    }
    })
}

function ObtenerDatosUsuario(){
    let datos = new Map(), 
        nombreUsuario = document.getElementById("pNombreUsuario").getAttribute("data-nombre_usuario"),
        selectorDatos = document.getElementById("slcPersonaCtzBrigada").querySelectorAll("option")
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
        let txtNombres = document.getElementById("txtNombreCtzBrigada"),
            txtApellidos = document.getElementById("txtApellidoCtzBrigada"),
            txtCorreo = document.getElementById("txtCorreoCtzBrigada"),
            txtTelefono = document.getElementById("txtTelefonoCtzBrigada"),
            slcMunicipio = document.getElementById("slcMunicipioCtzBrigada"),
            slcMunicipios = slcMunicipio.querySelectorAll("option"),
            txtDireccion = document.getElementById("txtDireccionCtzBrigada"),
            txtDetallesDireccion = document.getElementById("txtDetallesDireccionCtzBrigada"),
            txtBarrio = document.getElementById("txtBarrioCtzBrigada")
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
            if(slcMunicipios.innerHTML==datos.get("municipio")){
                slcMunicipio.selectedIndex = i
                break
            }
        }
    }else{
        let vacio = "",
            slcMunicipio = document.getElementById("slcMunicipioCtzBrigada")
        datos.set("nombreUsuario",vacio)
        datos.set("nombresUsuario",vacio)
        datos.set("apellidosUsuario",vacio)
        datos.set("correoUsuario",vacio)
        datos.set("telefonoUsuario",vacio)
        datos.set("municipioUsuario",vacio)
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
    var configuracionUsuario = document.getElementById("configuracionUsuario"),
        cuerpo = document.querySelector("body")
    cuerpo.removeChild(configuracionUsuario)
    return datos
}

function SeleccionarTipoRelleno(){
    var selectorTipoRelleno = document.getElementById("slcPersonaCtzBrigada")
        index_seleccionado = selectorTipoRelleno.selectedIndex
    switch(index_seleccionado){
        case 0:
            RellenarDatosUsuario()
            break
        case 1:
            RellenarDatosUsuario()
            let direccion_usuario = document.getElementById("txtDireccionCtzBrigada"),
                detallesDireccionUsuario = document.getElementById("txtDetallesDireccionCtzBrigada"),
                barrio_usuario = document.getElementById("txtBarrioCtzBrigada"),
                slcMunicipio = document.getElementById("slcMunicipioCtzBrigada")
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
            let formulario = document.getElementById("formCtzBrigada")
            formulario.reset()
            selectorTipoRelleno.selectedIndex = 2
            let txtNombres = document.getElementById("txtNombreCtzBrigada"),
                txtApellidos = document.getElementById("txtApellidoCtzBrigada"),
                txtCorreo = document.getElementById("txtCorreoCtzBrigada"),
                txtTelefono = document.getElementById("txtTelefonoCtzBrigada"),
                slcMunicipio_ = document.getElementById("slcMunicipioCtzBrigada"),
                txtDireccion = document.getElementById("txtDireccionCtzBrigada"),
                txtDetallesDireccion = document.getElementById("txtDetallesDireccionCtzBrigada"),
                txtBarrio = document.getElementById("txtBarrioCtzBrigada")
            txtNombres.disabled = false
            txtApellidos.disabled = false
            txtCorreo.disabled = false
            txtTelefono.disabled = false
            slcMunicipio_.disabled = false
            txtDireccion.disabled = false
            txtDetallesDireccion.disabled = false
            txtBarrio.disabled = false
            break
    }
}

function RellenarDatosUsuario(){
    let txtNombres = document.getElementById("txtNombreCtzBrigada"),
        txtApellidos = document.getElementById("txtApellidoCtzBrigada"),
        txtCorreo = document.getElementById("txtCorreoCtzBrigada"),
        txtTelefono = document.getElementById("txtTelefonoCtzBrigada"),
        slcMunicipio = document.getElementById("slcMunicipioCtzBrigada"),
        slcMunicipios = slcMunicipio.querySelectorAll("option"),
        txtDireccion = document.getElementById("txtDireccionCtzBrigada"),
        txtDetallesDireccion = document.getElementById("txtDetallesDireccionCtzBrigada"),
        txtBarrio = document.getElementById("txtBarrioCtzBrigada")
    txtNombres.disabled = true
    txtApellidos.disabled = true
    txtCorreo.disabled = true
    txtTelefono.disabled = true
    txtDireccion.disabled = true
    slcMunicipio.disabled = true
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
        if(slcMunicipios.innerHTML==datosUsuario.get("municipio")){
            slcMunicipio.selectedIndex = i
            break
        }
    }
}

function EnviarFormularioBrigada(){
    var clienteReceptor = document.getElementById("slcPersonaCtzBrigada"),
        nombres = document.getElementById("txtNombreCtzBrigada"),
        apellidos = document.getElementById("txtApellidoCtzBrigada"),
        correo = document.getElementById("txtCorreoCtzBrigada"),
        telefono = document.getElementById("txtTelefonoCtzBrigada"),
        municipio = document.getElementById("slcMunicipioCtzBrigada"),
        tipoEspacio = document.getElementById("txtEspacioCtzBrigada"),
        direccion = document.getElementById("txtDireccionCtzBrigada"),
        detalles_direccion = document.getElementById("txtDetallesDireccionCtzBrigada"),
        barrio = document.getElementById("txtBarrioCtzBrigada")
        metrosCuadEspacio = document.getElementById("txtMetrosEspacioCtzBrigada"),
        numPuestosTrabajo = document.getElementById("txtNroPuestosTrabajoCtzBrigada"),
        numCocinetas = document.getElementById("txtNroCocinetasCtzBrigada"),
        numBanios = document.getElementById("txtNroBanosCtzBrigada"),
        terminosCondiciones = document.getElementById("chkTerminosCtzBrigada"),
        formulario = document.getElementById("formCtzBrigada"),
        alerta = "No fue posible enviar sus datos para cotizar el servicio de Brigada, revise los conflictos: \n",
        permitirEnvio = true

    if(nombres.value == ""){
        alerta = alerta + "▪ El campo de nombres no debe estar vacío \n"
        permitirEnvio = false
    }else{
        if(datosUsuario.get("nombresUsuario")!=""){
            if(nombres.value != datosUsuario.get("nombresUsuario") && (clienteReceptor.value=="0" || clienteReceptor.value=="1")){
                alerta = alerta + "▪ El campo de nombres ha sido alterado y no coincide con la información del usuario \n"
                permitirEnvio = false
            }
        }
    }
    
    if(apellidos.value == ""){
        alerta = alerta + "▪ El campo de apellidos no debe estar vacío \n"
        permitirEnvio = false
    }else{
        if(datosUsuario.get("nombresUsuario")!=""){
            if(apellidos.value != datosUsuario.get("apellidosUsuario") && (clienteReceptor.value=="0" || clienteReceptor.value=="1")){
                alerta = alerta + "▪ El campo de apellidos ha sido alterado y no coincide con la información del usuario \n"
                permitirEnvio = false
            }
        }
    }
        
    if(correo.value == ""){
        alerta = alerta + "▪ El campo de correo no debe estar vacío \n"
        permitirEnvio = false
    }else{
        let expresionRegular = /^\w+([\.-]?\w+)*@[\w-]+(\.[\w-]+)*\.\w{2,}$/ 
        if(!expresionRegular.test(correo.value)){
            alerta = alerta + "▪ El correo no tiene formato válido (nombreusuario@servidor.dominio) \n"
            permitirEnvio = false
        }
        if(correo.value != datosUsuario.get("correoUsuario") && (clienteReceptor.value=="0" || clienteReceptor.value=="1")){
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
        if(telefono.value != datosUsuario.get("telefonoUsuario") && (clienteReceptor.value=="0" || clienteReceptor.value=="1")){
            alerta = alerta + "▪ El campo de teléfono ha sido alterado y no coincide con la información del usuario \n"
            permitirEnvio = false
        }
    }

    if(municipio.value == ""){
        alerta = alerta + "▪ Seleccione su municipio de residencia \n"
        permitirEnvio = false
    }

    if(tipoEspacio.value == ""){
        alerta = alerta + "▪ El campo de tipo de espacio no debe estar vacío \n"
        permitirEnvio = false
    }

    if(direccion.value == ""){
        alerta = alerta + "▪ El campo de dirección no debe estar vacío \n"
        permitirEnvio = false
    }else{
        if(datosUsuario.get("nombresUsuario")!=""){
            if(direccion.value != datosUsuario.get("direccionUsuario") && clienteReceptor.value=="0"){
                alerta = alerta + "▪ El campo de dirección ha sido alterado y no coincide con la información del usuario \n"
                permitirEnvio = false
            }

            if(detalles_direccion.value != datosUsuario.get("detallesDireccionUsuario") && clienteReceptor.value=="0"){
                alerta = alerta + "▪ El campo de detalles dirección ha sido alterado y no coincide con la información del usuario \n"
                permitirEnvio = false
            }
        }
    }

    if(barrio.value == ""){
        alerta = alerta + "▪ El campo de barrio no debe estar vacío \n"
        permitirEnvio = false
    }else{
        if(datosUsuario.get("nombresUsuario")!=""){
            if(barrio.value != datosUsuario.get("barrioUsuario") && clienteReceptor.value=="0"){
                alerta = alerta + "▪ El campo de barrio ha sido alterado y no coincide con la información del usuario \n"
                permitirEnvio = false
            }
        }
    }

    if(metrosCuadEspacio.value == ""){
        alerta = alerta + "▪ El campo de número de metros cuadrados del espacio no debe estar vacío \n"
        permitirEnvio = false
    }else{
        try {
            let num = parseInt(metrosCuadEspacio.value,10)
            if(num<=0){
                alerta = alerta + "▪ El número de metros cuadrados del espacio no puede ser menor o igual a cero \n"
                permitirEnvio = false
            }
        } catch (e) {
            alerta = alerta + "▪ El número de metros cuadrados del espacio no tiene formato válido (número) \n"
            permitirEnvio = false
        }
    }

    if(numPuestosTrabajo.value == ""){
        alerta = alerta + "▪ El campo de número de puestos de trabajo no debe estar vacío \n"
        permitirEnvio = false
    }else{
        try {
            let num = parseInt(numPuestosTrabajo.value,10)
            if(num<0){
                alerta = alerta + "▪ El número de puestos de trabajo no puede ser negativo \n"
                permitirEnvio = false
            }
        } catch (e) {
            alerta = alerta + "▪ El número de puestos de trabajo no tiene formato válido (número) \n"
            permitirEnvio = false
        }
    }

    if(numCocinetas.value == ""){
        alerta = alerta + "▪ El campo de número de cocinetas no debe estar vacío \n"
        permitirEnvio = false
    }else{
        try {
            let num = parseInt(numCocinetas.value,10)
            if(num<0){
                alerta = alerta + "▪ El número de cocinetas no puede ser negativo \n"
                permitirEnvio = false
            }
        } catch (e) {
            alerta = alerta + "▪ El número de cocinetas no tiene formato válido (número) \n"
            permitirEnvio = false
        }
    }

    if(numBanios.value == ""){
        alerta = alerta + "▪ El campo de número de baños no debe estar vacío \n"
        permitirEnvio = false
    }else{
        try {
            let num = parseInt(numBanios.value,10)
            if(num<0){
                alerta = alerta + "▪ El número de baños no puede ser negativo \n"
                permitirEnvio = false
            }
        } catch (e) {
            alerta = alerta + "▪ El número de baños no tiene formato válido (número) \n"
            permitirEnvio = false
        }
    }

    if(!terminosCondiciones.checked){
        alerta = alerta + "▪ Acepte tanto los términos y condiciones como la política de tratamiento de datos \n"
        permitirEnvio = false
    }

    if(permitirEnvio == false){
        window.alert(alerta)
    }else{
        nombres.disabled = false
        apellidos.disabled = false
        correo.disabled = false
        telefono.disabled = false
        municipio.disabled = false
        direccion.disabled = false
        detalles_direccion.disabled = false
        barrio.disabled = false
        tipoEspacio.disabled = false
        formulario.submit()
    }
}

