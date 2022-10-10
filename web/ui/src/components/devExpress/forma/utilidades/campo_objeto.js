import librerias       from '../../../../librerias/librerias.js';
import editor_opciones from './editor_opciones.js';
import validacion      from './validacion.js';

// Textbox definición
const campo_objeto = function(atributos={}) {
    let dataField      = librerias.cargaAtributo(atributos, "campo",    null) 
    let nombre         = librerias.cargaAtributo(atributos, "nombre",  null)  
    let editorType     = librerias.cargaAtributo(atributos, "tipo",     "dxTextBox")  
    let mode           = librerias.cargaAtributo(atributos, "modo",     "text")  
    let expandir       = librerias.cargaAtributo(atributos, "expandir", null)  
    let disabled       = librerias.cargaAtributo(atributos, "editable", 'si')  
    disabled = disabled == "si" ? false : true;
    // Visible
    let visible = librerias.cargaAtributo(atributos, "visible", "si")
    visible = visible == "si" ? true: false;

    // Manejo de titulos
    let tituloVisible = librerias.cargaAtributo(atributos, "tituloVisible", 'si')
    tituloVisible     = tituloVisible == "si" ? true : false;
    let label         = librerias.cargaAtributo(atributos, "titulo", {})
    if (typeof label === 'string') {
        label = {
            text   : label,
            visible: tituloVisible
        }
    }

    // Opciones del editor
    let editorOptions    = editor_opciones.editor_opciones(mode, atributos)
    // Reglas de validación
    let validacionReglas = validacion.reglas(mode, atributos)

    // Definición de la columna
    let definicion = {
        "editorType"     : editorType,
        "dataField"      : dataField, 
        "nombre"         : nombre,
        "editorOptions"  : editorOptions,  
        "validationRules": validacionReglas,
        "label"          : label,
        "colSpan"        : expandir,
        "disabled"       : disabled,
        "visible"        : visible
    }

    if (atributos.temporal != undefined) {
        definicion["temporal"] = atributos.temporal;
    }

    return definicion;
}


export default {
    campo_objeto: campo_objeto    
}