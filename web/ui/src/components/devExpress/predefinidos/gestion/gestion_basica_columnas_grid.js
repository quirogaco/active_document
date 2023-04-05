import grid_objeto from '../../grid/utilidades/grid_objeto.js'

let columnas = [
    grid_objeto.columna_opciones({
        campo    : "estado_vencimiento",
        titulo   : "Estado",
        ordena   : "si",
        filtra   : "si",
        ancho    : 130,
        //plantilla: '<i class="fas fa-traffic-light" style="color:yellow"></i> {{ plantilla_columna_data(data) }}',
        plantilla: '<div v-html="plantilla_columna_estado(data)"></div>',
        elementos: [
            { id: 'TERMINOS',  nombre: 'TERMINOS' },
            { id: 'VENCIDO',    nombre: 'VENCIDO' },    
        ]
    }),

    grid_objeto.columna_opciones({
        campo : "prioridad",
        titulo: "Prioridad",
        ordena: "si",
        filtra: "si",
        ancho : 100,
        elementos: [
            { id: 'ALTA',  nombre: 'ALTA' },
            { id: 'MEDIA', nombre: 'MEDIA' },
            { id: 'BAJA',  nombre: 'BAJA' },            
        ]
    }),

    grid_objeto.columna_texto({
        campo : "peticion_nombre",
        titulo: "Petición",
        filtra: "si",
        ordena: "si",
        ancho : 250,
    }),

    grid_objeto.columna_fecha({
        campo : "vence_en",
        titulo: "Vence en",
        filtra: "si",
        ordena: "si",
        ancho : 120,
    }),

    grid_objeto.columna_texto({
        campo : "responsable_nombre",
        titulo: "Responsable",
        filtra: "si",
        ordena: "si",
        ancho : 250,
    }),

    grid_objeto.columna_texto({
        campo : "dependencia_nombre",
        titulo: "Dependencia",
        filtra: "si",
        ordena: "si",
        ancho : 250,
    }),

    grid_objeto.columna_opciones({
        campo : "fuente",
        titulo: "Origen",
        ordena: "si",
        filtra: "si",
        ancho : 200,
        elementos: [
            { id: 'VENTANILLA', nombre: 'VENTANILLA' },
            { id: 'PQRS',       nombre: 'PQRS' }        
        ]
    }),

    grid_objeto.columna_texto({
        campo : "tipo",
        titulo: "Tipo de radicado",
        ordena: "si",
        filtra: "si",
        ancho : 200,       
    })
]

export default {
    columnas: columnas
}