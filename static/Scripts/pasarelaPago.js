var datosUsuario = ObtenerDatosUsuario(),
    sessionID = ""/*,
    valorPagarEntregado = parseInt(document.getElementById("valorPagar").value,10)*/

function ObtenerDatosUsuario(){
    let datos = new Map(), 
        nombreUsuario = document.getElementById("pNombreUsuario").getAttribute("data-nombre_usuario"),
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
    cuerpo.removeChild(confUsuario)
    return datos
}

function Siguiente(){
    var txtvalorPagar = document.getElementById("valorPagar"),
        txtSessionID =  document.getElementById("idSession"),
        formulario = document.getElementById("formInicioPasarelaPago")
    if(parseInt(txtvalorPagar.value,10)!=valorPagarEntregado){
        txtvalorPagar.value = valorPagarEntregado
    }
    if(txtSessionID.value!=sessionID){
        txtSessionID.value = sessionID
    }
    formulario.submit()
}

/*$wompi.initialize(function (data, error) {
    if(error === null) {
        var txtSessionID = document.getElementById("idSession")
        txtSessionID.value = data.sessionId
        sessionID = data.sessionId
    }else{
        console.log("Hay error bro")
    }
});*/
