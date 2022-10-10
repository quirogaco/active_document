let columnas = [
    // Nombre
    {
        caption    : "Asunto",
        dataField  : "nombre",
        dataType   : "string",        
        width      : 600       
    },

    // Subserie/Serie
    {
        caption       : "Serie/Subserie",
        dataField     : "serie_subserie",
        dataType      : "string",     
        width         : 350
    },

    // Dependencia
    {
        caption       : "Dependencia",
        dataField     : "dependencia_nombre",
        dataType      : "string",     
        width         : 350
    },


    /*
    // Codigo
    {
        caption    : "Codigo",
        dataField  : "codigo",
        dataType   : "string",        
        width      : 100   
    },
    */    
]

export default {
    columnas: columnas
}