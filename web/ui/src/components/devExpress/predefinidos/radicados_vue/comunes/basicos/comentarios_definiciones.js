import forma_definiciones from "../../../comunes_vue/forma/forma.js"

// Comentarios consulta
let columnas = [
    {
        'dataField': 'fecha',
        'caption'  : 'Fecha',
        'width'    : 150,
    }, 
    {
        'dataField': 'usuario',
        'caption'  : 'Usuario',
        'width'    : 300,
    },
    {
        'dataField': 'anotacion',
        'caption'  : 'Comentario',
        'width'    : 450,
    } 
]

const gestion_comentarios = function(id=null, atributos={}) {
    let atributos_base = {
        "columnas" : columnas,
        "eventos"  : {},
        "fuente"   : []
    }
    
    return forma_definiciones.genera_campo("grid", "gestion_comentarios", id, atributos_base, atributos)
}

export default {
    gestion_comentarios: gestion_comentarios
}