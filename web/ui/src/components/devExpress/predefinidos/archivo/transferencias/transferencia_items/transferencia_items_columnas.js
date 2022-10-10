let columnas = [
    // Fecha creación
    {
        caption  : "Fecha creación",
        dataField: "fecha_creacion",
        dataType : "date",         
        width    : "10%",
        format   : "y-MM-dd"  
    },

    // Tipod documental
    {
        caption     : "Tipo documental",
        dataField   : "tipo_nombre",
        dataType    : "string",        
        width       : "20%"  
    },

    // Detalle
    {
        caption       : "Descripción",
        dataField     : "detalle",
        dataType      : "string",     
        width         : "20%"
    },

    // Soporte
    {
        caption       : "Soporte",
        dataField     : "soporte",
        dataType      : "string",         
        width         : "10%"
    },

    // Folios fisicos
    {
        caption       : "Folios fisicos",
        dataField     : "folios_fisicos",
        dataType      : "integer",         
        width         : "10%"
    },

    // Folios electronicos
    {
        caption       : "Folios electronicos",
        dataField     : "folios_electronicos",
        dataType      : "integer",         
        width         : "10%",
        cssClass      : " bg-green-800 "
    },

    // Tipo de archivo
    {
        caption     : "Tipo",
        dataField   : "tipo_archivo",
        dataType    : "string",         
        width       : "10%",        
        cellTemplate: "tipo_icono_plantilla"
    },


    // Tamaño (bytes)
    {
        caption       : "Tamaño (bytes)",
        dataField     : "tamano",
        dataType      : "integer",         
        width         : "10%"
    },
]

export default {
    columnas: columnas
}