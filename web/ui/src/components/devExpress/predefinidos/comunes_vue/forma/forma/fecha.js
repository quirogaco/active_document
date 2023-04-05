import basicos      from './basicos.js'
import eventos      from './eventos.js'
import validaciones from './validaciones.js'

const fecha_hoy = function() {
    let fecha = new Date()
    //let hoy   = fecha.toISOString().split('T')[0]

    return fecha
}

const fecha = function(id, atributos) {
    let titulo        = window.$librerias.cargaAtributo(atributos, 'titulo', "")
    let eventos_campo = eventos.eventos(atributos)
    let validadores   = validaciones.validaciones(atributos)

    let editorOptions = {
        'dateSerializationFormat': window.$librerias.cargaAtributo(atributos, 'formato', "yyyy-MM-dd"),  
        'openOnFieldClick': window.$librerias.cargaAtributo(atributos, 'abierto', true),   
        "hint"            : window.$librerias.cargaAtributo(atributos, 'ayuda', titulo),  
        "placeholder"     : window.$librerias.cargaAtributo(atributos, 'mensaje', titulo),              
        'displayFormat'   : window.$librerias.cargaAtributo(atributos, 'formato', "yyyy-MM-dd"),            
        'pickerType'      : window.$librerias.cargaAtributo(atributos, 'selector', 'calendar'),  
        'max'             : window.$librerias.cargaAtributo(atributos, 'maxima',  fecha_hoy()),
        'min'             : window.$librerias.cargaAtributo(atributos, 'minima',  undefined),
        'readOnly'        : window.$librerias.cargaAtributo(atributos, 'lectura', false),
        'type'            : window.$librerias.cargaAtributo(atributos, 'tipo_fecha', 'date'),
        'value'           : window.$librerias.cargaAtributo(atributos, 'valor',  fecha_hoy()),
        'width'           : window.$librerias.cargaAtributo(atributos, 'ancho',  undefined),
        'height'          : window.$librerias.cargaAtributo(atributos, 'alto',  undefined),
        "maxLength"       : $librerias.cargaAtributo(atributos, 'longitud', undefined),
        "showClearButton" : $librerias.cargaAtributo(atributos, 'limpiar', true),
        "opened"          : $librerias.cargaAtributo(atributos, 'editor', false),
        'elementAttr'     : {
            "autocomplete": "off"
        }    
          
    }
    let opciones_totales = Object.assign(editorOptions, eventos_campo)

    let campo = {
        'dataField'      : id,
        'editorType'     : "dxDateBox",
        'label'          : basicos.label(atributos),  
        'itemType'       : 'simple',
        'name'           : window.$librerias.cargaAtributo(atributos, 'nombre', id),
        'visible'        : window.$librerias.cargaAtributo(atributos, 'visible', true),  
        'editorOptions'  : opciones_totales,
        "validationRules": validadores
    }

    return campo
}

export default {
    campo: fecha
}