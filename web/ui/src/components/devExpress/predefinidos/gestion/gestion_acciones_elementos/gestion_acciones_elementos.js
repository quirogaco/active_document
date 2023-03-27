let elemento_parametros = function(elemento_id) {   
    let parametros = {};
    parametros["alto"]  = 400;
    parametros["ancho"] = 1200;

    //HABILITAR_RESPUESTA_RAPIDA
    switch (elemento_id) {
        case 1:
            parametros["ventana"]       = "usuarioGestion";
            parametros["titulo"]        = "Asigna responsable";
            parametros["accion"]        = "ASIGNAR_RESPONSABLE";   
            parametros["boton_mensaje"] = "Asignar responsable";    
            parametros["fuente"]        = "usuarios_area";
            break;

        case 2:
            parametros["ventana"]       = "comentarioGestion";
            parametros["titulo"]        = "Devuelve a dependencia asignadora";
            parametros["accion"]        = "DEVOLVER_DEPENDENCIA";   
            parametros["boton_mensaje"] = "Devolver"; 
            parametros["alto"]          = 300;
            parametros["ancho"]         = 1200; 
            break;

        case 3:
            parametros["ventana"]       = "dependenciaGestion";
            parametros["titulo"]        = "Traslada a dependencia";
            parametros["accion"]        = "TRASLADAR_DEPENDENCIA";   
            parametros["boton_mensaje"] = "Trasladar";     
            break;

        case 4:
            parametros["ventana"]       = "apruebaGestion";
            parametros["titulo"]        = "Enviar a visto bueno";
            parametros["accion"]        = "ENVIAR_VISTO_BUENO";   
            parametros["boton_mensaje"] = "Enviar";    
            parametros["alto"]          = 400;
            parametros["ancho"]         = 1200;
            break;

        case 5:
            parametros["ventana"]       = "comentarioGestion";
            parametros["titulo"]        = "Finalizar gestión";
            parametros["accion"]        = "FINALIZAR_MANUAL";   
            parametros["boton_mensaje"] = "Finalizar";     
            parametros["alto"]          = 300;
            parametros["ancho"]         = 1200;
            break;

        case 6:
            parametros["ventana"]       = "borradorGestion";
            parametros["titulo"]        = "Selecciona plantilla para borrador";
            parametros["accion"]        = "SELECCION_PLANTILLA";  
            parametros["boton_mensaje"] = "Crear borrador";     
            parametros["alto"]          = 300;
            parametros["ancho"]         = 1200;
            break;
        
        case 7:
            parametros["ventana"]       = "ventanilla_salida_forma";
            parametros["titulo"]        = "Radicación documento";
            parametros["accion"]        = "RADICAR_DOCUMENTO";   
            parametros["boton_mensaje"] = "Crear borrador";     
            parametros["alto"]          = 600;
            parametros["ancho"]         = 1200;
            break;

        case 8:
            parametros["ventana"]       = "comentarioGestion";
            parametros["titulo"]        = "Devolver a encargado dependencia";
            parametros["accion"]        = "DEVOLVER_ASIGNADOR";   
            parametros["boton_mensaje"] = "Devolver";     
            parametros["alto"]          = 300;
            parametros["ancho"]         = 1200;
            break;

        case 9:
            parametros["ventana"]       = "trdGestion";
            parametros["titulo"]        = "Asigna expediente y tipo documental (TRD)";
            parametros["accion"]        = "ASIGNA_TRD";  
            parametros["boton_mensaje"] = "Asignar";     
            parametros["alto"]          = 300;
            parametros["ancho"]         = 1200;
            break;

        case 10:
            parametros["ventana"]       = "trdTemaSubtema";
            parametros["titulo"]        = "Asigna tema y subtema";
            parametros["accion"]        = "ASIGNA_TEMA_SUBTEMA";   
            parametros["boton_mensaje"] = "Asignar" ;    
            parametros["alto"]          = 300;
            parametros["ancho"]         = 1200;
            break;

        case 11:
            parametros["ventana"]       = "anexarGestion";
            parametros["titulo"]        = "Anexar archivo de gestión";
            parametros["accion"]        = "ANEXA_ARCHIVO";  
            parametros["boton_mensaje"] = "Anexar";     
            parametros["alto"]          = 400;
            parametros["ancho"]         = 1200;
            break;    
            
        case 12:
            parametros["ventana"]       = "comentarioGestion";
            parametros["titulo"]        = "Crea comentario";
            parametros["accion"]        = "CREA_COMENTARIO";   
            parametros["boton_mensaje"] = "Crear";     
            parametros["alto"]          = 400;
            parametros["ancho"]         = 1200;
            break; 

        case 13:
            parametros["ventana"]       = "usuarioGestion";
            parametros["titulo"]        = "Solicita respuesta colaborativa";
            parametros["accion"]        = "CREA_COLABORATIVA";   
            parametros["boton_mensaje"] = "Solicitar ayuda cooperativa";     
            parametros["alto"]          = 400;
            parametros["ancho"]         = 1200;
            parametros["fuente"]        = "usuarios";
            break;   
            
        case 14:
            parametros["ventana"]       = "apruebaGestion";
            parametros["titulo"]        = "Aprueba para radicar";
            parametros["accion"]        = "APROBAR_RADICAR";  
            parametros["boton_mensaje"] = "Aprobar";     
            parametros["alto"]          = 400;
            parametros["ancho"]         = 1200;
            break;

        case 15:
            parametros["ventana"]       = "comentarioGestion";
            parametros["titulo"]        = "Devuelve para revisión";
            parametros["accion"]        = "DEVOLVER_REVISION";
            parametros["boton_mensaje"] = "Devolver";     
            parametros["alto"]          = 400;
            parametros["ancho"]         = 1200;
            break; 

        case 16:
            parametros["ventana"]       = "usuarioGestion";
            parametros["titulo"]        = "Asigna responsable RESPÚESTA RAPIDA";
            parametros["accion"]        = "ASIGNAR_RESPONSABLE";   
            parametros["boton_mensaje"] = "Asignar responsable respuesta rapida";   
            parametros["fuente"]        = "usuarios_area";
            parametros["rapida"]        = "SI";
            break;

        case 20:               
            parametros["ventana"]       = "ventanilla_radicado_consulta";
            parametros["titulo"]        = "Consulta Radicado";
            parametros["accion"]        = "CONSULTA_RADICADO";   
            parametros["boton_mensaje"] = "";    
            parametros["alto"]          = 1200;
            parametros["ancho"]         = 1200;
            break;

        case 21:
            parametros["ventana"]       = "gestion_datos_consulta";
            parametros["titulo"]        = "Consulta datos gestión";
            parametros["accion"]        = "CONSULTA_GESTION";   
            parametros["boton_mensaje"] = "";     
            parametros["alto"]          = 1200;
            parametros["ancho"]         = 1200;
            break;
        
        // BORRADORES
        case 100:
            parametros["ventana"]       = "comentarioGestion";
            parametros["titulo"]        = "Crea borrador SALIDA";
            parametros["accion"]        = "CREA_BORRADOR_SALIDA";
            parametros["boton_mensaje"] = "Crear borrador SALIDA";    
            parametros["alto"]          = 400;
            parametros["ancho"]         = 1200;
            parametros["borrador"]      = true;
            break; 

        // BORRADORES
        case 101:
            parametros["ventana"]       = "comentarioGestion";
            parametros["titulo"]        = "Crea borrador INTERNO";
            parametros["accion"]        = "CREA_BORRADOR_INTERNO";
            parametros["boton_mensaje"] = "Crear borrador INTERNO";     
            parametros["alto"]          = 400;
            parametros["ancho"]         = 1200;
            parametros["borrador"]      = true;
            break; 

        default:
            break;
    }
    
    return parametros;
};

let asignar_responsable = { 
    id: 1, 
    titulo: 'Asignar responsable', 
    icon: "fas fa-user-check" 
};

let devolver_ventanilla = { 
    id: 2, 
    titulo: 'Devolver (Ventanilla, Servicio ciudadano)', 
    icon: "fas fa-backward" 
};

let trasladar_dependencia = { 
    id: 3, 
    titulo: 'Trasladar a otra dependencia', 
    icon: "fas fa-forward" 
};

let enviar_a_visto_bueno =  { 
    id: 4,  
    titulo: 'Enviar a visto bueno', 
    icon: "fas fa-clipboard-check" 
};

let finalizar = { 
    id: 5,  
    titulo: 'Finalizar', 
    icon: "fas fa-window-close" 
};

let crear_borrador = { 
    id: 6,  
    titulo: 'Crear borrador', 
    icon: "fas fa-file-import" 
};

let radicar_borrador = {
    id: 7,  
    titulo: 'Radicar borrador', 
    icon: "fas fa-edit" 
};

let devolver_asignador = { 
    id: 8,  
    titulo: 'Devolver a encargado/enlace dependencia', 
    icon: "fas fa-backspace"
};

let asigna_trd = { 
    id: 9,  
    titulo: 'Asigna expediente y tipo documental (TRD)', 
    icon: "fas fa-folder-plus" 
};

let anexar_archivo = { 
    id: 11, 
    titulo: 'Anexar archivo de gestión', 
    icon: "fas fa-file" 
};

let crea_comentario  = { 
    id: 12, 
    titulo: 'Crea comentario', 
    icon: "fas fa-comments" 
};

let ayuda_cooperativa =  { 
    id: 13, 
    titulo: 'Solicitar ayuda cooperativa', 
    icon: "fas fa-hands-helping" 
};

let aprobar = { 
    id: 14, 
    titulo: 'Aprobar para radicar', 
    icon: "fas fa-thumbs-up" 
};

let devolver = { 
    id: 15, 
    titulo: 'Devolver para revisión', 
    icon: "fas fa-undo-alt" 
};

let respuesta_rapida = { 
    id: 16, 
    titulo: 'Respuesta rapída', 
    icon: "fas fa-shipping-fast"
};

// componente: grid, forma
let items_gestion = function(componente, contexto, datos={}) {
    let items = [];
    
    if (contexto=="grid_gestion") {        
        if (
                (window.$usuario.roles_especificos.indexOf('CORRESPONDENCIA') > -1) || 
                (window.$usuario.roles_especificos.indexOf('PQRSD') > -1)
            ) {
            items = [
                asignar_responsable,
                //respuesta_rapida
                trasladar_dependencia,
                devolver_ventanilla,
                finalizar          
            ]
        }
        else {
            items = []
        }
    }
    else {      
        if ( componente.parametros.colaborativa != "" ) {
            items = [
                anexar_archivo,
                crea_comentario,
                finalizar
            ]
        }  
        else {
            if (datos.clase_radicado == "INTERNO") {
                items = [ 
                    finalizar        
                ]
            }
            else {
                let etapa_estado = componente.parametros.etapa_estado
                let borrador_existe = componente.borrador_existe
                console.log("BOTONES", etapa_estado, borrador_existe, datos.origen_tipo )
                switch (etapa_estado) {
                    case "ASIGNADO_DEPENDENCIA":
                        items = [
                            asignar_responsable,
                            trasladar_dependencia,
                            devolver_ventanilla,
                            finalizar
                            //respuesta_rapida
                        ]
                        break
                    
                    case "ASIGNADO_RESPONSABLE":
                        items = [
                            crear_borrador,                                          
                            asigna_trd,
                            anexar_archivo,
                            crea_comentario,
                            devolver_asignador,
                            ayuda_cooperativa     
                        ]

                        if (componente.parametros.total_tiempo == 0) {
                            items.push(finalizar)
                        }
                        
                        if ( 
                            (borrador_existe) && 
                            (datos.origen_tipo == "ENTRADA") 
                        ) {
                            items.push(enviar_a_visto_bueno); 
                            items.push(radicar_borrador);                           
                        }


                        if ( 
                            (borrador_existe) && 
                            (datos.origen_tipo == "SALIDA") 
                        ) {                            
                            items.push(radicar_borrador);                           
                        }

                        if ( 
                            (borrador_existe) && 
                            (datos.origen_tipo == "INTERNO") 
                        ) {                            
                            items.push(radicar_borrador);                           
                        }
                        
                        
                        break

                    case "DEVUELTO_ASIGNADORA":
                        items = [
                            asignar_responsable,
                            trasladar_dependencia,
                            devolver_ventanilla,
                            finalizar
                            //respuesta_rapida
                        ]
                        break
                    
                    case "DEVUELTO_ASIGNADOR":   
                        items = [
                            asignar_responsable,
                            trasladar_dependencia,
                            devolver_ventanilla,
                            finalizar
                            //respuesta_rapida
                        ]
                        break
                    
                    case "TRASLADO_DEPENDENCIA":                    
                        items = [
                            asignar_responsable,
                            trasladar_dependencia,
                            devolver_ventanilla,
                            finalizar
                            //respuesta_rapida
                        ]
                        break

                    case "VISTO_BUENO":
                        items = [
                            devolver_asignador,
                            aprobar,
                            finalizar,
                            devolver,
                            trasladar_dependencia
                        ]  
                        break

                    case "DEVUELTO_REVISION":
                        items = [
                            enviar_a_visto_bueno,           
                            crear_borrador,
                            asigna_trd,
                            anexar_archivo,
                            crea_comentario,
                            ayuda_cooperativa                 
                        ]
                        break
                    
                    case "APROBADO_RESPUESTA":
                        items = [
                            radicar_borrador, 
                            enviar_a_visto_bueno
                            //crear_borrador
                        ]
                        break

                    default:
                        items = [
                            crear_borrador,                                          
                            anexar_archivo,
                            crea_comentario,
                        ]

                        if (componente.parametros.total_tiempo == 0) {
                            items.push(finalizar)
                        }
                        
                        if ( borrador_existe ) {
                            items.push(enviar_a_visto_bueno)
                            //items.push(radicar_borrador)
                        }
                        break
                }
            }        
        }        
    }

    return items
};

let items_borradores = function(componente, contexto) {    
    let items = [
        { id: 100, titulo: 'SALIDA', icon: "fas fa-angle-double-right" },
        { id: 101, titulo: 'INTERNO', icon: "fas fa-angle-double-down" },
    ]

    return items
};

export default {
    items_gestion: items_gestion,
    items_borradores: items_borradores,
    elemento_parametros: elemento_parametros
};