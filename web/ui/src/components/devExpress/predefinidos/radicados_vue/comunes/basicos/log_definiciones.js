import forma_definiciones from "../../../comunes_vue/forma/forma.js"

// Logs consulta
let columnas = [
    {
        'dataField': 'creado_en_',
        'caption'  : 'Fecha',
        'width'    : 150,
    }, 
    {
        'dataField': 'accionante_nombre',
        'caption'  : 'Accionante',
        'width'    : 300,
    },
    {
        'dataField': 'destinatario_nombre',
        'caption'  : 'Destinatario',
        'width'    : 300,
    },
    {
        'dataField': 'accion',
        'caption'  : 'Acción',
        'width'    : 150,
    },   
    {
        'dataField': 'detalle',
        'caption'  : 'Detalle',
        'width'    : 450,
    },     
]

const logs_radicado = function(id=null, atributos={}) {
    let atributos_base = {
        "columnas" : columnas,
        "eventos"  : {},
        "fuente"   : []
    }
    
    return forma_definiciones.genera_campo("grid", "logs_radicado", id, atributos_base, atributos)
}

export default {
    logs_radicado: logs_radicado
}