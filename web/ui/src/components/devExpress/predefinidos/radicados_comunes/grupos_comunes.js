import forma_objeto      from '../../forma/utilidades/forma_objeto.js'
import comunes_remitente from '../radicados_comunes/comunes_remitente.js'
import comunes_generales from '../radicados_comunes/comunes_generales.js'
import comunes_tramite   from '../radicados_comunes/comunes_tramite.js'
import consulta_anexos   from './consulta_anexos.js'
import dialogos          from '../../../../librerias/dialogos.js'

let grupoBasico = function(tipo) {
    return forma_objeto.grupo_objeto({
        'titulo'     : 'Información basica documento',
        'elementos'  : [
            comunes_generales.clase_radicado(tipo),  
            comunes_generales.canal_visual,  
            comunes_generales.medio_notificacion_abierto,
            comunes_generales.fecha_documento,   
            comunes_generales.radicado_remitente,
            comunes_generales.empresa_mensajeria,
            comunes_generales.numero_guia, 
            comunes_generales.nro_folios,
            comunes_generales.anexos,
            comunes_generales.asunto, 
            comunes_generales.entidad_traslada,
            comunes_generales.persona_traslada
        ]
    })
}

let grupoIdentificacion = function(forma_id) {
    let campos = [
        comunes_remitente.clase_remitente(forma_id),
        comunes_remitente.tipo_tercero_id,
        comunes_remitente.busca_remitente(forma_id),
        comunes_remitente.tipo_identificacion_id,
        comunes_remitente.nit_nro_identificacion,
        comunes_remitente.razon_social,    
        comunes_remitente.nombres,
        comunes_remitente.apellidos,
        comunes_remitente.cargo,
        comunes_remitente.direccion,
        comunes_remitente.correo_electronico,  
        comunes_remitente.codigo_postal,    
        comunes_remitente.telefono,
        comunes_remitente.telefono_movil,  
        comunes_remitente.fax,
        comunes_remitente.ciudad_id
    ]

    return forma_objeto.grupo_objeto({
        'titulo'     : 'Remitente identificación',
        'elementos'  : campos
    })    
}

let grupoAnexos = function(plantillaAtributos) { 
    return forma_objeto.grupo_objeto({
        'titulo'     : 'Archivos anexos',
        'elementos'  : [
            consulta_anexos.grupoAnexos,
            comunes_generales.mensaje_archivo(plantillaAtributos),
            comunes_generales.archivos_anexos(plantillaAtributos)
        ]
    });
}

let grupoPeticion  = function(forma_id, tipo) {
    let campos = [
        comunes_tramite.horas_dias,
        comunes_tramite.total_tiempo,
        comunes_tramite.prioridad,
        comunes_tramite.reserva,        
        comunes_tramite.copia_usuarios_id,
        comunes_tramite.copia_grupos_id
    ]

    if (tipo == "VENTANILLA") {
        campos.unshift(
            comunes_tramite.pqrs(forma_id), 
            comunes_tramite.dependencia_id,
            comunes_tramite.peticion_id(forma_id),
        )
    }
    else {
        campos.unshift(
            comunes_tramite.ventanilla(forma_id),
            comunes_tramite.dependencia_pqrs_radica,
            comunes_tramite.peticion_id_pqrs(forma_id),
            comunes_tramite.tema_dependencia_radica,
            comunes_tramite.subtema_dependencia_radica,
        )
    }

    return forma_objeto.grupo_objeto({
        'titulo'     : 'Petición',
        'elementos'  : campos
    })
}

let campos = function(forma_id, tipo, plantillaAtributos) {
    return [
        grupoBasico(tipo),
        grupoIdentificacion(forma_id),
        grupoPeticion(forma_id, tipo),
        grupoAnexos(plantillaAtributos) 
    ]
}

let campos_ventanilla = function(forma_id, tipo, plantillaAtributos) {
    return [
        grupoBasico(tipo),
        grupoIdentificacion(forma_id),
        grupoPeticion(forma_id, tipo),
        grupoAnexos(plantillaAtributos) 
    ]
}

let campos_atributos = [
    // Base
    "canal_radicado_id",
    "fecha_documento",
    "nro_folios",
    "asunto",
    
    // Remitente
    "tercero_clase",
    "tercero_tipo_tercero_id",
    "tercero_tipo_identificacion_id",
    "tercero_razon_social",
    "tercero_nombres",
    "tercero_apellidos",
    "tercero_direccion",

    // Petición
    "gestion_peticion_id", 
    "gestion_horas_dias",
    "gestion_total_tiempo",
    "gestion_prioridad",
    "reserva"
]

let inicializa_forma = function(forma_id, tipo) {
    if (tipo == "VENTANILLA") {
        $lib.forma_componente_opcion(forma_id, "pqrs", "value", "NO")
    }
    else {
        $lib.forma_componente_opcion(forma_id, "ventanilla", "value", "NO")
    }    
    
    // Tipo de tiempo, total tiempo
    $lib.forma_atributo_items(forma_id, ["gestion_horas_dias", "gestion_total_tiempo"], "disabled", true)
            
    // Asigna valor a clase para obligar mostrar campos
    $lib.forma_componente_opcion(forma_id, "tercero_clase", "value", "JURIDICA"); 
    $lib.forma_componente_opcion(forma_id, "gestion_prioridad", "value", "MEDIA"); 
    $lib.forma_componente_opcion(forma_id, "reserva", "value", "NO"); 
    $lib.forma_componente_opcion(forma_id, "fecha_documento", "value", comunes_generales.fecha_hoy())    

    window.scroll(0,0)
}

let montado = function(forma_id, tipo, campos_atributos) {
    // Salva atributos de validación
    window.atributos_campos[forma_id] = $lib.leer_forma_atributo_items(forma_id, campos_atributos, "validationRules")
    inicializa_forma(forma_id, tipo)       
}

let retorno_envio = function(forma_id, tipo, respuesta) {
    inicializa_forma(forma_id, tipo)             
    let nro_radicado = respuesta["resultados"]["datos"]["nro_radicado"]
    dialogos.miMensaje("Radicación", (
        ("Documento radicado con número " + nro_radicado)
    ))     
}

export default {
    grupoBasico        : grupoBasico,
    grupoIdentificacion: grupoIdentificacion,
    grupoPeticion      : grupoPeticion,
    grupoAnexos        : grupoAnexos,
    campos             : campos,
    campos_ventanilla  : campos_ventanilla,
    campos_atributos   : campos_atributos,    
    
    // Funciones globales
    inicializa_forma   : inicializa_forma,
    montado            : montado,
    retorno_envio      : retorno_envio
}