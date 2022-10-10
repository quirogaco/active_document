import forma_objeto      from '../../forma/utilidades/forma_objeto.js'
import comunes_interno   from '../radicados_comunes/comunes_interno.js'
import comunes_generales from '../radicados_comunes/comunes_generales.js'
import dialogos          from '../../../../librerias/dialogos.js'

let grupoBasico = function(tipo) {
    return forma_objeto.grupo_objeto({
        'titulo'     : 'Información basica documento',
        'elementos'  : [            
            comunes_generales.nro_folios,
            comunes_generales.asunto, 
        ]
    })
}

let grupoRemitente = function(forma_id) {
    let campos = [
        comunes_interno.dependencia_envia_id,
        comunes_interno.funcionario_envia_id
    ]

    return forma_objeto.grupo_objeto({
        'titulo'     : 'Remitente',
        'elementos'  : campos
    })    
}

let grupoDestinatario = function(forma_id) {
    let campos = [
        comunes_interno.dependencia_recibe_id,
        comunes_interno.funcionario_recibe_id
    ]

    return forma_objeto.grupo_objeto({
        'titulo'     : 'Destinatario',
        'elementos'  : campos
    })    
}

let grupoAnexos = function(plantillaAtributos) { 
    return forma_objeto.grupo_objeto({
        'titulo'     : 'Archivos anexos',
        'elementos'  : [
            comunes_generales.mensaje_archivo(plantillaAtributos),
            comunes_generales.archivos_anexos(plantillaAtributos)
        ]
    });
}

let campos = function(forma_id, tipo, plantillaAtributos) {
    return [
        grupoBasico(tipo),
        grupoRemitente(forma_id),
        grupoDestinatario(forma_id),
        grupoAnexos(plantillaAtributos) 
    ]
}

let campos_atributos = [
    // Base
    "canal_radicado_id",
    "fecha_documento",
    "nro_folios",
    "asunto"
]

let inicializa_forma = function(forma_id, tipo) {            
    // Asigna valor a clase para obligar mostrar campos
    //$lib.forma_componente_opcion(forma_id, "fecha_documento", "value", comunes_generales.fecha_hoy())    

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
    grupoRemitente     : grupoRemitente,
    grupoDestinatario  : grupoDestinatario,
    grupoAnexos        : grupoAnexos,
    campos             : campos,
    campos_atributos   : campos_atributos,    
    
    // Funciones globales
    inicializa_forma   : inicializa_forma,
    montado            : montado,
    retorno_envio      : retorno_envio
}