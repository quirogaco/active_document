let columnas = [
    // Numero radicado
    {
        caption       : "Radicado",
        dataField     : "nro_radicado",
        dataType      : "string",
        width         : 100       
    },

    // Fecha radicado
    {
        caption       : "Fecha ",
        dataField     : "fecha_radicado",
        dataType      : "date",
        width         : 100       
    },

    // Destinatario
    {
        caption       : "Destinatario",
        dataField     : "tercero_nombre_completo",
        dataType      : "string",
        width         : 300
    },    

    // Direccion
    {
        caption       : "Dirección",
        dataField     : "tercero_direccion",
        dataType      : "string",
        width         : 300
    },
    
    // Ubicación
    {
        caption       : "Ubicación",
        dataField     : "tercero_ciudad_nombre",
        dataType      : "string",
        width         : 300
    }    
]

export default {
    columnas: columnas
}