import librerias            from '../../../../librerias/librerias.js';

// Boton item
const boton_objeto = function(atributos={}) {
    // Manejo de titulos
    let nombre     = librerias.cargaAtributo(atributos, "nombre",  null) 
    let titulo     = librerias.cargaAtributo(atributos, "titulo", "")
    let tipo       = librerias.cargaAtributo(atributos, "tipo", "success")
    let expandir   = librerias.cargaAtributo(atributos, "expandir", 1)
    let click      = librerias.cargaAtributo(atributos, "evt_click", null)
    let ancho      = librerias.cargaAtributo(atributos, "ancho",  null)
    let vertical   = librerias.cargaAtributo(atributos, "vertical", 'bottom')
    let horizontal = librerias.cargaAtributo(atributos, "horizontal", 'right')

    let boton_editor = {
        text   : titulo,
        type   : tipo,
        onClick: click,
        width  : ancho,
    };
    
    // Definición de la columna
    let definicion = {
        "itemType"           : 'button', 
        "nombre"             : nombre,
        "colSpan"            : expandir,
        "verticalAlignment"  : vertical,
        "horizontalAlignment": horizontal,
        "buttonOptions"      : boton_editor
    }

    return definicion;
}


export default {
    boton_objeto: boton_objeto   
}