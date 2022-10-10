let columnas = [
    // Numero radicado
    {
        caption       : "Radicado",
        dataField     : "nro_radicado",
        dataType      : "string",
        allowEditing  : false,
        width         : "130px"       
    },

    // Destinatario
    {
        caption       : "Destinatario",
        dataField     : "destinatario",
        dataType      : "string",
        allowEditing  : false,
        width         : 300
    },


    // Direccion
    {
        caption       : "Dirección",
        dataField     : "direccion",
        dataType      : "string",
        //allowEditing  : true,
        width         : 400
    },
    
    // Ubicación
    {
        caption       : "Ubicación",
        dataField     : "ubicacion",
        dataType      : "string",
        //allowEditing  : true,
        width         : 400
    },
    
    // Guia envio
    {
        caption       : "Guia envio",
        dataField     : "guia_envio",
        dataType      : "string",
        //allowEditing  : true,
        width         : 100
    },
]

export default {
    columnas: columnas
}