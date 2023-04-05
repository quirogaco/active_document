let columnas = [
    {
        caption     : "Tipo radicado",
        dataField   : "tipo_radicado",
        dataType    : "string",        
        width       : 100,
        //allowFiltering: true,
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
        width       : 150,
        allowFiltering: true
    },

    {
        caption     : "Estado",
        dataField   : "gestion_estado",
        dataType    : "string",        
        width       : 100,
       // allowFiltering: true,
        lookup        : {
            dataSource: {
                store: {
                    type: 'array',
                    data: [
                        { id: 'PENDIENTE', nombre: 'PENDIENTE' },
                        { id: 'FINALIZADO', nombre: 'FINALIZADO' }
                    ],
                    key: "id"
                },
                
            },
            valueExpr  : 'id', 
            displayExpr: 'nombre',            
        },
    },

    {
        caption     : "Estado vencimiento",
        dataField   : "gestion_estado_vencimiento",
        dataType    : "string",        
        width       : 100,
        lookup        : {
            dataSource: {
                store: {
                    type: 'array',
                    data: [
                        { id: 'TERMINOS', nombre: 'TERMINOS' },
                        { id: 'VENCIDO', nombre: 'VENCIDO' }
                    ],
                    key: "id"
                },
                
            },
            valueExpr  : 'id', 
            displayExpr: 'nombre',            
        },
    },

    {
        caption     : "Dias en gestión",
        dataField   : "dias_gestion",
        dataType    : "integer",        
        width       : 65,
        allowSorting: false,
        allowFiltering: false  
    },

    {
        caption     : "Fecha respuesta",
        dataField   : "fecha_respuesta",
        dataType    : "date",        
        width       : 120,
        allowFiltering: false
    },

    {
        caption     : "Contestado con",
        dataField   : "nro_respuesta",
        dataType    : "string",        
        width       : 120,
        allowFiltering: false
    },

    // Fecha Radicado
    {
        caption       : "Fecha radicado",
        dataField     : "fecha_radicado",
        dataType      : "datetime",          
        width         : 150,
        format        : 'y-MM-dd hh:mm:ss',
        //allowFiltering: true
    },

    {
        caption     : "Remitente entidad/dependencia",
        dataField   : "remite_ent_dep_nombre",
        dataType    : "string",        
        width       : 200,
        //allowSorting: false   
    },

    {
        caption     : "Remitente persona/funcionario",
        dataField   : "remite_per_fun_nombre",
        dataType    : "string",        
        width       : 200,
        //allowSorting: false   
    },

    {
        caption     : "Recibe entidad/dependencia",
        dataField   : "recibe_ent_dep_nombre",
        dataType    : "string",        
        width       : 200,
        //allowSorting: false   
    },

    {
        caption     : "Recibe persona/funcionario",
        dataField   : "recibe_per_fun_nombre",
        dataType    : "string",        
        width       : 200,
        //allowSorting: false   
    },

    // Asunto
    {
        caption     : "Asunto",
        dataField   : "asunto",
        dataType    : "string",        
        width       : 400,
        allowSorting: false   
    },

    // Asunto
    {
        caption     : "Radicado en",
        dataField   : "radicado_en_nombre",
        dataType    : "string",        
        width       : 400
    }
]

export default {
    columnas: columnas
}