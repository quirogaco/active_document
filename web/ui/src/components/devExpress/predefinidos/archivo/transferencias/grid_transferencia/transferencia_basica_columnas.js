let columnas = [
    // Fecha creación
    {
        caption    : "Creada en",
        dataField  : "fecha_creacion",
        dataType   : "date",        
        width      : 150,
        format     : "y-MM-dd"  
    },

    // Dependencia
    {
        caption       : "Dependencia",
        dataField     : "dependencia_nombre",
        dataType      : "string",     
        width         : 400
    },

    // Fecha creación
    {
        caption    : "Fecha de transferencia",
        dataField  : "fecha_transferencia",
        dataType   : "date",        
        width      : 250,
        format     : "y-MM-dd"       
    },

    // Etapa
    {
        caption       : "Estado",
        dataField     : "estado",
        dataType      : "string",         
        width         : 150
    },

    // Detalle
    {
        caption     : "Anotación",
        dataField   : "detalle",
        dataType    : "string",         
        width       : 350,
        allowEditing: true,  
    },
]

export default {
    columnas: columnas
}