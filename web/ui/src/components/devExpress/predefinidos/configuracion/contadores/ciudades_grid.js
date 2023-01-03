import grid_objeto from '../../../grid/utilidades/grid_objeto.js';

let columnas = [
    grid_objeto.columna_objeto({
        campo  : "codigo",
        titulo : "Codigo",
        ancho  : 200,
        filtra : 'si',
        ordena : 'si',
    }),

    grid_objeto.columna_objeto({
        campo  : "consecutivo",
        titulo : "Consecutivo",
        ancho  : 200,
    }),

    grid_objeto.columna_objeto({
        campo  : "estado_",
        titulo : "Estado",
        ancho  : 100,
        filtra : 'no',
        ordena : 'si',
    }),
]

let definicion = {
    'estructura': 'ciudades',
    'columnas'  : columnas,
    'titulos'   : {
        'principal': 'Manejo de Ciudades',
        'crear'    : 'Crear Ciudad',        
    },   
    'agrupa'    : 'si' 
}

let componente = grid_objeto.grid_objeto_crud(definicion);

export default componente;