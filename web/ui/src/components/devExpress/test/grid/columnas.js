
let columnas = [
    // Nombre
    {
        caption    : "Asunto",
        dataField  : "nombre",
        width      : 400,
    },

    // Subserie/Serie
    {
        caption       : "Serie/Subserie",
        dataField     : "serie_subserie",
        width         : 250,
    },

    // Dependencia
    {
        caption       : "Dependencia",
        dataField     : "dependencia_nombre",
        width         : 250,
    },
    
    // Etapa
    {
        caption       : "Etapa",
        dataField     : "etapa",
        width         : 90,
    },

    // Ubicacion
    {
        caption       : "Ubicación",
        dataField     : "ubicacion",
        width         : 90,
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
        width         : 120,
    },

    // Acceso
    {
        caption       : "Información",
        dataField     : "acceso_modo",
        width         : 120,
    }
]

export default {
    columnas: columnas
}