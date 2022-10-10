import notify from 'devextreme/ui/notify'

import forma_objeto      from '../../../forma/utilidades/forma_objeto.js'
import comunes_generales from '../../radicados_comunes/comunes_generales.js'
import comunes_interno   from '../../radicados_comunes/comunes_interno.js'
import comunes_respuesta from '../../radicados_comunes/comunes_respuesta.js'

let plantillaAtributos = forma_objeto.plantillaAtributos()
let forma_id           = "ventanilla_salida_forma"  
let tipo               = "VENTANILLA"  

window.atributos_campos = {
    forma_id: {}
}

let campos = [
    forma_objeto.grupo_objeto({
        'titulo'     : 'Información basica documento',
        'elementos'  : [            
            comunes_generales.fecha_documento,   
            //comunes_generales.nro_folios,
            comunes_generales.asunto, 
            comunes_generales.expediente_id, 
            comunes_generales.tipo_id
        ]
    }),

    forma_objeto.grupo_objeto({
        'titulo'     : 'Información remitente',
        'elementos'  : [            
            comunes_interno.dependencia_envia_id,
            comunes_interno.funcionario_envia_id
        ]
    }),

    /*
    forma_objeto.grupo_objeto({
        'titulo'     : 'Información destinatario',
        'elementos'  : [            
            comunes_interno.dependencia_recibe_id,
            comunes_interno.funcionario_recibe_id
        ]
    }),
    */

    /*
    forma_objeto.grupo_objeto({
        'titulo'     : 'Información envio',
        'elementos'  : [            
            comunes_respuesta.tipo_firma,
            comunes_generales.medio_notificacion_abierto,
        ]
    }),
    */

    forma_objeto.grupo_objeto({
        'titulo'     : 'Información destinatarios',
        'elementos'  : [            
            comunes_respuesta.listado_destinatario_id,
            comunes_respuesta.plantilla_id
        ]
    }),

]


const retorna_masivo = function() {
    window.$ocultar_esperar()
    window.$sistema["notifica"]("Masivo de INTERNOS generado!!", "success")
}

let definicion = {
    'estructura'  : 'radicados_interno',
    "titulo"      : "Ventanilla Radicación Internos",
    'campos'      : campos,
    'columnas'    : 1,
    'plantillaAtributos': plantillaAtributos,
    "nombre_forma": forma_id,    
    "botones"     : {
        crea       : true,
        titulo_crea: "Generar masivo Interno",
        modifica   : false,
        elimina    : false,
        regresa    : false,
    },
    "metodos"     : {
        "envia_datos": function(accion, datosForma) {              
            let parametros = {
                "accion": "generar_interno",
                "datos" : datosForma
            }    
            window.$mostrar_esperar("Radicando!, por favor espere..")    
            window.$f["http"].llamadoRestPost( this.urlCompleta, parametros, retorna_masivo, "")      
        },

        "retorno_envio": function(respuesta) {
            //window.$ocultar_esperar()
            this.notify("Operación realizada correctamente", "success")
        },
    },
    "eventos"     : {        
        "montado": function(objeto) {
            console.log(objeto)
            // Url de servicios
            objeto.urlCompleta = window.$direcciones.servidorDatos + '/masivos_salidas';
            objeto.notify = notify   
        },

        "inicializado": function(objeto) {}
    }
}

let componente = forma_objeto.forma_objeto_crud(definicion)

export default componente;