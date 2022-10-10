import items_campos from "./items_campos.js"; 

//*********************//
// DEPENDENCIA-ENTIDAD //
//*********************//
let dependencia_entidad = [
    items_campos.ubicacion_id,
    items_campos.dependencia_ubicacion_id,
    items_campos.comentario
];

//********************************//
// DEPENDENCIA - USUARIO LOGUEADO //
//********************************//
let dependencia_usuario = [
    items_campos.dependencia_ubicacion_logueado_id,
    items_campos.comentario
];

//*****************//
// USUARIO ENTIDAD //
//*****************//
let usuario_entidad = [
    items_campos.ubicacion_id,
    items_campos.dependencia_ubicacion_usuario_id,
    items_campos.usuario_id,
    items_campos.comentario
];

//**************//
// USUARIO SEDE //
//**************//
let usuario_sede_logueado = [
    items_campos.dependencia_ubicacion_usuario_logueado_id,
    items_campos.usuario_id,
    items_campos.comentario
];

//*******************************//
// USUARIO DEPENDENCIA LOGUEADO //
//******************************//
let usuario_dependencia_logueado = [
    items_campos.usuario_logueado_id,
    items_campos.comentario
];

//*********************//
// USUARIO RESPONSABLE //
//*********************//
let usuario_responsable_logueado = [
    items_campos.usuario_logueado_id,
    items_campos.comentario
];

//***********//
// FINALIZAR //
//***********//
let finalizar_comentario = [
    items_campos.comentario
];

//************//
// DEVOLUCIÓN //
//************//
let devolucion_comentario = [
    items_campos.comentario
];

//************//
// APROBACIÓN //
//************//
let aprobar_comentario = [
    items_campos.comentario
];

//*************//
// VISTO BUENO //
//*************//
let enviar_visto_bueno = [    
    items_campos.comentario
];


// DATOS
//**********************//
// COMENTARIO ANOTACIÓN //
//**********************//
let comentario_anotacion = [
    items_campos.comentario
];

//*****************//
// ARCHIVOS ANEXOS //
//*****************//
let archivos_anexos = [    
    items_campos.archivos_anexos
];

//************//
// EXPEDIENTE //
//************//
let expediente = [    
    items_campos.expediente_id,
    items_campos.tipo_id
];

//***********//
// PLANTILLA //
//***********//
let plantilla = [    
    items_campos.plantilla_id
];

// **************************** //
// CAMPOS  DE LA FORMA POR TIPO //
// **************************** //
let tipo_campos = {
    // Dependencia
    "dependencia_entidad": dependencia_entidad,
    "dependencia_usuario": dependencia_usuario,
    // Usuario
    "usuario_entidad"    : usuario_entidad,
    "usuario_sede"       : usuario_sede_logueado,
    "usuario_dependencia": usuario_dependencia_logueado,
    "usuario_responsable": usuario_responsable_logueado,

    "finalizar"          : finalizar_comentario,    
    "devolver"           : devolucion_comentario ,
    "aprobar"            : aprobar_comentario,
    "enviar_visto_bueno" : enviar_visto_bueno, 
    
    // Datos
    "comentario_anotacion": comentario_anotacion,    
    "archivos_anexos"     : archivos_anexos,    
    "expediente"          : expediente,  
    "plantilla"           : plantilla  
}

let basicos = {
    "componente": "grupo",
    "tipo"      : "grupo",
    "nombre"    : "basicos",
    "titulo"    : "",
    "elementos" : []
}

let grupos_datos = function(tipo) {
    basicos.elementos = [];     
    if ( (tipo !== undefined) && (tipo !== null) ) {
        basicos.elementos = tipo_campos[tipo];        
    }

    return [basicos];    
}

export default {
    items: grupos_datos
}