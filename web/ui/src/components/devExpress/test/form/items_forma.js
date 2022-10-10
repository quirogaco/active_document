// Dependencia nombre!!!

// Id
let id_field = {
    "componente": "campo",
    "id"        : "id",
    "visible"   : false
};

// Dependencia
let dependencia_id = {
    "componente"    : "campo",
    "tipo"          : "seleccion",
    "id"            : "dependencia_id",
    "titulo"        : "Dependencia xxx", 
    "fuente"        : "dependencias", 
    "filtros_fuente": ["estado_", "=", "ACTIVO"],
    "obligatorio"   : true,
    "eventos"    : {            
        "valor_cambiado": function(campo, definicion, forma, forma_id) {
            console.log("campo VALOR:", forma, forma_id)
            /*
            muestra_asigna(forma)
            if (campo.value != null) {                     
                 oculta_asigna(forma)
            }
            */
        }
    }
};

let serie_id = {
    "componente"    : "campo",
    "tipo"          : "seleccion",
    "id"            : "serie_id",
    "titulo"        : "Serie", 
    "fuente"        : "agn_serie_trd", 
    "filtros_fuente": ["estado_", "=", "ACTIVO"],
    "obligatorio"   : true,
};

let subserie_id = {
    "componente"    : "campo",
    "tipo"          : "seleccion",
    "id"            : "subserie_id",
    "titulo"        : "SubSerie", 
    "fuente"        : "agn_subserie_trd", 
    "filtros_fuente": ["estado_", "=", "ACTIVO"],
    "obligatorio"   : true,
};

let elementos = [
    id_field,
    dependencia_id,
    serie_id,
    subserie_id,
];

let basicos = {
    "componente": "grupo",
    "tipo"      : "grupo",
    "nombre"    : "basicos",
    "titulo"    : "Información Basica",
    "elementos" : elementos
}

let items = [
    basicos
]

let campos = [
    {
        "componente"    : "campo",
        "id"            : "texto",
        "titulo"        : "Campo de texto", 
        "obligatorio"   : true,
    }
]

export default {
    items: items
}