
let columnas = [
    // Nombre
    {
        caption    : "Nombre",
        dataField  : "nombre",
        width      : 400,
    },

    // Formulario
    {
        caption       : "Formulario",
        dataField     : "formulario_nombre",
        width         : 400,
    },

    // Total tiempo
    {
        caption       : "Tiempo",
        dataField     : "total_tiempo",
        width         : 150,
        allowSorting  : false
    },
    
    // Dias/Horas
    {
        caption       : "Dias/Horas",
        dataField     : "horas_dias",
        width         : 150,
        allowSorting  : false
    }
]

export default {
    columnas: columnas
}