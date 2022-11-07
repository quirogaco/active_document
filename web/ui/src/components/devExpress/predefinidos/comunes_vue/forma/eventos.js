const eventos_generales = {
    //"inicializado"   : "onInitialized",
    "contenido_listo"   : "onContentReady",
    "desechar"          : "onDisposing",
    "foco_entra"        : "onFocusIn",
    "foco_sale"         : "onFocusOut",    
    "opcion_cambiada"   : "onOptionChanged",
    "seleccion_cambiada": "onSelectionChanged",
    "valor_cambiado"    : "onValueChanged", 
    
    // data grid
    "fila_doble_click"  : "onRowDblClick"
}

// Funcion universal de eventos
const envoltura = function(forma, definicion, evento, forma_id) {
    const funcion_evento = function(object) {
        let forma_id = null;
        if (forma != null) {    
            forma_id = forma.basicas.forma_id                                
        }
        evento(object, definicion, forma, forma_id);
    }

    return funcion_evento;
}

const eventos = function(atributos) {
    let forma = window.$librerias.cargaAtributo(atributos, 'forma', null);     
    let mayuscula = window.$librerias.cargaAtributo(
        atributos, 
        'mayuscula', 
        "SI"
    );     
    let tipo = window.$librerias.cargaAtributo(atributos, 'tipo', "texto");        
    let eventos = window.$librerias.cargaAtributo(atributos, 'eventos', {});
    
    // evento inicial para todos los campos 
    // registra informacion de la forma y el campo
    const inicializado_general = function(campo) {     
        let forma_id = null  
        // Registra forma 
        // atributos en la instancia de la forma 
        if ( (forma != null) && (atributos.id != undefined) ) {  
            // informacion de campos de la forma
            if (forma._campos == undefined) {
                forma._campos = {}
            }
            // informacion de campos de archivo de la forma
            if (forma._archivos == undefined) {
                forma._archivos = {}
            }
            // id de la forma, usado para almacenar la forma y sus campos
            forma_id = forma.basicas.forma_id;
            // id de este campo
            let atributo_id = atributos.id;
            let contenedor = window.$componentes["_campos"][forma_id];
            // contenedor de componentes del aplicativo
            if (contenedor == undefined) {
                window.$componentes["_campos"][forma_id] = {};
                window.$componentes["_definicion"][forma_id] = {};
            }  
            let _componentes = window.$componentes;
            _componentes["_campos"][forma_id][atributo_id] = campo;
            _componentes["_definicion"][forma_id][atributo_id] = atributos;
            forma._campos[atributo_id] = campo;
            // Valida si es archivo
            if ( campo.component.NAME == "dFileUploader") {
                forma._archivos[atributo_id] = campo;
            }                                 
        };

        // Llama evento
        let inicializado = eventos["inicializado"];             
        if (inicializado != null) {
            inicializado(campo, atributos, forma, forma_id)
        }
    }
    
    let a_mayusculas = null;
    if ( 
            (mayuscula == "SI") && 
            ( 
                ( tipo == "texto") || 
                ( tipo == "correo") || 
                ( tipo == "texto_area") 
            ) 
        ) {

        a_mayusculas = function(campo) {     
            var valor = campo.component.option("value") 
            if ( 
                    (valor != null) && 
                    (valor != undefined) && 
                    (valor.toUpperCase != undefined) 
                ) {
                campo.component.option("value", valor.toUpperCase())
            };

            // Llama evento
            let valor_cambiado = eventos["valor_cambiado"]                
            if (valor_cambiado != null) {
                valor_cambiado(campo, atributos, forma, forma_id)
            }
        }
    }
    
    // Eventos especificos del campos
    let eventos_campo = {};
    let evento = "";
    let evento_devexpress = "";
    for (const propiedad in eventos) {
        evento_devexpress = eventos_generales[propiedad];
        if (evento_devexpress != undefined) {
            evento = eventos[propiedad];
            eventos_campo[evento_devexpress] = envoltura(
                forma, 
                atributos, 
                evento
            );
        }                
    }
    eventos_campo["onInitialized"] = inicializado_general;

    if (a_mayusculas != null) {
        eventos_campo["onValueChanged"] = a_mayusculas;
    };

    return eventos_campo;   
}

export default {
    eventos: eventos
}