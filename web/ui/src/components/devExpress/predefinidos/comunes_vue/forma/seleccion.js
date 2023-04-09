import basicos from './basicos.js'
import fuente from './fuente.js'
import eventos from './eventos.js'
import validaciones from './validaciones.js'

const seleccion = function(id, atributos) {
    let titulo        = $librerias.cargaAtributo(atributos, 'titulo', "")
    let eventos_campo = eventos.eventos(atributos)
    let validadores   = validaciones.validaciones(atributos)
    let filtros_ds    = $librerias.cargaAtributo(atributos, 'filtros_fuente', [])
    let eventos_ds    = $librerias.cargaAtributo(atributos, 'eventos_fuente', {})
    let dataSource    = fuente.fuente_datos('select', atributos, filtros_ds, eventos_ds)
    let editorOptions = {
        "dataSource"  : dataSource,
        "displayValue": $librerias.cargaAtributo(atributos, 'muestra_valor',"nombre"),
        "displayExpr" : $librerias.cargaAtributo(atributos, 'muestra_expresion',"nombre"),
        "searchExpr"  : $librerias.cargaAtributo(atributos, 'busqueda_expresion',"nombre"),
        "valueExpr"   : $librerias.cargaAtributo(atributos, 'valor_expresion',"id"),
        'height'       : $librerias.cargaAtributo(atributos, 'alto',  undefined),
        "hint"         : $librerias.cargaAtributo(atributos, 'ayuda', titulo),  
        'maxLength'    : $librerias.cargaAtributo(atributos, 'longitud', undefined),      
        "placeholder"  : $librerias.cargaAtributo(atributos, 'mensaje', titulo),       
        'readOnly'     : $librerias.cargaAtributo(atributos, 'lectura', false),
        "searchEnabled": $librerias.cargaAtributo(atributos, 'buscar', true),
        "searchTimeout": $librerias.cargaAtributo(atributos, 'buscar_tiempo', 500),
        'value'        : $librerias.cargaAtributo(atributos, 'valor',  ""),
        'width'        : $librerias.cargaAtributo(atributos, 'ancho',  undefined),
        'wrapItemText' : $librerias.cargaAtributo(atributos, 'ajusta_texto',  true),
        "minSearchLength"   : $librerias.cargaAtributo(atributos, 'caracteres_buscar', 0),
        "openOnFieldClick"  : $librerias.cargaAtributo(atributos, 'abrir_click', true),
        "showClearButton"   : $librerias.cargaAtributo(atributos, 'limpiar', true),   
        "showDropDownButton": $librerias.cargaAtributo(atributos, 'desplegable', true),  
        'elementAttr': {
            "autocomplete": "off"
        }
    }

    let opciones_totales = Object.assign(editorOptions, eventos_campo)

    let campo = {
        'dataField'      : id,
        'editorType'     : "dxSelectBox",
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
    campo: seleccion
}