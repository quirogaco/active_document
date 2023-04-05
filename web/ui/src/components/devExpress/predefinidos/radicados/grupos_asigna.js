import forma_objeto          from '../../forma/utilidades/forma_objeto.js';
import utilidades_estructura from '../../../../librerias/utilidades_estructura.js';
import dialogos              from '../../../../librerias/dialogos.js';

const crea_grupoAsignacion = function(plantillaAtributos_asigna) {
    // ##############################
    //  DEPENDENCIA, TEMA Y SUBTEMA #
    // ##############################

    // Dependencia responsable
    let dependencia_asigna = forma_objeto.select_objeto({
        "titulo"            : "Dependencia responsable", 
        "fuente"            : "dependencias",
        "campo"             : "dependencia_asignada",
        "nombre"            : "dependencia_asignada",
        "busqueda_expresion": "nombre_completo",
        "muestra_expresion" : "nombre_completo",
        "registrar"         : "si",
        "obligatorio"       : "si",  
        "eventos"           : {
            "seleccion_cambiada": async function(objeto) {
                // Dato seleccionado
                let id         = $lib.cargaAtributo(objeto.selectedItem, 'id', null); 
                let datos      = await utilidades_estructura.leer_registro_id("dependencias", id);  
                
                // Limpia temas y subtemas
                $lib.forma_componentes_opcion("asignar_pqrs_forma", ["tema_dependencia", "subtema_dependencia"], "value", null)    
                            
                // Fuentes tema y subtema
                let tds = $lib.traer_fuente_datos("asignar_pqrs_forma", "tema_dependencia")
                let sds = $lib.traer_fuente_datos("asignar_pqrs_forma", "subtema_dependencia");            
                // Limpia los datos de tema y subtema   
                tds.searchOperation("NO_BUSCAR")
                sds.searchOperation("NO_BUSCAR")            
                // Carga información
                if (datos != null) {  
                    // Limpia NO_BUSCAR
                    tds.searchOperation("") 
                    sds.searchOperation("")          
                    if ( $lib.sin_valor.indexOf(datos.pqrs_id) > -1 ) {        
                        dialogos.miMensaje("Información incompleta", (
                            datos.nombre_completo + " - " +  "No tiene responsable de manejo de PQRS"
                        ))
                        $lib.forma_componente_opcion("asignar_pqrs_forma", "dependencia_asignada", "value", null) 
                    } 
                    else{
                        // Fitro de tema
                        tds.filter(["dependencia_id", "=", id])                    
                    }                                  
                }    

                // Carga datos
                tds.reload()
                sds.reload()
            }
        }
    })

    // Tema Dependencia
    let tema_dependencia  = forma_objeto.select_objeto({
        "titulo"            : "Tema de la dependencia", 
        "fuente"            : "temas",
        "campo"             : "tema_dependencia",
        "nombre"            : "tema_dependencia",
        "registrar"         : "si",
        "obligatorio"       : "si",  
        "eventos"           : {
            "seleccion_cambiada": async function(objeto) {
                // Dato seleccionado tema
                let id = $lib.cargaAtributo(objeto.selectedItem, 'id', null)                
                // Carga datos Subtema
                let sds = $lib.traer_fuente_datos("asignar_pqrs_forma", "subtema_dependencia")  
                sds.searchOperation("NO_BUSCAR")            
                if (id != null) {
                    sds.searchOperation("")          
                    sds.filter(["tema_id", "=", id])       
                }
                sds.reload()

                // Subtemas
                $lib.forma_componentes_opcion("asignar_pqrs_forma", ["subtema_dependencia"], "value", null)                                               
            }
        }
    })

    // SubTema Dependencia
    let subtema_dependencia  = forma_objeto.select_objeto({
        "titulo"            : "Subtema de la dependencia", 
        "fuente"            : "subtemas",
        "campo"             : "subtema_dependencia",
        "nombre"            : "subtema_dependencia",
        "registrar"         : "si",
        "obligatorio"       : "si",  
        "eventos"           : {}
    })

    let grupoDependencia = forma_objeto.grupo_objeto({
        'titulo'     : 'Dependencia',
        'nombre'     : 'grupo_asignacion',
        "obligatorio": "si",  
        'elementos': [
            dependencia_asigna,
            tema_dependencia,
            subtema_dependencia
        ]
    });

    // #######################################
    //  TRAMITE, PRIORIDAD, ASUNTO, ARCHIVOS #
    // #######################################

    // Tipo de tramite
    let tipo_tramite = forma_objeto.select_objeto({
        "titulo"     : "Tipo de petición", 
        "fuente"     : "tipo_peticiones",
        "campo"      : "tipo_peticion",
        "nombre"     : "tipo_peticion",
        "registrar"  : "si",
        "obligatorio": "si",  
        "filtros"   : [
            ["estado_", "=", "ACTIVO"], 
            ["pqrs", "=", "si"]
        ],
        "eventos"           : {
            "seleccion_cambiada": async function(objeto) {},
            "recibe_foco"       : function (objeto) {},
            "cargar_datos_antes": function (opciones, idComponente) { },
        }
    })

    let prioridad = forma_objeto.radio_objeto({
        "campo"      : "prioridad",
        "titulo"     : "Prioridad de gestión", 
        "elementos"  : ["ALTA", "MEDIO", "NORMAL"],    
        "obligatorio": "si",      
    })

    let acepta_archivos = ["doc", "docx", "xls", "xlsx", "gif", "png", "bmp", "avi", "mp3", "pdf", "zip"];
    let archivos_anexos = function(plantillaAtributos) {
        let archivo = forma_objeto.archivo_objeto(
            {
                "campo"      : "archivos_anexos",
                "titulo"     : "Anexos adicionales", 
                "varios"     : "si",
                "maximo"     : 5000000,
                "acepta"     : acepta_archivos,                        
            }, 
            plantillaAtributos
        )

        return archivo;
    };

    let anotaciones = forma_objeto.campo_objeto({
        'campo'      : 'asunto',
        'tipo'       : 'dxTextArea',
        'titulo'     : 'Anotaciones',  
        //'expandir'   : 2,
        'obligatorio': 'si',
        'alto'       : '60',
        'maximo'     : 2048    
    })

    let grupoTramite = forma_objeto.grupo_objeto({
        'titulo'   : 'Petición',
        'nombre'   : 'grupo_peticion',
        'elementos': [    
            tipo_tramite,    
            prioridad,
            anotaciones,
            archivos_anexos(plantillaAtributos_asigna)
        ]
    });

    let boton_asigna = forma_objeto.boton_objeto({
        'titulo'   : 'Asignar',
        'tipo'     : 'default',   
        //'ancho'    : "100%", 
        'evt_click': function() {
            /*
            let forma = $lib.traer_componentes("asignar_pqrs_forma");
            let formaInstancia   = forma.referencia.$_instance;        
            let validacion       = formaInstancia.validate();
            let datosForma       = componente.leeeAtributoDinamico("formaDatos");
            console.log("asignar_pqrs_forma", datosForma)
            */

            window.$f.componentes_llamados_crud.enviaForma("asignar_pqrs_forma", "crea_radicado_gestion")
        },
    });

    let grupoAsignacion = forma_objeto.grupo_objeto({
        'titulo'   : 'Asignación responsable',
        'nombre'   : 'grupo_asignacion',
        'columnas' : 2,
        'expandir' : 3,
        'elementos': [
            grupoDependencia,
            grupoTramite,
            boton_asigna
        ]
    });

    return grupoAsignacion
}

export default {
    crea_grupoAsignacion: crea_grupoAsignacion
}