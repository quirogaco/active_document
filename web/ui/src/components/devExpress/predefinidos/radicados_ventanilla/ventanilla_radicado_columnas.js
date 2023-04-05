let columnas = [
    // Clase Radicado
    {
        caption       : "Tipo",
        dataField     : "clase_radicado",
        dataType      : "string",             
        width         : 110
    },

    // Clase Radicado
    {
        caption       : "Canal/Medio",
        dataField     : "canal_medio",
        dataType      : "string",             
        width         : 110
    },

    // Radicado
    {
        caption    : "Nro radicado",
        dataField  : "nro_radicado",
        dataType   : "string",        
        width      : 130       
    },

    // Fecha Radicado
    {
        caption       : "Fecha radicado",
        dataField     : "fecha_radicado",
        dataType      : "date",          
        width         : 120,
        format        : 'y-MM-dd'
    },

    // Nombre tercero
    {
        caption       : "Remitente",
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
        caption    : "Asunto",
        dataField  : "asunto",
        dataType   : "string",        
        width      : 600      
    },
]

export default {
    columnas: columnas
}