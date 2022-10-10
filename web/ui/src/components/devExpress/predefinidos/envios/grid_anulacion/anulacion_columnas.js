let columnas = [
    // Numero radicado
    {
        caption       : "Radicado",
        dataField     : "nro_radicado",
        dataType      : "string",
        allowEditing  : false,
        width         : 100       
    },

    // Fecha radicado
    {
        caption       : "Fecha ",
        dataField     : "fecha_radicado",
        dataType      : "date",
        width         : 100,     
        allowEditing  : false
    },

    // Correo elecronicos
    {
        caption       : "Correo",
        dataField     : "tercero_correo_electronico",
        dataType      : "string",
        allowEditing  : true,
        width         : 300
    },   

    // Nombre completo
    {
        caption       : "Nombre",
        dataField     : "tercero_nombre_completo",
        dataType      : "string",
        allowEditing  : true,
        width         : 500
    },  

    // Firmado
    {
        caption       : "Firmado",
        dataField     : "firmado_electronica",
        dataType      : "string",
        width         : 80,
        allowEditing  : false
    },

    // Devuelto
    {
        caption       : "Devuelto",
        dataField     : "envio_devuelto",
        dataType      : "string",
        width         : 80,
        allowEditing  : false
    },

    // Anulación
    {
        caption       : "Anulación",
        dataField     : "estado_anulado",
        dataType      : "string",
        width         : 100,
        allowEditing  : false
    },
    
    // Ubicación
    {
        caption       : "Ubicación",
        dataField     : "tercero_ciudad_nombre",
        dataType      : "string",
        width         : 300,
        allowEditing  : false
    }   
]

export default {
    columnas: columnas
}