import librerias       from '../../../../librerias/librerias.js';
import editor_opciones from './editor_opciones.js';
import validacion      from './validacion.js';

const select_objeto = function(atributos={}) {
    let dataField = librerias.cargaAtributo(atributos, "campo", null) 
    let nombre    = librerias.cargaAtributo(atributos, "nombre",  null)   
    
    // Manejo de titulos
    let label     = librerias.cargaAtributo(atributos, "titulo", {})
    if (typeof label === 'string') {
        label = {
            text: label
        }
    }

    // Opciones del editor
    let editorOptions    = editor_opciones.editor_opciones("select", atributos)
    // Reglas de validación
    let validacionReglas = validacion.reglas("select", atributos)

    // Definición de la columna
    let definicion = {
        "dataField"      : dataField, 
        "nombre"         : nombre,
        "editorType"     : "dxSelectBox",
        "editorOptions"  : editorOptions,  
        "validationRules": validacionReglas,
        "label"          : label
    }

    if (atributos.temporal != undefined) {
        definicion["temporal"] = atributos.temporal;
    }

    return definicion;
}

export default {
    select_objeto    : select_objeto,
}