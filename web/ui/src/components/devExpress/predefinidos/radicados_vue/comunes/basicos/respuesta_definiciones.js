import forma_definiciones from "../../../comunes_vue/forma/forma.js"

const respuesta_tipo = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo"     : 'Tipo respuesta', 
        "fuente"     : [
            {"id": "FINAL",      "nombre": "FINAL"},
            {"id": "PARCIAL",    "nombre": "PARCIAL"},
            {"id": "INCOMPLETA", "nombre": "INCOMPLETA"}
        ],  
        "valor"      : "FINAL",
        "obligatorio": true,
    }
    
    return forma_definiciones.genera_campo("radio", "respuesta_tipo", id, atributos_base, atributos)
}

const dependencia_responde_id = function(id=null, atributos={}) {
    let atributos_base = {
        'titulo'            : 'Dependencia remitente', 
        "fuente"            : "dependencias",   
        "busqueda_expresion": "nombre_completo",
        "muestra_expresion" : "nombre_completo",
        "filtros_fuente"    : ["estado_", "=", "ACTIVO"],
        'obligatorio'       : true,
        "eventos"           : {
            "seleccion_cambiada": function(campo, definicion, forma, forma_id) {  
                let datos = campo.selectedItem
                forma_definiciones.limpia_campos(forma, ["funcionario_responde_id"])                
                if (datos != null) {
                    let filtros = ["dependencia_id", "=", datos.id]
                    forma_definiciones.asigna_fuente_datos(forma, "funcionario_responde_id", "select", "usuarios", filtros, {})        
                }         
            }
        }
    }
    
    return forma_definiciones.genera_campo("seleccion", "dependencia_responde_id", id, atributos_base, atributos)
}

const funcionario_responde_id = function(id=null, atributos={}) {
    let atributos_base = {
        'titulo'        : 'Funcionario remitente', 
        "fuente"        : "usuarios", 
        "filtros_fuente": ["estado_", "=", "ACTIVO"],
        'obligatorio'   : true,
    }
    
    return forma_definiciones.genera_campo("seleccion", "funcionario_responde_id", id, atributos_base, atributos)
}

const reserva = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo"     : 'Tiene reserva', 
        "fuente"     : [
            {"id": "SI", "nombre": "SI"},
            {"id": "NO", "nombre": "NO"},
        ],  
        "valor"      : "NO",
        "obligatorio": true,
    }
    
    return forma_definiciones.genera_campo("radio", "reserva", id, atributos_base, atributos)
}

const medio_notificacion = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo"     : 'Medio(s) notificación', 
        "fuente"     : [
            {"id": "CORREO",    "nombre": "CORREO ELECTRÓNICO"},
            {"id": "DIRECCION", "nombre": "DIRECCIÓN FISICA"},
        ],  
        "obligatorio": true,
        "eventos"    : {
            "valor_cambiado": function(campo, definicion, forma, forma_id) {
                let valor = campo.value
                if ( valor.indexOf("CORREO") > -1 ) {
                    forma_definiciones.asigna_validador_forma(forma, ["tercero_correo_electronico"], "obligatorio")
                }
                else {
                    forma_definiciones.borra_validador_forma(forma, ["tercero_correo_electronico"], "obligatorio")
                }
                                
                if ( valor.indexOf("DIRECCION") > -1 ) {
                    forma_definiciones.asigna_validador_forma(forma, ["tercero_direccion"], "obligatorio")
                } 
                else {
                    forma_definiciones.borra_validador_forma(forma, ["tercero_direccion"], "obligatorio")
                }  
                  
            }           
        }
    }
    
    return forma_definiciones.genera_campo("etiqueta", "medio_notificacion", id, atributos_base, atributos)
}

const medio_notificacion_salida = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo"     : 'Medio(s) notificación', 
        "fuente"     : [
            {"id": "CORREO",    "nombre": "CORREO ELECTRÓNICO"},
            {"id": "DIRECCION", "nombre": "DIRECCIÓN FISICA"},
        ],  
        "obligatorio": true,
        "eventos"    : {
            "valor_cambiado": function(campo, definicion, forma, forma_id) {
                /*
                let valor = campo.value
                console.log("NOTIFICACIÓN****:", valor  )                                
                if ( valor.indexOf("CORREO") > -1 ) {
                    forma_definiciones.asigna_validador_forma(forma, ["tercero_correo_electronico"], "obligatorio")
                }
                else {
                    forma_definiciones.borra_validador_forma(forma, ["tercero_correo_electronico"], "obligatorio")
                }
                                
                if ( valor.indexOf("DIRECCION") > -1 ) {
                    forma_definiciones.asigna_validador_forma(forma, ["tercero_direccion"], "obligatorio")
                } 
                else {
                    forma_definiciones.borra_validador_forma(forma, ["tercero_direccion"], "obligatorio")
                }  
                */
            }           
        }
    }
    
    return forma_definiciones.genera_campo("etiqueta", "medio_notificacion", id, atributos_base, atributos)
}

const tipo_firma = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo"     : 'Firma', 
        "fuente"     : [
            {"id": "FISICA",      "nombre": "FISICA"},
            {"id": "ELECTRONICA", "nombre": "ELECTRONICA"},
            {"id": "DIGITAL",     "nombre": "DIGITAL"},
        ],  
        "obligatorio": true,
    }
    
    return forma_definiciones.genera_campo("etiqueta", "tipo_firma", id, atributos_base, atributos)
}

const copia_usuarios_id = function(id=null, atributos={}) {
    let atributos_base = {
        'titulo'        : 'Copia a usuarios', 
        "fuente"        : "usuarios", 
        "filtros_fuente": ["estado_", "=", "ACTIVO"]
    }
    
    return forma_definiciones.genera_campo("etiqueta", "copia_usuarios_id", id, atributos_base, atributos)
}

const copia_grupos_id = function(id=null, atributos={}) {
    let atributos_base = {
        'titulo'        : 'Copia a grupos', 
        "fuente"        : "grupo_usuarios", 
        "filtros_fuente": ["estado_", "=", "ACTIVO"]
    }
    
    return forma_definiciones.genera_campo("etiqueta", "copia_grupos_id", id, atributos_base, atributos)
}

const copia_terceros_id = function(id=null, atributos={}) {
    let atributos_base = {
        'titulo'            : 'Copia a terceros', 
        "fuente"            : "terceros", 
        "busqueda_expresion": "nombre_completo",
        "muestra_expresion" : "nombre_completo",
        "filtros_fuente"    : ["estado_", "=", "ACTIVO"]
    }
    
    return forma_definiciones.genera_campo("etiqueta", "copia_terceros_id", id, atributos_base, atributos)
}

// ##########
// INTERNOS #
// ##########
const dependencia_envia_id = function(id=null, atributos={}) {
    let atributos_base = {
        'titulo'            : 'Dependencia remitente', 
        "fuente"            : "dependencias",   
        "busqueda_expresion": "nombre_completo",
        "muestra_expresion" : "nombre_completo",
        "filtros_fuente"    : ["estado_", "=", "ACTIVO"],
        'obligatorio'       : true,
        "eventos"           : {
            "seleccion_cambiada": function(campo, definicion, forma, forma_id) {  
                let datos = campo.selectedItem
                forma_definiciones.limpia_campos(forma, ["funcionario_envia_id"])                
                if (datos != null) {
                    let filtros = ["dependencia_id", "=", datos.id]
                    forma_definiciones.asigna_fuente_datos(forma, "funcionario_envia_id", "select", "usuarios", filtros, {})        
                }         
            }
        }
    }
    
    return forma_definiciones.genera_campo("seleccion", "dependencia_envia_id", id, atributos_base, atributos)
}

const funcionario_envia_id = function(id=null, atributos={}) {
    let atributos_base = {
        'titulo'        : 'Funcionario remitente', 
        "fuente"        : "usuarios", 
        "filtros_fuente": ["estado_", "=", "ACTIVO"],
        'obligatorio'   : true,
    }
    
    return forma_definiciones.genera_campo("seleccion", "funcionario_envia_id", id, atributos_base, atributos)
}

const dependencia_recibe_id = function(id=null, atributos={}) {
    let atributos_base = {
        'titulo'            : 'Dependencia recibe', 
        "fuente"            : "dependencias",   
        "busqueda_expresion": "nombre_completo",
        "muestra_expresion" : "nombre_completo",
        "filtros_fuente"    : ["estado_", "=", "ACTIVO"],
        'obligatorio'       : true,
        "eventos"           : {
            "seleccion_cambiada": function(campo, definicion, forma, forma_id) {  
                let datos = campo.selectedItem
                forma_definiciones.limpia_campos(forma, ["funcionario_recibe_id"])                
                if (datos != null) {
                    let filtros = ["dependencia_id", "=", datos.id]
                    forma_definiciones.asigna_fuente_datos(forma, "funcionario_recibe_id", "select", "usuarios", filtros, {})        
                }         
            }
        }
    }
    
    return forma_definiciones.genera_campo("seleccion", "dependencia_recibe_id", id, atributos_base, atributos)
}

const funcionario_recibe_id = function(id=null, atributos={}) {
    let atributos_base = {
        'titulo'        : 'Funcionario remitente', 
        "fuente"        : "usuarios", 
        "filtros_fuente": ["estado_", "=", "ACTIVO"],
        'obligatorio'   : true,
    }
    
    return forma_definiciones.genera_campo("seleccion", "funcionario_recibe_id", id, atributos_base, atributos)
}

export default {
    respuesta_tipo           : respuesta_tipo,
    dependencia_responde_id  : dependencia_responde_id,
    funcionario_responde_id  : funcionario_responde_id,
    reserva                  : reserva,
    medio_notificacion       : medio_notificacion,
    medio_notificacion_salida: medio_notificacion_salida,
    tipo_firma               : tipo_firma,
    copia_usuarios_id        : copia_usuarios_id,
    copia_grupos_id          : copia_grupos_id,
    copia_terceros_id        : copia_terceros_id,

    // INTERNOS
    dependencia_envia_id     : dependencia_envia_id,
    funcionario_envia_id     : funcionario_envia_id,
    dependencia_recibe_id    : dependencia_recibe_id,
    funcionario_recibe_id    : funcionario_recibe_id
}