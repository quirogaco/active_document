let columnas = [
    {
        caption       : "#",
        dataField     : "consecutivo",
        dataType      : "integer",         
        width         : "40px"
    },
    
    {
        caption  : "Creado",
        dataField: "fecha_creacion",
        dataType : "date",         
        width    : "100px",
        format   : "y-MM-dd"  
    },

    {
        caption  : "Incorporado",
        dataField: "fecha_incorporado",
        dataType : "date",         
        width    : "100px",
        format   : "y-MM-dd"  
    },

    {
        caption     : "Tipo documental",
        dataField   : "tipo_nombre",
        dataType    : "string",        
        width       : "280px"  
    },

    {
        caption       : "Descripción",
        dataField     : "detalle",
        dataType      : "string",     
        width         : "280px"
    },

    {
        caption       : "Soporte",
        dataField     : "soporte",
        dataType      : "string",         
        width         : "110px"
    },

    {
        caption       : "Carpeta",
        dataField     : "carpeta_nro",
        dataType      : "string",         
        width         : "70px"
    },

    {
        caption       : "Folios fisicos",
        dataField     : "folios_fisicos",
        dataType      : "integer",         
        width         : "60px"
    },

    {
        caption       : "Folios electrónicos",
        dataField     : "folios_electronicos",
        dataType      : "integer",         
        width         : "100px",
        cssClass      : " bg-green-800 "
    },

    {
        caption     : "Tipo",
        dataField   : "tipo_archivo",
        dataType    : "string",         
        width       : "75px",        
        cellTemplate: "tipo_icono_plantilla"
    },


    {
        caption       : "Tamaño (bytes)",
        dataField     : "tamano",
        dataType      : "integer",         
        width         : "80px"
    },

    {
        caption       : "Observación",
        dataField     : "observacion",
        dataType      : "string",     
        width         : "300px"
    },
]

export default {
    columnas: columnas
}