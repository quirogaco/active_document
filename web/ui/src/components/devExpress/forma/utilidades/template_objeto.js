import librerias       from '../../../../librerias/librerias.js';
import plantillas      from '../../plantillas/plantillas.js';
import editor_opciones from './editor_opciones.js';
import validacion      from './validacion.js';

// Simpleitem template
const template_objeto = function(atributos={}) {
    let dataField      = librerias.cargaAtributo(atributos, "campo",    "")  
    
    // Manejo de titulos
    let label          = librerias.cargaAtributo(atributos, "titulo", {})
    if (typeof label === 'string') {
        label = {
            text: label
        }
    }    

    // Opciones del editor
    //let editorOptions    = editor_opciones.editor_opciones(mode, atributos)
    // Reglas de validación
    //let validacionReglas = validacion.reglas(mode, atributos)

    // Definición de la columna
    let definicion = {
        "dataField"      : dataField, 
        //"editorOptions"  : editorOptions,  
        //"validationRules": validacionReglas,
        "label"          : label,
        "template"       : "archivos"
        /*
        "template"       : function(a, b) {
            console.log("temmplate>>>", a, b)
        },     
        */
    }

    return definicion;
}


export default {
    template_objeto: template_objeto
}