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

    // Caja
    {
        caption       : "Caja",
        dataField     : "caja_transferencia",
        dataType      : "string",     
        width         : 80,
        allowEditing  : true,
    },

    // Anotación
    {
        caption       : "Anotación",
        dataField     : "anotacion",
        dataType      : "string",     
        width         : 140,
        allowEditing  : true,
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

    // Estado
    {
        caption       : "Estado",
        dataField     : "estado",
        dataType      : "string",         
        width         : 120,
        allowEditing  : false,
    },

]

export default {
    columnas: columnas
}