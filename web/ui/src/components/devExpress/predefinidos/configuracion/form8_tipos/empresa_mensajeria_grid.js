import grid_objeto from '../../../grid/utilidades/grid_objeto.js';

let columnas = [     
    grid_objeto.columna_objeto({
        campo : "nombre",
        titulo: "Nombre",
        ordena: "si",
        filtra: "si",
        ancho : 400,
    }),

    grid_objeto.columna_objeto({
        campo : "estado_",
        titulo: "Estado",    
        ordena: "si",
        filtra: "si",        
        ancho : 120,    
    })
]

let definicion = {
    'estructura': 'empresa_mensajeria',
    'columnas'  : columnas,
    'titulos'   : {
        'principal': 'Empresas de mensajería',
    }   
}

let componente = grid_objeto.grid_objeto_crud(definicion);

export default componente;