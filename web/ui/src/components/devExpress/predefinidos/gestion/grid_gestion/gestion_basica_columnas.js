let lista_acciones =  [
    { id: 'ASIGNADO_RESPONSABLE',              nombre: 'ASIGNADO RESPONSABLE' },
    { id: 'ASIGNADO',                          nombre: 'ASIGNADO DEPENDENCIA' },
    { id: 'TRASLADADO',                        nombre: 'TRASLADADO' },        
    { id: 'ASIGNADO_DEPENDENCIA',              nombre: 'ASIGNADO DEPENDENCIA' },        
    { id: 'DEVUELTO_ASIGNADORA',               nombre: 'DEVUELTO ASIGNADORA' },        
    { id: 'DEVUELTO_ASIGNADOR',                nombre: 'DEVUELTO ASIGNADOR' },        
    { id: 'TRASLADO_DEPENDENCIA',              nombre: 'TRASLADO DEPENDENCIA' },        
    { id: 'FINALIZADO_MANUAL',                 nombre: 'FINALIZADO MANUAL' },        
    { id: 'VISTO_BUENO',                       nombre: 'VISTO BUENO' },        
    { id: 'SOLICITADO_COLABORATIVA',           nombre: 'SOLICITADO COLABORATIVA' },        
    { id: 'HABILITADO_RAPIDA',                 nombre: 'HABILITADO RAPIDA' },        
    { id: 'DEVUELTO_REVISION',                 nombre: 'DEVUELTO REVISION' },    
    { id: 'DOCUMENTO_RADICADO',                nombre: 'DOCUMENTO_RADICADO' },                               
    { id: 'ASIGNADO_RESPONSABLE_COLABORATIVA', nombre: 'ASIGNADO RESPONSABLE COLABORATIVA' },
    { id: 'FINALIZADA_COLABORATIVA',           nombre: 'FINALIZADA_COLABORATIVA' },    
    { id: 'ASIGNADO_RESPONSABLE',              nombre: 'ASIGNADO_RESPONSABLE' },  
    { id: 'ASIGNADO_RESPONSABLE',              nombre: 'ASIGNADO_RESPONSABLE' },  
    { id: 'MIS_APROBACIONES',                  nombre: 'MIS APROBACIONES' },    
    { id: 'ASIGNADOS',                         nombre: 'ASIGNADOS' },    
]
lista_acciones.sort(function(a, b) {
    if (a.nombre < b.nombre) {
        return -1;
      }
      if (a.nombre > b.nombre) {
        return 1;
      }
      // a debe ser igual b
      return 0;
});


let columnas = [
    // Estado vencimiento
    {
        caption       : "Estado",
        dataField     : "estado_vencimiento",
        dataType      : "string",
        allowSorting  : true,
        allowFiltering: true,
        lookup        : {
            dataSource: {
                store: {
                    type: 'array',
                    data: [
                        { id: 'TERMINOS',  nombre: 'TERMINOS' },
                        { id: 'VENCIDO',   nombre: 'VENCIDO' },    
                    ],
                    key: "id"
                },
                
            },
            valueExpr  : 'id', 
            displayExpr: 'nombre',            
        },
        cellTemplate: "estado_vencimiento_plantilla",
        width      : "150px"       
    },

    // Vence en
    {
        caption       : "Vence en",
        dataField     : "vence_en",
        dataType      : "date",
        allowSorting  : true,
        allowFiltering: true,
        width         : "95px",
        format        : 'y-MM-dd'
    },

    // Prioridad
    {
        caption       : "Prioridad",
        dataField     : "prioridad",
        dataType      : "string",
        allowSorting  : true,
        allowFiltering: true,
        lookup        : {
            dataSource: {
                store: {
                    type: 'array',
                    data: [
                        { id: 'ALTA',  nombre: 'ALTA' },
                        { id: 'MEDIA', nombre: 'MEDIA' },
                        { id: 'BAJA',  nombre: 'BAJA' },        
                    ],
                    key: "id"
                },
                
            },
            valueExpr  : 'id', 
            displayExpr: 'nombre',           
        },  
        width      : "95px"
    },

    // Etapa gestion
    {
        caption       : "Acción",
        dataField     : "etapa_estado",
        dataType      : "string",
        allowSorting  : true,
        allowFiltering: true,
        lookup        : {
            dataSource: {
                store: {
                    type: 'array',
                    data: lista_acciones,
                    key: "id"
                },
                
            },
            valueExpr  : 'id', 
            displayExpr: 'nombre',           
        },  
        width         : "200px"
    },

    // Tipo documento
    {
        caption       : "Tipo",
        dataField     : "origen_tipo",
        dataType      : "string",
        allowSorting  : true,
        allowFiltering: true,
        lookup        : {
            dataSource: {
                store: {
                    type: 'array',
                    data: [
                        { id: 'ENTRADA', nombre: 'ENTRADA' },    
                        { id: 'SALIDA',  nombre: 'SALIDA' }, 
                        { id: 'INTERNO', nombre: 'INTERNO' }
                    ],
                    key: "id"
                },
                
            },
            valueExpr  : 'id', 
            displayExpr: 'nombre',           
        }, 
        width         : "110px"
    },

    // Numero de radicado
    {
        caption       : "# Radicado",
        dataField     : "nro_radicado",
        dataType      : "string",
        allowSorting  : true,
        allowFiltering: true,
        width         : "110px"
    },

    // Tipo gestión
    {
        caption       : "Tipo gestión",
        dataField     : "tipo_gestion",
        dataType      : "string",
        allowSorting  : true,
        allowFiltering: true,
        width         : "120px"
    },

    // Radicado
    {
        caption       : "Fecha de radicación",
        dataField     : "fecha_radicado",
        dataType      : "date",
        allowSorting  : true,
        allowFiltering: true,
        width         : "130px",
        format        : 'y-MM-dd HH:MM'
    },
    
    // Nombre tercero
    {
        caption       : "Nombre remitente",
        dataField     : "tercero_nombres_apellidos",
        dataType      : "string",         
        width         : "150px",
        allowSorting  : true,
        allowFiltering: true,
    },

    // Razon social
    {
        caption       : "Razon social",
        dataField     : "tercero_razon_social",
        dataType      : "string",         
        width         : "150px",
        allowSorting  : true,
        allowFiltering: true,
    },

     // Asunto
     {
        caption       : "Asunto",
        dataField     : "asunto",
        dataType      : "string",         
        width         : "120px",
        allowSorting  : false,
        allowFiltering: true,
    },

    // Peticion nombre
    {
        caption       : "Petición",
        dataField     : "peticion_nombre",
        dataType      : "string",
        allowSorting  : true,
        allowFiltering: true,
        width         : "150px",
    },

    // Etapa
    {
        caption       : "Etapa",
        dataField     : "etapa_gestion",
        dataType      : "string",
        allowSorting  : true,
        allowFiltering: true,
        width         : 200
    },

    // Clase tercero
    {
        caption       : "Clase remitente",
        dataField     : "tercero_clase",
        dataType      : "string",         
        width         : 90,
        allowSorting  : true,
        allowFiltering: true,
    },

    // Tipo tercero
    {
        caption       : "Tipo remitente",
        dataField     : "tercero_tipo_tercero_nombre",
        dataType      : "string",         
        width         : 130,
        allowSorting  : true,
        allowFiltering: true,
    },

    // Responsable nombre
    {
        caption       : "Responsable",
        dataField     : "responsable_nombre",
        dataType      : "string",
        allowSorting  : true,
        allowFiltering: true,
        width         : 250
    },

    // Dependencia nombre
    {
        caption       : "Dependencia",
        dataField     : "dependencia_nombre",
        dataType      : "string",
        allowSorting  : true,
        allowFiltering: true,
        width         : 250
    },

    // Fuente
    {
        caption       : "Origen",
        dataField     : "clase_radicado",
        dataType      : "string",
        allowSorting  : true,
        allowFiltering: true,
        lookup        : {
            dataSource: {
                store: {
                    type: 'array',
                    data: [
                        { id: 'VENTANILLA', nombre: 'VENTANILLA' },
                        { id: 'PQRS',       nombre: 'PQRS' }   
                    ],
                    key: "id"
                },
                
            },
            valueExpr  : 'id', 
            displayExpr: 'nombre',           
        },  
        width      : "150px"
    },
]

export default {
    columnas: columnas
}