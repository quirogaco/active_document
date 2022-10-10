import forma_objeto           from '../../forma/utilidades/forma_objeto.js'
import grupos_comunes_interno from '../radicados_comunes/grupos_comunes_interno.js'

let plantillaAtributos = forma_objeto.plantillaAtributos()
let forma_id           = "ventanilla_interno_forma"  
let tipo               = "VENTANILLA"  

window.atributos_campos = {
    forma_id: {}
}

let definicion = {
    'estructura'  : 'radicados_interno',
    "titulo"      : "Ventanilla Radicación Internos",
    'campos'      : grupos_comunes_interno.campos(forma_id, tipo, plantillaAtributos),
    'columnas'    : 1,
    'plantillaAtributos': plantillaAtributos,
    "nombre_forma": forma_id,    
    "botones"     : {
        titulo_crea: "Radicar Interno"        
    },
    "metodos"     : {
        "retorno_envio": function(respuesta) {
            grupos_comunes_interno.retorno_envio(forma_id, tipo, respuesta)
        }
    },
    "eventos"     : {        
        "montado": function(objeto) {  
            grupos_comunes_interno.montado(forma_id, tipo, grupos_comunes_interno.campos_atributos)
            console.log("retorno envio interno:", window.$salida_gestion, window.$emergente_gestion)
        },

        "inicializado": function(objeto) {}
    }
}

let componente = forma_objeto.forma_objeto_crud(definicion)

export default componente;