import basicos from './basicos.js'
import eventos from './eventos.js'
import fuente  from './fuente.js'

const grid = function(id, atributos) {
    let eventos_campo = eventos.eventos(atributos)    
    let filtros_ds    = $librerias.cargaAtributo(atributos, 'filtros_fuente', [])
    let eventos_ds    = $librerias.cargaAtributo(atributos, 'eventos_fuente', {})
    let dataSource    = fuente.fuente_datos('grid', atributos, filtros_ds, eventos_ds)

    let editorOptions = {
        "hoverStateEnabled"    : true,
        "rowAlternationEnabled": true,
        "dataSource"           : dataSource,
        'width'                : $librerias.cargaAtributo(atributos, 'ancho',  undefined),
        'wordWrapEnabled'      : $librerias.cargaAtributo(atributos, 'ajusta_texto',  true),
        'columns'              : $librerias.cargaAtributo(atributos, 'columnas',  []),
    }
    let opciones_totales = Object.assign(editorOptions, eventos_campo)
    
    let campo = {
        'dataField'      : "",
        'editorType'     : "dxDataGrid",
        'itemType'       : 'simple',
        'label'          : basicos.label(atributos),  
        'name'           : $librerias.cargaAtributo(atributos, 'nombre', id),
        'visible'        : $librerias.cargaAtributo(atributos, 'visible', true),  
        'editorOptions'  : opciones_totales
    }
    
    return campo;
}

export default {
    campo: grid
}