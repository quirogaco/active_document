let columnas = [
    // Nombre
    {
        caption    : "Descripción",
        dataField  : "nombre",
        dataType   : "string",        
        width      : 600       
    },

    // Versión
    {
        caption    : "Versión",
        dataField  : "version",
        dataType   : "string",        
        width      : 100   
    },

    // Fecha
    {
        caption       : "Fecha aprobación",
        dataField     : "fecha_version",
        dataType      : "date",          
        width         : 150,
        format        : 'y-MM-dd'
    },

    // Fondo
    {
        caption       : "Fondo",
        dataField     : "fondo_nombre",
        dataType      : "string",         
        width         : 500
    },

    // Fondo
    {
        caption       : "Estado",
        dataField     : "estado_",
        dataType      : "string",         
        width         : 120
    }
]

export default {
    columnas: columnas
}