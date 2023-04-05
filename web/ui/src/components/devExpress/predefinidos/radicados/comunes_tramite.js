import forma_objeto      from '../../forma/utilidades/forma_objeto.js';

let dependencia_id = forma_objeto.select_objeto({
    "campo"      : "gestion_dependencia_id",
    "titulo"     : "Dependencia", 
    "fuente"     : "dependencias",
    'obligatorio': 'si',
    "filtros"    : [["estado_", "=", "ACTIVO"]]
})

let valor_anterior = null
const actualiza_forma = function(forma, datos_forma, valor, horas_dias, total_tiempo) {
    datos_forma["gestion_peticion_id"]  = valor  
    datos_forma["gestion_horas_dias"]   = horas_dias  
    datos_forma["gestion_total_tiempo"] = total_tiempo    
    forma.option("formData", datos_forma)      
}

let peticion_id = forma_objeto.select_objeto({
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
            let forma_id = "ventanilla_radicado_forma"                    
            let forma    = $lib.traer_componentes(forma_id).formaInstancia         
            let valor    = objeto.component.option("value") 
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
    }
})

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
    dependencia_id   : dependencia_id,
    peticion_id      : peticion_id,
    horas_dias       : horas_dias,
    total_tiempo     : total_tiempo,
    prioridad        : prioridad,
    reserva          : reserva,
    copia_usuarios_id: copia_usuarios_id,
    copia_grupos_id  : copia_grupos_id
}