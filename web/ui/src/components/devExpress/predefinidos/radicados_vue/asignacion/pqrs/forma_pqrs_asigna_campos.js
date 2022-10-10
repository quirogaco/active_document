import forma_definiciones     from "../../../comunes_vue/forma/forma.js"
import campos_basicos_comunes from "../../../comunes_vue/forma/campos_basicos_comunes.js"
import basicos_definiciones   from "../../../radicados_vue/comunes/basicos/basicos_definiciones.js"
import tercero_definiciones   from "../../../radicados_vue/comunes/basicos/tercero_definiciones.js"
import respuesta_definiciones from "../../../radicados_vue/comunes/basicos/respuesta_definiciones.js"
import archivo_definiciones   from "../../../radicados_vue/comunes/basicos/archivo_definiciones.js"
import asigna_definiciones    from "../../../radicados_vue/comunes/basicos/asigna_definiciones.js"

let barra_botones = function(forma, basicas) {
    return  [       
        { 
            widget  : "dxButton",           
            options :{ //0
                icon       : 'fas fa-plus-square',
                alignment  : 'center',
                hint       : 'asigna_pqrs',
                type       : 'success',
                text       : 'Asignar pqrs', 
                stylingMode: "contained", 
                onClick    : forma.boton_click,
            } 
        },
        
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
            "titulo"   : "Información basica del documento",
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

// ########### //
// ASIGNACION  //
// ########### //
let asignacion_opciones = function(forma) {
    return forma_definiciones.grupo(
        'clase_grupo',            
        {
            "visible"  : true,
            "elementos": [
                asigna_definiciones.es_ventanilla(null, {forma: forma}),
                //asigna_definiciones.resuelto_inmediato(null, {forma: forma}), no aplica para asignacion traslado                
                asigna_definiciones.comentario_traslado(null, {forma: forma})
            ]
        }
    )
};

let asignacion_generales = function(forma) {
    return forma_definiciones.grupo(
        'respuesta_datos',        
        {
            "titulo"   : "Datos especificos",
            "elementos": [                                   
                asigna_definiciones.gestion_peticion_id(null, {forma: forma}),
                asigna_definiciones.gestion_horas_dias(null, {forma: forma}),    
                asigna_definiciones.gestion_total_tiempo(null, {forma: forma}),    
                asigna_definiciones.gestion_prioridad(null, {forma: forma}),    
                asigna_definiciones.reserva(null, {forma: forma}),       
                asigna_definiciones.gestion_dependencia_id(null, {forma: forma}),       
                asigna_definiciones.gestion_dependencia_responsable(null, {forma: forma}),             
                asigna_definiciones.tema_dependencia_id(null, {forma: forma}),    
                asigna_definiciones.subtema_dependencia_id(null, {forma: forma}),                
                respuesta_definiciones.copia_usuarios_id(null, {forma: forma}),
                respuesta_definiciones.copia_grupos_id(null, {forma: forma})
            ]
        }
    )
};

let asignacion_grupo = function(forma) {
    return forma_definiciones.grupo(
        'respuesta',        
        {
            "titulo"   : "Información de traslado/asignación",
            "elementos": [
                asignacion_opciones(forma),
                asignacion_generales(forma)
            ]
        }
    )
};

// ######## //
// ARCHIVOS //
// ######## //
let archivos_grupo = function(forma) {
    return forma_definiciones.grupo(
        'archivos',        
        {
            "titulo"   : "Información de archivos",
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
        asignacion_grupo(forma),
        archivos_grupo(forma),
        basico_grupo(forma),
        tercero_grupo(forma)              
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