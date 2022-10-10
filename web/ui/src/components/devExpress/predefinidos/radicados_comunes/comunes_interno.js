import forma_objeto          from '../../forma/utilidades/forma_objeto.js'

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

let dependencia_recibe_id = forma_objeto.select_objeto({
    "campo"      : "dependencia_recibe_id",
    "titulo"     : "Dependencia recibe", 
    "fuente"     : "dependencias",
    "busqueda_expresion": "nombre_completo",
    "muestra_expresion" : "nombre_completo",
    "registrar"         : "si",
    'obligatorio': 'si',
    "filtros"    : [["estado_", "=", "ACTIVO"]]
})

let funcionario_recibe_id = forma_objeto.select_objeto({
    "campo"      : "funcionario_recibe_id",
    "titulo"     : "Funcionario recibe", 
    "fuente"     : "usuarios",
    "busqueda_expresion": "nombre",
    "muestra_expresion" : "nombre",
    "registrar"         : "si",
    'obligatorio': 'si',
    "filtros"    : [["estado_", "=", "ACTIVO"]]
})



export default {
    dependencia_envia_id   : dependencia_envia_id,
    funcionario_envia_id   : funcionario_envia_id,
    dependencia_recibe_id  : dependencia_recibe_id,
    funcionario_recibe_id  : funcionario_recibe_id
}