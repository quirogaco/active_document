const label = function(atributos) {
    let definicion = {
        'text'     : window.$librerias.cargaAtributo(atributos, 'titulo',     ""),
        'alignment': window.$librerias.cargaAtributo(atributos, 'alineacion', "rigth"),
        'location' : window.$librerias.cargaAtributo(atributos, 'ubicacion',  "left"),    
    }

    return definicion
}

export default {
    label: label
}