import librerias            from '../../../../librerias/librerias.js';

// Grupo item
const grupo_objeto = function(atributos={}) {
    // Manejo de titulos
    let nombre    = librerias.cargaAtributo(atributos, "nombre",  null)   
    let titulo    = librerias.cargaAtributo(atributos, "titulo",   null)
    let expandir  = librerias.cargaAtributo(atributos, "expandir", 1)
    let items     = librerias.cargaAtributo(atributos, "elementos", [])
    let columnas  = librerias.cargaAtributo(atributos, "columnas", 1)
    let cssClase  = librerias.cargaAtributo(atributos, "cssClase", "shadow-sm p-2 m-1 bg_grupo rounded")
    
    // Definición de la columna
    let definicion = {
        "itemType": 'group', 
        "nombre"  : nombre,
        "caption" : titulo,
        "items"   : items,
        "colSpan" : expandir,
        "colCount": columnas,
        'cssClass': cssClase
    }

    return definicion;
}


export default {
    grupo_objeto: grupo_objeto   
}