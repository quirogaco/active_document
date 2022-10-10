import librerias  from '../../../../librerias/librerias.js';
import tipos_mime from './tipos_mime.js';

const campo_archivo = function(atributos, editorOptions, dataField) {
    let uploadMode = librerias.cargaAtributo(atributos, "envia", "useForm")          
    // Uno o varios archivos
    let varios    = librerias.cargaAtributo(atributos, "varios", "no") 
    let multiple  = false;
    if (varios == "si") multiple = true; 
    
    // Tipos de archivos
    let acepta       = librerias.cargaAtributo(atributos, "acepta", null) 
    let acepta_texto = tipos_mime.crea_mime(acepta); 
    
    // Maximo tamaño
    let maximo    = librerias.cargaAtributo(atributos, "maximo", "0") 
    
    // direccionCarga
    let uploadUrl = librerias.cargaAtributo(atributos, "direccionCarga", null)   

    editorOptions["uploadMode"]  = uploadMode;
    editorOptions["multiple"]    = multiple;
    editorOptions["maxFileSize"] = maximo;    
    editorOptions["accept"]     = acepta_texto;
    editorOptions["uploadUrl"]  = uploadUrl;

    //editorOptions["labelText"]                   = "O soltar archivo aquí";
    editorOptions["labelText"]                   = "";
    if (multiple == true) {
        editorOptions["selectButtonText"]            = "Seleccione archivo(s)";    
    }
    else {
        editorOptions["selectButtonText"]            = "Seleccione archivo";    
    }            
    editorOptions["invalidFileExtensionMessage"] = "El tipo de archivo no está permitido";
    editorOptions["invalidMaxFileSizeMessage"]   = "El archivo es demasiado grande";
    editorOptions["invalidMinFileSizeMessage"]   = "El archivo es demasiado pequeño";
    editorOptions["readyToUploadMessage"]        = "Listo para subir";
    editorOptions["uploadedMessage"]             = "Subido";
    editorOptions["uploadFailedMessage"]         = "Subida fallida";   
    
    if (editorOptions["value"] == "") {
        editorOptions["value"] = []
    }

    return editorOptions;
}


export default {
    campo_archivo: campo_archivo
}