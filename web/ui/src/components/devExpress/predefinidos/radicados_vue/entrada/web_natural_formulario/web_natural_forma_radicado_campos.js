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

// ####### //
// TERCERO //
// ####### //

// GENERALES
let tercero_generales = function(forma) {
    return forma_definiciones.grupo(
        'tercero_generales',        
        {
            "elementos": [            
                tercero_definiciones.tipo_identificacion(null, {forma: forma, visible:true}),
                tercero_definiciones.nro_identificacion(null, {forma: forma, obligatorio:true, titulo:"Número de identificación"}),
                tercero_definiciones.nombres(null, {forma: forma, obligatorio:true}),
                tercero_definiciones.apellidos(null, {forma: forma, obligatorio:true}),         
            ]
        }
    )
}

let tercero_grupo = function(forma) {
    return forma_definiciones.grupo(
        'tercero',        
        {
            "titulo"   : "Remitente información",
            'columna'  : 1,
            "elementos": [
                tercero_generales(forma)
            ]
        }
    )
}


// Notificación
let notificacion_grupo = function(forma) {
    return forma_definiciones.grupo(
        'notificacion',        
        {
            "titulo"   : "Notificación",
            'columna'  : 1,
            "elementos": [
                respuesta_definiciones.medio_notificacion(null, {forma: forma, eventos: eventos, obligatorio:true}),       
            ]
        }
    )
}

// UBICACIÓN
let eventos = {
    "valor_cambiado": function(campo, definicion, forma, forma_id) {  
        let datos_forma = forma_definiciones.forma_lee_datos(forma)
        console.log("datos_forma:", datos_forma)
        
        // CORREO notifica
        let correo    = campo.value.indexOf("CORREO") > -1 ? true : false                
        if ( correo == true) {
            forma_definiciones.asigna_validador_forma(forma, ["tercero_correo_electronico"], "obligatorio")
        }
        else {
            forma_definiciones.borra_validador_forma(forma, ["tercero_correo_electronico"], "obligatorio")  
        }

        // DIRECCIÓN notifica
        let direccion = campo.value.indexOf("DIRECCION") > -1 ? true : false
        if ( direccion == true) {
            forma_definiciones.asigna_validador_forma(forma, ["tercero_direccion"], "obligatorio")
        }
        else {
            forma_definiciones.borra_validador_forma(forma, ["tercero_direccion"], "obligatorio")  
        }

        forma_definiciones.asigna_valor(forma, "tercero_correo_electronico", datos_forma["tercero_correo_electronico"])
        forma_definiciones.asigna_valor(forma, "tercero_direccion",          datos_forma["tercero_direccion"])
        forma_definiciones.asigna_valor(forma, "tercero_telefono",           datos_forma["tercero_telefono"])
        forma_definiciones.asigna_valor(forma, "tercero_ciudad_id",          datos_forma["tercero_ciudad_id"])
    }
}

let tercero_ubicacion = function(forma) {
    return forma_definiciones.grupo(
        'tercero_ubicacion',        
        {
            "elementos": [                
                tercero_definiciones.correo_electronico(null, {forma: forma}),                
                tercero_definiciones.direccion(null, {forma: forma, obligatorio:true}),                                
                tercero_definiciones.telefono(null, {forma: forma}),                
                tercero_definiciones.ciudad(null, {forma: forma, obligatorio:true})
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

// ############## //
// CLASIFICACIÓN //
// ############## //
let clasificacion_grupo = function(forma) {
    return forma_definiciones.grupo(
        'asunto',        
        {
            "titulo"   : "Información de clasificación",
            'columna'  : 1,
            "elementos": [
                tercero_definiciones.tipo_tercero_id(null, { forma: forma, filtros_fuente: ["tipo", "=", "NATURAL"], eventos: {}, titulo:"Tipo de ciudadano"}),
                web_definiciones.discapacidad_id(null, { forma: forma }),
                web_definiciones.poblacion_id(null, { forma: forma }),
                web_definiciones.rango_id(null, { forma: forma }),
                web_definiciones.genero_id(null, { forma: forma })
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
        tercero_grupo(forma),
        notificacion_grupo(forma),
        ubicacion_grupo(forma),
        detalle_grupo(forma),  
        archivo_grupo(forma),
        clasificacion_grupo(forma),   
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