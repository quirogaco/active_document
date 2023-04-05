import basicos      from './basicos.js'
import fuente       from './fuente.js'
import eventos      from './eventos.js'
import validaciones from './validaciones.js'

const radio = function(id, atributos) {
    let titulo        = $librerias.cargaAtributo(atributos, 'titulo', "");
    let eventos_campo = eventos.eventos(atributos);
    let validadores   = validaciones.validaciones(atributos);

    let filtros_ds    = [];
    let eventos_ds    = [];
    let dataSource    = fuente.fuente_datos('radio', atributos, filtros_ds, eventos_ds);
    
    let editorOptions = {
        "dataSource" : dataSource,
        "displayExpr":  $librerias.cargaAtributo(atributos, 'mostrar_expresion', "nombre"),
        "valueExpr"  : $librerias.cargaAtributo(atributos, 'valor_expresion',  "id"),
        "layout"     : $librerias.cargaAtributo(atributos, 'diseno', "horizontal"),
        'height'     : $librerias.cargaAtributo(atributos, 'alto',  undefined),
        "hint"       : $librerias.cargaAtributo(atributos, 'ayuda', titulo),  
        'readOnly'   : $librerias.cargaAtributo(atributos, 'lectura', false),
        'value'      : $librerias.cargaAtributo(atributos, 'valor',  null),
        'width'      : $librerias.cargaAtributo(atributos, 'ancho',  undefined)
    }
    let opciones_totales = Object.assign(editorOptions, eventos_campo);
    
    let campo = {
        'dataField'      : id,
        'editorType'     : "dxRadioGroup",
        'label'          : basicos.label(atributos),  
        //'isRequired'     : $librerias.cargaAtributo(atributos, 'obligatorio', false),    
        'itemType'       : 'simple',
        'name'           : $librerias.cargaAtributo(atributos, 'nombre', id),
        'visible'        : $librerias.cargaAtributo(atributos, 'visible', true),  
        'editorOptions'  : opciones_totales,
        "validationRules": validadores
    }

    return campo
}

export default {
    campo: radio
}