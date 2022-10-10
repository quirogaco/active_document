let columnas = [
    // Nombre
    {
        caption  : "Descripción",
        dataField: "descripcion",
        dataType : "string",        
        width    : 600       
    },

    // Dependencia
    {
        caption  : "Dependencia",
        dataField: "dependencia_nombre",
        dataType : "date",          
        dataType : "string",        
        width    : 340
    },

    // Archivo
    {
        caption  : "Archivo",
        dataField: "tipo_archivo",
        dataType : "string",         
        width    : 150
    }
]

export default {
    columnas: columnas
}