import librerias        from '../../../../librerias/librerias.js';

let temporal_id = 0;
const registra_componente = function(tipoEditor, atributos, editorOptions, nombreCampo) {
    // Registra componente
    let registrar = librerias.cargaAtributo(atributos, 'registrar', "no");  

    // No es componente developer express
    let nde       = librerias.cargaAtributo(atributos, 'nde', "no");     
    if ( (registrar == "si") || (tipoEditor == "archivo") ) {
        temporal_id += 1;
        let temporal          = temporal_id; 
        atributos["temporal"] = {temporal_id: temporal};

        // Eventos del componente
        let eventos           = librerias.cargaAtributo(atributos, "eventos", {});
        let inicializado      = librerias.cargaAtributo(eventos, "inicializado", null);   

        // Evento inicializado
        let onInitialized = function(e) {               
            let componente       = e.component;
            let formaId          = window.$temporales[temporal].formaId;
            let nombreComponente = formaId + "_" + nombreCampo;
            if (window.$ns[formaId+"_"] == undefined) {
                window.$ns[formaId+"_"] = {}
            }
            // Campo directo
            window.$ns[nombreComponente]         = componente;  
            // Campos registrados de la forma
            window.$ns[formaId+"_"][nombreCampo] = componente;
            if (nde == "si") {
                window.$componentesNDET[formaId][nombreComponente] = componente;
            }        
            if (inicializado != null) inicializado(e); 
        };
        editorOptions["onInitialized"] = onInitialized;
        
        // Registro temporal
        window.$temporales[temporal] = {}
    }
} 


export default {
    registra_componente: registra_componente
}
