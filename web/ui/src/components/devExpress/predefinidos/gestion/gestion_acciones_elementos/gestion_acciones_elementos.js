let elemento_parametros = function(elemento_id) {   
    let parametros = {}
    parametros["alto"]  = 400
    parametros["ancho"] = 800

    //HABILITAR_RESPUESTA_RAPIDA
    switch (elemento_id) {
        case 1:
            parametros["ventana"]       = "usuarioGestion"
            parametros["titulo"]        = "Asigna responsable"
            parametros["accion"]        = "ASIGNAR_RESPONSABLE"   
            parametros["boton_mensaje"] = "Asignar responsable"    
            parametros["fuente"]        = "usuarios_area"
            break;

        case 2:
            parametros["ventana"]       = "comentarioGestion"
            parametros["titulo"]        = "Devuelve a dependencia asignadora"
            parametros["accion"]        = "DEVOLVER_DEPENDENCIA"   
            parametros["boton_mensaje"] = "Devolver"  
            parametros["alto"]          = 300
            parametros["ancho"]         = 700  
            break;

        case 3:
            parametros["ventana"]       = "dependenciaGestion"
            parametros["titulo"]        = "Traslada a dependencia"
            parametros["accion"]        = "TRASLADAR_DEPENDENCIA"   
            parametros["boton_mensaje"] = "Trasladar"     
            break;

        case 4:
            parametros["ventana"]       = "apruebaGestion"
            parametros["titulo"]        = "Enviar a visto bueno"
            parametros["accion"]        = "ENVIAR_VISTO_BUENO"   
            parametros["boton_mensaje"] = "Enviar"     
            parametros["alto"]          = 400
            parametros["ancho"]         = 700
            break;

        case 5:
            parametros["ventana"]       = "comentarioGestion"
            parametros["titulo"]        = "Finalizar gestión"
            parametros["accion"]        = "FINALIZAR_MANUAL"   
            parametros["boton_mensaje"] = "Finalizar"     
            parametros["alto"]          = 300
            parametros["ancho"]         = 700
            break;

        case 6:
            parametros["ventana"]       = "borradorGestion"
            parametros["titulo"]        = "Selecciona plantilla para borrador"
            parametros["accion"]        = "SELECCION_PLANTILLA"   
            parametros["boton_mensaje"] = "Crear borrador"     
            parametros["alto"]          = 300
            parametros["ancho"]         = 700
            break;
        
        case 7:
            parametros["ventana"]       = "ventanilla_salida_forma"
            parametros["titulo"]        = "Radicación documento"
            parametros["accion"]        = "RADICAR_DOCUMENTO"   
            parametros["boton_mensaje"] = "Crear borrador"     
            parametros["alto"]          = 600
            parametros["ancho"]         = 1200
            break;

        case 8:
            parametros["ventana"]       = "comentarioGestion"
            parametros["titulo"]        = "Devolver a encargado dependencia"
            parametros["accion"]        = "DEVOLVER_ASIGNADOR"   
            parametros["boton_mensaje"] = "Devolver"     
            parametros["alto"]          = 300
            parametros["ancho"]         = 700
            break;

        case 9:
            parametros["ventana"]       = "trdGestion"
            parametros["titulo"]        = "Asigna expediente y tipo documental (TRD)"
            parametros["accion"]        = "ASIGNA_TRD"   
            parametros["boton_mensaje"] = "Asignar"     
            parametros["alto"]          = 300
            parametros["ancho"]         = 700
            break;

        case 10:
            parametros["ventana"]       = "trdTemaSubtema"
            parametros["titulo"]        = "Asigna tema y subtema"
            parametros["accion"]        = "ASIGNA_TEMA_SUBTEMA"   
            parametros["boton_mensaje"] = "Asignar"     
            parametros["alto"]          = 300
            parametros["ancho"]         = 700
            break;

        case 11:
            parametros["ventana"]       = "anexarGestion"
            parametros["titulo"]        = "Anexar archivo de gestión"
            parametros["accion"]        = "ANEXA_ARCHIVO"   
            parametros["boton_mensaje"] = "Anexar"     
            parametros["alto"]          = 400
            parametros["ancho"]         = 700
            break;    
            
        case 12:
            parametros["ventana"]       = "comentarioGestion"
            parametros["titulo"]        = "Crea comentario"
            parametros["accion"]        = "CREA_COMENTARIO"   
            parametros["boton_mensaje"] = "Crear"     
            parametros["alto"]          = 400
            parametros["ancho"]         = 700
            break; 

        case 13:
            parametros["ventana"]       = "usuarioGestion"
            parametros["titulo"]        = "Solicita respuesta colaborativa"
            parametros["accion"]        = "CREA_COLABORATIVA"   
            parametros["boton_mensaje"] = "Solicitar ayuda cooperativa"     
            parametros["alto"]          = 400
            parametros["ancho"]         = 700
            parametros["fuente"]        = "usuarios"
            break;   
            
        case 14:
            parametros["ventana"]       = "apruebaGestion"
            parametros["titulo"]        = "Aprueba para radicar"
            parametros["accion"]        = "APROBAR_RADICAR"   
            parametros["boton_mensaje"] = "Aprobar"     
            parametros["alto"]          = 400
            parametros["ancho"]         = 700
            break;

        case 15:
            parametros["ventana"]       = "comentarioGestion"
            parametros["titulo"]        = "Devuelve para revisión"
            parametros["accion"]        = "DEVOLVER_REVISION"
            parametros["boton_mensaje"] = "Devolver"     
            parametros["alto"]          = 400
            parametros["ancho"]         = 700
            break; 

        case 16:
            parametros["ventana"]       = "usuarioGestion"
            parametros["titulo"]        = "Asigna responsable RESPÚESTA RAPIDA"
            parametros["accion"]        = "ASIGNAR_RESPONSABLE"   
            parametros["boton_mensaje"] = "Asignar responsable respuesta rapida"    
            parametros["fuente"]        = "usuarios_area"
            parametros["rapida"]        = "SI"
            break;

        case 20:
            parametros["ventana"]       = "ventanilla_radicado_consulta"
            parametros["titulo"]        = "Consulta Radicado"
            parametros["accion"]        = "CONSULTA_RADICADO"   
            parametros["boton_mensaje"] = ""     
            parametros["alto"]          = 800
            parametros["ancho"]         = 1200
            break;

        case 21:
            parametros["ventana"]       = "gestion_datos_consulta"
            parametros["titulo"]        = "Consulta datos gestión"
            parametros["accion"]        = "CONSULTA_GESTION"   
            parametros["boton_mensaje"] = ""     
            parametros["alto"]          = 700
            parametros["ancho"]         = 1200
            break;
        
        // BORRADORES
        case 100:
            parametros["ventana"]       = "comentarioGestion"
            parametros["titulo"]        = "Crea borrador SALIDA"
            parametros["accion"]        = "CREA_BORRADOR_SALIDA"
            parametros["boton_mensaje"] = "Crear borrador SALIDA"     
            parametros["alto"]          = 400
            parametros["ancho"]         = 700
            parametros["borrador"]      = true
            break; 

        // BORRADORES
        case 101:
            parametros["ventana"]       = "comentarioGestion"
            parametros["titulo"]        = "Crea borrador INTERNO"
            parametros["accion"]        = "CREA_BORRADOR_INTERNO"
            parametros["boton_mensaje"] = "Crear borrador INTERNO"     
            parametros["alto"]          = 400
            parametros["ancho"]         = 700
            parametros["borrador"]      = true
            break; 

        default:
            break;
    }
    
    return parametros;
} 

// componente: grid, forma
let items_gestion = function(componente, contexto) {
    console.log("omponente.parametros:", componente.parametros)
    let items = [
        { id: 1,  titulo: 'Asignar responsable', icon: "fas fa-user-check" },
        { id: 16, titulo: 'Respuesta rapída',    icon: "fas fa-shipping-fast" },
    ]

    if (contexto=="grid_gestion") {
        items = [
            { id: 1,  titulo: 'Asignar responsable',                        icon: "fas fa-user-check" },
            //{ id: 16, titulo: 'Respuesta rapída',                           icon: "fas fa-shipping-fast" },
            { id: 3,  titulo: 'Trasladar a otra dependencia',               icon: "fas fa-forward" },
            { id: 2,  titulo: 'Devolver (Ventanilla, Servicio ciudadano)',  icon: "fas fa-backward" }          
        ]
    }
    else {      
        if ( componente.parametros.colaborativa != "" ) {
            items = [
                { id: 11, titulo: 'Anexar archivo de gestión', icon: "fas fa-file" },
                { id: 12, titulo: 'Crea comentario',           icon: "fas fa-comments" },
                { id: 5,  titulo: 'Finalizar',                 icon: "fas fa-window-close" }
            ]
        }  
        else {
            let etapa_estado    = componente.parametros.etapa_estado
            let borrador_existe = componente.parametros.borrador_existe 
            switch (etapa_estado) {
                case "ASIGNADO_DEPENDENCIA":
                    items = [
                        { id: 1,  titulo: 'Asignar responsable', icon: "fas fa-user-check" },
                        { id: 16, titulo: 'Respuesta rapída',    icon: "fas fa-shipping-fast" },
                    ]
                    break
                
                case "ASIGNADO_RESPONSABLE":
                    items = [
                        { id: 6,  titulo: 'Crear borrador',                            icon: "fas fa-file-import" },                                            
                        { id: 9,  titulo: 'Asigna expediente y tipo documental (TRD)', icon: "fas fa-folder-plus" },
                        { id: 11, titulo: 'Anexar archivo de gestión',                 icon: "fas fa-file" },
                        { id: 12, titulo: 'Crea comentario',                           icon: "fas fa-comments" },
                        { id: 8,  titulo: 'Devolver a encargado/enlace dependencia',   icon: "fas fa-backward" },
                        { id: 13, titulo: 'Solicitar ayuda cooperativa',               icon: "fas fa-hands-helping" }                   
                    ]

                    if (componente.parametros.total_tiempo == 0) {
                        items.push({ id: 5,  titulo: 'Finalizar', icon: "fas fa-window-close" })
                    }
                    
                    //if ( borrador_existe ) {
                        items.push({ id: 4,  titulo: 'Enviar a visto bueno', icon: "fas fa-clipboard-check" })
                        items.push({ id: 7,  titulo: 'Radicar borrador'    , icon: "fas fa-edit" })
                    //}
                    break

                case "DEVUELTO_ASIGNADORA":
                    items = []
                    break
                
                case "DEVUELTO_ASIGNADOR":
                    items = []
                    break
                
                case "TRASLADO_DEPENDENCIA":
                    items = []
                    break

                case "VISTO_BUENO":
                    items = [
                        { id: 8,  titulo: 'Devolver a asignador dependencia',  icon: "fas fa-backspace" },
                        { id: 14, titulo: 'Aprobar para radicar',              icon: "fas fa-thumbs-up" },
                        { id: 5,  titulo: 'Finalizar',                         icon: "fas fa-window-close" },
                        { id: 15, titulo: 'Devolver para revisión',            icon: "fas fa-undo-alt" },
                        { id: 3,  titulo: 'Trasladar a otra dependencia',      icon: "fas fa-forward" },
                    ]  
                    break

                case "DEVUELTO_REVISION":
                    items = [
                        { id: 4,  titulo: 'Enviar a visto bueno', icon: "fas fa-clipboard-check" },                    
                        { id: 6,  titulo: 'Crear borrador',       icon: "fas fa-file-import" },                 
                    ]
                    break
                
                case "APROBADO_RESPUESTA":
                    items = [
                        { id: 7,  titulo: 'Radicar', icon: "fas fa-edit" },                        
                    ]
                    break

                default:
                    items = [
                        { id: 6,  titulo: 'Crear borrador',                            icon: "fas fa-file-import" },                                            
                        { id: 11, titulo: 'Anexar archivo de gestión',                 icon: "fas fa-file" },
                        { id: 12, titulo: 'Crea comentario',                           icon: "fas fa-comments" },
                    ]

                    if (componente.parametros.total_tiempo == 0) {
                        items.push({ id: 5,  titulo: 'Finalizar', icon: "fas fa-window-close" })
                    }
                    
                    //if ( borrador_existe ) {
                        items.push({ id: 4,  titulo: 'Enviar a visto bueno', icon: "fas fa-clipboard-check" })
                        items.push({ id: 7,  titulo: 'Radicar borrador'    , icon: "fas fa-edit" })
                    //}
                    break
            }        
        }        
    }

    return items
}

let items_borradores = function(componente, contexto) {    
    let items = [
        { id: 100, titulo: 'SALIDA',  icon: "fas fa-angle-double-right" },
        { id: 101, titulo: 'INTERNO', icon: "fas fa-angle-double-down" },
    ]

    return items
}

export default {
    items_gestion      : items_gestion,
    items_borradores   : items_borradores,
    elemento_parametros: elemento_parametros
}