import forma_definiciones     from "../../../comunes_vue/forma/forma.js"
import campos_basicos_comunes from "../../../comunes_vue/forma/campos_basicos_comunes.js"
import basicos_definiciones   from "../../../radicados_vue/comunes/basicos/basicos_definiciones.js"
import tercero_definiciones   from "../../../radicados_vue/comunes/basicos/tercero_definiciones.js"
import archivo_definiciones   from "../../../radicados_vue/comunes/basicos/archivo_definiciones.js"
import gestion_definiciones   from "../../../radicados_vue/comunes/basicos/gestion_definiciones.js"
import copia_definiciones     from "../../../radicados_vue/comunes/basicos/copia_definiciones.js"
import log_definiciones       from "../../../radicados_vue/comunes/basicos/log_definiciones.js"

let barra_botones = function(forma, basicas) {
    return  [       
        { 
            widget  : "dxButton",           
            options :{ //0
                icon       : 'fas fa-angle-left',
                alignment  : 'center',
                hint       : 'regresar',
                type       : 'normal',  
                text       : 'Regresar',   
                stylingMode: "contained",  
                onClick    : forma.boton_click,
            } 
        } 
    ]              
}


//********************//
// Campos de la forma //
//********************//

// ####### //
// BASICA //
// ####### //
let basico_grupo = function(forma) {
    return forma_definiciones.grupo(
        'basico',        
        {
            "titulo"   : "Información basica",
            "elementos": forma_definiciones.genera_campos_lectura(forma, basicos_definiciones.basicos_campos_consulta)
        }
    )
}

// ######## //
// TERCERO  //
// ######## //
let tercero_grupo = function(forma) {
    return forma_definiciones.grupo(
        'tercero',        
        {
            "titulo"   : "Información de remitente",
            "elementos": forma_definiciones.genera_campos_lectura(forma, tercero_definiciones.tercero_campos_consulta)
        }
    )
}

// ######## //
// ARCHIVOS //
// ######## //
let archivos_grupo = function(forma) {
    return forma_definiciones.grupo(
        'archivos',        
        {
            "titulo"   : "Información de archivos",
            "elementos": [    
                archivo_definiciones.anexos_radicado(null, {forma: forma})                            
            ]
        }
    )
}

// ######## //
// GESTION  //
// ######## //
let gestion_grupo = function(forma) {
    return forma_definiciones.grupo(
        'gestion',        
        {
            "titulo"   : "Información de gestión",
            "elementos": forma_definiciones.genera_campos_lectura(forma, gestion_definiciones.gestion_consulta)
        }
    )
}

// #### //
// LOGS //
// #### //
let logs_grupo = function(forma) {
    return forma_definiciones.grupo(
        'logs',        
        {
            "titulo"   : "Historico",
            "expandir" : 2,
            "elementos": [    
                log_definiciones.logs_radicado(null, {forma: forma})                            
            ]
        }
    )
}

// ###### //
// COPIAS //
// ###### //
let copias_grupo = function(forma) {
    return forma_definiciones.grupo(
        'logs',        
        {
            "titulo"   : "Con copia a",
            "expandir" : 2,
            "elementos": [    
                copia_definiciones.con_copia(null, {forma: forma})                            
            ]
        }
    )
}

// ###### //
// CAMPOS //
// ###### //
const campos_especificos = function(forma, basicas) {
    // Barra de botones
    let campos = {
        "barra_botones": barra_botones(forma, basicas)
    }

    campos["elementos"] =  [
        tercero_grupo(forma),    
        gestion_grupo(forma),             
        archivos_grupo(forma),             
        basico_grupo(forma),   
        logs_grupo(forma),          
        copias_grupo(forma) 
    ]

    return campos
}

let campos_forma = function(forma, basicas) {
    let campos = {
        ...campos_basicos_comunes.campos(forma, basicas),  
        ...campos_especificos(forma, basicas)      
    }

    return campos
} 

export default {
    campos_forma: campos_forma
}