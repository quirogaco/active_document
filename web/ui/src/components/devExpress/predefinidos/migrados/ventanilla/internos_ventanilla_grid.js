import grid_objeto from '../../../grid/utilidades/grid_objeto.js';

let columnas = [     
    grid_objeto.columna_objeto({
        campo : "radicado_en",
        titulo: "Territorial",
        ordena: "si",
        filtra: "si",
        ancho : 250,
    }),

    grid_objeto.columna_objeto({
        campo : "nro_radicado",
        titulo: "Número radicado",
        ordena: "si",
        filtra: "si",
        ancho : 150,
    }),

    grid_objeto.columna_fecha({
        campo : "fecha_radicado",
        tipo  : "date",  
        ordena: "si",
        filtra: "si",
        titulo: "Fecha radicado",    
        ancho : 120,    
    }),

    grid_objeto.columna_objeto({
        campo : "area_sender_name",
        titulo: "Dependencia envia",
        ordena: "si",
        filtra: "si",
        ancho : 250,
    }),

    grid_objeto.columna_objeto({
        campo : "sender_name",
        titulo: "Persona envia",
        ordena: "si",
        filtra: "si",
        ancho : 250,
    }),

    grid_objeto.columna_objeto({
        campo : "asunto",
        titulo: "Asunto",
        filtra: "si",
        ancho : 400,
    }),
]

let definicion = {
    'estructura': 'internos_ventanilla',
    'columnas'  : columnas,
    'adiciona'  : 'no',
    'campos_adicionales': [],    
    'titulos'   : {
        'principal': 'Consulta de Internos Ventanilla',
    }   
}

let componente = grid_objeto.grid_objeto_crud(definicion);

export default componente;