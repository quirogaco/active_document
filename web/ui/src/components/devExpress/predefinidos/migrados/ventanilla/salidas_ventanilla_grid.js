import grid_objeto from '../../../grid/utilidades/grid_objeto.js';

let columnas = [     
    grid_objeto.columna_objeto({
        campo : "radicado_en",
        titulo: "Territorial",
        ordena: "si",
        filtra: "si",
        ancho : 200,
    }),

    grid_objeto.columna_objeto({
        campo : "nro_radicado",
        titulo: "Número radicado",
        ordena: "si",
        filtra: "si",
        ancho : 130,
    }),

    grid_objeto.columna_fecha({
        campo : "fecha_radicado",
        tipo  : "date",  
        ordena: "si",
        filtra: "si",
        titulo: "Fecha radicado",    
        ancho : 110,    
    }),

    grid_objeto.columna_objeto({
        campo : "name",
        titulo: "Entidad",
        ordena: "si",
        filtra: "si",
        ancho : 180,
    }),

    grid_objeto.columna_objeto({
        campo : "sender",
        titulo: "Destinatario",
        ordena: "si",
        filtra: "si",
        ancho : 180,
    }),

    grid_objeto.columna_objeto({
        campo : "area_sender_name",
        titulo: "Remite dependencia",
        ordena: "si",
        filtra: "si",
        ancho : 180,
    }),

    grid_objeto.columna_objeto({
        campo : "sender_name",
        titulo: "Remite funcionario",
        ordena: "si",
        filtra: "si",
        ancho : 180,
    }),
    
    grid_objeto.columna_objeto({
        campo : "asunto",
        titulo: "Asunto",
        filtra: "si",
        ancho : 300,
    })
]

let definicion = {
    'estructura': 'salidas_ventanilla',
    'columnas'  : columnas,
    'adiciona'  : 'no',
    'campos_adicionales': [],    
    'titulos'   : {
        'principal': 'Consulta de Salidas Ventanilla',
    }   
}

let componente = grid_objeto.grid_objeto_crud(definicion);

export default componente;