import forma_objeto      from '../../forma/utilidades/forma_objeto.js';

let discapacidad_id = forma_objeto.select_objeto({
    "campo"      : "discapacidad_id",
    "titulo"     : "¿ Presenta algún tipo de discapacidad ?", 
    "fuente"     : "discapacidad",
})

let poblacion_id = forma_objeto.select_objeto({
    "campo"      : "poblacion_id",
    "titulo"     : "¿ Perteneces a algún tipo de población especial ?", 
    "fuente"     : "tipo_poblacion",
})

let rango_id = forma_objeto.select_objeto({
    "campo"      : "rango_id",
    "titulo"     : "Selecione su rango de edad", 
    "obligatorio": "si",        
    "fuente"     : "rango_edad",
})

let genero_id = forma_objeto.select_objeto({
    "campo"      : "genero_id",
    "titulo"     : "¿ Con cuál genero se identifica ?", 
    "obligatorio": "si",        
    "fuente"     : "genero",
})

let tipo_ciudadano_id = forma_objeto.select_objeto({
    "campo"      : "ciudadano_id",
    "titulo"     : "Tipo de ciudadano", 
    //"obligatorio": "si",        
    "fuente"     : "tipo_ciudadano",
})

export default {
    discapacidad_id  : discapacidad_id,
    poblacion_id     : poblacion_id,
    rango_id         : rango_id,
    genero_id        : genero_id,
    tipo_ciudadano_id: tipo_ciudadano_id
}