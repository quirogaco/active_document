const button = function(id, atributos) {
    let editorOptions = {
        'text'   : (atributos.titulo != undefined? atributos.titulo : '...'),  
        'icon'   : (atributos.icon != undefined? atributos.icon : null),  
        'type'   : (atributos.type != undefined? atributos.type : 'default'),  
        'onClick': (atributos.click != undefined? atributos.click : null)
    }
    let opciones_totales = Object.assign(editorOptions, {})

    let button = {
        'itemType'           : 'button',
        'name'               : $librerias.cargaAtributo(atributos, 'nombre', id),
        'visible'            : $librerias.cargaAtributo(atributos, 'visible', true),  
        'horizontalAlignment': $librerias.cargaAtributo(atributos, 'horizontal', "left"),  
        'verticalAlignment'  : $librerias.cargaAtributo(atributos, 'vertical', "center"),  
        'buttonOptions'      : opciones_totales
    }

    return button
}

export default {
    campo: button
}