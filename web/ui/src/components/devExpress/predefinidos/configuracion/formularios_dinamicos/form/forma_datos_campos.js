let id_field = {
    "componente": "campo",
    "id"        : "id",
    "visible"   : false
}

let codigo = {
    "componente" : "campo",
    "tipo"       : "texto",
    "id"         : "codigo",
    "titulo"     : "Codigo", 
    "longitud"   : 100,
    'ancho'      : 500,
    "obligatorio": true
}

let nombre = {
    "componente" : "campo",
    "tipo"       : "texto",
    "id"         : "nombre",
    "titulo"     : "Nombre", 
    "longitud"   : 200,
    'ancho'      : 1000,
    "obligatorio": true
}


let elementos = [
    id_field,
    codigo,
    nombre 
]

let basicos = {
    "componente": "grupo",
    "tipo"      : "grupo",
    "nombre"    : "basicos",
    "titulo"    : "Información Formulario",
    "elementos" : elementos
}

let items = [
    basicos
]

export default {
    items: items
}