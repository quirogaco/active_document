import basicos      from './basicos.js'
import eventos      from './eventos.js'
import validaciones from './validaciones.js'

const texto = function(id, atributos) {
    let titulo        = $librerias.cargaAtributo(atributos, 'titulo', "")
    let eventos_campo = eventos.eventos(atributos)
    let validadores   = validaciones.validaciones(atributos)

    let editorOptions = {
        "hint"           : $librerias.cargaAtributo(atributos, 'ayuda', titulo),  
        "placeholder"    : $librerias.cargaAtributo(atributos, 'mensaje', titulo),        
        'maxLength'      : $librerias.cargaAtributo(atributos, 'longitud', undefined),
        'mode'           : $librerias.cargaAtributo(atributos, 'modo', 'text'),   
        'readOnly'       : $librerias.cargaAtributo(atributos, 'lectura', false),
        'spellcheck'     : $librerias.cargaAtributo(atributos, 'revision', true),
        'value'          : $librerias.cargaAtributo(atributos, 'valor',  ""),
        'width'          : $librerias.cargaAtributo(atributos, 'ancho',  undefined),
        'height'         : $librerias.cargaAtributo(atributos, 'alto',  undefined),
        "showClearButton": $librerias.cargaAtributo(atributos, 'limpiar', true),
        "validationRules": undefined, // Revisar
        'elementAttr'    : {
            "autocomplete": "off"
        }
    }
    let opciones_totales = Object.assign(editorOptions, eventos_campo)

    let campo = {
        'dataField'      : id,
        'editorType'     : "dxTextBox",
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
    campo: texto
}