import forma_objeto          from '../../forma/utilidades/forma_objeto.js'
import utilidades_estructura from '../../../../librerias/utilidades_estructura.js';

let dependencia_id = forma_objeto.select_objeto({
    "campo"      : "dependencia_responde_id",
    "titulo"     : "Dependencia remitente", 
    "fuente"     : "dependencias",
    "busqueda_expresion": "nombre_completo",
    "muestra_expresion" : "nombre_completo",
    "registrar"         : "si",
    'obligatorio': 'si',
    "filtros"    : [["estado_", "=", "ACTIVO"]]
})

let funcionario_id = forma_objeto.select_objeto({
    "campo"      : "funcionario_responde_id",
    "titulo"     : "Funcionario remitente", 
    "fuente"     : "usuarios",
    "busqueda_expresion": "nombre",
    "muestra_expresion" : "nombre",
    "registrar"         : "si",
    'obligatorio': 'si',
    "filtros"    : [["estado_", "=", "ACTIVO"]]
})


// Tema Dependencia
let tema_dependencia  = forma_objeto.select_objeto({
    "titulo"            : "Tema/tramite de la dependencia", 
    "fuente"            : "temas",
    "campo"             : "tema_dependencia",
    "registrar"         : "si",
    "obligatorio"       : "si",  
    "eventos"           : {
        "seleccion_cambiada": async function(objeto) {
            // Dato seleccionado tema
            let id = $lib.cargaAtributo(objeto.selectedItem, 'id', null)                
            // Carga datos Subtema
            let sds = $lib.traer_fuente_datos("radicados_salida", "subtema_dependencia")  
            sds.searchOperation("NO_BUSCAR")            
            if (id != null) {
                sds.searchOperation("")          
                sds.filter(["tema_id", "=", id])       
            }
            sds.reload()

            // Subtemas
            $lib.forma_componentes_opcion("radicados_salida", ["subtema_dependencia"], "value", null)                                               
        }
    }
})

// SubTema Dependencia
let subtema_dependencia  = forma_objeto.select_objeto({
    "titulo"            : "Subtema de la dependencia", 
    "fuente"            : "subtemas",
    "campo"             : "subtema_dependencia",
    "nombre"            : "subtema_dependencia",
    "registrar"         : "si",
    //"obligatorio"       : "si",  
    "eventos"           : {}
})

let reserva = forma_objeto.radio_objeto({
    "campo"      : "reserva",
    "titulo"     : "Reserva", 
    "elementos"  : ["SI", "NO"],   
    "valor"      : "NO", 
    'obligatorio': 'si',
    "registrar"  : "si"    
})

let tipo_firma = forma_objeto.radio_objeto({
    "campo"      : "tipo_firma",
    "titulo"     : "Tipo de firma", 
    "elementos"  : ["FISICA", "DIGITAL"],   
    "valor"      : "FISICA", 
    'obligatorio': 'si',
    "registrar"  : "si"    
})

let copia_usuarios_id = forma_objeto.tag_objeto({
    "titulo"     : "Copia a usuarios", 
    "fuente"     : "usuarios",
    "campo"      : "copia_usuarios_id",
    "nombre"     : "copia_usuarios_id",
    "registrar"  : "si",
})

let copia_grupos_id = forma_objeto.tag_objeto({
    "titulo"     : "Copia a grupos de usuarios", 
    "fuente"     : "grupo_usuarios",
    "campo"      : "copia_grupos_id",
    "nombre"     : "copia_grupos_id",
    "registrar"  : "si",
})

let listado_destinatario_id = forma_objeto.select_objeto({
    "campo"      : "listado_id",
    "titulo"     : "Listado de destinatarios", 
    "fuente"     : "destinatarios_listado",
    "busqueda_expresion": "detalle",
    "muestra_expresion" : "detalle",
    "registrar"         : "si",
    'obligatorio': 'si',
    "filtros"    : [["estado_", "=", "ACTIVO"]]
})

let plantilla_id = forma_objeto.select_objeto({
    "campo"      : "plantilla_id",
    "titulo"     : "Plantilla", 
    "fuente"     : "plantillas",
    "busqueda_expresion": "descripcion",
    "muestra_expresion" : "descripcion",
    "registrar"  : "si",
    'obligatorio': 'si',
    "filtros"    : [["estado_", "=", "ACTIVO"]]
})

let dependencia_envia_id = forma_objeto.select_objeto({
    "campo"      : "dependencia_envia_id",
    "titulo"     : "Dependencia remitente", 
    "fuente"     : "dependencias",
    "busqueda_expresion": "nombre_completo",
    "muestra_expresion" : "nombre_completo",
    "registrar"         : "si",
    'obligatorio': 'si',
    "filtros"    : [["estado_", "=", "ACTIVO"]]
})

let funcionario_envia_id = forma_objeto.select_objeto({
    "campo"      : "funcionario_envia_id",
    "titulo"     : "Funcionario remitente", 
    "fuente"     : "usuarios",
    "busqueda_expresion": "nombre",
    "muestra_expresion" : "nombre",
    "registrar"         : "si",
    'obligatorio': 'si',
    "filtros"    : [["estado_", "=", "ACTIVO"]]
})

/*
let plantilla_id = forma_objeto.campo_objeto({
    "campo"  : "plantilla_id",
    "titulo" : "Plantilla comunicación", 
    'maximo' : 64
})
*/

export default {
    dependencia_id         : dependencia_id,
    funcionario_id         : funcionario_id,
    dependencia_envia_id   : dependencia_envia_id,
    funcionario_envia_id   : funcionario_envia_id,
    tema_dependencia       : tema_dependencia,
    subtema_dependencia    : subtema_dependencia,
    tipo_firma             : tipo_firma,
    reserva                : reserva,
    copia_usuarios_id      : copia_usuarios_id,
    copia_grupos_id        : copia_grupos_id,
    listado_destinatario_id: listado_destinatario_id,
    plantilla_id           : plantilla_id
}