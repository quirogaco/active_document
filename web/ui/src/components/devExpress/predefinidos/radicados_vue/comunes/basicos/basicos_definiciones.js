import forma_definiciones from "../../../comunes_vue/forma/forma.js"

const id = function(id=null, atributos={}) {
    let atributos_base = {
        'titulo'     : 'Id del registro', 
        'visible'    : false
    }
    
    return forma_definiciones.genera_campo("texto", "id", id, atributos_base, atributos)
}

const canal_radicado_id = function(id=null, atributos={}) {
    let atributos_base = {
        'titulo'        : 'Canal de recepción', 
        "fuente"        : "canales_comunicacion", 
        "filtros_fuente": ["estado_", "=", "ACTIVO"],
        'obligatorio'   : true,
    }
    
    return forma_definiciones.genera_campo("seleccion", "canal_radicado_id", id, atributos_base, atributos)
}

const fecha_documento = function(id=null, atributos={}) {
    let atributos_base = {
        'titulo'     : 'Fecha del documento', 
        'obligatorio': true, 
    }
    
    return forma_definiciones.genera_campo("fecha", "fecha_documento", id, atributos_base, atributos)
}

const radicado_remitente = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo"    : 'Radicado remitente', 
        "mensaje"   : "Digite radicado del remitente",
    }
    
    return forma_definiciones.genera_campo("texto", "radicado_remitente", id, atributos_base, atributos)
}

const empresa_mensajeria_id = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo"        : 'Empresa mensajeria', 
        "fuente"        : "empresas_mensajeria", 
        "filtros_fuente": ["estado_", "=", "ACTIVO"],
        "mensaje"       : "Seleccione empresa de mensajeria",
    }
    
    return forma_definiciones.genera_campo("seleccion", "empresa_mensajeria_id", id, atributos_base, atributos)
}

const numero_guia = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo"    : 'Número de guia', 
        "mensaje"   : "Digite número de guia de mensajeria",
    }
    
    return forma_definiciones.genera_campo("texto", "numero_guia", id, atributos_base, atributos)
}

const radicado_responde = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo"    : 'Responde radicado', 
        "mensaje"   : "Digite radicado de entrada",
    }
    
    return forma_definiciones.genera_campo("texto", "radicado_responde", id, atributos_base, atributos)
}

const nro_folios = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo"     : 'Número de folios', 
        "mensaje"    : "Número de hojas fisicas",
        'obligatorio': true,
        "longitud"   : "3",
        'valor'      : 1, 
        "ancho"      : 180
    }
    
    return forma_definiciones.genera_campo("entero", "nro_folios", id, atributos_base, atributos)
}

const anexos = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo"     : 'Anexos', 
        "longitud"   : "250",
        "mensaje"    : "Anexos fisicos que vienen con el documemto (ej. Cd, libro, etc)"
    }
    
    return forma_definiciones.genera_campo("texto_area", "anexos", id, atributos_base, atributos)
}

const asunto = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo"     : 'Asunto del documento', 
        'obligatorio': true,       
        "longitud"   : "2000", 
        "mensaje"    : "Resumen del contenido del documento"
    }
    
    return forma_definiciones.genera_campo("texto_area", "asunto", id, atributos_base, atributos)
}

const entidad_traslada = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo"    : 'Entidad que traslada', 
        "mensaje"   : "Digite nombre de la entidad que traslada",
    }

    return forma_definiciones.genera_campo("texto", "entidad_traslada", id, atributos_base, atributos)
}

const persona_traslada = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo"    : 'Persona que traslada', 
        "mensaje"   : "Digite nombre de la persona que traslada",
    }
    
    return forma_definiciones.genera_campo("texto", "persona_traslada", id, atributos_base, atributos)
}

const relacionados_id = function(id=null, atributos={}) {
    let atributos_base = {
        'titulo'            : 'Radicados relacionados', 
        "fuente"            : "radicados_entrada", 
        "busqueda_expresion": "nro_radicado",
        "muestra_expresion" : "nro_radicado",
        "filtros_fuente"    : ["estado_", "=", "ACTIVO"]
    }
    
    return forma_definiciones.genera_campo("etiqueta", "relacionados_id", id, atributos_base, atributos)
}

const campos_asigna = [
    "es_ventanilla",
    "resuelto_inmediato",
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
]

const muestra_asigna = function(forma=null) {  
    forma_definiciones.muestra_campos(forma, campos_asigna)
}

const oculta_asigna = function(forma=null) {
    forma_definiciones.oculta_campos(forma, campos_asigna)
}

const repone_id = function(id=null, atributos={}) {
    let atributos_base = {
        'titulo'            : 'Reposición sobre', 
        "fuente"            : "radicados_entrada", 
        "busqueda_expresion": "nro_radicado",
        "muestra_expresion" : "nro_radicado",
        "filtros_fuente"    : ["gestion_estado", "=", "FINALIZADO"],
        "eventos"    : {            
            "valor_cambiado": function(campo, definicion, forma, forma_id) {
                console.log("campo VALOR:", campo)
                muestra_asigna(forma)
                if (campo.value != null) {                     
                     oculta_asigna(forma)
                }
            }
        }
    }
    
    return forma_definiciones.genera_campo("seleccion", "repone_id", id, atributos_base, atributos)
}

let basicos_campos_consulta = [    
    {
        "id"    : "clase_radicado",
        "titulo": "Clase",
    },
    {
        "id"    : "canal_radicado_nombre",
        "titulo": "Canal",
    },
    {
        "id"    : "nro_radicado",
        "titulo": "Número de radicado",
    },
    {
        "id"    : "fecha_radicado",
        "titulo": "Fecha de radicación",
    },
    {
        "id"    : "fecha_documento",
        "titulo": "Fecha del documento",
    },
    {
        "id"    : "radicado_remitente",
        "titulo": "Número origen del documento",
    },
    {
        "id"    : "asunto",
        "titulo": "Asunto",
        "tipo"  : "texto_area"
    },
    {
        "id"    : "nro_folios",
        "titulo": "Número de folios",
    },
    {
        "id"    : "anexos",
        "titulo": "Anexos",
        "tipo"  : "texto_area"
    },
    {
        "id"    : "medio_notificacion",
        "titulo": "Medio de notificación",
    },
    {
        "id"    : "reserva",
        "titulo": "Documento con reserva",
    },
    {
        "id"    : "manejo_informacion",
        "titulo": "Manejo de información",
    },
    {
        "id"    : "empresa_mensajeria_nombre",
        "titulo": "Empresa mensajeria",
    },    
    {
        "id"    : "numero_guia",
        "titulo": "Número guia",
    },
    {
        "id"    : "entidad_traslada",
        "titulo": "Entidad que traslada",
    },
    {
        "id"    : "persona_traslada",
        "titulo": "Persona que traslada",
    },
    {
        "id"    : "radicado_por_nombre",
        "titulo": "Radicado por",
    },
    {
        "id"    : "radicado_en_nombre",
        "titulo": "Radicado en",
    }
]

let basicos_salida_consulta = [
    {
        "id"    : "nro_radicado",
        "titulo": "Número de radicado",
    },
    {
        "id"    : "fecha_radicado",
        "titulo": "Fecha de radicación",
    },
    {
        "id"    : "fecha_documento",
        "titulo": "Fecha documento",
    },
    {
        "id"    : "radicado_responde",
        "titulo": "Número radicado que responde",
    },
    {
        "id"    : "asunto",
        "titulo": "Asunto",
        "tipo"  : "texto_area"
    },
    {
        "id"    : "nro_folios",
        "titulo": "Número de folios",
    },
    {
        "id"    : "anexos",
        "titulo": "Anexos",
        "tipo"  : "texto_area"
    },
    {
        "id"    : "medio_notificacion",
        "titulo": "Medio de notificación",
    },
    {
        "id"    : "reserva",
        "titulo": "Documento con reserva",
    },
    {
        "id"    : "radicado_por_nombre",
        "titulo": "Radicado por",
    },
    {
        "id"    : "radicado_en_nombre",
        "titulo": "Radicado en",
    }
]   

let basicos_interno_consulta = [
    {
        "id"    : "nro_radicado",
        "titulo": "Número de radicado",
    },
    {
        "id"    : "fecha_radicado",
        "titulo": "Fecha de radicación",
    },
    {
        "id"    : "fecha_documento",
        "titulo": "Fecha documento",
    },

    {
        "id"    : "dependencia_envia_nombre",
        "titulo": "Dependencia remitente",
    },

    {
        "id"    : "funcionario_envia_nombre",
        "titulo": "Funcionario remitente",
    },

    {
        "id"    : "dependencia_recibe_nombre",
        "titulo": "Dependencia recibe",
    },

    {
        "id"    : "funcionario_recibe_nombre",
        "titulo": "Funcionario recibe",
    },
   
    {
        "id"    : "tipo_firma",
        "titulo": "Firma",
    },

    {
        "id"    : "reserva",
        "titulo": "Tiene reserva ?",
    },

    {
        "id"    : "medio_notificacion",
        "titulo": "Medio(s) notificación",
    },

    {
        "id"    : "asunto",
        "titulo": "Asunto",
        "tipo"  : "texto_area"
    },
    {
        "id"    : "nro_folios",
        "titulo": "Número de folios",
    },
    {
        "id"    : "anexos",
        "titulo": "Anexos",
        "tipo"  : "texto_area"
    },
    {
        "id"    : "medio_notificacion",
        "titulo": "Medio de notificación",
    },
   
    {
        "id"    : "radicado_por_nombre",
        "titulo": "Radicado por",
    },
    
    {
        "id"    : "radicado_en_nombre",
        "titulo": "Radicado en",
    }
]

export default {
    id                     : id,
    canal_radicado_id      : canal_radicado_id,
    fecha_documento        : fecha_documento,
    radicado_remitente     : radicado_remitente,
    empresa_mensajeria_id  : empresa_mensajeria_id,
    numero_guia            : numero_guia,
    radicado_responde      : radicado_responde,
    nro_folios             : nro_folios,
    anexos                 : anexos,
    asunto                 : asunto,
    entidad_traslada       : entidad_traslada,
    persona_traslada       : persona_traslada,
    relacionados_id        : relacionados_id,
    repone_id              : repone_id,

    basicos_campos_consulta: basicos_campos_consulta,
    basicos_salida_consulta: basicos_salida_consulta,
    basicos_interno_consulta: basicos_interno_consulta
}