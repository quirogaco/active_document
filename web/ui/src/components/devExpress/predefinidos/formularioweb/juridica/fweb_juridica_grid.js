import grid_objeto from '../../../grid/utilidades/grid_objeto.js';

let columnas = [
    grid_objeto.columna_objeto({
        campo : "nro_radicado",
        titulo: "Número radicado",
        ancho : 130,
        ordena: "si",
        filtra: "si",
    }),

    grid_objeto.columna_fecha_hora({
        campo : "fecha_radicado",
        titulo: "Fecha radicado", 
        ancho : 150,  
        ordena: "si",
        filtra: "si",     
    }),
    
    grid_objeto.columna_objeto({
        campo : "nombre_entidad",
        titulo: "Nombre entidad",
        ordena: "si",
        filtra: "si",
    }),

    grid_objeto.columna_objeto({
        campo : "tipo_entidad_nombre",
        titulo: "Tipo entidad",
        ordena: "si",
        filtra: "si",
    }),

    grid_objeto.columna_objeto({
        campo : "correo",
        titulo: "Correo electrónico",
        ordena: "si",
        filtra: "si",
    }),

    /*
    grid_objeto.columna_objeto({
        campo : "nombres",
        titulo: "Nombres remitente",
        ordena: "si",
        filtra: "si",
    }),
    

    grid_objeto.columna_objeto({
        campo : "apellidos",
        titulo: "Apellidos remitente",
        ordena: "si",
        filtra: "si",
    }),
    */

]

let definicion = {
    'estructura': 'fweb_juridica',
    'columnas'  : columnas,
    // Esto no esta activado....
    //'filtros'   : [ ['tipo_radicado', '=', 'JURIDICA'] ],
    'titulos'   : {
        'principal': 'Formulario web PERSONA JURIDICA',
        'crear'    : 'Crear radicado',        
    }   
}

let componente = grid_objeto.grid_objeto_crud(definicion);

export default componente;