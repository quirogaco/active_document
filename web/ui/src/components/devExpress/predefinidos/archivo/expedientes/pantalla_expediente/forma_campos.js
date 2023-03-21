import forma_definiciones from "../../../comunes_vue/forma/forma.js"

let items_basicos = [
    {
        "id": "id",
        "lectura": true,
        "visible": false
    },

    {
        "componente": "campo",
        "tipo": "seleccion",
        "id": "dependencia_id",
        "titulo": "Dependencia", 
        "fuente": "agn_dependencia_trd", 
        "filtros_fuente": ["estado_", "=", "ACTIVO"],
        "muestra_expresion": "nombre_largo",
        "muestra_valor": "nombre_largo",
        "busqueda_expresion": "nombre_largo",
        "obligatorio": true,
        "eventos"           : {
            "seleccion_cambiada": function(campo, definicion, forma, forma_id) { 
                let datos = campo.selectedItem;                  
                if (datos != null) {                        
                    let filtros = ["dependencia_id", "=", datos.id];                                  
                    if (window.$pantalla_expediente.consulta == false) {                                            
                        forma_definiciones.limpia_campos(forma, ["serie_id"]) 
                        forma_definiciones.asigna_fuente_datos(forma, "serie_id", "select", "agn_serie_trd", filtros, {})        
                    }      
                };                   
            }
        }

    },

    {
        "componente": "campo",
        "tipo": "seleccion",
        "id": "serie_id",
        "titulo": "Serie", 
        "fuente": "agn_serie_trd", 
        "filtros_fuente": ["estado_", "=", "ACTIVO"],
        "muestra_expresion": "nombre",
        "muestra_valor": "nombre",
        "busqueda_expresion": "nombre",
        "obligatorio": true,
        "eventos"           : {
            "foco_entra": function(campo, definicion, forma, forma_id) {                 
                let filtros = ["serie_id", "=", ".."];
                let dependencia_id = forma_definiciones.lee_valor(forma, "dependencia_id")
                console.log("FOCO->dependencia_id:", dependencia_id);                           
            },

            "seleccion_cambiada": function(campo, definicion, forma, forma_id) { 
                let filtros = ["serie_id", "=", ".."];     
                let datos = campo.selectedItem;
                window.$pantalla_expediente.serie_id = null;
                if (datos != null) {                        
                     filtros = ["serie_id", "=", datos.id];
                    window.$pantalla_expediente.serie_id = datos.id;
                    if (window.$pantalla_expediente.consulta == false) {    
                        forma_definiciones.limpia_campos(forma, ["subserie_id"])                                                                                            
                        forma_definiciones.asigna_fuente_datos(forma, "subserie_id", "select", "agn_subserie_trd", filtros, {})        
                    }    
                }                
            }
        }

    },

    {
        "componente": "campo",
        "tipo": "seleccion",
        "id": "subserie_id",
        "titulo": "Subserie", 
        "fuente": "agn_subserie_trd", 
        "filtros_fuente": ["estado_", "=", "ACTIVO"],
        "muestra_expresion": "nombre",
        "muestra_valor": "nombre",
        "busqueda_expresion": "nombre",
       // "obligatorio": true,
        "eventos"           : {
            "seleccion_cambiada": function(campo, definicion, forma, forma_id) {
                let datos = campo.selectedItem;
                window.$pantalla_expediente.subserie_id = null;
                if (datos != null) {
                    window.$pantalla_expediente.subserie_id = datos.id;
                }
            }
        }

    },

    {
        "componente" : "campo",
        "tipo": "texto",
        "id": "nombre",
        "titulo": "Nombre expediente", 
        "obligatorio": true,
        "longitud": 250,
        "ancho": 320
    },

    {
        "componente" : "campo",
        "tipo": "texto",
        "id": "caja",
        "titulo": "Caja", 
        "longitud": 50,
        "ancho": 150
    },

    {
        "componente" : "campo",
        "tipo": "texto",
        "id": "ubicacion_topografica",
        "titulo": "Ubicación topografica", 
        "longitud": 50,
        "ancho": 200
    },

    {
        "componente" : "campo",
        "tipo": "texto_area",
        "id": "observacion",
        "titulo": "Observaciones"
    }
];

let grupo_basico = {
    "tipo": 'grupo',
    'elementos': items_basicos
}


let items_general = [
    {
        "id": "carpetas",
        "titulo": "Carpetas", 
        "ancho": 320,
        "lectura": true
    },

    {
        "id": "total_documentos",
        "titulo": "Numero de registros", 
        "ancho": 320,
        "lectura": true
    },

    {
        "id": "folios_fisicos",
        "titulo": "Folios fisicos", 
        "ancho": 320,
        "lectura": true
    },

    {
        "id": "folios_electronicos",
        "titulo": "Folios electronicos", 
        "ancho": 320,
        "lectura": true
    },

    {
        "id": "etapa",
        "titulo": "Etapa de archivo", 
        "ancho": 320,
        "lectura": true
    },

    {
        "id": "estado",
        "titulo": "Estado", 
        "ancho": 320,
        "lectura": true
    },

    {
        "id": "acceso_modo",
        "titulo": "Acceso", 
        "ancho": 320,
        "lectura": true
    },

    {
        "id": "tipo_expediente",
        "titulo": "Tipo de expediente", 
        "ancho": 320,
        "lectura": true
    },

    {
        "id": "ubicacion",
        "titulo": "Ubicación expediente", 
        "ancho": 320,
        "lectura": true
    },

    {
        "id": "disposicion_aplicada",
        "titulo": "Disposición final", 
        "ancho": 320,
        "lectura": true
    }
    // 
];

let grupo_general = {
    "tipo": 'grupo',
    'elementos': items_general
}


let items_especifico = [
    {
        "id": "fecha_inicial",
        "titulo": "Fecha inicial", 
        "ancho": 320,
        "lectura": true
    },

    {
        "id": "fecha_final",
        "titulo": "Fecha final", 
        "ancho": 320,
        "lectura": true
    },

    {
        "id": "anos_gestion",
        "titulo": "Años en gestión", 
        "ancho": 320,
        "lectura": true
    },

    {
        "id": "vence_gestion",
        "titulo": "Gestión vence", 
        "ancho": 320,
        "lectura": true
    },

    {
        "id": "anos_central",
        "titulo": "Años en Central", 
        "ancho": 320,
        "lectura": true
    },

    {
        "id": "vence_central",
        "titulo": "Central vence", 
        "ancho": 320,
        "lectura": true
    },

    {
        "id": "seleccion",
        "titulo": "Selección", 
        "ancho": 320,
        "lectura": true
    },

    {
        "id": "eliminacion",
        "titulo": "Eliminación", 
        "ancho": 320,
        "lectura": true
    },

    {
        "id": "conservacion",
        "titulo": "Conservación", 
        "ancho": 320,
        "lectura": true
    },

    {
        "id": "micro_digitalizacion",
        "titulo": "Medio técnico", 
        "ancho": 320,
        "lectura": true
    }
];

let grupo_especifico = {
    "tipo": 'grupo',
    'elementos': items_especifico
}


const get_items = function() {
    //return items_basicos
    return [
        grupo_basico,
        grupo_general,
        grupo_especifico
    ]
}

export default {
    items: get_items
}