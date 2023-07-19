ValidarContenido()

function ValidarContenido(){
    var configuracionPagina = document.getElementById("configuracionUsuario"),
        cuerpo = document.querySelector("body")
    cuerpo.removeChild(configuracionPagina)
}