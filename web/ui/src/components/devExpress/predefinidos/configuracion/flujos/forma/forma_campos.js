let id_field = {
    "componente": "campo",
    "id"        : "id",
    "visible"   : false
}

let nombre = {
    "componente" : "campo",
    "tipo"       : "texto",
    "id"         : "nombre",
    "titulo"     : "Nombre", 
    "obligatorio": true
}

let detalle = {
    "componente" : "campo",
    "tipo"       : "texto_area",
    "id"         : "detalle",
    "titulo"     : "Detalle", 
    "mensaje"    : "Descripcion detallada"
}

let total_tiempo = {
    "componente" : "campo",
    "tipo"       : "entero",
    "id"         : "total_tiempo",
    "titulo"     : "Tiempo total",
    "maxima"     : 999,
    "minima"     : 0
}

let alertar_tiempo = {
    "componente" : "campo",
    "tipo"       : "texto",
    "id"         : "alertar_tiempo",
    "titulo"     : "Alertar en tiempo",
    "mensaje"    : "Separar valores con coma"
}

let alertar_porcentaje = {
    "componente" : "campo",
    "tipo"       : "texto",
    "id"         : "alertar_porcentaje",
    "titulo"     : "Alertar en porcentaje",
    "mensaje"    : "Separar valores con coma"
}

let horas_dias = {
    "componente" : "campo",
    "tipo"       : "radio",
    "id"         : "horas_dias",
    "fuente"     : [
        {id:"HORAS", nombre:"HORAS"},
        {id:"DIAS",  nombre:"DIAS"}
    ],
    "titulo"     : "Tiempo asignado en"
}

let tipo_tiempo = {
    "componente" : "campo",
    "tipo"       : "radio",
    "id"         : "tipo_tiempo",
    "fuente"     : [
        {id:"HABILES",     nombre:"HABILES"},
        {id:"CALENDARIO",  nombre:"CALENDARIO"}
    ],
    "titulo"     : "Tipo de tiempo asignado"
}

let notifica_id = {
    "componente"       : "campo",
    "tipo"             : "etiqueta",
    "id"               : "notifica_id",
    "titulo"           : "Notificar a", 
    "fuente"           : "usuarios", 
    "filtros_fuente"   : ["estado_", "=", "ACTIVO"],
    "muestra_expresion": "nombre_completo"
}

let formulario_id = {
    "componente"    : "campo",
    "tipo"          : "etiqueta",
    "id"            : "formulario_id",
    "titulo"        : "Formulario asociado", 
    "fuente"        : "formularios_dinamicos",
    "filtros_fuente": ["estado_", "=", "ACTIVO"]
}

let elementos = [
    id_field,
    nombre,    
    detalle,
    total_tiempo,
    alertar_tiempo,
    alertar_porcentaje,
    horas_dias,    
    tipo_tiempo,
    notifica_id,
    formulario_id
]

let basicos = {
    "componente": "grupo",
    "tipo"      : "grupo",
    "nombre"    : "basicos",
    "titulo"    : "Información Tramite",
    "elementos" : elementos
}

let items = [
    basicos
]

export default {
    items: items
}