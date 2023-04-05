import grid_objeto from '../../../grid/utilidades/grid_objeto.js';

let columnas = [     
    grid_objeto.columna_objeto({
        campo : "codigo",
        titulo: "Codigo",
        ordena: "si",
        filtra: "si",
        ancho : 250,
    }),

    grid_objeto.columna_objeto({
        campo : "nombre",
        titulo: "Nombre",
        ordena: "si",
        filtra: "si",
        ancho : 500,
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
    'estructura': 'roles',
    'columnas'  : columnas,
    'titulos'   : {
        'principal': 'Roles del sistema',
    }   
}

let componente = grid_objeto.grid_objeto_crud(definicion);

export default componente;