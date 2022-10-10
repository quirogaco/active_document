
let columnas = [
    // Tipo radicado
    {
        caption    : "Tipo radicado",
        dataField  : "radicado_tipo",
        width      : 120,
    },

    // Nro radicado
    {
        caption       : "Nro radicado",
        dataField     : "radicado_nro",
        width         : 150,
    },

    // Asunto
    {
        caption       : "Asunto",
        dataField     : "radicado_asunto",
        width         : 550,
        allowSorting  : false
    },
    
    // Con copia a
    {
        caption       : "Con copia a",
        dataField     : "destinatario_nombre",
        width         : 350,
        allowSorting  : false
    }
]

export default {
    columnas: columnas
}