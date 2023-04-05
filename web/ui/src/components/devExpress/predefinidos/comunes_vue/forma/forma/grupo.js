const grupo = function(id, atributos) {
    let campo = {
        'itemType': "group",
        'caption' : window.$librerias.cargaAtributo(atributos, 'titulo', ""),
        'colSpan' : window.$librerias.cargaAtributo(atributos, 'expandir', undefined),
        'items'   : window.$librerias.cargaAtributo(atributos, 'elementos', []),
        'name'    : window.$librerias.cargaAtributo(atributos, 'nombre', id),
        'visible' : window.$librerias.cargaAtributo(atributos, 'visible', true),
        'colCount': window.$librerias.cargaAtributo(atributos, 'columna', 1),
        'cssClass': "rounded-2 bg-light shadow-sm  p-1 m-1  border border-2 border-white"
    }
   
    return campo
}

export default {
    campo: grupo
}