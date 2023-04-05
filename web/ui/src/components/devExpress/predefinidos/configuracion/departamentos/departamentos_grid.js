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
        campo : "pais_nombre",
        titulo: "Pais",
        ordena: "si",
        filtra: "si",
        ancho : 400,
    }),

    grid_objeto.columna_objeto({
        campo : "continente_nombre",
        titulo: "Continente",
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
    'estructura': 'departamentos',
    'columnas'  : columnas,
    'titulos'   : {
        'principal': 'Departamentos',
    }   
}

let componente = grid_objeto.grid_objeto_crud(definicion);

export default componente;