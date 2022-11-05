import forma_definiciones     from "../../../../comunes_vue/forma/forma.js"
import campos_basicos_comunes from "../../../../comunes_vue/forma/campos_basicos_comunes.js"
import basicos_definiciones   from "../../../../radicados_vue/comunes/basicos/basicos_definiciones.js"
import tercero_definiciones   from "../../../../radicados_vue/comunes/basicos/tercero_definiciones.js"
import respuesta_definiciones from "../../../../radicados_vue/comunes/basicos/respuesta_definiciones.js"
import archivo_definiciones   from "../../../../radicados_vue/comunes/basicos/archivo_definiciones.js"
import asigna_definiciones    from "../../../../radicados_vue/comunes/basicos/asigna_definiciones.js"

let barra_botones = function(forma) {
    return  [       
        { 
            widget  : "dxButton",           
            options :{ //0
                icon       : 'fas fa-plus-square',
                alignment  : 'center',
                hint       : 'radicar_ventanilla',
                type       : 'success',
                text       : 'Radicar Documento', 
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
                basicos_definiciones.canal_radicado_id(null, {forma: forma}),
                respuesta_definiciones.medio_notificacion(null, {forma: forma, "obligatorio": false}),
                basicos_definiciones.fecha_documento(null, {forma: forma}),
                basicos_definiciones.radicado_remitente(null, {forma: forma}),
                basicos_definiciones.empresa_mensajeria_id(null, {forma: forma}),
                basicos_definiciones.numero_guia(null, {forma: forma}),
                basicos_definiciones.nro_folios(null, {forma: forma}),
                basicos_definiciones.anexos(null, {forma: forma}),
                basicos_definiciones.asunto(null, {forma: forma}),
                basicos_definiciones.entidad_traslada(null, {forma: forma}),
                basicos_definiciones.persona_traslada(null, {forma: forma}),
                basicos_definiciones.relacionados_id(null, {forma: forma}),
            ]
        }
    )
}

// ####### //
// TERCERO //
// ####### //
let clase_grupo = function(forma) {
    return forma_definiciones.grupo(
        'clase_grupo',            
        {
            "visible"  : true,
            "elementos": [
                tercero_definiciones.clase_tercero(null, {forma: forma, "titulo": "Clase remitente"})
            ]
        }
    )
};

let tipo_tercero_id = function(forma) {
    return tercero_definiciones.tipo_tercero_id(null, {forma: forma, "titulo": "Tipo remitente"})
};

let tercero_juridica = function(forma) {
    return forma_definiciones.grupo(
        'tercero_juridica',        
        {
            "titulo"   : "Datos persona juridica",
            "visible"  : true,
            "elementos": [
                tipo_tercero_id(forma),
                tercero_definiciones.busca_remitente(null, {forma: forma, "titulo": "Busca remitente"}),
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
};

let tercero_natural = function(forma) {
    return forma_definiciones.grupo(
        'tercero_natural',        
        {
            "titulo"   : "Datos persona natural",
            "visible"  : false,
            "elementos": [
                tipo_tercero_id(forma),
                tercero_definiciones.busca_remitente(null, {forma: forma, "titulo": "Busca remitente"}),
                tercero_definiciones.tipo_identificacion(null, {forma: forma}),
                tercero_definiciones.nro_identificacion(null, {forma: forma}),
                tercero_definiciones.nombres(null, {forma: forma, 'obligatorio': true}),
                tercero_definiciones.apellidos(null, {forma: forma, 'obligatorio': true}),
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
};

let tercero_anonimo = function(forma) {
    return forma_definiciones.grupo(
        'tercero_anonimo',        
        {
            "titulo"   : "Datos anonimo",
            "visible"  : false,
            "elementos": [                
                tercero_definiciones.correo_electronico(null, {forma: forma})                            
            ]
        }
    )
};

let tercero_grupo = function(forma) {
    return forma_definiciones.grupo(
        'tercero',        
        {
            "titulo"   : "Información Remitente",
            "elementos": [
                clase_grupo(forma),     
                tercero_juridica(forma),                 
                tercero_natural(forma),  
                tercero_anonimo(forma),                                                            
            ]
        }
    )
};

// ########### //
// ASIGNACION  //
// ########### //
let asignacion_opciones = function(forma) {
    return forma_definiciones.grupo(
        'clase_grupo',            
        {
            "visible"  : true,
            "elementos": [
                asigna_definiciones.es_pqrs(null, {forma: forma}),
                //asigna_definiciones.comentario_traslado(null, {forma: forma})
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
                archivo_definiciones.archivos_anexos(null, {forma: forma})                
            ]
        }
    )
}

// ###### //
// CAMPOS //
// ###### //
const campos_especificos = function(forma) {
    // Barra de botones
    let campos = {
        "barra_botones": barra_botones(forma)
    }

    campos["elementos"] =  [
        basicos_grupo(forma),        
        // tercero_grupo(forma),
        // asignacion_grupo(forma),
        // archivo_grupo(forma)
    ]

    return campos
}

let campos_forma = function(forma, basicas) {
    let campos = {
        ...campos_especificos(forma)
    }

    return campos
} 

export default {
    campos_forma: campos_forma
}