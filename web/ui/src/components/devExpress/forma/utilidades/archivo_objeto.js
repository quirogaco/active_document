import librerias       from '../../../../librerias/librerias.js';
import editor_opciones from './editor_opciones.js';
import validacion      from './validacion.js';
import plantillas      from '../../plantillas/plantillas.js';

let contador_plantilla = 0;

// Archivo definición
const archivo_objeto = function(atributos={}, plantillaAtributos) {
    let dataField      = librerias.cargaAtributo(atributos, "campo",  null)  
    let nombre         = librerias.cargaAtributo(atributos, "nombre",  null)  

    // Manejo de titulos
    let label          = librerias.cargaAtributo(atributos, "titulo", {})
    if (typeof label === 'string') {
        label = {
            text: label
        }
    }    

    // Opciones del editor
    atributos["nde"]  = "si";
    let editorOptions = editor_opciones.editor_opciones("archivo", atributos);

    // Reglas de validación
    let validacionReglas = validacion.reglas("archivo", atributos);
    
    contador_plantilla      += 1;    
    let valoresPlantilla     = plantillas.plantillaDosPuntosDiccionario(editorOptions, dataField);    
    let cuerpoPlantilla      = plantillas.plantillaCompletaComponente("DxFileUploader", valoresPlantilla);    
    let plantillaConsecutivo = "template_" + contador_plantilla;
    let plantilla            = plantillas.genera_template(plantillaConsecutivo, cuerpoPlantilla);
    
    plantillaAtributos.opciones_items[dataField] = editorOptions;
    plantillaAtributos.texto_plantilla.push(plantilla);
    
    let definicion = {
        "dataField"    : dataField, 
        "nombre"       : nombre,
        "editorType"   : "dxFileUploader", // Se requiere, para envio de forma detecta que es archivos
        "template"     : plantillaConsecutivo,        
        "label"        : label,
        "validationRules": validacionReglas,         
    }

    if (atributos.temporal != undefined) {
        definicion["temporal"] = atributos.temporal;
    }

    return definicion;
}


export default {
    archivo_objeto: archivo_objeto   
}