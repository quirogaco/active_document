import eventos      from './eventos.js';

const contenido = function(id, atributos) {
    let eventos_campo = eventos.eventos(atributos);
 
    let editorOptions = {
        'value'      : $librerias.cargaAtributo(atributos, 'valor',  ""),
        'width'      : $librerias.cargaAtributo(
            atributos, 
            'ancho',  
            undefined
        ),
        'height'     : $librerias.cargaAtributo(
            atributos, 
            'alto',  
            undefined
        )
    }
    let opciones_totales = Object.assign(editorOptions, eventos_campo)

    let campo = {
        'dataField': "",
        'editorType': "",
        'template': $librerias.cargaAtributo(
            atributos, 
            'template', 
            "contenido-template"
        ),
        'name': $librerias.cargaAtributo(
            atributos, 
            'nombre', 
            id
        ),
        'visible': $librerias.cargaAtributo(
            atributos, 
            'visible', 
            true
        ),  
        'editorOptions': opciones_totales
    }

    return campo
}

export default {
    campo: contenido
}