import librerias       from '../../../../librerias/librerias.js';
import editor_opciones from './editor_opciones.js';
import validacion      from './validacion.js';
import plantillas      from '../../plantillas/plantillas.js';

let contador_objeto = 10000;

// Contenido base
const contenido_objeto = function(atributos={}, plantillaAtributos) {
    let dataField = librerias.cargaAtributo(atributos, "campo",     null) 
    let nombre    = librerias.cargaAtributo(atributos, "nombre",  null)  
    
    let contenido = librerias.cargaAtributo(atributos, "contenido", "")  
    contador_objeto += 1;
    
    let cuerpoPlantilla = plantillas.plantillaContenido("Contenido", contenido);
    let plantillaConsecutivo = "template_" + contador_objeto;
    let plantilla       = plantillas.genera_template(plantillaConsecutivo, cuerpoPlantilla);    
    //plantillaAtributos.opciones_items[dataField] = {};
    plantillaAtributos.texto_plantilla.push(plantilla);
    
    let definicion = {
        "dataField"    : dataField, 
        "nombre"       : nombre,
        "editorType"   : "Contenido", // Se requiere, para envio de forma detecta que es archivos
        "template"     :  plantillaConsecutivo,        
        "label"        : null,
        "validationRules": null,         
    }

    if (atributos.temporal != undefined) {
        definicion["temporal"] = atributos.temporal;
    }

    return definicion;
}


export default {
    contenido_objeto: contenido_objeto   
}