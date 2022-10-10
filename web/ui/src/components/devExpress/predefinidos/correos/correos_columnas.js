let columnas = [
    // Fecha correo
    {
        caption       : "Fecha correo",
        dataField     : "fecha_correo",
        dataType      : "date",
        width         : 120,
        format        : 'y-MM-dd'
    },

    // Correo
    {
        caption       : "Correo origen",
        dataField     : "correo_origen",
        dataType      : "string",
        width         : 400
    },
    
    // Asunto
    {
        caption       : "Asunto",
        dataField     : "asunto",
        dataType      : "string",
        width         : 750
    },

    // Estado vencimiento
    {
        caption  : "Estado",
        dataField: "estado",
        dataType : "string",
        width    : "130px"       
    }
]

export default {
    columnas: columnas
}