import grid_objeto from '../../../grid/utilidades/grid_objeto.js';

let columnas = [
    grid_objeto.columna_fecha({
        campo : "festivo",
        titulo: "Dia festivo", 
        ordena: "si",
        filtra: "si",       
    }),

    grid_objeto.columna_texto({
        campo : "estado_",
        titulo: "Estado",
        ancho : 100,
        ordena: "si",
        filtra: "si",
    })
]

let definicion = {
    'estructura': 'festivo',
    'columnas'  : columnas,
    'titulos'   : {
        'principal': 'Manejo de Festivos',
        'crear'    : 'Crear Festivo',        
    }   
}

let componente = grid_objeto.grid_objeto_crud(definicion);

export default componente;