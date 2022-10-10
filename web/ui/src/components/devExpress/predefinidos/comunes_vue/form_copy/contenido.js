import basicos      from './basicos.js'
import eventos      from './eventos.js'
import validaciones from './validaciones.js'

const contenido = function(id, atributos) {
    let titulo        = $librerias.cargaAtributo(atributos, 'titulo', "")
    let eventos_campo = eventos.eventos(atributos)
    let validadores   = validaciones.validaciones(atributos)

    let editorOptions = {
        'value'      : $librerias.cargaAtributo(atributos, 'valor',  ""),
        'width'      : $librerias.cargaAtributo(atributos, 'ancho',  undefined),
        'height'     : $librerias.cargaAtributo(atributos, 'alto',  undefined)
    }
    let opciones_totales = Object.assign(editorOptions, eventos_campo)

    let campo = {
        'dataField'      : "",
        'editorType'     : "",
        'template'       : "contenido-template",
        //'label'          : basicos.label(atributos),  
        'name'           : $librerias.cargaAtributo(atributos, 'nombre', id),
        'visible'        : $librerias.cargaAtributo(atributos, 'visible', true),  
        'editorOptions'  : opciones_totales,
    }

    return campo
}

export default {
    campo: contenido
}