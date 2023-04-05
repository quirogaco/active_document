import grid_objeto from '../../../grid/utilidades/grid_objeto.js';

let columnas = [
    grid_objeto.columna_texto({
        campo : "codigo",
        titulo: "Codigo",
        ordena: "si",
        filtra: "si",
        ancho : 200,
    }),

    grid_objeto.columna_texto({
        campo : "nombre",
        titulo: "Nombre",  
        ordena: "si",
        filtra: "si",      
    }),

    grid_objeto.columna_texto({
        campo : "correo",
        titulo: "Correo",  
        ordena: "si",
        filtra: "si",      
    }),
    
    grid_objeto.columna_objeto({
        campo : "estado_",
        titulo: "Estado",
        ordena: "si",
        filtra: "si",    
        ancho : 100,        
    })
]


let definicion = {
    'estructura': 'ubicaciones',
    'columnas'  : columnas,
    'titulos'   : {
        'principal': 'Manejo de Ubicación Geografica',
        'crear'    : 'Crear Ubicación Geografica',        
    }   
}

let componente = grid_objeto.grid_objeto_crud(definicion);

export default componente;