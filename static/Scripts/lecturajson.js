/*const fs = require('fs');

let data = fs.readFileSync('static/Json/agendas/AGNCLB001.json');
//let agenda = JSON.parse(data);
//let agenda = JSON.parse(data).abril["1"];
//let agenda = JSON.parse(data).abril["1"][0];
let agenda = JSON.parse(data).abril;
console.log(agenda);
console.log(typeof(agenda));*/

/*let jsonData = require('static/Json/agendas/AGNCLB001.json');
console.log(jsonData);
console.log(typeof(jsonData));*/

let data ={
    "cursos": [{
        "codigo": "1",
        "nombre": "matematicas"
    },{
        "codigo": "2",
        "nombre": "quimica"
    },{
        "codigo": "3",
        "nombre": "lenguaje"
    },{
        "codigo": "4",
        "nombre": "programacion"
    }]
}

const fs = require('fs')
let jsonData = JSON.stringify(data)
console.log(jsonData);
console.log(typeof(jsonData));

fs.writeFile('static/Json/agendas/cursos.json',jsonData, (error)=>{
    if(error){
        console.log('Error: ${error}')
    }else{
        console.log("Archivo Json creado correctamente")
    }
})