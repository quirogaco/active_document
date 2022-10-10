import grid_objeto from '../../../grid/utilidades/grid_objeto.js';

let columnas = [
    grid_objeto.columna_objeto({
        campo : "nro_radicado",
        titulo: "Número radicado",
        ordena: "si",
        filtra: "si",
        ancho : 120,
    }),

    grid_objeto.columna_fecha({
        campo : "fecha_radicado",
        tipo  : "date",  
        ordena: "si",
        filtra: "si",
        titulo: "Fecha radicado",    
        ancho : 120,    
    }),

    grid_objeto.columna_objeto({
        campo : "nombre",
        titulo: "Nombre remitente",
        ordena: "si",
        filtra: "si",
        ancho : 200,
    }),

    grid_objeto.columna_objeto({
        campo : "correoelectronico",
        titulo: "Correo electronico",
        ordena: "si",
        filtra: "si",
        ancho : 200,
    }),

    grid_objeto.columna_objeto({
        campo : "nroidentificacion",
        titulo: "Número identificación",
        ordena: "si",
        filtra: "si",
        ancho : 100,
    }),

    grid_objeto.columna_objeto({
        campo : "asunto",
        titulo: "Asunto",
        filtra: "si",
        ancho : 450,
    }),

    grid_objeto.columna_objeto({
        campo : "direccion",
        titulo: "Dirección",
        filtra: "si",
        ancho : 200,
    })
    
]

let definicion = {
    'estructura': 'radicado_pqr',
    'columnas'  : columnas,
    'adiciona'  : 'no',
    'campos_adicionales': [],    
    'titulos'   : {
        'principal': 'Consulta de PQRS Migrados',
    }   
}

let componente = grid_objeto.grid_objeto_crud(definicion);

export default componente;