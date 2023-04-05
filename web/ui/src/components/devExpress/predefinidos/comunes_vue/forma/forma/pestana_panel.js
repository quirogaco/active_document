const pestana_panel = function(id, atributos) {
    let tab_panel_opciones = {
        'deferRendering' : false
    }

    let campo = {
        'itemType'       : "tabbed",
        'colSpan'        : window.$librerias.cargaAtributo(atributos, 'expandir', undefined),
        'tabs'           : window.$librerias.cargaAtributo(atributos, 'elementos', []),
        'name'           : window.$librerias.cargaAtributo(atributos, 'nombre', id),
        'tabPanelOptions': window.$librerias.cargaAtributo(atributos, 'opciones', tab_panel_opciones),
        'visible'        : window.$librerias.cargaAtributo(atributos, 'visible', true),
        'cssClass'       : "rounded-3 bg-light shadow-sm  p-2 m-1  border border-5 border-white"
    }

    return campo
}

export default {
    campo: pestana_panel
}