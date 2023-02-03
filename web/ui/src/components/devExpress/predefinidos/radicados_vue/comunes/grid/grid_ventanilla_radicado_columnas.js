let columnas = [
    // Clase Radicado
    {
        caption       : "Tipo",
        dataField     : "clase_radicado",
        dataType      : "string",             
        width         : 130,
        //cellTemplate  : "icono_pdf_template"
    },

    // Clase Radicado
    {
        caption       : "Canal/Medio",
        dataField     : "canal_radicado_nombre",
        dataType      : "string",             
        width         : 120
    },

    // Radicado
    {
        caption    : "Nro radicado",
        dataField  : "nro_radicado",
        dataType   : "string",        
        width      : 130       
    },

    // Fecha Radicado
    {
        caption       : "Fecha radicado",
        dataField     : "fecha_radicado",
        dataType      : "datetime",          
        width         : 210,
        format        : 'y-MM-dd hh:mm:ss'
    },

    // Nombre tercero
    {
        caption       : "Razon social",
        dataField     : "tercero_razon_social",
        dataType      : "string",         
        width         : 200
    },

    // Nombre tercero
    {
        caption       : "Remitente nombre",
        dataField     : "tercero_nombres_apellidos",
        dataType      : "string",         
        width         : 200
    },

    // Nit/Documento de identificación
    {
        caption       : "Nit/Identificación",
        dataField     : "tercero_nro_identificacion",
        dataType      : "string",         
        width         : 130
    },

    // Clase tercero
    {
        caption       : "Clase",
        dataField     : "tercero_clase",
        dataType      : "string",         
        width         : 90
    },

    // Tipo tercero
    {
        caption       : "Tipo",
        dataField     : "tercero_tipo_tercero_nombre",
        dataType      : "string",         
        width         : 130
    },

    // Asunto
    {
        caption     : "Asunto",
        dataField   : "asunto",
        dataType    : "string",        
        width       : 600,
        allowSorting: false   
    },

    // Dependencia
    {
        caption     : "Dependencia responsable",
        dataField   : "gestion_dependencia_nombre",
        dataType    : "string",        
        width       : 400,
        allowSorting: true
    },

    // Dependencia
    {
        caption     : "Funcionario responsable",
        dataField   : "gestion_responsable_nombre",
        dataType    : "string",        
        width       : 300,
        allowSorting: true
    },
]

export default {
    columnas: columnas
}