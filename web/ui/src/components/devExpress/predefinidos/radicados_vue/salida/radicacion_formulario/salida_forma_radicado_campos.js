import forma_definiciones     from "../../../comunes_vue/forma/forma.js"
import campos_basicos_comunes from "../../../comunes_vue/forma/campos_basicos_comunes.js"
import basicos_definiciones   from "../../../radicados_vue/comunes/basicos/basicos_definiciones.js"
import tercero_definiciones   from "../../../radicados_vue/comunes/basicos/tercero_definiciones.js"
import respuesta_definiciones from "../../../radicados_vue/comunes/basicos/respuesta_definiciones.js"
import archivo_definiciones   from "../../../radicados_vue/comunes/basicos/archivo_definiciones.js"

let barra_botones = function(forma, basicas) {
    return  [       
        { 
            widget  : "dxButton",           
            options :{ //0
                icon       : 'fas fa-plus-square',
                alignment  : 'center',
                hint       : 'radicar_salida',
                type       : 'success',
                text       : 'Radicar Salida', 
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
                basicos_definiciones.fecha_documento(null, {forma: forma}),
                basicos_definiciones.radicado_responde(null, {forma: forma}),
                basicos_definiciones.nro_folios(null, {forma: forma}),
                basicos_definiciones.anexos(null, {forma: forma}),
                basicos_definiciones.asunto(null, {forma: forma})
            ]
        }
    )
}

// ####### //
// TERCERO //
// ####### //
let clase_item = function(forma) {
    return tercero_definiciones.clase_tercero(null, {forma: forma})
}

let tercero_generales = function(forma) {
    return forma_definiciones.grupo(
        'tercero_datos',        
        {
            "elementos": [
                tercero_definiciones.tipo_tercero_id(null, {forma: forma}),
                tercero_definiciones.busca_remitente(null, {forma: forma}),
                tercero_definiciones.tipo_identificacion(null, {forma: forma}),
                tercero_definiciones.nro_identificacion(null, {forma: forma}),
                tercero_definiciones.razon_social(null, {forma: forma}),
                tercero_definiciones.nombres(null, {forma: forma}),
                tercero_definiciones.apellidos(null, {forma: forma}),
                tercero_definiciones.correo_electronico(null, {forma: forma}),
                tercero_definiciones.cargo(null, {forma: forma}),
                tercero_definiciones.direccion(null, {forma: forma}),
                tercero_definiciones.codigo_postal(null, {forma: forma}),
                tercero_definiciones.telefono_movil(null, {forma: forma}),
                tercero_definiciones.telefono(null, {forma: forma}),
                tercero_definiciones.fax(null, {forma: forma}),
                tercero_definiciones.ciudad(null, {forma: forma})
            ]
        }
    )
}

let tercero_grupo = function(forma) {
    return forma_definiciones.grupo(
        'tercero',        
        {
            "titulo"   : "Información Destinatario",
            'columna'  : 1,
            "elementos": [
                clase_item(forma),
                tercero_generales(forma)
            ]
        }
    )
}

// ######### //
// RESPUESTA //
// ######### //
let respuesta_grupo = function(forma) {
    return forma_definiciones.grupo(
        'respuesta',        
        {
            "titulo"   : "Información Respuesta",
            'columna'  : 1,
            "elementos": [
                respuesta_definiciones.respuesta_tipo(null, {forma: forma}),
                respuesta_definiciones.dependencia_responde_id(null, {forma: forma}),
                respuesta_definiciones.funcionario_responde_id(null, {forma: forma}),
                respuesta_definiciones.tipo_firma(null, {forma: forma}),
                respuesta_definiciones.reserva(null, {forma: forma}),
                respuesta_definiciones.medio_notificacion_salida(null, {forma: forma}),
                respuesta_definiciones.copia_usuarios_id(null, {forma: forma}),
                respuesta_definiciones.copia_grupos_id(null, {forma: forma}),
                respuesta_definiciones.copia_terceros_id(null, {forma: forma}),
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
        tercero_grupo(forma),
        respuesta_grupo(forma),
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