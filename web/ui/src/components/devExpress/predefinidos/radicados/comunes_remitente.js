import forma_objeto      from '../../forma/utilidades/forma_objeto.js';

let forma_id = "ventanilla_radicado_forma"

let busca_remitente = forma_objeto.select_objeto({
    "titulo"            : "Buscar remitente", 
    "fuente"            : "terceros",
    "nombre"            : "busca_remitente",
    "busqueda_expresion": "nombre_completo",
    "muestra_expresion" : "nombre_completo",    
    "registrar"  : "si",
    "eventos"           : {
        "seleccion_cambiada": async function(objeto) {            
            let id    = $lib.cargaAtributo(objeto.selectedItem, 'id', null); 
            let datos = await utilidades_estructura.leer_registro_id("terceros", id);
            if (datos != null) {
                // Carga información del tercero
                let atributos = [
                    "nro_identificacion",
                    "razon_social",
                    "apellidos",
                    "nombres",
                    "direccion",
                    "correo_electronico",
                    "codigo_postal",
                    "telefono",
                    "telefono_movil",
                    "fax",
                    "ciudad_id"
                ]
                let campos = $lib.traer_componentes("ventanilla_radicado_forma",  atributos);                
                for (let atributo of atributos) {                    
                    campos[atributo].option("value", datos[atributo]);       
                }                
            }                        
        }
    }
}) 

let campos_basicos = [
    "busca_remitente",
    "tercero_tipo_tercero_id",
    "tercero_tipo_identificacion_id",
    "tercero_nro_identificacion",        
    "tercero_razon_social",
    "tercero_nombres",
    "tercero_apellidos",     
    "tercero_cargo",                   
    "tercero_direccion",
    "tercero_correo_electronico",
    "tercero_codigo_postal",
    "tercero_telefono",
    "tercero_telefono_movil",
    "tercero_fax",
    "tercero_ciudad_id"
]

let mostrar_todos = function() {
    $lib.forma_atributo_items(forma_id, campos_basicos, "visible", true, false); 
}

let limpiar_todos = function() {
    $lib.forma_componentes_opcion(forma_id, campos_basicos, "value", null); 
}

let marcar_obligatorios = function() {
    // Obligatorios
    let campos_obligatorios = [
        "tercero_razon_social",
        "tercero_nombres",
        "tercero_apellidos",                        
        "tercero_ciudad_id"
    ]    
    // Reglas validacion   
    let nombre, valor_atributo;                 
    for (const indice in campos_obligatorios) {
        nombre         = campos_obligatorios[indice]
        valor_atributo = window.atributos_campos[forma_id][nombre]
        $lib.forma_atributo_item(forma_id, nombre, "validationRules", valor_atributo, false); 
    }       

    // Requerido
    $lib.forma_atributo_items(forma_id, campos_obligatorios, "isRequired", true, false); 
}

let marcar_no_obligatorios = function(campos_no_obligatorios) {    
    // Reglas validacion   
    let nombre, valor_atributo;                 
    for (const indice in campos_no_obligatorios) {
        nombre         = campos_no_obligatorios[indice]
        valor_atributo = window.atributos_campos[forma_id][nombre]
        $lib.forma_atributo_item(forma_id, nombre, "validationRules", null, false); 
    }
    
    // Requerido
    $lib.forma_atributo_items(forma_id, campos_no_obligatorios, "isRequired", false, false); 
}

let ocultar_campos = function(campos_no_visibles) {
    $lib.forma_atributo_items(forma_id, campos_no_visibles, "visible", false, false); 
}

let carga_forma = function(forma, datos_forma) {
    forma.beginUpdate()
    forma.option("formData", datos_forma)   
    forma.endUpdate()
}

let valor_anterior = null
let clase_remitente = forma_objeto.radio_objeto({
    "campo"      : "tercero_clase",
    "titulo"     : "Clase remitente", 
    "elementos"  : ["JURIDICA", "NATURAL", "ANONIMO"],    
    'obligatorio': 'si',
    "registrar"  : "si",
    "eventos"           : {
        "seleccion_cambiada": function(objeto) {            
            let forma       = $lib.traer_componentes(forma_id).formaInstancia 
            let datos_forma = forma.option("formData")
            let valor       = objeto.value    
            if (valor_anterior != valor) {               
                // Estado inicial
                mostrar_todos()
                limpiar_todos()
                marcar_obligatorios()
                
                // Cambia campos visuales                
                switch (valor) {
                    case "JURIDICA":  
                        // NO obligatorios
                        marcar_no_obligatorios(["tercero_direccion", "tercero_nombres", "tercero_apellidos"])
                        // Ocultar                     
                        ocultar_campos(["tercero_tipo_identificacion_id"])      
                        break
        
                    case "NATURAL":
                        // NO obligatorios
                        marcar_no_obligatorios(["tercero_razon_social", "tercero_direccion", "tercero_correo_electronico"])   
                        // Ocultar                     
                        ocultar_campos(["tercero_razon_social", "tercero_cargo"]) 
                        break
        
                    case "ANONIMO":                        
                        mostrar_todos()

                        // NO obligatorios
                        let campos_no_obligatorios = [
                            "tercero_nro_identificacion",
                            "tercero_razon_social",
                            "tercero_nombres",
                            "tercero_apellidos",                        
                            "tercero_direccion",
                            "tercero_correo_electronico",
                            "tercero_codigo_postal",
                            "tercero_telefono",
                            "tercero_telefono_movil",
                            "tercero_fax",
                            "tercero_ciudad_id"                   
                        ]
                        marcar_no_obligatorios(campos_no_obligatorios)                                     
                        // Ocultar           
                        let campos_no_visibles = [
                            "busca_remitente",
                            "tercero_tipo_tercero_id",
                            "tercero_tipo_identificacion_id",
                            "tercero_nro_identificacion",
                            "tercero_razon_social",
                            "tercero_nombres",
                            "tercero_apellidos", 
                            "tercero_cargo",                       
                            "tercero_direccion",
                            "tercero_codigo_postal",
                            "tercero_telefono",
                            "tercero_telefono_movil",
                            "tercero_fax",
                            "tercero_ciudad_id"                                  
                        ]
                        ocultar_campos(campos_no_visibles)
                        break
                }       
                forma.repaint()       
                // Carga datos
                carga_forma(forma, datos_forma)                     
                $lib.traer_componentes(forma_id, "tercero_clase").focus()   
                
                // Filtro tipo remitente
                // Despues de escondido e inhabilitado no funciona
                // Debe ir aqui carga_forma limpia el filtro
                try {
                    let ds = $lib.traer_fuente_datos(forma_id, "tercero_tipo_tercero_id")
                    ds.filter(["tipo", "=", valor])
                }
                catch {}     
            }
            valor_anterior = valor                                   
        }
    }
})

let tipo_tercero_id = forma_objeto.select_objeto({
    "campo"      : "tercero_tipo_tercero_id",
    "titulo"     : "Tipo de remitente", 
    "obligatorio": "si",    
    "fuente"     : "tipo_terceros",    
    "registrar"  : "si",
})

let tipo_identificacion_id = forma_objeto.select_objeto({
    "campo"      : "tercero_tipo_identificacion_id",
    "titulo"     : "Tipo de identificación", 
    "obligatorio": "si",    
    "fuente"     : "tipo_identificaciones",
    "registrar"  : "si",
})

let nro_identificacion = forma_objeto.campo_objeto({
    'campo'      : 'tercero_nro_identificacion',
    'titulo'     : 'Número de identificación',
    'obligatorio': 'si',             
    'maximo'     : 64,
    "registrar"  : "si",
})

let nit_nro_identificacion = forma_objeto.campo_objeto({
    'campo'      : 'tercero_nro_identificacion',
    'titulo'     : 'Nit / Número de identificación',
    //'obligatorio': 'si',             
    'maximo'     : 64,
    "registrar"  : "si",
})

let razon_social = forma_objeto.campo_objeto({
    'campo'      : 'tercero_razon_social',
    'titulo'     : 'Razon social',
    "registrar"  : "si",        
    'obligatorio': 'si',
    'maximo'     : 256
})

let cargo = forma_objeto.campo_objeto({
    'campo'      : 'tercero_cargo',
    'titulo'     : 'Cargo',
    "registrar"  : "si",        
    'maximo'     : 128
})

let nombres = forma_objeto.campo_objeto({
    'campo'      : 'tercero_nombres',
    'titulo'     : 'Nombres remitente',
    'obligatorio': 'si',
    'maximo'     : 128,
    "registrar"  : "si",
})

let apellidos = forma_objeto.campo_objeto({
    'campo'      : 'tercero_apellidos',
    'titulo'     : 'Apellidos remitente',
    'obligatorio': 'si',
    'maximo'     : 128,
    "registrar"  : "si",
})

let correo_electronico = forma_objeto.campo_objeto({
    'campo'      : 'tercero_correo_electronico',
    'titulo'     : 'Correo electrónico',
    //'obligatorio': 'si',
    'modo'       : 'email',
    'maximo'     : 128,
    "registrar"  : "si",
})

let direccion = forma_objeto.campo_objeto({
    'campo'      : 'tercero_direccion',
    'titulo'     : 'Dirección',
    'obligatorio': 'si',
    'maximo'     : 128,
    "registrar"  : "si",
})

let codigo_postal = forma_objeto.campo_objeto({
    'campo'      : 'tercero_codigo_postal',
    'titulo'     : 'Codigo postal',
    "registrar"  : "si",        
    'maximo'     : 64,
    "registrar"  : "si",  
})

let telefono = forma_objeto.campo_objeto({
    'campo'      : 'tercero_telefono',
    'titulo'     : 'Telefono',    
    'maximo'     : 64,
    "registrar"  : "si",
})

let telefono_movil = forma_objeto.campo_objeto({
    'campo'      : 'tercero_telefono_movil',
    'titulo'     : 'Telefono movil',
    'maximo'     : 64,
    "registrar"  : "si",
})

let fax = forma_objeto.campo_objeto({
    'campo'      : 'tercero_fax',
    'titulo'     : 'Fax',
    'maximo'     : 64,
    "registrar"  : "si",
})

let ciudad_id = forma_objeto.select_objeto({
    "campo"             : "tercero_ciudad_id",
    "busqueda_expresion": "nombre_completo",
    "muestra_expresion" : "nombre_completo",
    "obligatorio"       : "si",
    "titulo"            : "Ciudad", 
    "fuente"            : "ciudades",
    "registrar"         : "si",
})

export default {
    busca_remitente       : busca_remitente,
    clase_remitente       : clase_remitente,
    tipo_tercero_id       : tipo_tercero_id,
    nit_nro_identificacion: nit_nro_identificacion,
    tipo_identificacion_id: tipo_identificacion_id,
    razon_social          : razon_social,
    cargo                 : cargo,
    nombres               : nombres,
    apellidos             : apellidos,
    correo_electronico    : correo_electronico,
    direccion             : direccion,
    codigo_postal         : codigo_postal,
    telefono              : telefono,
    telefono_movil        : telefono_movil,
    fax                   : fax,
    ciudad_id             : ciudad_id
}