let columnas = [
    // Clase radicado
    {
        caption    : "Clase radicado",
        dataField  : "clase_radicado",
        dataType   : "string",        
        width      : 120  
    },

    // Número radicado
    {
        caption    : "# Radicado",
        dataField  : "nro_radicado",
        dataType   : "string",        
        width      : 120  
    },

    // Fecha radicado
    {
        caption       : "Fecha radicado",
        dataField     : "fecha_radicado",
        dataType      : "datetime",          
        width         : 160,
        format        : 'yyyy-MM-dd HH:mm:ss'
    },

    // Nombre tercero
    {
        caption       : "Nombre remitente",
        dataField     : "tercero_nombres_apellidos",
        dataType      : "string",         
        width         : 200
    },

    // Razon social
    {
        caption       : "Razon social",
        dataField     : "tercero_razon_social",
        dataType      : "string",         
        width         : 200
    },

    // Clase tercero
    {
        caption       : "Clase remitente",
        dataField     : "tercero_clase",
        dataType      : "string",         
        width         : 90
    },

    // Tipo tercero
    {
        caption       : "Tipo remitente",
        dataField     : "tercero_tipo_tercero_nombre",
        dataType      : "string",         
        width         : 130
    },

    // Asunto
    {
        caption       : "Asunto",
        dataField     : "asunto",
        dataType      : "string",         
        width         : 500
    },

    // Correo
    {
        caption       : "Correo",
        dataField     : "tercero_correo_electronico",
        dataType      : "string",         
        width         : 260
    }
]

export default {
    columnas: columnas
}