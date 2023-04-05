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

    grid_objeto.columna_fecha({
        campo : "estado_",
        titulo: "Estado",    
        ordena: "si",
        filtra: "si",        
        ancho : 120,    
    })
]

let definicion = {
    'estructura': 'continentes',
    'columnas'  : columnas,
    'titulos'   : {
        'principal': 'Continentes',
    }   
}

let componente = grid_objeto.grid_objeto_crud(definicion);

export default componente;