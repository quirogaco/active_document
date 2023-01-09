let columnas = [
    // Radicado
    {
        caption     : "Salida #",
        dataField   : "nro_radicado",
        dataType    : "string",        
        width       : 140,
        cellTemplate: "icono_pdf_template"     
    },

    {
        caption     : "Entrada responde",
        dataField   : "radicado_responde",
        dataType    : "string",        
        width       : 125
    },

    // Fecha Radicado
    {
        caption       : "Fecha radicado",
        dataField     : "fecha_radicado",
        dataType      : "datetime",          
        width         : 180,
        format        : 'y-MM-dd hh:mm:ss'
    },

    // Nombre tercero
    {
        caption       : "Destinatario",
        dataField     : "tercero_nombres_apellidos",
        dataType      : "string",         
        width         : 250
    },


    // Clase tercero
    {
        caption       : "Clase",
        dataField     : "tercero_clase",
        dataType      : "string",         
        width         : 90
    },

    // Tipo tercero
    {
        caption       : "Tipo",
        dataField     : "tercero_tipo_tercero_nombre",
        dataType      : "string",         
        width         : 130
    },

    // Asunto
    {
        caption     : "Asunto",
        dataField   : "asunto",
        dataType    : "string",        
        width       : 600,
        allowSorting: false   
    }
]

export default {
    columnas: columnas
}