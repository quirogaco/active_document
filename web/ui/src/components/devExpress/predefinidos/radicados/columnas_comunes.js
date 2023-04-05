import grid_objeto from '../../grid/utilidades/grid_objeto.js';

let clase_radicado = grid_objeto.columna_objeto({
    campo : "clase_radicado",
    titulo: "Tipo",
    ancho : 110,
    ordena: "si",
    filtra: "si",
})

let canal_radicado = grid_objeto.columna_objeto({
    campo : "canal_radicado_nombre",
    titulo: "Canal",
    ancho : 110,
    ordena: "si",
    filtra: "si",
});

let nro_radicado = grid_objeto.columna_objeto({
    campo : "nro_radicado",
    titulo: "Radicado",
    ancho : 130,
    ordena: "si",
    filtra: "si",
});

let fecha_radicado = grid_objeto.columna_fecha_hora({
    campo : "fecha_radicado",
    titulo: "Fecha radicado", 
    ancho : 150,  
    ordena: "si",
    filtra: "si",     
});

let razon_social = grid_objeto.columna_objeto({
    campo : "tercero_razon_social",
    titulo: "Razon social",
    ancho : 300,  
    ordena: "si",
    filtra: "si",
});

let nombres = grid_objeto.columna_objeto({
    campo : "tercero_nombres",
    titulo: "Nombres",
    ancho : 250, 
    ordena: "si",
    filtra: "si",
});

let apellidos = grid_objeto.columna_objeto({
    campo : "tercero_apellidos",
    titulo: "Apellidos",
    ancho : 250, 
    ordena: "si",
    filtra: "si",
})

let nombre_completo = grid_objeto.columna_objeto({
    campo : "tercero_nombre_completo",
    titulo: "Nombre completo",
    ancho : 250, 
    ordena: "si",
    filtra: "si",
})

let correo_electronico = grid_objeto.columna_objeto({
    campo : "tercero_correo_electronico",
    titulo: "Correo electrónico",
    ordena: "si",
    filtra: "si",
    ancho : 250, 
})

let asunto = grid_objeto.columna_objeto({
    campo : "asunto",
    titulo: "Asunto",
    filtra: "si",
    ancho : 650, 
})

export default {
    clase_radicado    : clase_radicado,
    canal_radicado    : canal_radicado,
    nro_radicado      : nro_radicado,
    fecha_radicado    : fecha_radicado,
    razon_social      : razon_social,
    nombres           : nombres,
    apellidos         : apellidos,
    nombre_completo   : nombre_completo,
    correo_electronico: correo_electronico,
    asunto            : asunto
}