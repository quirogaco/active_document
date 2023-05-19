import librerias  from '../../../../librerias/librerias.js';

const eventos = function(atributos, editorOptions) {
    let eventos = librerias.cargaAtributo(atributos, "eventos", {}) 
    let selección_cambiada = librerias.cargaAtributo(eventos, "seleccion_cambiada", null)
    let cambiar = librerias.cargaAtributo(eventos, "cambiar", null)     
    let recibe_foco = librerias.cargaAtributo(eventos, "recibe_foco", null)     
    
    editorOptions["onSelectionChanged"] = selección_cambiada;
    editorOptions["onChanged"] = cambiar;
    editorOptions["onFocusIn"] = recibe_foco;
    //console.log("editorOptions:", editorOptions)
    
    return editorOptions;
}

export default {
    eventos: eventos
}