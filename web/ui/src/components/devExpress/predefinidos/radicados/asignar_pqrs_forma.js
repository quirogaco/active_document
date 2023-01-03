import ArrayStore              from 'devextreme/data/array_store'
import forma_objeto            from '../../forma/utilidades/forma_objeto.js'
import consulta_basicos        from '../radicados_comunes/consulta_basicos.js'
import consulta_identificacion from '../radicados_comunes/consulta_identificacion.js'
import comunes_generales       from '../radicados_comunes/comunes_generales.js';
import comunes_tramite         from '../radicados_comunes/comunes_tramite.js';
import grupos_accion           from './grupos_accion.js';
import dialogos                from '../../../../librerias/dialogos.js'
import consulta_anexos         from '../radicados_comunes/consulta_anexos.js'

let plantillaAtributos = forma_objeto.plantillaAtributos()
let forma_id           = "asignar_pqrs_forma"  

let grupoPeticion  = forma_objeto.grupo_objeto({
    'titulo'     : 'Asignación',
    'elementos'  : [
        comunes_tramite.ventanilla,
        comunes_tramite.dependencia_pqrs,
        comunes_tramite.peticion_id_pqrs(forma_id),
        comunes_tramite.horas_dias,
        comunes_tramite.total_tiempo,
        comunes_tramite.prioridad,
        comunes_tramite.reserva,
        comunes_tramite.tema_dependencia,
        comunes_tramite.subtema_dependencia,
        comunes_tramite.copia_usuarios_id,
        comunes_tramite.copia_grupos_id
    ]
});

let grupoAnexos = forma_objeto.grupo_objeto({
    'titulo'     : 'Archivos anexos',
    'elementos'  : [
        consulta_anexos.grupoAnexos,
        comunes_generales.mensaje_archivo(plantillaAtributos),
        comunes_generales.archivos_anexos(plantillaAtributos)        
    ]
});

let campos = [
    consulta_basicos.grupoBasico,
    consulta_identificacion.grupoIdentificacion,
    grupoPeticion,
    grupoAnexos,
    grupos_accion.grupoAcciones
]

let inicializa_forma = function() {
    // Tipo de tiempo, total tiempo
    $lib.forma_atributo_items(forma_id, ["gestion_horas_dias", "gestion_total_tiempo"], "disabled", true)
    //$lib.forma_componente_opcion(forma_id, "ventanilla", "value", "NO")
    //$lib.forma_componente_opcion(forma_id, "gestion_prioridad", "value", "MEDIA") 
    //$lib.forma_componente_opcion(forma_id, "reserva", "value", "NO")
    //console.log("window.$ns['asignar_pqrs_forma']:", window.$ns['asignar_pqrs_forma'])
    window.scroll(0,0)
}

let definicion = {
    'estructura'  : 'pqrs_asigna_responsable',
    "titulo"      : "Asignación y traslado de PQRSD",
    'campos'      : campos,
    'plantillaAtributos': plantillaAtributos,
    "nombre_forma": "asignar_pqrs_forma",
    'columnas'    : 2,
    'botones'     : {
        crea    : false, 
        modifica: false, 
        elimina : false, 
        regresa : false
    },

    "metodos"     : {
        "retorno_envio": function(respuesta) {
            inicializa_forma()      
            dialogos.miMensaje("Asignación", (
                "Radicado asignado"
            ))
            window.$router.push({path: "asignar_pqrs_grid"})
        },

        "cambiaDatosEvento": function(forma, datos) {
            let grid_anexo = window.$ns["asignar_pqrs_forma_archivos"]  
            let archivos   = datos["archivos"]   
            let fuenteAnexo = new ArrayStore({
                data: archivos,
                key : 'id'
            })        
            grid_anexo.option('dataSource', fuenteAnexo)        
        }
    },

    "eventos"     : {        
        "montado": function(objeto) {   
            inicializa_forma()            
        },

        "contenido_listo": function(objeto, forma, datos) {}
    }
}

let componente = forma_objeto.forma_objeto_crud(definicion);

export default componente;