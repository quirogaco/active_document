import forma_definiciones     from "../../../comunes_vue/forma/forma.js"
import campos_basicos_comunes from "../../../comunes_vue/forma/campos_basicos_comunes.js"
import basicos_definiciones   from "../../../radicados_vue/comunes/basicos/basicos_definiciones.js"
import respuesta_definiciones from "../../../radicados_vue/comunes/basicos/respuesta_definiciones.js"
import archivo_definiciones   from "../../../radicados_vue/comunes/basicos/archivo_definiciones.js"

let barra_botones = function(forma, basicas) {
    return  [       
        { 
            widget  : "dxButton",           
            options :{ //0
                icon       : 'fas fa-plus-square',
                alignment  : 'center',
                hint       : 'radicar_interno',
                type       : 'success',
                text       : 'Radicar Interno', 
                stylingMode: "contained", 
                onClick    : forma.boton_click,
            } 
        },
        
        {
            widget  : "dxButton",           
            options :{ //1
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
// BASICOS //
// ####### //
let basicos_grupo = function(forma) {
    return forma_definiciones.grupo(
        'basicos',
        {
            "titulo"   : "Información Basica",
            'columna'  : 1,
            "elementos": [                
                basicos_definiciones.id(null, {forma: forma}),                
                respuesta_definiciones.dependencia_envia_id(null, {forma: forma}),
                respuesta_definiciones.funcionario_envia_id(null, {forma: forma}),
                respuesta_definiciones.dependencia_recibe_id(null, {forma: forma}),
                respuesta_definiciones.funcionario_recibe_id(null, {forma: forma}),
                respuesta_definiciones.tipo_firma(null, {forma: forma}),
                respuesta_definiciones.reserva(null, {forma: forma}),
                respuesta_definiciones.medio_notificacion_salida(null, {forma: forma}),
                
                basicos_definiciones.fecha_documento(null, {forma: forma}),
                basicos_definiciones.nro_folios(null, {forma: forma}),
                basicos_definiciones.anexos(null, {forma: forma}),
                basicos_definiciones.asunto(null, {forma: forma}),    
                basicos_definiciones.relacionados_id(null, {forma: forma}),                
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
                archivo_definiciones.anexos_radicado(null, {forma: forma}),
                archivo_definiciones.mensaje_archivo(null, {forma: forma}),
                archivo_definiciones.archivos_anexos(null, {forma: forma})                
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
        basicos_grupo(forma),        
        archivo_grupo(forma)
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