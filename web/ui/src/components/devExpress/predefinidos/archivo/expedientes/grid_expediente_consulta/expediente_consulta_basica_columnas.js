let columnas = [
    // Tabla
    {
        caption    : "TABLA",
        dataField  : "tabla",
        dataType   : "string",        
        width      : 60      
    },

    // Nombre
    {
        caption    : "Asunto",
        dataField  : "nombre",
        dataType   : "string",        
        width      : 200       
    },

    // Nombre
    {
        caption    : "Dependencia",
        dataField  : "dependencia_nombre",
        dataType   : "string",        
        width      : 200       
    },

    // Subserie/Serie
    {
        caption       : "Serie/Subserie",
        dataField     : "serie_subserie",
        dataType      : "string",     
        width         : 250
    },

    // Tipo expediente
    {
        caption       : "Tipo expediente",
        dataField     : "tipo_expediente",
        dataType      : "string",         
        width         : 90
    },

    // Etapa
    {
        caption       : "Etapa",
        dataField     : "etapa",
        dataType      : "string",         
        width         : 90
    },

    // Ubicacion
    {
        caption       : "Ubicación",
        dataField     : "ubicacion",
        dataType      : "string",         
        width         : 90
    },

    // Vence gestión
    {
        caption       : "Vence gestión",
        dataField     : "vence_gestion",
        dataType      : "date",
        format        : "yyyy-mm-dd",         
        width         : 120
    },


    // Vence central
    {
        caption       : "Vence central",
        dataField     : "vence_central",
        dataType      : "date",
        format        : "yyyy-mm-dd",         
        width         : 120
    },

    // Estado
    {
        caption       : "Estado",
        dataField     : "estado",
        dataType      : "string",         
        width         : 1020
    }
]

export default {
    columnas: columnas
}