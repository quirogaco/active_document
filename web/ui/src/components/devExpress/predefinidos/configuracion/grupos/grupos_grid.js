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
    })
]


let definicion = {
    'estructura': 'grupos',
    'columnas'  : columnas,
    'titulos'   : {
        'principal': 'Grupos',
    }   
}

let componente = grid_objeto.grid_objeto_crud(definicion);

export default componente;