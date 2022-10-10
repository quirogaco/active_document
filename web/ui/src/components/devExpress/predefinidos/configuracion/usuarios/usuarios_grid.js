import grid_objeto from '../../../grid/utilidades/grid_objeto.js';

let columnas = [     
    grid_objeto.columna_objeto({
        campo : "codigo",
        titulo: "Codigo",
        ordena: "si",
        filtra: "si",
        ancho : 150,
    }),

    grid_objeto.columna_objeto({
        campo : "nombre",
        titulo: "Nombre",
        ordena: "si",
        filtra: "si",
        ancho : 400,
    }),

    grid_objeto.columna_objeto({
        campo : "dependencia_nombre",
        titulo: "Dependencia",
        ordena: "si",
        filtra: "si",
        ancho : 400,
    }),

    grid_objeto.columna_objeto({
        campo : "ubicacion_nombre",
        titulo: "Territorial/Regional",
        ordena: "si",
        filtra: "si",
        ancho : 400,
    }),

    grid_objeto.columna_fecha({
        campo : "estado_",
        titulo: "Estado",    
        ordena: "si",
        filtra: "si",        
        ancho : 120,    
    })
]


let definicion = {
    'estructura': 'usuarios',
    'columnas'  : columnas,
    'titulos'   : {
        'principal': 'Usuarios del sistema',
    }   
}

let componente = grid_objeto.grid_objeto_crud(definicion);

export default componente;