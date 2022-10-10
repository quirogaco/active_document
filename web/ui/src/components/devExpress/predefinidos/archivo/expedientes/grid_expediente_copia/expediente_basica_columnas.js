let columnas = [
    // Nombre
    {
        caption    : "Asunto",
        dataField  : "nombre",
        dataType   : "string",        
        width      : 400,
        allowEditing  : false,       
    },

    // Subserie/Serie
    {
        caption       : "Serie/Subserie",
        dataField     : "serie_subserie",
        dataType      : "string",     
        width         : 250,
        allowEditing  : false,
    },

    // Dependencia
    {
        caption       : "Dependencia",
        dataField     : "dependencia_nombre",
        dataType      : "string",     
        width         : 250,
        allowEditing  : false,
    },
    
    // Etapa
    {
        caption       : "Etapa",
        dataField     : "etapa",
        dataType      : "string",         
        width         : 90,
        allowEditing  : false,
    },

    // Ubicacion
    {
        caption       : "Ubicación",
        dataField     : "ubicacion",
        dataType      : "string",         
        width         : 90,
        allowEditing  : false,
    },

    // Vence gestión
    {
        caption       : "Vence gestión",
        dataField     : "vence_gestion",
        dataType      : "date",
        format        : "yyyy-MM-dd",         
        width         : 120,
        allowEditing  : false,
    },


    // Vence central
    {
        caption       : "Vence central",
        dataField     : "vence_central",
        dataType      : "date",
        format        : "yyyy-MM-dd",         
        width         : 120,
        allowEditing  : false,
    },

    // Estado
    {
        caption       : "Estado",
        dataField     : "estado",
        dataType      : "string",         
        width         : 120,
        allowEditing  : false,
    },

    // Acceso
    {
        caption       : "Información",
        dataField     : "acceso_modo",
        dataType      : "string",         
        width         : 120,
        allowEditing  : false, 
    }
]

export default {
    columnas: columnas
}