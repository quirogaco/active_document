let columnas = [
    // Dependencia
    {
        caption       : "Dependencia",
        dataField     : "dependencia_nombre",
        dataType      : "string",
        width         : 500       
    },

    // Detalle
    {
        caption       : "Detalle",
        dataField     : "detalle",
        dataType      : "string",
        width         : 700       
    },

    // Creado en
    {
        caption       : "Fecha creación",
        dataField     : "creado_en_",
        dataType      : "date",
        width         : 150
    },

    // Origen
    {
        caption       : "Origen",
        dataField     : "origen",
        dataType      : "string",
        width         : 150       
    },
]

export default {
    columnas: columnas
}