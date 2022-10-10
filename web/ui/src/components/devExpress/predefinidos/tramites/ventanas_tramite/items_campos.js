import utilidades_estructura from '../../../../../librerias/utilidades_estructura.js';
import forma_definiciones from "../../comunes_vue/forma/forma.js";

// Ubicación
let ubicacion_id = {
    "componente"    : "campo",
    "tipo"          : "seleccion",
    "id"            : "ubicacion_id",
    "titulo"        : "Sede/Territorial", 
    "fuente"        : "ubicaciones", 
    "filtros_fuente": ["estado_", "=", "ACTIVO"],
    "obligatorio"   : true,
    "eventos"       : {            
        "valor_cambiado": function(campo, definicion, forma, forma_id) {              
            forma_definiciones.limpia_campos(forma, ["dependencia_id"]); 
            let filtros = ["ubicacion_id", "=", campo.value];
            forma_definiciones.asigna_fuente_datos(forma, "dependencia_id", "select", "dependencias", filtros, {});            
        }
    }
};

// Dependencia ubicacion
let dependencia_ubicacion_id = {
    "componente"       : "campo",
    "tipo"             : "seleccion",
    "id"               : "dependencia_id",
    "titulo"           : "Dependencia", 
    "fuente"           : "dependencias", 
    "muestra_expresion": "nombre_completo",
    "filtros_fuente"   : ["estado_", "=", "ACTIVO"],
    "obligatorio"      : true
};

// Dependencia ubicacion, que filtra usuarios
let dependencia_ubicacion_usuario_id = {
    "componente"       : "campo",
    "tipo"             : "seleccion",
    "id"               : "dependencia_id",
    "titulo"           : "Dependencia", 
    "fuente"           : "dependencias", 
    "muestra_expresion": "nombre_completo",
    "filtros_fuente"   : ["estado_", "=", "ACTIVO"],
    "obligatorio"      : true,
    "eventos"          : {            
        "valor_cambiado": function(campo, definicion, forma, forma_id) {            
            forma_definiciones.limpia_campos(forma, ["usuario_id"]); 
            let filtros = ["dependencia_id", "=", campo.value];
            forma_definiciones.asigna_fuente_datos(forma, "usuario_id", "select", "usuarios", filtros, {});            
        }
    }
};

// Dependencia ubicacion usuario logueado
let dependencia_ubicacion_logueado_id = {
    "componente"       : "campo",
    "tipo"             : "seleccion",
    "id"               : "dependencia_id",
    "titulo"           : "Dependencia", 
    "fuente"           : "dependencias", 
    "muestra_expresion": "nombre_completo",
    "filtros_fuente"   : [ ["estado_", "=", "ACTIVO"], ["ubicacion_id", "=", window.$usuario.ubicacion_id] ],
    "obligatorio"      : true,
    "eventos"          : {            
        "valor_cambiado": function(campo, definicion, forma, forma_id) {}
    }
};

// Dependencia ubicacion usuario logueado, filtra usuario
let dependencia_ubicacion_usuario_logueado_id = {
    "componente"       : "campo",
    "tipo"             : "seleccion",
    "id"               : "dependencia_id",
    "titulo"           : "Dependencia", 
    "fuente"           : "dependencias", 
    "muestra_expresion": "nombre_completo",
    "filtros_fuente"   : [ ["estado_", "=", "ACTIVO"], ["ubicacion_id", "=", window.$usuario.ubicacion_id] ],
    "obligatorio"      : true,
    "eventos"          : {            
        "valor_cambiado": function(campo, definicion, forma, forma_id) {
            forma_definiciones.limpia_campos(forma, ["usuario_id"]); 
            let filtros = ["dependencia_id", "=", campo.value];
            forma_definiciones.asigna_fuente_datos(forma, "usuario_id", "select", "usuarios", filtros, {});       
        }
    }
};

// Usuario
let usuario_id = {
    "componente"       : "campo",
    "tipo"             : "seleccion",
    "id"               : "usuario_id",
    "titulo"           : "Usuario", 
    "fuente"           : "usuarios", 
    "muestra_expresion": "nombre_completo",
    "obligatorio"      : true,
    "eventos"          : {            
        "valor_cambiado": function(campo, definicion, forma, forma_id) {}
    }
};

// Usuarios dependencias - usuario logueado
let usuario_logueado_id = {
    "componente"       : "campo",
    "tipo"             : "seleccion",
    "id"               : "usuario_id",
    "titulo"           : "Usuario", 
    "fuente"           : "usuarios", 
    "muestra_expresion": "nombre_completo",
    "obligatorio"      : true,
    "filtros_fuente"   : [ ["estado_", "=", "ACTIVO"], ["dependencia_id", "=", window.$usuario.dependencia_id] ],
    "eventos"          : {            
        "valor_cambiado": function(campo, definicion, forma, forma_id) {}
    }
};

//********//
// DATOS //
//*******//
// Comentario
let comentario = {
    "componente" : "campo",
    "tipo"       : "texto_area",
    "id"         : "comentario",
    "titulo"     : "Comentario/Mensaje", 
    "obligatorio": true
};

// Archivos anexos
let acepta_archivos = [".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".gif", ".png", ".bmp", ".avi", ".mp3", ".pdf", ".zip"]
let archivos_anexos = {
    'titulo'       : 'Archivo anexo',
    "id"           : "archivos",
    'tipo'         : 'archivo',
    //"multiple"     : true,
    "tamano_maximo": 5000000,
    'obligatorio'  : true,
    'extensiones'  : acepta_archivos
}

// Expedientes
let expediente_id = {
    "componente"       : "campo",
    "tipo"             : "seleccion",
    "id"               : "expediente_id",
    "titulo"           : "Expediente", 
    "fuente"           : "agn_expedientes_trd", 
    "muestra_expresion": "nombre",
    "filtros_fuente"   : [ ["estado_", "=", "ACTIVO"], ["dependencia_id", "=", window.$usuario.dependencia_id] ],
    "obligatorio"      : true,
    "eventos"          : {            
        "valor_cambiado": async function(campo, definicion, forma, forma_id) {    
            forma_definiciones.limpia_campos(forma, ["tipo_id"]);          
            if ( (campo.value != null) && (campo.value != undefined) ) {  
                let datos   = await utilidades_estructura.leer_registro_id("agn_expedientes_trd", campo.value);            
                let filtros = [ ["serie_id", "=", datos.serie_id] ];
                if (datos.subserie_id != undefined) {
                    filtros.push( ["subserie_id", "=", datos.subserie_id] )
                }
                forma_definiciones.asigna_fuente_datos(forma, "tipo_id", "select", "agn_tipo_documental_trd", filtros, {}); 
            }     
        }
    }
};

// Tipo documental
let tipo_id = {
    "componente"       : "campo",
    "tipo"             : "seleccion",
    "id"               : "tipo_id",
    "titulo"           : "Tipo documental", 
    "fuente"           : "agn_tipo_documental_trd", 
    "obligatorio"      : true
};

// Plantillas de word
let plantilla_id = {
    "componente"       : "campo",
    "tipo"             : "seleccion",
    "id"               : "plantilla_id",
    "titulo"           : "Plantilla borrador", 
    "fuente"           : "plantillas", 
    "muestra_expresion": "descripcion",
    "obligatorio"      : true
};

export default {
    ubicacion_id                             : ubicacion_id,
    dependencia_ubicacion_id                 : dependencia_ubicacion_id,
    dependencia_ubicacion_usuario_id         : dependencia_ubicacion_usuario_id,
    dependencia_ubicacion_logueado_id        : dependencia_ubicacion_logueado_id,
    dependencia_ubicacion_usuario_logueado_id: dependencia_ubicacion_usuario_logueado_id,
    usuario_id                               : usuario_id,
    usuario_logueado_id                      : usuario_logueado_id,
    comentario                               : comentario,
    archivos_anexos                          : archivos_anexos,
    expediente_id                            : expediente_id,
    tipo_id                                  : tipo_id,
    plantilla_id                             : plantilla_id
}