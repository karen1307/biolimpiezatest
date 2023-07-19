AgregarEventosInterfaz()
ValidarSesion()

function AgregarEventosInterfaz(){
    //Sentencias para el menú lateral de pantallas pequeñas
    var menu = document.querySelector('.menu'),
        menuBtn = document.querySelector('.menu-btn'),
        closeBtn = document.querySelector('.close-btn')
        
    menuBtn.addEventListener("click", () => {
    menu.classList.add('active');
    });

    closeBtn.addEventListener("click", () => {
    menu.classList.remove('active');
    });

    window.addEventListener('beforeunload', function(e) {
        $.ajax({
          url: '/cerrarsesion/',  
          method: 'POST',
          async: false,
        });
      });
}

function ValidarSesion(){
    var nombreUsuario = document.getElementById("pNombreUsuario").getAttribute("data-nombre_usuario"),
        permisosAdministrativos = document.getElementById("pNombreUsuario").getAttribute("data-perm_adm"),
        navegacion = document.getElementById("ulMenuNav"),
        menuIngresar = document.getElementById("liIngreso"),
        menuCuenta = document.getElementById("liCuenta"),
        menuRegistro = document.getElementById("liRegistro"),
        menuAdministrativo = document.getElementById("liAdministrativo")
        
    if(nombreUsuario!=""){
        navegacion.removeChild(menuIngresar)
        navegacion.removeChild(menuRegistro)
        if(permisosAdministrativos!="True"){
            navegacion.removeChild(menuAdministrativo)
        }
    }else{
        navegacion.removeChild(menuCuenta)
        navegacion.removeChild(menuAdministrativo)
    }
}