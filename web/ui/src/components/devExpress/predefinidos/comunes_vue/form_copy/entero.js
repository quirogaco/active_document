import basicos      from './basicos.js'
import eventos      from './eventos.js'
import validaciones from './validaciones.js'

const entero = function(id, atributos) {
    let titulo        = window.$librerias.cargaAtributo(atributos, 'titulo', "")
    let eventos_campo = eventos.eventos(atributos)    
    let validadores   = validaciones.validaciones(atributos)

    let editorOptions = {
        "hint"       : window.$librerias.cargaAtributo(atributos, 'ayuda', titulo),  
        "placeholder": window.$librerias.cargaAtributo(atributos, 'mensaje', titulo),        
        'maxLength'  : window.$librerias.cargaAtributo(atributos, 'longitud', undefined),
        'mode'       : window.$librerias.cargaAtributo(atributos, 'modo', 'text'),   
        'readOnly'   : window.$librerias.cargaAtributo(atributos, 'lectura', false),
        'max'        : window.$librerias.cargaAtributo(atributos, 'maxima',  undefined),
        'min'        : window.$librerias.cargaAtributo(atributos, 'minima',  0),
        'spellcheck' : window.$librerias.cargaAtributo(atributos, 'revision', true),
        'value'      : window.$librerias.cargaAtributo(atributos, 'valor',  "0"),
        'width'      : window.$librerias.cargaAtributo(atributos, 'ancho',  undefined),
        'height'     : window.$librerias.cargaAtributo(atributos, 'alto',  undefined),
        "showClearButton": $librerias.cargaAtributo(atributos, 'limpiar', true),
        "showSpinButtons": $librerias.cargaAtributo(atributos, 'girar', true),
        'elementAttr': {
            "autocomplete": "off"
        }             
    }
    let opciones_totales = Object.assign(editorOptions, eventos_campo)

    let campo = {
        'dataField'      : id,
        'editorType'     : "dxNumberBox",
        'label'          : basicos.label(atributos),  
        //'isRequired'   : window.$librerias.cargaAtributo(atributos, 'obligatorio', false),    
        'itemType'       : 'simple',
        'name'           : window.$librerias.cargaAtributo(atributos, 'nombre', id),
        'visible'        : window.$librerias.cargaAtributo(atributos, 'visible', true),          
        'editorOptions'  : opciones_totales,
        "validationRules": validadores
    }

    return campo
}

export default {
    campo: entero
}