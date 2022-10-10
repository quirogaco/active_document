import librerias            from '../../../../librerias/librerias.js';

// Tab item
const tab_objeto = function(atributos={}) {
    let alignItemLabels = librerias.cargaAtributo(atributos, "alineacion",  "si")  
    alignItemLabels = alignItemLabels == "si" ? true : false;
    
    let badge           = librerias.cargaAtributo(atributos, "insignia",  "")  
    let colCount        = librerias.cargaAtributo(atributos, "columnas", 1)
    
    let disabled        = librerias.cargaAtributo(atributos, "habilitado", "si")
    disabled = disabled == "si" ? false : true;
    
    let icon            = librerias.cargaAtributo(atributos, "icono", undefined)
    let items           = librerias.cargaAtributo(atributos, "elementos", [])
    let title           = librerias.cargaAtributo(atributos, "titulo", [])
    let cssClase        = librerias.cargaAtributo(atributos, "cssClase", null)

    let visible         = librerias.cargaAtributo(atributos, "visible", "si")
    visible = visible == "si" ? true : false;

    // Definición de la columna
    let definicion = {
        "alignItemLabels": alignItemLabels, 
        "badge"          : badge,
        "colCount"       : colCount,
        "disabled"       : disabled,
        "icon"           : icon,
        "items"          : items,
        "title"          : title,
        "visible"        : visible,
        'cssClass'       : cssClase
    }

    return definicion;
}


export default {
    tab_objeto: tab_objeto
}