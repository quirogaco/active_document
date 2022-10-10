let columnas = [
    // clase
    {
        caption       : "Razon social",
        dataField     : "razon_social",
        dataType      : "string",
        allowEditing  : true,
        width         : 250
    },

    {
        caption       : "Nombre",
        dataField     : "nombre_completo",
        dataType      : "string",
        allowEditing  : true,
        width         : 300
    },
    
    // Detalle
    {
        caption       : "Direccción",
        dataField     : "direccion",
        dataType      : "string",
        allowEditing  : true,
        width         : 300,     
    },

    // Correo elecronicos
    {
        caption       : "Correo",
        dataField     : "correo_electronico",
        dataType      : "string",
        allowEditing  : true,
        width         : 200
    },   

    // Ubicación
    {
        caption       : "Ubicación",
        dataField     : "ciudad_nombre",
        dataType      : "string",
        width         : 200,
        allowEditing  : true
    }    
]

export default {
    columnas: columnas
}