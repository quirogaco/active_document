import forma_objeto          from '../../forma/utilidades/forma_objeto.js';
import utilidades_estructura from '../../../../librerias/utilidades_estructura.js';
import dialogos              from '../../../../librerias/dialogos.js';

let mostrar_todos = function(forma_id, campos_basicos) {
    $lib.forma_atributo_items(forma_id, campos_basicos, "visible", true, false); 
}

let carga_forma = function(forma, datos_forma) {
    forma.beginUpdate()
    forma.option("formData", datos_forma)   
    forma.endUpdate()
}

let ocultar_campos = function(forma_id, campos_basicos) {
    console.log("OCULTA CAMPOS:", forma_id, campos_basicos)
    $lib.forma_atributo_items(forma_id, campos_basicos, "visible", false, false); 
}

// PQRS
let campos_basicos_pqrs = [
    "gestion_dependencia_id",
    "gestion_peticion_id",
    "gestion_horas_dias",
    "gestion_total_tiempo",
    "gestion_prioridad",
    "reserva",
    "copia_usuarios_id",
    "copia_grupos_id",
]
let valor_anterior_pqrs = null
let pqrs = function(forma_id) {
    return forma_objeto.radio_objeto({
        "campo"      : "pqrs",
        "titulo"     : "Es PQRS", 
        "elementos"  : ["SI", "NO"],    
        'obligatorio': 'si',
        "registrar"  : "si",
        "eventos"           : {
            "seleccion_cambiada": function(objeto) { 
                let forma       = $lib.traer_componentes(forma_id).formaInstancia 
                let datos_forma = forma.option("formData")
                let valor       = objeto.value    
                if (valor_anterior_pqrs != valor) {  
                    // Estado inicial
                    mostrar_todos(forma_id, campos_basicos_pqrs)
                    
                    // Cambia campos visuales                
                    switch (valor) {
                        case "NO":  
                            break
            
                        case "SI":
                            // Ocultar                     
                            ocultar_campos(forma_id, campos_basicos_pqrs)
                            break
                    }       
                    forma.repaint()       
                    // Carga datos
                    carga_forma(forma, datos_forma)                     
                    $lib.traer_componentes(forma_id, "pqrs").focus()
                }
                valor_anterior_pqrs = valor                                   
            }
        }
    })
}

// VENTANILLA
let valor_anterior_ventanilla = null
let campos_basicos_ventanilla = [
    "gestion_dependencia_id",
    "gestion_peticion_id",
    "gestion_horas_dias",
    "gestion_total_tiempo",
    "gestion_prioridad",
    "reserva",
    "copia_usuarios_id",
    "copia_grupos_id",
    "tema_dependencia_radica_id",
    "subtema_dependencia_radica_id",
]
let ventanilla = function(forma_id) {
    return forma_objeto.radio_objeto({
        "campo"      : "ventanilla",
        "titulo"     : "Es documento ventanilla", 
        "elementos"  : ["SI", "NO"],    
        'obligatorio': 'si',
        "registrar"  : "si",
        "eventos"           : {
            "seleccion_cambiada": function(objeto) {   
                let forma       = $lib.traer_componentes(forma_id).formaInstancia 
                let datos_forma = forma.option("formData")
                let valor       = objeto.value    
                if (valor_anterior_ventanilla != valor) {  
                    // Estado inicial
                    mostrar_todos(forma_id, campos_basicos_ventanilla)
                    
                    // Cambia campos visuales                
                    switch (valor) {
                        case "NO":  
                            break
            
                        case "SI":
                            // Ocultar                     
                            ocultar_campos(forma_id, campos_basicos_ventanilla) 
                            break
                    }       
                    forma.repaint()       
                    // Carga datos
                    carga_forma(forma, datos_forma)                     
                    $lib.traer_componentes(forma_id, "ventanilla").focus()
                }
                valor_anterior_ventanilla = valor                                   
            }
        }
    })
}

let dependencia_id = forma_objeto.select_objeto({
    "campo"      : "gestion_dependencia_id",
    "titulo"     : "Dependencia", 
    "fuente"     : "dependencias",
    "busqueda_expresion": "nombre_completo",
    "muestra_expresion" : "nombre_completo",
    "registrar"         : "si",
    'obligatorio': 'si',
    "filtros"    : [["estado_", "=", "ACTIVO"]],
    "eventos"           : {
        "seleccion_cambiada": async function(objeto) {
            let forma_id   = "ventanilla_radicado_forma"      
            // Dato seleccionado
            let id         = $lib.cargaAtributo(objeto.selectedItem, 'id', null); 
            let datos      = await utilidades_estructura.leer_registro_id("dependencias", id);              
            // Carga información
            if (datos != null) {  
                // Limpia NO_BUSCAR
                if ( $lib.sin_valor.indexOf(datos.archivo_id) > -1 ) {        
                    dialogos.miMensaje("Información incompleta", (
                        datos.nombre_completo + " - " +  "No tiene responsable de manejo de Archivo"
                    ))
                    $lib.forma_componente_opcion(forma_id, "gestion_dependencia_id", "value", null) 
                }                                                  
            }
        }
    }
})

// ********************** //
// FORMA ASIGNACION PQRS //
// ********************** //
// PQRS campos especificos
// Dependencia responsable
let dependencia_pqrs = forma_objeto.select_objeto({
    "titulo"            : "Dependencia responsable", 
    "fuente"            : "dependencias",
    "campo"             : "gestion_dependencia_id",
    "busqueda_expresion": "nombre_completo",
    "muestra_expresion" : "nombre_completo",
    "registrar"         : "si",
    "obligatorio"       : "si",  
    "eventos"           : {
        "seleccion_cambiada": async function(objeto) {
            let forma_id   = "asignar_pqrs_forma"      
            // Dato seleccionado
            let id         = $lib.cargaAtributo(objeto.selectedItem, 'id', null); 
            let datos      = await utilidades_estructura.leer_registro_id("dependencias", id);  
            
            // Limpia temas y subtemas
            $lib.forma_componentes_opcion(forma_id, ["tema_dependencia_id", "subtema_dependencia_id"], "value", null)    
                        
            // Fuentes tema y subtema
            let tds = $lib.traer_fuente_datos(forma_id, "tema_dependencia_id")
            let sds = $lib.traer_fuente_datos(forma_id, "subtema_dependencia_id");            
            // Limpia los datos de tema y subtema   
            tds.searchOperation("NO_BUSCAR")
            sds.searchOperation("NO_BUSCAR")            
            // Carga información
            if (datos != null) {  
                // Limpia NO_BUSCAR
                tds.searchOperation("") 
                sds.searchOperation("")          
                if ( $lib.sin_valor.indexOf(datos.pqrs_id) > -1 ) {        
                    dialogos.miMensaje("Información incompleta", (
                        datos.nombre_completo + " - " +  "No tiene responsable de manejo de PQRS/VENTANILLA"
                    ))
                    $lib.forma_componente_opcion(forma_id, "gestion_dependencia_id", "value", null) 
                } 
                else{
                    // Fitro de tema
                    tds.filter(["dependencia_id", "=", id])                    
                }                                  
            }    

            // Carga datos
            tds.reload()
            sds.reload()
        }
    }
})

// Tema Dependencia
let tema_dependencia  = forma_objeto.select_objeto({
    "titulo"            : "Tema de la dependencia", 
    "fuente"            : "temas",
    "campo"             : "tema_dependencia_id",
    "registrar"         : "si",
    "obligatorio"       : "si",  
    "eventos"           : {
        "seleccion_cambiada": async function(objeto) {
            // Dato seleccionado tema
            let id = $lib.cargaAtributo(objeto.selectedItem, 'id', null)                
            // Carga datos Subtema
            let sds = $lib.traer_fuente_datos("asignar_pqrs_forma", "subtema_dependencia_id")  
            sds.searchOperation("NO_BUSCAR")            
            if (id != null) {
                sds.searchOperation("")          
                sds.filter(["tema_id", "=", id])       
            }
            sds.reload()

            // Subtemas
            $lib.forma_componentes_opcion("asignar_pqrs_forma", ["subtema_dependencia_id"], "value", null)                                               
        }
    }
})

// SubTema Dependencia
let subtema_dependencia  = forma_objeto.select_objeto({
    "titulo"            : "Subtema de la dependencia", 
    "fuente"            : "subtemas",
    "campo"             : "subtema_dependencia_id",
    "nombre"            : "subtema_dependencia_id",
    "registrar"         : "si",
    "obligatorio"       : "si",  
    "eventos"           : {}
})

// ******************** //
// FORMA RADICADO PQRS //
// ******************* //

let dependencia_pqrs_radica = forma_objeto.select_objeto({
    "titulo"            : "Dependencia responsable", 
    "fuente"            : "dependencias",
    "campo"             : "gestion_dependencia_id",
    "busqueda_expresion": "nombre_completo",
    "muestra_expresion" : "nombre_completo",
    "registrar"         : "si",
    "obligatorio"       : "si",  
    "eventos"           : {
        "seleccion_cambiada": async function(objeto) {
            let forma_id = "pqrs_radicado_forma"    
            // Dato seleccionado
            let id         = $lib.cargaAtributo(objeto.selectedItem, 'id', null); 
            let datos      = await utilidades_estructura.leer_registro_id("dependencias", id);  
            
            // Limpia temas y subtemas
            $lib.forma_componentes_opcion(forma_id, ["tema_dependencia_radica_id", "subtema_dependencia_radica_id"], "value", null)    
                        
            // Fuentes tema y subtema
            let tds = $lib.traer_fuente_datos(forma_id, "tema_dependencia_radica_id")
            let sds = $lib.traer_fuente_datos(forma_id, "subtema_dependencia_radica_id");            
            // Limpia los datos de tema y subtema   
            tds.searchOperation("NO_BUSCAR")
            sds.searchOperation("NO_BUSCAR")            
            // Carga información
            if (datos != null) {  
                // Limpia NO_BUSCAR
                tds.searchOperation("") 
                sds.searchOperation("")          
                if ( $lib.sin_valor.indexOf(datos.pqrs_id) > -1 ) {        
                    dialogos.miMensaje("Información incompleta", (
                        datos.nombre_completo + " - " +  "No tiene responsable de manejo de PQRS"
                    ))
                    $lib.forma_componente_opcion(forma_id, "gestion_dependencia_id", "value", null) 
                } 
                else{
                    // Fitro de tema
                    tds.filter(["dependencia_id", "=", id])                    
                }                                  
            }    

            // Carga datos
            tds.reload()
            sds.reload()
        }
    }
})

// Tema Dependencia
let tema_dependencia_radica = forma_objeto.select_objeto({
    "titulo"            : "Tema de la dependencia", 
    "fuente"            : "temas",
    "campo"             : "tema_dependencia_radica_id",
    "registrar"         : "si",
    "obligatorio"       : "si",  
    "eventos"           : {
        "seleccion_cambiada": async function(objeto) {
            let forma_id = "pqrs_radicado_forma"  
            // Dato seleccionado tema
            let id = $lib.cargaAtributo(objeto.selectedItem, 'id', null)                
            // Carga datos Subtema
            let sds = $lib.traer_fuente_datos(forma_id, "subtema_dependencia_radica_id")  
            sds.searchOperation("NO_BUSCAR")            
            if (id != null) {
                sds.searchOperation("")          
                sds.filter(["tema_id", "=", id])       
            }
            sds.reload()

            // Subtemas
            $lib.forma_componentes_opcion(forma_id, ["subtema_dependencia_radica_id"], "value", null)                                               
        }
    }
})

// SubTema Dependencia
let subtema_dependencia_radica  = forma_objeto.select_objeto({
    "titulo"            : "Subtema de la dependencia", 
    "fuente"            : "subtemas",
    "campo"             : "subtema_dependencia_radica_id",
    "nombre"            : "subtema_dependencia_radica_id",
    "registrar"         : "si",
    "obligatorio"       : "si",  
    "eventos"           : {}
})

// PQRS Termina

let valor_anterior = null
const actualiza_forma = function(forma, datos_forma, valor, horas_dias, total_tiempo) {
    datos_forma["gestion_peticion_id"]  = valor  
    datos_forma["gestion_horas_dias"]   = horas_dias  
    datos_forma["gestion_total_tiempo"] = total_tiempo    
    forma.option("formData", datos_forma)      
}

let valores_peticion = function(forma_id, objeto) {
    let forma = $lib.traer_componentes(forma_id).formaInstancia         
    let valor = objeto.component.option("value") 
    if (valor_anterior != valor) {  
        // Limpia valores, horas_dias, total_tiempo
        $lib.traer_componentes(forma_id, "gestion_horas_dias").option("value", null)      
        $lib.traer_componentes(forma_id, "gestion_total_tiempo").option("value", null)     

        // Datos
        let datos_forma = JSON.parse( JSON.stringify(forma.option("formData")) ) // Convierte proxy a objeto simple                                                   
        let peticion    = objeto.selectedItem       

        forma.beginUpdate()
        if (peticion !== null) {                                                                                                                                                                                             
            let deshabilita = peticion.modifica_tiempo == "SI" ? false : true 
            $lib.forma_atributo_items(forma_id, ["gestion_horas_dias", "gestion_total_tiempo"], "disabled", deshabilita)
            actualiza_forma(forma, datos_forma, valor, peticion.horas_dias, peticion.total_tiempo )
        }
        else {
            $lib.forma_atributo_items(forma_id, ["gestion_horas_dias", "gestion_total_tiempo"], "disabled", true)
            actualiza_forma(forma, datos_forma, valor, null, null)                       
        }        
        forma.endUpdate()  
                        
        $lib.traer_componentes(forma_id, "gestion_peticion_id").focus()                   
    } 
    valor_anterior = valor 
}

let peticion_id_pqrs = function(forma_id) {
    return forma_objeto.select_objeto({
        "titulo"     : "Tipo de petición", 
        "fuente"     : "tipo_peticiones",
        "campo"      : "gestion_peticion_id",
        "registrar"  : "si",
        "obligatorio": "si",  
        "filtros"   : [
            ["estado_", "=", "ACTIVO"], 
            ["pqrs", "=", "si"]
        ],
        "eventos"           : {
            "seleccion_cambiada": function(objeto) { 
                valores_peticion(forma_id, objeto)                
            }        
        }
    })
}

let peticion_id = function(forma_id) {
    return forma_objeto.select_objeto({
        "titulo"     : "Tipo de petición", 
        "fuente"     : "tipo_peticiones",
        "campo"      : "gestion_peticion_id",
        "registrar"  : "si",
        "obligatorio": "si",  
        "filtros"   : [
            ["estado_", "=", "ACTIVO"], 
            ["pqrs", "=", "no"]
        ],
        "eventos"           : {
            "seleccion_cambiada": function(objeto) { 
                valores_peticion(forma_id, objeto)                
            }        
        }
    })
}

let horas_dias  = forma_objeto.radio_objeto({
    "campo"      : "gestion_horas_dias",
    "titulo"     : "Plazo en", 
    "elementos"  : ["DIAS", "HORAS"],    
    'obligatorio': 'si',
    "registrar"  : "si"    
})

let total_tiempo = forma_objeto.campo_objeto({
    'campo'      : 'gestion_total_tiempo',
    'tipo'       : "dxNumberBox",
    'titulo'     : 'Plazo para contestar',  
    'valor'      : 0,
    'obligatorio': 'si',
    "registrar"  : "si"        
})

let prioridad = forma_objeto.radio_objeto({
    "campo"      : "gestion_prioridad",
    "titulo"     : "Prioridad", 
    "elementos"  : ["ALTA", "MEDIA", "BAJA"],    
    "valor"      : "MEDIA",
    'obligatorio': 'si',
    "registrar"  : "si"    
})

let reserva = forma_objeto.radio_objeto({
    "campo"      : "reserva",
    "titulo"     : "Reserva", 
    "elementos"  : ["SI", "NO"],   
    "valor"      : "NO", 
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

export default {
    pqrs                   : pqrs,
    ventanilla             : ventanilla,
    dependencia_id         : dependencia_id,
    
    // PQRS ASIGNA
    dependencia_pqrs       : dependencia_pqrs,
    tema_dependencia       : tema_dependencia,
    subtema_dependencia    : subtema_dependencia,
    
    // PQRS RADICA
    dependencia_pqrs_radica   : dependencia_pqrs_radica,
    tema_dependencia_radica   : tema_dependencia_radica,
    subtema_dependencia_radica: subtema_dependencia_radica,
    

    peticion_id            : peticion_id,
    peticion_id_pqrs       : peticion_id_pqrs,
    horas_dias             : horas_dias,
    total_tiempo           : total_tiempo,
    prioridad              : prioridad,
    reserva                : reserva,
    copia_usuarios_id      : copia_usuarios_id,
    copia_grupos_id        : copia_grupos_id
}