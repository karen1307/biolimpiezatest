ValidarContenido()

function ValidarContenido(){
    var configuracionUsuario = document.getElementById("configuracionUsuario"),
        cuerpo = document.querySelector("body")
    cuerpo.removeChild(configuracionUsuario)
}