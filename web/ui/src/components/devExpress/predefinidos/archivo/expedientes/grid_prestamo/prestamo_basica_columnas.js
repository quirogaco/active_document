let columnas = [
    // Nombre
    {
        caption    : "Expediente",
        dataField  : "expediente_nombre",
        dataType   : "string",        
        width      : 400       
    },

    // Estado
    {
        caption       : "Estado",
        dataField     : "estado",
        dataType      : "string",     
        width         : 120
    },

    // Motivo
    {
        caption       : "Motivo",
        dataField     : "motivo",
        dataType      : "string",     
        width         : 120
    },

    // Solicitado en
    {
        caption       : "Solicitado en",
        dataField     : "fecha_peticion",
        dataType      : "date",  
        format        : 'y-MM-dd',       
        width         : 120
    },

    // Vence en
    {
        caption       : "Vence en",
        dataField     : "fecha_vencimiento",
        dataType      : "date",  
        format        : 'y-MM-dd',       
        width         : 120
    },

    // Vencido
    {
        caption       : "Vencido",
        dataField     : "vencido",
        dataType      : "string",         
        width         : 120
    },

    // Anotación
    {
        caption       : "Anotacion",
        dataField     : "anotacion",
        dataType      : "string",         
        width         : 200
    },

    // Anotación
    {
        caption       : "Funcionario",
        dataField     : "usuario_nombre",
        dataType      : "string",         
        width         : 300
    }
]

export default {
    columnas: columnas
}