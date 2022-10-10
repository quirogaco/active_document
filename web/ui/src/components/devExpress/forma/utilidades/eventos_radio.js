import librerias  from '../../../../librerias/librerias.js';

const eventos = function(atributos, editorOptions) {
    let eventos            = librerias.cargaAtributo(atributos, "eventos", {}) 
    let selección_cambiada = librerias.cargaAtributo(eventos, "seleccion_cambiada", null)     
    let recibe_foco        = librerias.cargaAtributo(eventos, "recibe_foco", null)    
    
    editorOptions["onValueChanged"] = selección_cambiada;
    editorOptions["onFocusIn"]      = recibe_foco;
    
    return editorOptions;}

export default {
    eventos: eventos
}