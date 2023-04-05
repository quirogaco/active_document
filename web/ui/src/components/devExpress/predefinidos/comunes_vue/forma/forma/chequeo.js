import basicos      from './basicos.js'
import fuente       from './fuente.js'
import eventos      from './eventos.js'
import validaciones from './validaciones.js'

const chequeo = function(id, atributos) {
    let titulo        = $librerias.cargaAtributo(atributos, 'titulo', "")
    let eventos_campo = eventos.eventos(atributos)
    let validadores   = validaciones.validaciones(atributos)

    let editorOptions = {
        'readOnly': window.$librerias.cargaAtributo(atributos, 'lectura', false),
        'height'  : $librerias.cargaAtributo(atributos, 'alto',  undefined),
        "hint"    : $librerias.cargaAtributo(atributos, 'ayuda', titulo),  
        'text'    : $librerias.cargaAtributo(atributos, 'valor',  ""),
        'width'   : $librerias.cargaAtributo(atributos, 'ancho',  undefined),
    }
    let opciones_totales = Object.assign(editorOptions, eventos_campo)

    let campo = {
        'dataField'      : id,
        'editorType'     : "dxCheckBox",
        'label'          : basicos.label(atributos), 
        'itemType'       : 'simple',
        'name'           : $librerias.cargaAtributo(atributos, 'nombre', id),
        'visible'        : $librerias.cargaAtributo(atributos, 'visible', true),  
        'editorOptions'  : opciones_totales,
        "validationRules": validadores
    }

    return campo
}

export default {
    campo: chequeo
}