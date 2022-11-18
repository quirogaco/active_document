import forma_definiciones    from "../../../comunes_vue/forma/forma.js"
import utilidades_estructura from '../../../../../../librerias/utilidades_estructura.js'
import dialogos              from '../../../../../../librerias/dialogos.js'

const muestra_asigna = function(forma=null) {  
    forma_definiciones.muestra_campos(forma, ["respuesta_datos"]);
    forma_definiciones.muestra_campos(forma, [
        "gestion_peticion_id",
        "gestion_dependencia_id",     
        "gestion_horas_dias",
        "gestion_total_tiempo",
        "gestion_prioridad",
        "reserva",
        "tema_dependencia_id",
        "subtema_dependencia_id",
        "copia_usuarios_id",
        "copia_grupos_id",
        "reserva",
        "gestion_dependencia_responsable"
    ]);
};

const muestra_asigna_ventanilla = function(forma=null) {  
    forma_definiciones.muestra_campos(forma, ["respuesta_datos"]);
    forma_definiciones.oculta_campos(forma, [
        "tema_dependencia_id"
    ]);
    forma_definiciones.muestra_campos(forma, [
        "gestion_peticion_id",
        "gestion_dependencia_id",     
        "gestion_horas_dias",
        "gestion_total_tiempo",
        "gestion_prioridad",
        "reserva",
        //"tema_dependencia_id",
        "copia_usuarios_id",
        "copia_grupos_id",
        "reserva",
        "gestion_dependencia_responsable"
    ]);
};

const muestra_asigna_ventanilla_tramite = function(forma=null) {  
    console.log(".......")
    forma_definiciones.muestra_campos(forma, ["respuesta_datos"]);
    forma_definiciones.oculta_campos(forma, [
        "gestion_peticion_id",
        "gestion_dependencia_id",
        "gestion_dependencia_responsable"
    ]);
    
    forma_definiciones.muestra_campos(forma, [
        "gestion_horas_dias",
        "gestion_total_tiempo",
        "gestion_prioridad",
        "reserva",
        "tema_dependencia_id",
        "copia_usuarios_id",
        "copia_grupos_id",
        "reserva"
    ]);
};

const oculta_asigna = function(forma=null) {    
    forma_definiciones.oculta_campos(forma, ["respuesta_datos"]);
};

const muestra_parcial_asigna = function(forma=null) {    
    forma_definiciones.muestra_campos(forma, ["respuesta_datos"]);
    forma_definiciones.muestra_campos(forma, [
        "gestion_horas_dias",
        "gestion_total_tiempo",
        "gestion_prioridad",
        "reserva",
        "copia_usuarios_id",
        "copia_grupos_id",
        "reserva",
        "gestion_dependencia_responsable"
    ]);
};

const oculta_parcial_asigna = function(forma=null) {    
    forma_definiciones.muestra_campos(forma, ["respuesta_datos"]);
    forma_definiciones.oculta_campos(forma, [
        "gestion_horas_dias",
        "gestion_total_tiempo",
        "gestion_prioridad",
        "reserva",
        "copia_usuarios_id",
        "copia_grupos_id",
        "reserva",
        "gestion_dependencia_responsable"
    ]);
};


// Valida si es VENTANILLA
const es_ventanilla = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo"     : 'Es documento de ventanilla', 
        "fuente"     : [
            {"id": "SI", "nombre": "SI"},
            {"id": "NO", "nombre": "NO"}
        ],  
        //"valor"      : "NO",
        "eventos"    : {            
            "valor_cambiado": function(campo, definicion, forma, forma_id) {
                let valor = campo.value;
                forma.forma.beginUpdate(); 
                switch (valor) {
                    case "NO":  
                        muestra_asigna(forma);
                        break
        
                    case "SI":
                        oculta_asigna(forma);   
                        break
                };
                forma.forma.endUpdate();
                // Cuando se modifica se repinta el valor vuelve a default
                $forma.asigna_valor(forma, "es_ventanilla", valor);                      
            }
        }
    }
    
    return forma_definiciones.genera_campo("radio", "es_ventanilla", id, atributos_base, atributos)
};

const resuelto_inmediato = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo"     : 'Resuelto primer contacto', 
        "fuente"     : [
            {"id": "SI", "nombre": "SI"},
            {"id": "NO", "nombre": "NO"}
        ],
        //"valor"      : "NO",  
        "eventos"    : {            
            "valor_cambiado": function(campo, definicion, forma, forma_id) {
                let valor = campo.value;
                forma.forma.beginUpdate();                 
                switch (valor) {
                    case "NO":  
                        muestra_parcial_asigna(forma); 
                        break
        
                    case "SI":
                        oculta_parcial_asigna(forma);    
                        break
                };
                forma.forma.endUpdate();
                // Cuando se modifica se repinta el valor vuelve a default
                $forma.asigna_valor(forma, "resuelto_inmediato", valor);          
            }            
        }
    }
    
    return forma_definiciones.genera_campo("radio", "resuelto_inmediato", id, atributos_base, atributos)
}

// Valida si es PQRS
const es_pqrs = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo"     : 'Tipo', 
        "fuente"     : [
            {"id": "PQRSD", "nombre": "PQRSD"},
            {"id": "TRAMITE", "nombre": "TRAMITE"},            
            {"id": "DOCUMENTO", "nombre": "DOCUMENTO"}
        ],  
        "valor"      : "DOCUMENTO",
        "eventos"    : {            
            "valor_cambiado": function(campo, definicion, forma, forma_id) {                  
                let valor = campo.value;
                //oculta_asigna(forma);
                forma.forma.beginUpdate(); 
                switch (valor) {
                    case "DOCUMENTO": 
                        muestra_asigna_ventanilla(forma); 
                        break
                    
                    case "TRAMITE":                         
                        muestra_asigna_ventanilla_tramite(forma); 
                        break
        
                    case "PQRSD":
                        oculta_asigna(forma)    
                        break
                };
                forma.forma.endUpdate();
                // Cuando se modifica se repinta el valor vuelve a default
                $forma.asigna_valor(forma, "es_pqrs", valor);       
            }
        }
    }
    
    return forma_definiciones.genera_campo("radio", "es_pqrs", id, atributos_base, atributos)
};


// #########//
// Petición //
//##########//
let valores_peticion = function(forma, objeto) {
    let peticion = objeto.selectedItem       

    // Limpia valores, horas_dias, total_tiempo
    forma_definiciones.asigna_opcion(forma, ["gestion_horas_dias", "gestion_total_tiempo"], "readOnly", true)        
    forma_definiciones.asigna_valor(forma, "gestion_horas_dias", null)
    forma_definiciones.asigna_valor(forma, "gestion_total_tiempo", null)
    if (peticion !== null) {                                                                                                                                                                                             
        let deshabilita = peticion.modifica_tiempo == "SI" ? false : true 
        forma_definiciones.asigna_opcion(forma, ["gestion_horas_dias", "gestion_total_tiempo"], "readOnly", deshabilita)
        forma_definiciones.asigna_valor(forma, "gestion_horas_dias", peticion.horas_dias)
        forma_definiciones.asigna_valor(forma, "gestion_total_tiempo", peticion.total_tiempo)
    }
};

const gestion_peticion_id = function(id=null, atributos={}) {
    let atributos_base = {
        'titulo'        : 'Tipo de petición', 
        "fuente"        : "tipo_peticiones", 
        "filtros_fuente": [
            ["estado_", "=", "ACTIVO"], 
            ["pqrs", "=", "si"]
        ],
        'obligatorio'   : true,
        "eventos"       : {
            "seleccion_cambiada": function(campo, definicion, forma, forma_id) {  
                valores_peticion(forma, campo)
            }
        }
    }
    
    return forma_definiciones.genera_campo("seleccion", "gestion_peticion_id", id, atributos_base, atributos)
};

// Tipo de tiempo horas/dias
const gestion_horas_dias = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo"     : 'Plazo en', 
        "fuente"     : [
            {"id": "DIAS",  "nombre": "DIAS"},
            {"id": "HORAS", "nombre": "HORAS"}
        ], 
        'lectura'    : true, 
        "obligatorio": true
    }
    
    return forma_definiciones.genera_campo("radio", "gestion_horas_dias", id, atributos_base, atributos)
}

const gestion_total_tiempo = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo"     : 'Plazo para contestar', 
        'lectura'    : true, 
        'obligatorio': true,
        "longitud"   : "3",
        "valor"      : 0,
        "ancho"      : 180
    }
    
    return forma_definiciones.genera_campo("entero", "gestion_total_tiempo", id, atributos_base, atributos)
}

// Prioridad para responder
const gestion_prioridad = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo"     : 'Prioridad de gestión', 
        'obligatorio': true,
        "fuente"     : [
            {"id": "ALTA",  "nombre": "ALTA"},
            {"id": "MEDIA", "nombre": "MEDIA"},
            {"id": "BAJA",  "nombre": "BAJA"},
        ], 
        "valor"      : "MEDIA",
    }
    
    return forma_definiciones.genera_campo("radio", "gestion_prioridad", id, atributos_base, atributos)
}

// Reserva del documento
const reserva = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo"     : 'Documento con reserva', 
        "fuente"     : [
            {"id": "SI",  "nombre": "SI"},
            {"id": "NO", "nombre": "NO"}
        ],  
        "valor"      : "NO",
        "obligatorio": true
    }
    
    return forma_definiciones.genera_campo("radio", "reserva", id, atributos_base, atributos)
}

// #####################
// Dependencia destino #
// #####################
const gestion_dependencia_id = function(id=null, atributos={}) {
    let atributos_base = {
        'titulo'            : 'Dependencia responsable', 
        "fuente"            : "dependencias",   
        "busqueda_expresion": "nombre_completo",
        "muestra_expresion" : "nombre_completo",
        'obligatorio'       : true,
        "eventos"           : {
            "seleccion_cambiada": async function(campo, definicion, forma, forma_id) {  
                let datos = await utilidades_estructura.leer_registro_id("dependencias", campo.selectedItem.id);
                forma_definiciones.asigna_valor(forma, "tema_dependencia_id", null);
                forma_definiciones.asigna_valor(forma, "subtema_dependencia_id", null);
                forma_definiciones.asigna_valor(forma, "gestion_dependencia_responsable", null);
                let responsable_tipo = $get_params("_radica_dependencia_")["responsable"];
                let responsable = datos[responsable_tipo];
                console.log("seleccion_cambiada:", responsable_tipo, responsable);
                if ( $lib.sin_valor.indexOf(responsable) > -1 ) {        
                    dialogos.miMensaje("Información incompleta", (
                        datos.nombre_completo + " - " +  "No tiene responsable de manejo de PQRS"
                    ))
                }
                else {
                    let filtros     = [
                        ["dependencia_id", "=", campo.selectedItem.id],
                            'or',
                        ["dependencia_id", "=", ""]
                    ];
                    let responsable = await utilidades_estructura.leer_registro_id("usuarios", responsable);
                    try {
                        forma_definiciones.asigna_fuente_datos(forma, "tema_dependencia_id", "select", "temas", filtros, {}); 
                    } catch (error) {}  
                    forma_definiciones.asigna_valor(forma, "gestion_dependencia_responsable", responsable["nombre"]);
                }                
            }
        }
    }
    
    return forma_definiciones.genera_campo("seleccion", "gestion_dependencia_id", id, atributos_base, atributos)
}

const gestion_dependencia_responsable = function(id=null, atributos={}) {
    let atributos_base = {
        'titulo' : 'Funcionario responsable',
        'lectura': true
    }
    
    return forma_definiciones.genera_campo("texto", "gestion_dependencia_responsable", id, atributos_base, atributos)
}


// Tema de la dependencia
const tema_dependencia_id = function(id=null, atributos={}) {
    let atributos_base = {
        'titulo'        : 'Tema/tramite de la dependencia', 
        "fuente"        : "temas", 
        "filtros_fuente": ["estado_", "=", "ACTIVO"],
        'obligatorio'   : true,
        "eventos"       : {
            "seleccion_cambiada": function(campo, definicion, forma, forma_id) {  
                let filtros = ["tema_id", "=", campo.selectedItem.id]
                forma_definiciones.asigna_fuente_datos(forma, "subtema_dependencia_id", "select", "subtemas", filtros, {})   
            }
        }
    }
    
    return forma_definiciones.genera_campo("seleccion", "tema_dependencia_id", id, atributos_base, atributos)
}

// Subtema de la dependencia
const subtema_dependencia_id = function(id=null, atributos={}) {
    let atributos_base = {
        'titulo'        : 'Subtema de la dependencia', 
        "fuente"        : "subtemas", 
        "filtros_fuente": ["estado_", "=", "ACTIVO"],
        //'obligatorio'   : true
    }
    
    return forma_definiciones.genera_campo("seleccion", "subtema_dependencia_id", id, atributos_base, atributos)
}

// Comentario de traslado
const comentario_traslado = function(id=null, atributos={}) {
    let atributos_base = {
        'titulo'        : 'Anotación/comentarios',         
        'obligatorio'   : true
    }
    
    return forma_definiciones.genera_campo("texto_area", "comentario_traslado", id, atributos_base, atributos)
}

export default {
    es_ventanilla                  : es_ventanilla,
    resuelto_inmediato             : resuelto_inmediato,
    es_pqrs                        : es_pqrs,
    gestion_dependencia_id         : gestion_dependencia_id,
    gestion_dependencia_responsable: gestion_dependencia_responsable,
    gestion_peticion_id            : gestion_peticion_id,
    gestion_horas_dias             : gestion_horas_dias,
    gestion_total_tiempo           : gestion_total_tiempo,
    gestion_prioridad              : gestion_prioridad,
    reserva                        : reserva,
    tema_dependencia_id            : tema_dependencia_id,
    subtema_dependencia_id         : subtema_dependencia_id,
    comentario_traslado            : comentario_traslado
}