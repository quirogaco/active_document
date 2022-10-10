import forma_definiciones from "../../../comunes_vue/forma/forma.js"

// Trd consulta
let columnas = [
    {
        'dataField': 'trd_dependencia_nombre',
        'caption'  : 'Dependencia',
        'width'    : 350,
    }, 

    {
        'dataField': 'expediente_nombre',
        'caption'  : 'Expediente',
        'width'    : 350,
    }, 

    {
        'dataField': 'tipo_nombre',
        'caption'  : 'Tipo documental',
        'width'    : 350,
    }, 
]

const expedientes_tipos = function(id=null, atributos={}) {
    let atributos_base = {
        "columnas" : columnas,
        "eventos"  : {},
        "fuente"   : []
    }
    
    return forma_definiciones.genera_campo("grid", "expedientes_tipos", id, atributos_base, atributos)
}

export default {
    expedientes_tipos: expedientes_tipos
}