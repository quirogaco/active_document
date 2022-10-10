import { confirm }     from 'devextreme/ui/dialog';
import visores_archivo from "../../../../librerias/visores_archivo.js"
import forma_objeto    from '../../forma/utilidades/forma_objeto.js'
import grupos_comunes  from '../radicados_comunes/grupos_comunes.js'

let plantillaAtributos = forma_objeto.plantillaAtributos()
let forma_id           = "pqrs_radicado_forma"  
let tipo               = "PQRS"  

window.atributos_campos = {
    forma_id: {}
}

let definicion = {
    'estructura'  : 'radicados_entrada',
    "titulo"      : "PQRS Radicación",
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
            window.$router.push({path: "pqrs_radicado_grid"});                  
        }
    },
    "eventos"     : {        
        "montado": function(objeto) {  
            grupos_comunes.montado(forma_id, tipo, grupos_comunes.campos_atributos)
        },
        "inicializado": function(objeto) {}
    }
}

let componente = forma_objeto.forma_objeto_crud(definicion)

export default componente;