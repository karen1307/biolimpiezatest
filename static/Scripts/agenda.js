var cantidadDeServicios = 0,
    algunItemSinConfirmar = false,
    moldeRegistroTabla = MoldearRegistroTabla(),
    agendas = ObtenerAgendas(),
    mapasFechasDisp = [],
    primerVezmapasFechasDisp = true,
    precio_jornada_am = parseInt(document.getElementById("valorMediaJornadaManana").value,10),
    precio_jornada_pm = parseInt(document.getElementById("valorMediaJornadaTarde").value,10),
    precio_jornada_comp = parseInt(document.getElementById("valorJornadaCompleta").value,10),
    totalPagar = 0

DistribuirCalendarios()
MostrarCalendario("1")
OcultarColaboradoras()
VerificarDisponibilidadPorAgenda()
ValidarContenido()

function ValidarContenido(){
    var configuracionUsuario = document.getElementById("configuracionUsuario"),
        //accion = document.getElementById("pAccion").innerHTML,
        tablaContenedoraPedidos = document.getElementById("listaServiciosAgendados"),
        txtValorJornadaCompleta = document.getElementById("valorJornadaCompleta"),
        txtValorMediaJornadaManana = document.getElementById("valorMediaJornadaManana"),
        txtValorMediaJornadaTarde =  document.getElementById("valorMediaJornadaTarde"),
        cuerpo = document.querySelector("body")
    /*if(accion == "agendado" || accion == "fallido"){
        if(accion == "agendado"){
            window.alert("Se ha agendado correctamente a la colaboradora")
        }else{
            let mensajeError = document.getElementById("pMensajeError").innerHTML
            window.alert("Ha ocurrido un error: \n" +  mensajeError + "\n" +  "por favor intente nuevamente")
        }   
    }*/
    cuerpo.removeChild(configuracionUsuario)
    tablaContenedoraPedidos.removeChild(txtValorJornadaCompleta)
    tablaContenedoraPedidos.removeChild(txtValorMediaJornadaManana)
    tablaContenedoraPedidos.removeChild(txtValorMediaJornadaTarde)
    //cuerpo.removeChild(configuracionPagina)
}

function seleccionarNumeroHorasServicio(boton){
    if(algunItemSinConfirmar == true){
        window.alert("Tiene pendiente confirmar o descartar una fecha y jornada seleccionada")
    }else{
        var botones = boton.parentNode.querySelectorAll("button"),
            txtNumeroHorasServicio = document.getElementById("txtNumHorasAgenda"),
            botonesAgendarPor = document.getElementById("botonesAgendarPor").querySelectorAll("button")
        
        const equivalenciaJornada = {
            0: "completa",
            1: "media_am",
            2: "media_pm"
        };

        for(let i=0; i<botones.length; i++){
            if(botones[i]==boton){
                boton.setAttribute("class","hr_activo")
                txtNumeroHorasServicio.value = equivalenciaJornada[i]
                txtNumeroHorasServicio.setAttribute("value",equivalenciaJornada[i])
                if (botonesAgendarPor[0].classList.contains("ag_activo")){
                    VerificarDisponibilidadPorAgenda()
                }else{
                    VerificarDisponibilidadPorColaboradora()
                }
            }else{
                botones[i].setAttribute("class","hr_inactivo")
            }
        }
    }
}

function SeleccionarTipoAgendamiento(boton){
    if(algunItemSinConfirmar == true){
        window.alert("Tiene pendiente confirmar o descartar una fecha y jornada seleccionada")
    }else{
        var botones = boton.parentNode.querySelectorAll("button"),
            selectorColaboradora = document.getElementById("selectorColaboradora"),
            botonesHorario = document.getElementById("botonesHoras").querySelectorAll("button")
        for(let i=0; i<botones.length; i++){
            if(botones[i]==boton){
                botones[i].classList.remove("ag_inactivo")
                botones[i].classList.add("ag_activo")
                selectorColaboradora.selectedIndex = 0
                OcultarColaboradoras()
                if(i==0){
                    selectorColaboradora.setAttribute("disabled","")
                    for(let j=0; j<botonesHorario.length;j++){
                        if(botonesHorario[j].classList.contains("hr_activo")){
                            VerificarDisponibilidadPorAgenda()
                        }
                    }
                }else{
                    selectorColaboradora.removeAttribute("disabled")
                    DeshabilitarCalendario()
                }
            }else{
                botones[i].classList.remove("ag_activo")
                botones[i].classList.add("ag_inactivo")
            }
        }
    }
}

function DistribuirCalendarios(){
    var numeroDiasMes = parseInt(document.getElementById("pNumeroDiasMes").innerHTML, 10),
        numeroDiasMesSiguiente = parseInt(document.getElementById("pNumeroDiasMesSiguiente").innerHTML, 10),
        mes = document.getElementById("calendarioMesActual").querySelector("ol"),
        mesActualCadena = document.getElementById("pMes").innerHTML,
        anioMesActual = document.getElementById("pAnio").innerHTML,
        mesSiguiente = document.getElementById("calendarioMesSiguiente").querySelector("ol"),
        mesSigCadena = document.getElementById("pMesSiguiente").innerHTML,
        anioMesSig = document.getElementById("pAnioSiguiente").innerHTML,
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

    for(let i=7; i<diaActual+6; i++){
        diasMes[i].classList.remove("disponible")
        diasMes[i].classList.add("no_disponible")
    }

    for(let i=diaActual+6; i<limite;i++){
        let diaCasilla = diasMes[i].innerHTML,
            diaCasillaNum = parseInt(diaCasilla, 10),
            anioCasilla = anioMesActual

        if (diaCasillaNum < 10) {
            diaCasilla = "0" + diaCasillaNum
        }
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
        let mesCasilla = equivalenciaMes[mesActualCadena],
            fechaCasilla =  anioCasilla + "-" + mesCasilla + "-" + diaCasilla
        
        diasMes[i].setAttribute("data-fecha",fechaCasilla)
        diasMes[i].classList.remove("disponible")
        diasMes[i].classList.add("no_disponible")
    }

    limite = diasMesSiguiente.length - (31 - parseInt(numeroDiasMesSiguiente,10))
    for(let i=7; i<diasMesSiguiente.length;i++){
        let diaCasilla = diasMesSiguiente[i].innerHTML,
            diaCasillaNum = parseInt(diaCasilla, 10),
            anioCasilla = anioMesSig

        if (diaCasillaNum < 10) {
            diaCasilla = "0" + diaCasillaNum
        }
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
        let mesCasilla = equivalenciaMes[mesSigCadena],
            fechaCasilla =  anioCasilla + "-" + mesCasilla + "-" + diaCasilla
        
        diasMesSiguiente[i].setAttribute("data-fecha",fechaCasilla)
        diasMesSiguiente[i].classList.remove("disponible")
        diasMesSiguiente[i].classList.add("no_disponible")
    }
    inhabilitarDomingos()
}

function inhabilitarDomingos(){
    var numeroDiasMes = parseInt(document.getElementById("pNumeroDiasMes").innerHTML, 10),
        numeroDiasMesSiguiente = parseInt(document.getElementById("pNumeroDiasMesSiguiente").innerHTML, 10),
        mes = document.getElementById("calendarioMesActual").querySelector("ol"),
        mesSiguiente = document.getElementById("calendarioMesSiguiente").querySelector("ol"),
        diasMes = mes.getElementsByTagName("li"),
        diasMesSiguiente = mesSiguiente.getElementsByTagName("li"),
        diaActual = parseInt(document.getElementById("pDiaActual").innerHTML,10),
        primerDiaMes = mes.querySelector(".primer_dia"),
        primerDiaMesSiguiente = mesSiguiente.querySelector(".primer_dia_siguiente"),
        style = getComputedStyle(primerDiaMes),
        columna = style.gridColumnStart,
        ubicador = 7 - columna,
        diaReferencia = parseInt(diasMes[7+ubicador].innerHTML,10),
        acumulador = diaReferencia,
        domingos = []

    while(acumulador <= numeroDiasMes){
        domingos.push(acumulador)
        acumulador = acumulador+7
    }

    for(let i=diaActual+6; i<diasMes.length;i++){
        if(domingos.indexOf(parseInt(diasMes[i].innerHTML,10))!=-1){
            diasMes[i].classList.remove("disponible")
            diasMes[i].removeAttribute("onclick")
            diasMes[i].classList.add("no_disponible")
        }
    }

    style = getComputedStyle(primerDiaMesSiguiente)
    columna = style.gridColumnStart
    ubicador = 7 - columna
    diaReferencia = parseInt(diasMesSiguiente[7+ubicador].innerHTML,10)
    acumulador = diaReferencia
    domingos = []

    while(acumulador <= numeroDiasMes){
        domingos.push(acumulador)
        acumulador = acumulador+7
    }

    for(let i=7; i<diasMesSiguiente.length;i++){
        if(domingos.indexOf(parseInt(diasMesSiguiente[i].innerHTML,10))!=-1){
            diasMesSiguiente[i].classList.remove("disponible")
            diasMesSiguiente[i].removeAttribute("onclick")
            diasMesSiguiente[i].classList.add("no_disponible")
        }
    }
}

function VerificarDisponibilidadPorAgenda(){
    var mes = document.getElementById("calendarioMesActual").querySelector("ol"),
        mesSiguiente = document.getElementById("calendarioMesSiguiente").querySelector("ol"),
        diasMes = mes.getElementsByTagName("li"),
        diasMesSiguiente = mesSiguiente.getElementsByTagName("li"),
        diaActual = parseInt(document.getElementById("pDiaActual").innerHTML,10),
        mes = document.getElementById("pMes").innerHTML,
        mesSiguiente = document.getElementById("pMesSiguiente").innerHTML,
        numeroDiasMes  = parseInt(document.getElementById("pNumeroDiasMes").innerHTML),
        numeroDiasMesSiguiente = parseInt(document.getElementById("pNumeroDiasMesSiguiente").innerHTML),
        selectorColaboradora = document.getElementById("selectorColaboradora").querySelectorAll("option"),
        colaboradoras = [],
        limite = diasMes.length - (31 - parseInt(numeroDiasMes,10)),
        txtNumeroHorasSeleccionado = document.getElementById("txtNumHorasAgenda")
    
    for(let i=1;i<selectorColaboradora.length;i++){
        let colaboradorID = selectorColaboradora[i].getAttribute("value")
        colaboradoras.push(colaboradorID)
    }
    let jornada = txtNumeroHorasSeleccionado.value
    for(let i=diaActual+6;i<limite;i++){
        let disponibilidad = true,
            fechaCont = diasMes[i].getAttribute("data-fecha"),
            fecha = new Date(fechaCont),
            mapa = new Map(),
            colabDisponibles = []
        
        if(primerVezmapasFechasDisp==true){
            mapa.set("fecha",fechaCont)
        }else{
            for(let z=0;z<mapasFechasDisp.length;z++) {
                let item = mapasFechasDisp[z]
                if(item.get("fecha") === fechaCont) {
                  mapa = item
                  z = mapasFechasDisp.length
                }
            }    
        }
        
        if(diasMes[i].classList.contains("dia_actual")){
            fecha.setHours(23)
            fecha.setMinutes(59)
            fecha.setSeconds(59)
        }
        fecha.setDate(fecha.getDate()+1)

        for(let j=0;j<colaboradoras.length;j++){
            let encontrado = false,
                marcado = false
            for(let k=0;k<agendas.length;k++){
                let colaboradorAgenda = agendas[k].get("colaboradorID")
                if(colaboradorAgenda==colaboradoras[j]){
                    encontrado = true
                    let fechaAgenda = agendas[k].get("fecha").toLocaleDateString(),
                        fecha_ = fecha.toLocaleDateString()
                    if(fechaAgenda==fecha_){
                        let jornadaAgenda = agendas[k].get("jornada")
                        if(jornadaAgenda=="completa" || jornadaAgenda==jornada){
                            k = agendas.length
                            marcado = true
                        }else{
                            if(jornada=="completa"){ 
                                k = agendas.length
                                marcado = true
                            }else{
                                colabDisponibles.push(colaboradoras[j]) 
                            }
                        }
                    }
                }
            }
            if(encontrado==false || marcado==false){
                colabDisponibles.push(colaboradoras[j])
            }
        }
        disponibilidad = colabDisponibles.length > 0
        if(disponibilidad==true){
            diasMes[i].classList.remove("no_disponible")
            diasMes[i].classList.add("disponible")
            diasMes[i].setAttribute("onclick","AgregarATabla(this)")
        }else{
            diasMes[i].classList.remove("disponible")
            diasMes[i].classList.add("no_disponible")
            diasMes[i].removeAttribute("onclick")
        }
        mapa.set("colaboradorasDisponibles",colabDisponibles)
        if(primerVezmapasFechasDisp==true){
            mapasFechasDisp.push(mapa)
        }
    }

    limite = diasMesSiguiente.length - (31 - parseInt(numeroDiasMesSiguiente,10))
    for(let i=7;i<limite;i++){
        let disponibilidad = true,
            fechaCont = diasMesSiguiente[i].getAttribute("data-fecha"),
            fecha = new Date(fechaCont),
            mapa = new Map(),
            colabDisponibles = []
        
        if(primerVezmapasFechasDisp==true){
            mapa.set("fecha",fechaCont)
        }else{
            for(let z=0;z<mapasFechasDisp.length;z++) {
                let item = mapasFechasDisp[z]
                if(item.get("fecha") === fechaCont) {
                  mapa = item
                  z = mapasFechasDisp.length
                }
            }    
        }
        
        fecha.setDate(fecha.getDate()+1)
        for(let j=0;j<colaboradoras.length;j++){
            let encontrado = false,
                marcado = false
            for(let k=0;k<agendas.length;k++){
                let colaboradorAgenda = agendas[k].get("colaboradorID")
                if(colaboradorAgenda==colaboradoras[j]){
                    encontrado = true
                    let fechaAgenda = agendas[k].get("fecha").toLocaleDateString(),
                        fecha_ = fecha.toLocaleDateString()
                    if(fechaAgenda==fecha_){
                        let jornadaAgenda = agendas[k].get("jornada")
                        if(jornadaAgenda=="completa" || jornadaAgenda==jornada){
                            k = agendas.length
                            marcado = true
                        }else{
                            if(jornada=="completa"){ 
                                k = agendas.length
                                marcado = true
                            }else{
                                colabDisponibles.push(colaboradoras[j])
                            }
                        }
                    }
                }
            }
            if(encontrado==false || marcado==false){
                colabDisponibles.push(colaboradoras[j])
            }
        }
        disponibilidad = colabDisponibles.length > 0
        if(disponibilidad==true){
            diasMesSiguiente[i].classList.remove("no_disponible")
            diasMesSiguiente[i].classList.add("disponible")
            diasMesSiguiente[i].setAttribute("onclick","AgregarATabla(this)")
        }else{
            diasMesSiguiente[i].classList.remove("disponible")
            diasMesSiguiente[i].classList.add("no_disponible")
            diasMesSiguiente[i].removeAttribute("onclick")
        }
        mapa.set("colaboradorasDisponibles",colabDisponibles)
        if(primerVezmapasFechasDisp==true){
            mapasFechasDisp.push(mapa)
        }
    }
    inhabilitarDomingos()
    primerVezmapasFechasDisp=false
}

function VerificarDisponibilidadPorColaboradora(){
    var mes = document.getElementById("calendarioMesActual").querySelector("ol"),
        mesSiguiente = document.getElementById("calendarioMesSiguiente").querySelector("ol"),
        diasMes = mes.getElementsByTagName("li"),
        diasMesSiguiente = mesSiguiente.getElementsByTagName("li"),
        diaActual = parseInt(document.getElementById("pDiaActual").innerHTML,10),
        mes = document.getElementById("pMes").innerHTML,
        mesSiguiente = document.getElementById("pMesSiguiente").innerHTML,
        numeroDiasMes  = parseInt(document.getElementById("pNumeroDiasMes").innerHTML),
        numeroDiasMesSiguiente = parseInt(document.getElementById("pNumeroDiasMesSiguiente").innerHTML),
        selector = document.getElementById("selectorColaboradora"),
        limite = diasMes.length - (31 - parseInt(numeroDiasMes,10)),
        txtNumeroHorasSeleccionado = document.getElementById("txtNumHorasAgenda")

    if(selector.value != "0"){
        let colaboradorID = selector.value,
            jornada = txtNumeroHorasSeleccionado.value

        for(let i=diaActual+6;i<limite;i++){
            let disponibilidad = true,
                fechaCont = diasMes[i].getAttribute("data-fecha"),
                fecha = new Date(fechaCont)
            if(diasMes[i].classList.contains("dia_actual")){
                fecha.setHours(23)
                fecha.setMinutes(59)
                fecha.setSeconds(59)
            }
            fecha.setDate(fecha.getDate()+1)
            for(let j=0;j<agendas.length;j++){
                let colaboradorAgenda = agendas[j].get("colaboradorID")
                if(colaboradorAgenda==colaboradorID){
                    let fechaAgenda = agendas[j].get("fecha").toLocaleDateString(),
                        fecha_ = fecha.toLocaleDateString()
                    if(fechaAgenda==fecha_){
                        let jornadaAgenda = agendas[j].get("jornada")
                        if(jornadaAgenda=="completa" || jornadaAgenda==jornada){
                            disponibilidad = false
                            j = agendas.length
                        }else{
                            if(jornada=="completa"){
                                disponibilidad = false
                                j = agendas.length
                            }
                        }
                    }
                }
            }
            if(disponibilidad==true){
                diasMes[i].classList.remove("no_disponible")
                diasMes[i].classList.add("disponible")
                diasMes[i].setAttribute("onclick","AgregarATabla(this)")
            }else{
                diasMes[i].classList.remove("disponible")
                diasMes[i].classList.add("no_disponible")
                diasMes[i].removeAttribute("onclick")
            }
        }
    
        limite = diasMesSiguiente.length - (31 - parseInt(numeroDiasMesSiguiente,10))
        for (let i=7;i<limite;i++){
            let disponibilidad = true,
                fechaCont = diasMesSiguiente[i].getAttribute("data-fecha"),
                fecha = new Date(fechaCont)
            
            fecha.setDate(fecha.getDate()+1)
            for(let j=0;j<agendas.length;j++){
                let colaboradorAgenda = agendas[j].get("colaboradorID")
                if(colaboradorAgenda==colaboradorID){
                    let fechaAgenda = agendas[j].get("fecha").toLocaleDateString(),
                        fecha_ = fecha.toLocaleDateString()
                    if(fechaAgenda==fecha_){
                        let jornadaAgenda = agendas[j].get("jornada")
                        if(jornadaAgenda=="completa" || jornadaAgenda==jornada){
                            disponibilidad = false
                            j = agendas.length
                        }else{
                            if(jornada=="completa"){
                                disponibilidad = false
                                j = agendas.length
                            }
                        }
                    }
                }
            }
            if(disponibilidad==true){
                diasMesSiguiente[i].classList.remove("no_disponible")
                diasMesSiguiente[i].classList.add("disponible")
                diasMesSiguiente[i].setAttribute("onclick","AgregarATabla(this)")
            }else{
                diasMesSiguiente[i].classList.remove("disponible")
                diasMesSiguiente[i].classList.add("no_disponible")
                diasMesSiguiente[i].removeAttribute("onclick")
            }
        }
        inhabilitarDomingos()
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

function AgregarATabla(numeroDia){
    if(algunItemSinConfirmar == false){
        var informacionMes = numeroDia.parentNode.parentNode,
            mes = informacionMes.querySelector(".p_mes").innerHTML,
            anio = informacionMes.querySelector(".p_anio").innerHTML,
            txtNumeroHorasServicio = document.getElementById("txtNumHorasAgenda"),
            fecha = mes + " " + numeroDia.innerHTML + " de " + anio,
            datosFechaSeleccionada = document.getElementById("datosFechaSeleccionada").querySelectorAll("td"),
            botonesAgendarPor = document.getElementById("botonesAgendarPor").querySelectorAll("button")
        if(numeroDia.classList.contains("itemSeleccionado")){
            window.alert("Si desea eliminar el servicio de la fecha seleccionada, dirijase a la tabla de servicios")
        }else{
            var tabla = document.getElementById("tablaServiciosAgendados"),
                datosFechaSeleccionadaReg = document.getElementById("datosFechaSeleccionada"),
                txtTotalPagar = document.getElementById("totalPagar"),
                txtTotalPagarPasarela = document.getElementById("totalPagarPasarela")
            const equivalenciaJornadaTabla = {
                "completa": "8 horas",
                "media_am": "4 horas - am",
                "media_pm": "4 horas - pm"
            };
            const equivalenciaValorJornadaTabla = {
                "8 horas": precio_jornada_comp,
                "4 horas - am": precio_jornada_am,
                "4 horas - pm": precio_jornada_pm
            }; 
        
            tabla.classList.remove("tbl_conf")
            datosFechaSeleccionadaReg.classList.remove("tbl_conf")
            numeroDia.classList.add("itemSeleccionado")
            datosFechaSeleccionada[0].innerHTML = fecha
            datosFechaSeleccionada[0].setAttribute("data-valor",numeroDia.getAttribute("data-fecha"))
            datosFechaSeleccionada[1].innerHTML = equivalenciaJornadaTabla[txtNumeroHorasServicio.value]
            datosFechaSeleccionada[1].setAttribute("data-valor",txtNumeroHorasServicio.value)
            datosFechaSeleccionada[3].innerHTML = equivalenciaValorJornadaTabla[datosFechaSeleccionada[1].innerHTML]
            datosFechaSeleccionada[5].innerHTML = informacionMes.getAttribute("id")
            datosFechaSeleccionada[6].innerHTML = numeroDia.innerHTML
            totalPagar = totalPagar + parseInt(datosFechaSeleccionada[3].innerHTML,10)
            txtTotalPagar.value = totalPagar
            txtTotalPagarPasarela.value = totalPagar

            if(botonesAgendarPor[1].classList.contains("ag_activo")){
                var selector = document.getElementById("selectorColaboradora"),
                    nombreColaboradora = document.getElementById(selector.value).querySelector("h4").innerHTML
                datosFechaSeleccionada[2].innerHTML = nombreColaboradora
                datosFechaSeleccionada[2].setAttribute("data-valor",selector.value)
                selector.setAttribute("disabled","")
            }else{
                let parametroFecha = numeroDia.getAttribute("data-fecha"),
                    mapa = new Map()
                for(let z=0;z<mapasFechasDisp.length;z++) {
                    let item = mapasFechasDisp[z]
                    if(item.get("fecha") === parametroFecha) {
                      mapa = item
                      z = mapasFechasDisp.length
                    }
                }    
                MostrarColaboradoras(mapa.get("colaboradorasDisponibles"))
                datosFechaSeleccionada[2].innerHTML = "Pendiente por seleccionar"
            }
            algunItemSinConfirmar = true
        }
    }else{
        window.alert("Tiene pendiente confirmar o descartar una fecha seleccionada")
    }
   
}

function MostrarColaboradoras(codColaboradoras){
    var colaboradoras = document.getElementsByClassName("colaboradora"),
        //codColaboradoras = lista.split(','),
        limite = 0

    if(codColaboradoras.length > 3){
        limite = 3
    }else{
        limite = codColaboradoras.length
    }

    for(let i=0; i<limite; i++){
        for(let j=0; j<colaboradoras.length; j++){
            if(colaboradoras[j].getAttribute("id") == codColaboradoras[i]){
                colaboradoras[j].classList.remove("inactivo")
                j = colaboradoras.length
            }
        }
    }
}

function OcultarColaboradoras(){
    var colaboradoras = document.getElementsByClassName("colaboradora")
    for(let i=0; i<colaboradoras.length; i++){
        colaboradoras[i].classList.add("inactivo")
    }
}

function MostrarColaboradora(){
    var selector = document.getElementById("selectorColaboradora"),
        colaboradora = selector.value,
        colaboradoras = document.getElementsByClassName("colaboradora"),
        btnesHora = document.getElementById("botonesHoras").querySelectorAll("button")
    
    for(let i=0; i<colaboradoras.length; i++){
        if(colaboradoras[i].getAttribute("id") == colaboradora){
            colaboradoras[i].classList.remove("inactivo")
        }else{
            colaboradoras[i].classList.add("inactivo")
        }
    }

    for(let i=0;i<btnesHora.length;i++){
        if(btnesHora[i].classList.contains("hr_activo")){
            VerificarDisponibilidadPorColaboradora()
        }
    }
}

function ObtenerAgendas(){
    var divListaAgendas = document.getElementById("listaAgendas"),
        divAgendas = document.querySelectorAll(".agenda"),
        coleccion = [],
        cuerpo = document.querySelector(".contenedor_b")
    if(divAgendas.length>0){
        const equivalenciaMesAgenda = {
            "Enero": "01",
            "Febrero": "02",
            "Marzo": "03",
            "Abril": "04",
            "Mayo": "05",
            "Junio": "06",
            "Julio": "07",
            "Agosto": "08",
            "Septiembre": "09",
            "Octubre": "10",
            "Noviembre": "11",
            "Diciembre": "12"
        };

        for(let i=0; i<divAgendas.length; i++){
            let contenedorFecha = divAgendas[i].querySelector(".agend_fecha"),
                contenedorPrestacServID = divAgendas[i].querySelector(".agend_id_prest_servicio"),
                contenedorColaboradorID = divAgendas[i].querySelector(".agend_id_colaborador"),
                contenedorJornada = divAgendas[i].querySelector(".agend_jornada"),
                agenda = new Map(),
                fechaCadena = contenedorFecha.innerHTML,
                fechasinDe = fechaCadena.replaceAll("de",""),
                fechasinEspacios = fechasinDe.replace(/  /g, ''),
                indexFinal = fechasinEspacios.length - 4,
                diaFechaNum = parseInt(fechasinEspacios.substr(0, 2)),
                diaFecha = "",
                anioFecha = fechasinEspacios.slice(-4),
                mesFechaNom = "",
                fechaFormateada = "",
                prestacServID = contenedorPrestacServID.innerHTML,
                colaboradorID = contenedorColaboradorID.innerHTML,
                jornada = contenedorJornada.innerHTML
            
            if(diaFechaNum<10){
                diaFecha = "0" + diaFechaNum.toString()
                mesFechaNom = fechasinEspacios.slice(1,indexFinal)
            }else{
                diaFecha = diaFechaNum.toString()
                mesFechaNom = fechasinEspacios.slice(2,indexFinal)
            }
            mesFecha = equivalenciaMesAgenda[mesFechaNom]
            fechaFormateada = anioFecha + "-" + mesFecha + "-" + diaFecha + " 23:59:59"
            fecha = new Date(fechaFormateada)
            agenda.set("fecha",fecha)
            agenda.set("jornada",jornada)
            agenda.set("prestacServID",prestacServID)
            agenda.set("colaboradorID",colaboradorID)
            coleccion.push(agenda)
        }
    }
    cuerpo.removeChild(divListaAgendas)
    return coleccion
}

function DeshabilitarCalendario(){
    var numeroDiasMes = parseInt(document.getElementById("pNumeroDiasMes").innerHTML, 10),
    numeroDiasMesSiguiente = parseInt(document.getElementById("pNumeroDiasMesSiguiente").innerHTML, 10),
    mes = document.getElementById("calendarioMesActual").querySelector("ol"),
    mesSiguiente = document.getElementById("calendarioMesSiguiente").querySelector("ol"),
    diasMes = mes.getElementsByTagName("li"),
    diasMesSiguiente = mesSiguiente.getElementsByTagName("li"),
    diaActual = parseInt(document.getElementById("pDiaActual").innerHTML,10),
    limite = diasMes.length - (31 - parseInt(numeroDiasMes,10))

    for(let i=diaActual+6; i<limite;i++){
        diasMes[i].classList.remove("disponible")
        diasMes[i].classList.add("no_disponible")
        diasMes[i].removeAttribute("onclick")
    }

    limite = diasMesSiguiente.length - (31 - parseInt(numeroDiasMesSiguiente,10) )
    for(let i=7; i<limite;i++){
        diasMes[i].classList.remove("disponible")
        diasMes[i].classList.add("no_disponible")
        diasMes[i].removeAttribute("onclick")
    }
}

function MoldearRegistroTabla(){
    var molde = document.getElementById("datosFechaSeleccionada")
        nuevoRegistro = molde.cloneNode(true)
    nuevoRegistro.removeAttribute("id")
    return nuevoRegistro
}

function SeleccionarColaboradora(boton){
    var datosFechaSeleccionada = document.getElementById("datosFechaSeleccionada").querySelectorAll("td"),
        nombreColaboradora = boton.parentNode.parentNode.querySelector(".caracteristicas").querySelector("h4").innerHTML,
        idColaboradora = boton.parentNode.parentNode.getAttribute("id")
    datosFechaSeleccionada[2].innerHTML = nombreColaboradora
    datosFechaSeleccionada[2].setAttribute("data-valor",idColaboradora)
}

function ConfirmarDia(){
    var datosFechaSeleccionada = document.getElementById("datosFechaSeleccionada").querySelectorAll("td"),
        tabla = document.getElementById("tablaServiciosAgendados").querySelector("tbody")
    if(datosFechaSeleccionada[2].innerHTML == "--" || datosFechaSeleccionada[2].innerHTML == "Pendiente por seleccionar") {
        window.alert("Tiene pendiente seleccionar la colaboradora para hacer el servicio")
    }else{
        var molde = moldeRegistroTabla.cloneNode(true),
            cajaTexto = document.getElementById("cantidadServicios")
        registro = tabla.children[1].cloneNode(true)
        registro.removeAttribute("id")
        tabla.removeChild(document.getElementById("datosFechaSeleccionada"))
        molde.setAttribute("id", "datosFechaSeleccionada")
        if (cantidadDeServicios == 0){
            tabla.appendChild(molde)
        }else{
            tabla.insertBefore(molde,tabla.children[1])
        }
        var botonConfirmar = registro.querySelector(".botones_accion_registro").querySelector(".btnConfirmarRegistro")
        botonConfirmar.classList.remove("activado")
        botonConfirmar.classList.add("desactivado")
        tabla.appendChild(registro)
        cantidadDeServicios++
        cajaTexto.value = cantidadDeServicios
        algunItemSinConfirmar = false
    }
}

function DescartarDia(boton){
    var registro = boton.parentNode.parentNode,
        configuracion = registro.querySelectorAll(".tbl_conf"),
        mes = document.getElementById(configuracion[0].innerHTML).querySelector("ol"),
        dias = mes.querySelectorAll("li"),
        dia = dias[parseInt(configuracion[1].innerHTML,10)+6],
        tabla = document.getElementById("tablaServiciosAgendados"),
        botonesAgendarPor = document.getElementById("botonesAgendarPor").querySelectorAll("button"),
        datosFechaSeleccionadaReg = document.getElementById("datosFechaSeleccionada"),
        txtTotalPagar = document.getElementById("totalPagar"),
        txtTotalPagarPasarela = document.getElementById("totalPagarPasarela"),
        contenedorvalorRestar = registro.querySelectorAll("td"),
        valorRestar = parseInt(contenedorvalorRestar[3].innerHTML,10),
        cajaCantidadServicios = document.getElementById("cantidadServicios")
    
    dia.classList.remove("itemSeleccionado")
    
    if(cantidadDeServicios==0 || cantidadDeServicios==1){
        var columnas = registro.querySelectorAll("td")
        for(let i=0; i<columnas.length; i++){
            if(i!=4){
                columnas[i].innerHTML="--"
            }
        }
        registro.classList.add("tbl_conf")
        if(cantidadDeServicios==1){
            cantidadDeServicios--
            cajaCantidadServicios.value = cantidadDeServicios
        }
    }else{
        if(cantidadDeServicios>=2){
            var tabla = registro.parentNode
            tabla.removeChild(registro)
            cantidadDeServicios--
            cajaCantidadServicios.value = cantidadDeServicios
        }
    }
    totalPagar = totalPagar - valorRestar
    txtTotalPagar.value = totalPagar
    txtTotalPagarPasarela.value = totalPagar
     
    if(cantidadDeServicios == 0){
        tabla.classList.add("tbl_conf")
    }

    if(botonesAgendarPor[0].classList.contains("ag_activo")){
        OcultarColaboradoras()
    }
    algunItemSinConfirmar = false
}

function pasarApasarela(){
    var formulario = document.getElementById("formEnlacePasarela"),
        txtcantidadServicios = document.getElementById("cantidadServiciosPasarela")
    txtcantidadServicios.value = cantidadDeServicios
    if(cantidadDeServicios<=0){
        alert("No hay servicios agendados")
    }else{
        let listaPrestacServicios = [],
            regPrestacServicios = document.getElementById("tablaServiciosAgendados").querySelectorAll("tr"),
            txtJsonPasarela = document.getElementById("jsonPasarela"),
            txtCodServicioPasarela = document.getElementById('codServicioPasarela'),
            txtCodPedidoPasarela = document.getElementById('codPedidoPasarela'),
            txtCodReceptorPasarela = document.getElementById('codReceptorPasarela')
        for(let i=0;i<cantidadDeServicios;i++){
            let campos = regPrestacServicios[i+2].querySelectorAll("td")
            let prestacionServ = {
                fecha: campos[0].getAttribute("data-valor"),
                jornada: campos[1].getAttribute("data-valor"),
                colaboradora: campos[2].getAttribute("data-valor")
            }
            listaPrestacServicios.push(prestacionServ)
        }
        let convJson = JSON.stringify(listaPrestacServicios),
            url = "/agenda/"+txtCodServicioPasarela.value+"/"+txtCodPedidoPasarela.value+"/"+txtCodReceptorPasarela.value
        txtJsonPasarela.value = convJson
        formulario.action = url
        formulario.submit()
    }
}