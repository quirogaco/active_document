let columnas = [
    // Numero radicado
    {
        caption       : "Radicado",
        dataField     : "nro_radicado",
        dataType      : "string",
        allowEditing  : false,
        width         : "130px"       
    },

    // Guia envio
    {
        caption       : "Guia devolución",
        dataField     : "guia_devolucion",
        dataType      : "string",
        allowEditing  : true,
        width         : 150
    },

    // Motivo devolución
    {
        caption       : "Motivo devolución",
        dataField     : "motivo_devolucion",
        dataType      : "string",
        allowEditing  : true,
        width         : 150
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
        width         : 300
    },
    
    // Ubicación
    {
        caption       : "Ubicación",
        dataField     : "ubicacion",
        dataType      : "string",
        width         : 300
    },

]

export default {
    columnas: columnas
}