import forma_definiciones from "../../../comunes_vue/forma/forma.js"

// ****************** // 
// CAMPOS DE CONTROL  //
// ****************** // 
let datos_clase = [
    {"id": "JURIDICA", "nombre": "JURIDICA"},
    {"id": "NATURAL",  "nombre": "NATURAL"},
    {"id": "ANONIMO",  "nombre": "ANONIMO"}
];

// MANEJO DE CAMPOS
const limpiar_tercero = function(forma=null) {
    let campos_limpiar = [
        "tercero_tercero_tipo_id", 
        "busca_remitente"
    ];
    forma_definiciones.limpia_campos(forma, campos_limpiar);
};

let obligatorios_tercero = function(forma, campos=null) {
    // Obligatorios
    let campos_obligatorios = [
        "tercero_razon_social",
        "tercero_nombres",
        "tercero_apellidos",                        
        "tercero_ciudad_id"
    ];
    campos = ( campos != null ? campos: campos_obligatorios );
    forma_definiciones.asigna_validador_forma(forma, campos, "obligatorio");
};

let no_obligatorios_tercero = function(forma, campos) {   
    forma_definiciones.borra_validador_forma(forma, campos, "obligatorio");
};

const campos_generales = [
    "tercero_datos"
];

const muestra_tercero = function(forma=null, campos=null) {  
    campos = ( campos != null ? campos: campos_generales );
    forma_definiciones.muestra_campos(forma, campos);
};

const oculta_tercero = function(forma=null, campos=null) {
    campos = ( campos != null ? campos: campos_generales );
    forma_definiciones.oculta_campos(forma, campos);
};

const clase_tercero = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo"     : 'Clase de destinatario', 
        "fuente"     : datos_clase,  
        "valor"      : "JURIDICA",
        "obligatorio": true,
        "eventos"    : {
            "valor_cambiado": function(campo, definicion, forma, forma_id) { 
                let valor = campo.value;
                forma.forma.beginUpdate(); 
                limpiar_tercero(forma);              
                if ( (valor == "JURIDICA") || (valor == "NATURAL") ) {                    
                    // Por tipo especifico
                    if (valor == "JURIDICA") {
                        oculta_tercero(forma, ["tercero_anonimo"]); 
                        oculta_tercero(forma, ["tercero_natural"]);                     
                        muestra_tercero(forma, ["tercero_juridica"]);  
                    };

                    if (valor == "NATURAL") {
                        oculta_tercero(forma, ["tercero_anonimo"]); 
                        oculta_tercero(forma, ["tercero_juridica"]);                     
                        muestra_tercero(forma, ["tercero_natural"]);                                            
                    };                                                 
                }
                else {
                    oculta_tercero(forma, ["tercero_juridica"]); 
                    oculta_tercero(forma, ["tercero_natural"]);                     
                    muestra_tercero(forma, ["tercero_anonimo"]);            
                }
                forma.forma.endUpdate();

                // Despues de endUpate para que tome elfiltro
                if ( (valor == "JURIDICA") || (valor == "NATURAL") ) {     
                    let filtros = ["tipo", "=", valor];
                    forma_definiciones.asigna_fuente_datos(forma, "tercero_tercero_tipo_id", "select", "tipo_terceros", filtros, {});
                };
                // Cuando se modifica se repinta el valor vuelve a default
                $forma.asigna_valor(forma, "tercero_clase", valor);   
            }
        }
    }
    
    return forma_definiciones.genera_campo("radio", "tercero_clase", id, atributos_base, atributos)
};

const tipo_tercero_id = function(id=null, atributos={}) {
    let atributos_base = {
        'titulo'        : 'Tipo de destinatario', 
        "fuente"        : "tipo_terceros",   
        "filtros_fuente": ["tipo", "=", "JURIDICA"],
        'obligatorio'   : true,
        "eventos"    : {
            "seleccion_cambiada": function(campo, definicion, forma, forma_id) {  
                let datos = campo.selectedItem
                if (datos != null) {
                    let filtros = [ ["clase", "=", datos.tipo], ["tipo_tercero_nombre", "=", datos.nombre] ];
                    forma_definiciones.asigna_fuente_datos(forma, "busca_remitente", "select", "terceros", filtros, {});      
                }         
            }
        }
    }
    
    return forma_definiciones.genera_campo("seleccion", "tercero_tercero_tipo_id", id, atributos_base, atributos)
};

const busca_remitente = function(id=null, atributos={}) {
    let atributos_base = {
        'titulo'            : 'Buscar destinatario', 
        "fuente"            : "terceros", 
        "busqueda_expresion": "nombre_completo",
        "muestra_expresion" : "nombre_completo",
        "eventos"    : {
            "seleccion_cambiada": function(campo, definicion, forma, forma_id) {
                if (campo.selectedItem != null) {
                    let campos_valor = {
                        "nro_identificacion"    : "tercero_nro_identificacion",
                        "razon_social"          : "tercero_razon_social",
                        "apellidos"             : "tercero_apellidos",
                        "nombres"               : "tercero_nombres",
                        "direccion"             : "tercero_direccion",
                        "correo_electronico"    : "tercero_correo_electronico",
                        "codigo_postal"         : "tercero_codigo_postal",
                        "telefono"              : "tercero_telefono",
                        "telefono_movil"        : "tercero_telefono_movil",
                        "fax"                   : "tercero_fax",
                        "ciudad_id"             : "tercero_ciudad_id",
                        "cargo"                 : "tercero_cargo",
                        "tipo_identificacion_id": "tercero_tipo_identificacion_id"                        
                    };
                    forma_definiciones.asigna_valor_campos(forma, campos_valor, campo.selectedItem);
                }
            }
        }
    }
    
    return forma_definiciones.genera_campo("seleccion", "busca_remitente", id, atributos_base, atributos)
}

// ************************ // 
// CAMPOS BASICOS TERCERO  //
// *********************** // 
const tipo_identificacion = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo"     : 'Tipo de identificación', 
        "fuente"     : "tipo_identificaciones",
        "obligatorio": true,
        "visible"    : false        
    };
    
    return forma_definiciones.genera_campo("seleccion", "tercero_tipo_identificacion_id", id, atributos_base, atributos)
}

const nro_identificacion = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo"  : 'Número de identificación/Nit', 
        "longitud": 60,
    };
    
    return forma_definiciones.genera_campo("texto", "tercero_nro_identificacion", id, atributos_base, atributos)
}

const razon_social = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo"     : 'Razón social',
        "obligatorio": true,
        "longitud"   : 250, 
    };
    
    return forma_definiciones.genera_campo("texto", "tercero_razon_social", id, atributos_base, atributos)
}

const nombres = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo"     : 'Nombres',
        "longitud"   : 250, 
    };
    
    return forma_definiciones.genera_campo("texto", "tercero_nombres", id, atributos_base, atributos)
}

const apellidos = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo"     : 'Apellidos',
        "longitud"   : 250, 
    };
    
    return forma_definiciones.genera_campo("texto", "tercero_apellidos", id, atributos_base, atributos)
}

const correo_electronico = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo"     : 'Correo electrónico',
        "longitud"   : 125, 
        //"obligatorio": true,
        "validadores": [
            "correo_multiple"
        ]
    };
    
    return forma_definiciones.genera_campo("correo", "tercero_correo_electronico", id, atributos_base, atributos)
}

const cargo = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo"  : 'Cargo',
        "longitud": 125, 
    };
    
    return forma_definiciones.genera_campo("texto", "tercero_cargo", id, atributos_base, atributos)
}

const direccion = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo"  : 'Dirección',
        "longitud": 125, 
    };
    
    return forma_definiciones.genera_campo("texto", "tercero_direccion", id, atributos_base, atributos)
}

const codigo_postal = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo" : 'Codigo postal',
        "longitud": 125, 
    };
    
    return forma_definiciones.genera_campo("texto", "tercero_codigo_postal", id, atributos_base, atributos)
}

const telefono = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo" : 'Telefono',
        "longitud": 60, 
    };
    
    return forma_definiciones.genera_campo("texto", "tercero_telefono", id, atributos_base, atributos)
}

const telefono_movil = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo" : 'Telefono movil',
        "longitud": 60, 
    };
    
    return forma_definiciones.genera_campo("texto", "tercero_telefono_movil", id, atributos_base, atributos)
}

const fax = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo" : 'Fax',
        "longitud": 60, 
    };
    
    return forma_definiciones.genera_campo("texto", "tercero_fax", id, atributos_base, atributos)
}

const ciudad = function(id=null, atributos={}) {
    let atributos_base = {
        'titulo'            : 'Ciudad', 
        "fuente"            : "ciudades", 
        "obligatorio"       : true,
        "busqueda_expresion": "nombre_completo",
        "muestra_expresion" : "nombre_completo",        
    };
    
    return forma_definiciones.genera_campo("seleccion", "tercero_ciudad_id", id, atributos_base, atributos)
}

let tercero_campos_consulta = [
    {
        "id"    : "tercero_clase",
        "titulo": "Clase",
    },
    {
        "id"    : "tercero_tipo_tercero_nombre",
        "titulo": "Tipo",
    },
    {
        "id"    : "tercero_tipo_identificacion_nombre",
        "titulo": "Tipo identificación",
    },
    {
        "id"    : "tercero_nro_identificacion",
        "titulo": "Nit/Nro identificación",
    },
    {
        "id"    : "tercero_razon_social",
        "titulo": "Razón social",
    },
    {
        "id"    : "tercero_nombres",
        "titulo": "Nombres",
    },
    {
        "id"    : "tercero_apellidos",
        "titulo": "Apellidos",
    },
    {
        "id"    : "tercero_cargo",
        "titulo": "Cargo",
    },
    {
        "id"    : "tercero_correo_electronico",
        "titulo": "Correo electrónico",
    },
    {
        "id"    : "tercero_direccion",
        "titulo": "Dirección",
    },
    {
        "id"    : "tercero_telefono",
        "titulo": "Telefono",
    },
    {
        "id"    : "tercero_telefono_movil",
        "titulo": "Telefono movil",
    },
    {
        "id"    : "tercero_fax",
        "titulo": "Fax",
    },
    {
        "id"    : "tercero_codigo_postal",
        "titulo": "Codigo postal",
    },
    {
        "id"    : "tercero_ciudad_nombre",
        "titulo": "Ciudad",
    }
]

export default {
    tipo_tercero_id      : tipo_tercero_id,
    clase_tercero        : clase_tercero,
    busca_remitente      : busca_remitente,
    tipo_identificacion  : tipo_identificacion,
    nro_identificacion   : nro_identificacion,
    razon_social         : razon_social,
    nombres              : nombres,
    apellidos            : apellidos,
    correo_electronico   : correo_electronico,
    cargo                : cargo,
    direccion            : direccion,
    codigo_postal        : codigo_postal,
    telefono             : telefono,
    telefono_movil       : telefono_movil,
    fax                  : fax,
    ciudad               : ciudad,

    tercero_campos_consulta: tercero_campos_consulta
}