import grid_objeto from '../../../grid/utilidades/grid_objeto.js';

let columnas = [
    grid_objeto.columna_objeto({
        campo : "codigo",
        titulo: "Codigo",
        width : 200,
    }),

    grid_objeto.columna_objeto({
        campo : "nombre",
        titulo: "Nombre",        
    }),
    
    grid_objeto.columna_objeto({
        campo : "ubicacion_nombre",
        titulo: "Territorial/Regional",
        ancho : 200
    }),

    grid_objeto.columna_objeto({
        campo : "estado_",
        titulo: "Estado",
        ancho : 100,
    })
]

let definicion = {
    'estructura': 'dependencias',
    'columnas'  : columnas,
    'titulos'   : {
        'principal': 'Manejo de Dependencias',
        'crear'    : 'Crear Dependencia',        
    }   
}

let componente = grid_objeto.grid_objeto_crud(definicion);

export default componente;