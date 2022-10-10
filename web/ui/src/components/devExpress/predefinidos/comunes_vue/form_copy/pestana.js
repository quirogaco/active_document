const pestana = function(id, atributos) {
    let campo = {
        "alignItemLabels": window.$librerias.cargaAtributo(atributos, "alineacion",  true), 
        "badge"          : window.$librerias.cargaAtributo(atributos, "insignia",  "")  ,
        "colCount"       : window.$librerias.cargaAtributo(atributos, "columnas", 1),
        "disabled"       : window.$librerias.cargaAtributo(atributos, "habilitado", true),
        "icon"           : window.$librerias.cargaAtributo(atributos, "icono", undefined),
        "items"          : window.$librerias.cargaAtributo(atributos, "elementos", []),
        "title"          : window.$librerias.cargaAtributo(atributos, "titulo", []),
        "visible"        : window.$librerias.cargaAtributo(atributos, 'visible', true),
        'cssClass'       : window.$librerias.cargaAtributo(atributos, "cssClase", null)
    }

    return campo
}

export default {
    campo: pestana
}