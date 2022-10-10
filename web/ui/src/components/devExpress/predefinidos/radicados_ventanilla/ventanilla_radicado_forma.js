import ArrayStore      from 'devextreme/data/array_store'
import { alert }       from 'devextreme/ui/dialog'
import visores_archivo from "../../../../librerias/visores_archivo.js"
import forma_objeto    from '../../forma/utilidades/forma_objeto.js'
import grupos_comunes  from '../radicados_comunes/grupos_comunes.js'

let plantillaAtributos = forma_objeto.plantillaAtributos()
let forma_id           = "ventanilla_radicado_forma"  
let tipo               = "VENTANILLA"  

window.atributos_campos = {
    forma_id: {}
}

let definicion = {
    'estructura'  : 'radicados_entrada',
    "titulo"      : "Ventanilla Radicación",
    'campos'      : grupos_comunes.campos(forma_id, tipo, plantillaAtributos),
    'columnas'    : 2,
    'plantillaAtributos': plantillaAtributos,
    "nombre_forma": forma_id,        
    "botones"     : {
        titulo_crea: "Radicar"
    },
    "metodos"     : {
        "retorno_envio": function(respuesta) {
            grupos_comunes.inicializa_forma(forma_id, tipo)  
            let nro_radicado = respuesta.resultados.datos.nro_radicado
            let resultado    = alert("Documento radicado con Nro " + nro_radicado, "Radicación" )
            /*
            let resultado    = confirm(("Descarga PDF con información registrada ?"), "Petición " + nro_radicado)
            resultado.then(dialogo => {
                if (dialogo == true) {
                    visores_archivo.ver_descarga_archivo({
                        archivo_id    : ("ENTRADA__" + nro_radicado), 
                        tipo_documento: "pdf", 
                        descarga      : 'si',
                        operacion     : 'radicado_pdf'
                    })   
                }
            }) 
            */
            window.$router.push({path: "ventanilla_radicado_grid"})     
        }
    },
    "eventos"     : {        
        "montado": function(objeto) {              
            grupos_comunes.montado(forma_id, tipo, grupos_comunes.campos_atributos)
            if (window.$correo_datos != undefined) {
                objeto.asignaAtributoDinamico("formaDatos", window.$correo_datos)
                let grid_anexo = window.$ns["ventanilla_radicado_forma_archivos_anexos"]  
                let anexos     = window.$correo_datos.archivos_anexos                              
                setTimeout(() => {
                    console.log("anexos:", anexos)  
                    console.log("grid_anexo:", grid_anexo)    
                    let fuenteAnexo = new ArrayStore({
                        data: anexos,
                        key : 'id'
                    })        
                    grid_anexo.option('dataSource', fuenteAnexo)   
                }, 3000)
            }               
        },

        "desmontado": function() {  
            window.$correo_datos = undefined
        },

        "inicializado": function(objeto) {}
    }
}

let componente = forma_objeto.forma_objeto_crud(definicion)

export default componente;