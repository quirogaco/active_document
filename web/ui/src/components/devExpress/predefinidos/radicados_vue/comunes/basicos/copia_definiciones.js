import forma_definiciones from "../../../comunes_vue/forma/forma.js"

// Copia consulta
let columnas = [
    {
        'dataField': 'destinatario_tipo',
        'caption'  : 'Destinatario tipo',
        'width'    : 150,
    }, 
    {
        'dataField': 'destinatario_nombre',
        'caption'  : 'Destinatario nombre',
        'width'    : 700,
    },
    {
        'dataField': 'estado',
        'caption'  : 'Estado',
        'width'    : 300,
    }
]

const con_copia = function(id=null, atributos={}) {
    let atributos_base = {
        "columnas" : columnas,
        "eventos"  : {},
        "fuente"   : []
    }
    
    return forma_definiciones.genera_campo("grid", "con_copia", id, atributos_base, atributos)
}

export default {
    con_copia: con_copia
}