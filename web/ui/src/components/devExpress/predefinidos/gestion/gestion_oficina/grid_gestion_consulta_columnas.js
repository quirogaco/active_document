let columnas = [
    {
        caption     : "Tipo radicado",
        dataField   : "tipo_radicado",
        dataType    : "string",        
        width       : 200,
        allowFiltering: true,
        lookup        : {
            dataSource: {
                store: {
                    type: 'array',
                    data: [
                        { id: 'ENTRADA', nombre: 'ENTRADA' },
                        { id: 'SALIDA', nombre: 'SALIDA' },    
                        { id: 'INTERNO', nombre: 'INTERNO' },    
                    ],
                    key: "id"
                },
                
            },
            valueExpr  : 'id', 
            displayExpr: 'nombre',            
        },
    },

    {
        caption     : "# Radicado",
        dataField   : "nro_radicado",
        dataType    : "string",        
        width       : 200,
        allowFiltering: true
    },

    // Fecha Radicado
    {
        caption       : "Fecha radicado",
        dataField     : "fecha_radicado",
        dataType      : "datetime",          
        width         : 180,
        format        : 'y-MM-dd hh:mm:ss',
        allowFiltering: true
    },

    // Asunto
    {
        caption     : "Asunto",
        dataField   : "asunto",
        dataType    : "string",        
        width       : 600,
        allowSorting: false   
    }

    // // Nombre tercero
    // {
    //     caption       : "Dependencia",
    //     dataField     : "dependencia_responde_nombre",
    //     dataType      : "string",         
    //     width         : 250
    // },

    // // Nombre tercero
    // {
    //     caption       : "Destinatario",
    //     dataField     : "tercero_nombres_apellidos",
    //     dataType      : "string",         
    //     width         : 250
    // },

    // // Clase tercero
    // {
    //     caption       : "Clase",
    //     dataField     : "tercero_clase",
    //     dataType      : "string",         
    //     width         : 90
    // },

    // // Tipo tercero
    // {
    //     caption       : "Tipo",
    //     dataField     : "tercero_tipo_tercero_nombre",
    //     dataType      : "string",         
    //     width         : 130
    // },
]

export default {
    columnas: columnas
}