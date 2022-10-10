import forma_definiciones       from "../../comunes_vue/forma/forma.js"
import campos_basicos_comunes   from "../../comunes_vue/forma/campos_basicos_comunes.js"
import archivo_definiciones     from "../../radicados_vue/comunes/basicos/archivo_definiciones.js"
import comentarios_definiciones from "../../radicados_vue/comunes/basicos/comentarios_definiciones.js"
import trd_definiciones         from "../../radicados_vue/comunes/basicos/trd_definiciones.js"

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

// #### //
// TRD  //
// #### //
let trd_grupo = function(forma) {
    return forma_definiciones.grupo(
        'logs',        
        {
            "titulo"   : "Expedientes y tipos documentales (TRD)",
            "expandir" : 2,
            "elementos": [    
                trd_definiciones.expedientes_tipos(null, {forma: forma})                            
            ]
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
            "titulo"   : "Información anexos de gestión",
            "elementos": [    
                archivo_definiciones.anexos_radicado(null, {forma: forma})                            
            ]
        }
    )
}

// ######## //
// GESTIÓN //
// ####### //
let comentarios_grupo = function(forma) {
    return forma_definiciones.grupo(
        'logs',        
        {
            "titulo"   : "Comentarios/Anotaciones",
            "expandir" : 2,
            "elementos": [    
                comentarios_definiciones.gestion_comentarios(null, {forma: forma})                            
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
        archivos_grupo(forma),
        comentarios_grupo(forma),
        trd_grupo(forma)                    
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