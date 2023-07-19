DistribuirCalendarios()
MostrarCalendario("1")
MostrarDiaSeleccionado()
ValidarContenido()

function ValidarContenido(){
    var configuracionPagina = document.getElementById("configuracionPagina"),
        configuracionUsuario = document.getElementById("configuracionUsuario"),
        accion = document.getElementById("pAccion").innerHTML,
        cuerpo = document.querySelector("body")
    if(accion == "agendado" || accion == "fallido"){
        if(accion == "agendado"){
            window.alert("Se ha agendado correctamente a la colaboradora")
        }else{
            let mensajeError = document.getElementById("pMensajeError").innerHTML
            window.alert("Ha ocurrido un error: \n" +  mensajeError + "\n" +  "por favor intente nuevamente")
        }   
    }
    cuerpo.removeChild(configuracionUsuario)
    cuerpo.removeChild(configuracionPagina)
}

function DistribuirCalendarios(){
    var numeroDiasMes = parseInt(document.getElementById("pNumeroDiasMes").innerHTML, 10),
        numeroDiasMesSiguiente = parseInt(document.getElementById("pNumeroDiasMesSiguiente").innerHTML, 10),
        mes = document.getElementById("calendarioMesActual").querySelector("ol"),
        mesSiguiente = document.getElementById("calendarioMesSiguiente").querySelector("ol"),
        diasMes = mes.getElementsByTagName("li"),
        diasMesSiguiente = mesSiguiente.getElementsByTagName("li"),
        diaComienzoMes = document.getElementById("pDiaComienzoMes").innerHTML,
        diaComienzoMesSiguiente = document.getElementById("pDiaComienzoMesSiguiente").innerHTML,
        primerDiaMes = mes.querySelector(".primer_dia"),
        primerDiaMesSiguiente = mesSiguiente.querySelector(".primer_dia_siguiente"),
        diaActual = parseInt(document.getElementById("pDiaActual").innerHTML,10),
        limite = diasMes.length - (31 - parseInt(numeroDiasMes,10))
       
    if(numeroDiasMes < 31){
        for(let i=numeroDiasMes+7; i<diasMes.length; i++){
            diasMes[i].setAttribute("hidden","")
        }
    }

    if(numeroDiasMesSiguiente < 31){
        for(let i=numeroDiasMesSiguiente+7; i<diasMesSiguiente.length; i++){
            diasMesSiguiente[i].setAttribute("hidden","")
        }
    }

    primerDiaMes.setAttribute("style",'grid-column-start: ' + diaComienzoMes + ';')
    primerDiaMesSiguiente.setAttribute("style",'grid-column-start: ' + diaComienzoMesSiguiente + ';')
    diasMes[diaActual+6].classList.add("dia_actual")

    for(let i=7; i<limite;i++){
        diasMes[i].setAttribute("onclick","SeleccionarDia(this)")
    }

    limite = diasMesSiguiente.length - (31 - parseInt(numeroDiasMesSiguiente,10))
    for(let i=7; i<diasMesSiguiente.length;i++){
        diasMesSiguiente[i].setAttribute("onclick","SeleccionarDia(this)")
    }
}

function MostrarCalendario(opcion){
    var calendarioMesActual = document.getElementById("calendarioMesActual"),
        calendarioMesSiguiente = document.getElementById("calendarioMesSiguiente")
    if(opcion=="0"){
        calendarioMesSiguiente.removeAttribute("hidden")
        calendarioMesActual.setAttribute("hidden","")
    }else{
        calendarioMesActual.removeAttribute("hidden")
        calendarioMesSiguiente.setAttribute("hidden","")
    }
}

function SeleccionarDia(casilla){
    var contenedorCalendario = casilla.parentNode.parentNode,
        fecha = "",
        anio = contenedorCalendario.querySelector(".p_anio").innerHTML,
        mes = contenedorCalendario.querySelector(".p_mes").innerHTML,
        dia =  casilla.innerHTML,
        dia_ = parseInt(dia, 10),
        txtFecha = document.getElementById("txtBusqFecha"),
        formulario = document.getElementById("formBusqFecha")
    const equivalenciaMes = {
        "enero": "01",
        "febrero": "02",
        "marzo": "03",
        "abril": "04",
        "mayo": "05",
        "junio": "06",
        "julio": "07",
        "agosto": "08",
        "septiembre": "09",
        "octubre": "10",
        "noviembre": "11",
        "diciembre": "12"
    };
    if (dia_ < 10) {
        dia = "0" + dia
    }
    fecha = anio + "-" + equivalenciaMes[mes] + "-" + dia
    txtFecha.value = fecha
    formulario.submit()
}

function MostrarDiaSeleccionado(){
    var fechaSeleccionada = document.getElementById("pFechaSeleccionada").innerHTML,
        fecha_basica = fechaSeleccionada,
        fechaSeleccionada = fechaSeleccionada + " 00:00:00.0",
        fechaFormateada = new Date(fechaSeleccionada),
        mes = fechaFormateada.getMonth().toString(),
        dia = fechaFormateada.getDate(),
        formulario = document.getElementById("formBusqFecha"),
        txtFechaAsignacion = document.getElementById("txtFechaAsignacion")

    txtFechaAsignacion.value = fecha_basica
    formulario.removeChild(document.getElementById("pFechaSeleccionada"))
    const equivalenciaMes = {
        "0": "enero",
        "1": "febrero",
        "2": "marzo", 
        "3": "abril", 
        "4": "mayo", 
        "5": "junio", 
        "6": "julio", 
        "7": "agosto", 
        "8": "septiembre",
        "9": "octubre", 
        "10": "noviembre", 
        "11": "diciembre" 
    };

    var mesEquivalente = equivalenciaMes[mes],
        etiquetaMesActual = document.getElementById("pMes"),
        etiquetaMesSiguiente = document.getElementById("pMesSiguiente"),
        contenedorMesActual =  etiquetaMesActual.parentNode,
        contenedorMesSiguiente =  etiquetaMesSiguiente.parentNode

    if(etiquetaMesActual.innerHTML == mesEquivalente){
        var etiquetaDeMes = etiquetaMesActual
        contenedorMesActual.removeAttribute("hidden")
        contenedorMesSiguiente.setAttribute("hidden","")     
    }else{
        var etiquetaDeMes = etiquetaMesSiguiente
        contenedorMesSiguiente.removeAttribute("hidden")
        contenedorMesActual.setAttribute("hidden","")     
    }

    var contenedorCalendario = etiquetaDeMes.parentNode.querySelector("ol").querySelectorAll("li"),
        casilla = contenedorCalendario[6+dia]
   casilla.classList.add("itemSeleccionado")
}

function SeleccionarTablero(opcion){
    var btnVerAgenda = document.getElementById("btnVerAgendaAdm"),
        btnAsignarProfesional = document.getElementById("btnAsignarAgendaAdm"),
        contenedorAgendas = document.getElementById("contenedorAgendas"),
        contenedorAsignacion = document.getElementById("contenedorAsignacion")

    switch(opcion){
        case('1'):
            btnVerAgenda.classList.remove("btn_activo_agenda_adm")
            contenedorAgendas.classList.add("contenedor_inactivo")
            btnAsignarProfesional.classList.add("btn_activo_agenda_adm")
            contenedorAsignacion.classList.remove("contenedor_inactivo")
            break
        default:
            btnAsignarProfesional.classList.remove("btn_activo_agenda_adm")
            contenedorAsignacion.classList.add("contenedor_inactivo")
            btnVerAgenda.classList.add("btn_activo_agenda_adm")
            contenedorAgendas.classList.remove("contenedor_inactivo")
            break
    }
}

function asignarProfesional(){
    var txtFechaAsignacion = document.getElementById("txtFechaAsignacion").value + " 23:59:59.0",
        fechaActual = new Date(),
        fechaComparacion = new Date(txtFechaAsignacion),
        alerta = "No es posible asignar profesional, revise los conflictos: \n",
        formulario = document.getElementById("formAgendarPrestServicio"),
        permitirAsignacion = true
    
    if(fechaComparacion.getTime() < fechaActual.getTime()){
        alerta = alerta + "▪ La fecha seleccionada es anterior a la fecha actual \n"
        permitirAsignacion = false
    }

    if(permitirAsignacion == false){
        window.alert(alerta)
    }else{
        formulario.submit()
    }
}