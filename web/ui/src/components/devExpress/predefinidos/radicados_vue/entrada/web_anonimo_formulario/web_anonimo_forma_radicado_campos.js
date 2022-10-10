import forma_definiciones     from "../../../comunes_vue/forma/forma.js"
import campos_basicos_comunes from "../../../comunes_vue/forma/campos_basicos_comunes.js"
import basicos_definiciones   from "../../../radicados_vue/comunes/basicos/basicos_definiciones.js"
import tercero_definiciones   from "../../../radicados_vue/comunes/basicos/tercero_definiciones.js"
import respuesta_definiciones from "../../../radicados_vue/comunes/basicos/respuesta_definiciones.js"
import archivo_definiciones   from "../../../radicados_vue/comunes/basicos/archivo_definiciones.js"
import web_definiciones       from "../../../radicados_vue/comunes/basicos/web_definiciones.js"

let barra_botones = function(forma, basicas) {
    return  [       
        { 
            widget  : "dxButton",           
            options :{ //0
                icon       : 'fas fa-plus-square',
                alignment  : 'center',
                hint       : 'radicar_entrada',
                type       : 'success',
                text       : 'Enviar información', 
                stylingMode: "contained", 
                onClick    : forma.boton_click,
            } 
        }               
    ]              
}

//********************//
// Campos de la forma //
//********************//


// UBICACIÓN
let tercero_ubicacion = function(forma) {
    return forma_definiciones.grupo(
        'tercero_ubicacion',        
        {
            "elementos": [                
                tercero_definiciones.correo_electronico(null, {forma: forma}),  
            ]
        }
    )
}

let ubicacion_grupo = function(forma) {
    return forma_definiciones.grupo(
        'ubicacion',        
        {
            "titulo"   : "Remitente ubicación",
            'columna'  : 1,
            "elementos": [
                tercero_ubicacion(forma)
            ]
        }
    )
}

// ###### //
// ASUNTO //
// ###### //
let detalle_grupo = function(forma) {
    return forma_definiciones.grupo(
        'asunto',        
        {
            "titulo"   : "Detalle de la petición",
            'columna'  : 1,
            "elementos": [
                basicos_definiciones.asunto(null, {forma: forma, obligatorio:true, titulo:"Asunto", mensaje: "Describa su petición"})
            ]
        }
    )
}

// ######### //
// ARCHIVOS //
// ######### //
let archivo_grupo = function(forma) {
    return forma_definiciones.grupo(
        'respuesta',        
        {
            "titulo"   : "Anexos",
            'columna'  : 1,
            "elementos": [
                archivo_definiciones.mensaje_archivo(null, {forma: forma}),
                archivo_definiciones.archivos_anexos(null, {forma: forma, titulo:"Anexos en formato electrónico"})                
            ]
        }
    )
}

// ############# //
// INFORMAACIÓN //
// ############# //
let informacion_grupo = function(forma) {
    return forma_definiciones.grupo(
        'asunto',        
        {
            "titulo"   : "Manejo de información",
            'columna'  : 1,
            "elementos": [                
                web_definiciones.mensaje_informacion(null, { forma: forma }),
                web_definiciones.manejo_informacion(null, { forma: forma })
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
        ubicacion_grupo(forma),
        detalle_grupo(forma),  
        archivo_grupo(forma),
        informacion_grupo(forma),
    ]

    return campos
}

let campos_forma = function(forma, basicas) {
    let campos = {
        // aqui va tipo predefinido para radicación
        ...campos_basicos_comunes.campos(forma, basicas),  
        ...campos_especificos(forma, basicas)      
    }

    return campos
} 

export default {
    campos_forma: campos_forma
}