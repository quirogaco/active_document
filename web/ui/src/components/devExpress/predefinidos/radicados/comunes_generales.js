import forma_objeto          from '../../forma/utilidades/forma_objeto.js';

let clase_radicado = function(clase) {
    let campo = forma_objeto.campo_objeto({
        "campo"  : "clase_radicado",
        "valor"  : clase,
        "visible": "no"
    })

    return campo;
}

let canal_radicado  = function(canal) {
    let campo = forma_objeto.campo_objeto({
        "campo"  : "canal_radicado_id",
        "valor"  : canal,
        "visible": "no"
    })

    return campo;
}

let canal_visual  = forma_objeto.select_objeto({
    "campo"      : "canal_radicado_id",
    "titulo"     : "Canal de recepción", 
    'obligatorio': 'si',
    "fuente"     : "canales_comunicacion"    
})

let medio_notificacion = forma_objeto.radio_objeto({
    "campo"      : "medio_notificacion",
    "titulo"     : "Medio notificación", 
    "elementos"  : ["CORREO", "DIRECCIÓN FISICA"],    
    //'obligatorio': 'si'
})

const tipos_notificacion =  [
    { id: "CORREO",           nombre: "CORREO"},
    { id: "DIRECCION FISICA", nombre: "DIRECCIÓN FISICA"}    
];

let medio_notificacion_abierto = forma_objeto.tag_objeto({
    "campo"      : "medio_notificacion",
    "titulo"     : "Medio notificación", 
    "elementos"  : tipos_notificacion,    
    //'obligatorio': 'si'
})

let fecha = new Date();
let hoy   = fecha.toISOString().split('T')[0];
let fecha_documento = forma_objeto.campo_objeto({
    'campo'       : 'fecha_documento',
    'tipo'        : "dxDateBox",
    'titulo'      : 'Fecha documento',  
    'formato'     : "yyyy-MM-dd",
    'fecha_maxima': hoy,
    'valor'       : hoy,
    'registrar'   : 'si',
    'obligatorio' : 'si'    
})

let radicado_remitente = forma_objeto.campo_objeto({
    "campo"  : "radicado_remitente",
    "titulo" : "Radicado remitente", 
    'maximo' : 64
})

let nro_folios  = forma_objeto.campo_objeto({
    'campo'      : 'nro_folios',
    'tipo'       : "dxNumberBox",
    'titulo'     : 'Número de folios',  
    'obligatorio': 'si'    
})

let empresa_mensajeria  = forma_objeto.select_objeto({
    "campo"      : "empresa_mensajeria_id",
    "titulo"     : "Empresa mensajeria", 
    "fuente"     : "empresas_mensajeria"
})

let numero_guia = forma_objeto.campo_objeto({
    "campo"  : "numero_guia",
    "titulo" : "Numero de guia", 
    'maximo' : 64
})

let anexos = forma_objeto.campo_objeto({
    "campo"  : "anexos",
    "titulo" : "Anexos", 
    'tipo'   : 'dxTextArea',
    'alto'   : '50',
    'maximo' : 256   
})

let entidad_traslada = forma_objeto.campo_objeto({
    "campo"  : "entidad_traslada",
    "titulo" : "Entidad que traslada", 
    'maximo' : 64
})

let persona_traslada = forma_objeto.campo_objeto({
    "campo"  : "persona_traslada",
    "titulo" : "Persona que traslada", 
    'maximo' : 64
})

let asunto = forma_objeto.campo_objeto({
    'campo'      : 'asunto',
    'tipo'       : 'dxTextArea',
    'titulo'     : 'Asunto',  
    'expandir'   : 2,
    'obligatorio': 'si',
    'alto'       : '80',
    'maximo'     : 2048    
})

let acepta_archivos = ["doc", "docx", "xls", "xlsx", "gif", "png", "bmp", "avi", "mp3", "pdf", "zip"];
let archivos_anexos = function(plantillaAtributos) {
    let archivo = forma_objeto.archivo_objeto(
        {
            "campo"      : "archivos_anexos",
            "titulo"     : "Anexos", 
            "varios"     : "si",
            "maximo"     : 5000000,
            //"obligatorio": "si",            
            "acepta"     : acepta_archivos,                        
        }, 
        plantillaAtributos
    )

    return archivo;
}

let mensaje_archivo = function(plantillaAtributos) {
    let mensaje = forma_objeto.contenido_objeto(
        {
            "contenido"  : 
            `
                <div class="card text-dark bg-light mb-3">
                    <div class="card-body fs-6">
                        Los anexos permitidos son de tipo (word, excel, pdf, gif, png, zip),      
                        Tamaño individual maximo de 5 megas,     
                        Tamaño total maximo 25 megas (sumatoria de todos los archivos).
                    </div>
                </div>
            `
        },
        plantillaAtributos
    )

    return mensaje
}

export default {
    canal_visual              : canal_visual,
    clase_radicado            : clase_radicado,
    canal_radicado            : canal_radicado,
    medio_notificacion        : medio_notificacion,
    medio_notificacion_abierto: medio_notificacion_abierto,
    fecha_documento           : fecha_documento,
    radicado_remitente        : radicado_remitente,
    numero_guia               : numero_guia,
    empresa_mensajeria        : empresa_mensajeria,
    nro_folios                : nro_folios,
    anexos                    : anexos,
    entidad_traslada          : entidad_traslada,
    persona_traslada          : persona_traslada,
    asunto                    : asunto,
    archivos_anexos           : archivos_anexos,    
    mensaje_archivo           : mensaje_archivo
}