let columnas = [
    // Nombre
    {
        caption    : "Asunto",
        dataField  : "nombre",
        dataType   : "string",        
        width      : 300,
    },

    // Serie
    {
        caption       : "Serie",
        dataField     : "serie_nombre",
        dataType      : "string",     
        width         : 250,
    },

    // Subserie
    {
        caption       : "Subserie",
        dataField     : "subserie_nombre",
        dataType      : "string",     
        width         : 250,
    },

    // Dependencia
    {
        caption       : "Dependencia",
        dataField     : "dependencia_nombre",
        dataType      : "string",     
        width         : 250,
    },

    {
        caption    : "Codigo",
        dataField  : "codigo",
        dataType   : "string",        
        width      : 120,
    },

    // Inicial
    {
        caption       : "Fecha inicial",
        dataField     : "fecha_inicial",
        dataType      : "date",
        format        : "yyyy-MM-dd",         
        width         : 120,
    },

    // Final
    {
        caption       : "Fecha final",
        dataField     : "fecha_final",
        dataType      : "date",
        format        : "yyyy-MM-dd",         
        width         : 120,
    },

    // Folios fisicos
    {
        caption       : "Folios fisicos",
        dataField     : "folios_fisicos",
        dataType      : "integer",   
        width         : 70,
    },

    // Folios electronicos
    {
        caption       : "Folios electrónicos",
        dataField     : "folios_electronicos",
        dataType      : "integer",   
        width         : 90,
    },

    // Soporte
    {
        caption       : "Soporte",
        dataField     : "tipo_expediente",
        dataType      : "string",         
        width         : 100,
    },

    // Vence gestión
    {
        caption       : "Vence gestión",
        dataField     : "vence_gestion",
        dataType      : "date",
        format        : "yyyy-MM-dd",         
        width         : 120,
    },

    // Vence central
    {
        caption       : "Vence central",
        dataField     : "vence_central",
        dataType      : "date",
        format        : "yyyy-MM-dd",         
        width         : 120,
    },

    // Estado
    {
        caption       : "Estado",
        dataField     : "estado",
        dataType      : "string",         
        width         : 120,
    },

    // Acceso
    {
        caption       : "Información",
        dataField     : "acceso_modo",
        dataType      : "string",         
        width         : 120,
    },

     // Etapa
     {
        caption       : "Etapa",
        dataField     : "etapa",
        dataType      : "string",         
        width         : 90,
    },

    // Ubicacion
    {
        caption       : "Ubicación",
        dataField     : "ubicacion",
        dataType      : "string",         
        width         : 90,
    },

    // conservacion
    {
        caption       : "Conservación",
        dataField     : "conservacion",
        dataType      : "string",         
        width         : 110,
    },

    // eliminacion
    {
        caption       : "Eliminación",
        dataField     : "eliminacion",
        dataType      : "string",         
        width         : 90,
    },
    
    // seleccion
    {
        caption       : "Selección",
        dataField     : "seleccion",
        dataType      : "string",         
        width         : 80,
    },

    // medio tecnico
    {
        caption       : "Medio tecnico",
        dataField     : "micro_digitalizacion",
        dataType      : "string",         
        width         : 60,
    }
]

export default {
    columnas: columnas
}