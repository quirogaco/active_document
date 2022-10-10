import { ref }     from 'vue'
import fuenteDatos from '../../remoto/fuenteDatos.js';

const registra_campo = function(campos, ruta, componente_id) { 
    let campo;
    for (const indice in campos) {
        campo         = campos[indice];
        campo["ruta"] = ruta;
        if (campo.temporal != undefined) {            
            window.$temporales[campo.temporal.temporal_id] = {
                "ruta"   : ruta,
                "formaId": componente_id,
            }
        }

        // Tipos de campo con items internos
        let tipoCampo = campo.itemType;
        let tipos_complejos = ["group", "tabbed"]
        if ( (tipos_complejos.indexOf(tipoCampo) > -1) || (campo.items != undefined) ) {
            let elementos = ( campo.items != undefined ? campo.items : campo.tabs )
            registra_campo(elementos, ruta, componente_id)
        }
    }
}

const creaAtributos = function(componente_id, configuracion, otros={}) {
    let   tipoComponente = "forma";

    // ################################
    // Variable generales de la forma #
    // ################################
    // Atributos especificos JCR !!
    let ruta             = window.$librerias.cargaAtributo(configuracion, 'ruta', ""); 
    let nombre_forma     = window.$librerias.cargaAtributo(configuracion, 'nombre_forma', ""); 
    let fuenteDatosForma = window.$librerias.cargaAtributo(configuracion, 'fuente', null); 
    let tipoFuente       = window.$librerias.cargaAtributo(configuracion, 'tipofuente', null);
    let opciones_items   = window.$librerias.cargaAtributo(configuracion, 'opciones_items', {}); 
    let elementosBarra   = window.$librerias.cargaAtributo(configuracion, 'elementosBarra', []); 
    let barraVisible     = window.$librerias.cargaAtributo(configuracion, 'barraVisible', true); 
    let tituloForma      = window.$librerias.cargaAtributo(configuracion, 'titulo', ""); 
    let deshabilitada    = window.$librerias.cargaAtributo(configuracion, 'lectura', false); 
    let columnasForma    = window.$librerias.cargaAtributo(configuracion, 'columnasForma', 1); 
    // Notifica mensaje de tarea realizada
    let notifica         = window.$librerias.cargaAtributo(configuracion, 'notifica', "si"); 
    notifica = notifica == "si" ? true: false;    
    let ancho            = window.$librerias.cargaAtributo(configuracion, 'ancho', "800"); 
    // Eventos
    let eventos           = window.$librerias.cargaAtributo(configuracion, 'eventos', {}); 

    // Opciones items
    let plantillaAtributos = window.$librerias.cargaAtributo(configuracion, 'plantillaAtributos', {});
    opciones_items         = Object.assign(opciones_items, plantillaAtributos.opciones_items);

    // Definición de campos
    let campos             = window.$librerias.cargaAtributo(configuracion, 'campos', []);

    // Registra este campo y sus items
    if (nombre_forma != "") {
        ruta = nombre_forma
    }
    registra_campo(campos, ruta, componente_id)
    
    // ############################################
    // Diccionario atributos de setup de la FORMA #
    // ############################################
    let atributosBase = {            
        // Referencias
        referencia           : ref(null),        
        referenciaToolbar    : ref(null),

        // Barra de acciones
        toolbar              : ref(false), // enabled, disabled -> toolbar
            
        // Popup atributos            
        popupVisible         : ref(false),
        popupTitulo          : ref(""),
        popupMensaje         : ref(""), 
        
        titulo               : ref(tituloForma),
        formaDatos           : ref({}),
        campos               : ref(campos),  
        columnasForma        : ref(columnasForma),
        ancho                : ref(ancho),
        regresarComponente   : ref(""),   
        componente_id        : ref(componente_id),            
        
        loadIndicatorVisible : ref(false),
        deshabilitada        : ref(deshabilitada),        
        fuenteDatos          : fuenteDatos.creaFuenteDatosForma(tipoComponente, tipoFuente, componente_id, fuenteDatosForma),

        opciones_items       : ref(opciones_items),

        // Barra de acciones
        barraVisible         : ref(barraVisible),
        elementosBarra       : ref(elementosBarra),
        
        // Eventos
        eventos              : eventos,

        // Notificación virtual
        notifica             : ref(notifica)
    }

    const atributos = Object.assign(otros, atributosBase); 
    
    return atributos
}

export default {
    creaAtributos: creaAtributos
}