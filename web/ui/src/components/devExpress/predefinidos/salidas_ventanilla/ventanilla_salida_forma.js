import forma_objeto          from '../../forma/utilidades/forma_objeto.js'
import grupos_comunes        from '../radicados_comunes/grupos_comunes.js'
import grupos_comunes_salida from '../radicados_comunes/grupos_comunes_salida.js'

let plantillaAtributos = forma_objeto.plantillaAtributos()
let forma_id           = "ventanilla_salida_forma"  
let tipo               = "VENTANILLA"  

window.atributos_campos = {
    forma_id: {}
}

let definicion = {
    'estructura'  : 'radicados_salida',
    "titulo"      : "Ventanilla Radicación Salidas",
    'campos'      : grupos_comunes_salida.campos(forma_id, tipo, plantillaAtributos),
    'columnas'    : 2,
    'plantillaAtributos': plantillaAtributos,
    "nombre_forma": forma_id,    
    "metodos"     : {
        "retorno_envio": function(respuesta) {
            grupos_comunes_salida.retorno_envio(forma_id, tipo, respuesta)            
            if (window.$salida_gestion == "SI") {
                window.$emergente_gestion.hide()
                window.$router.push({path: "gestion_basica_grid"})
            }
        }
    },
    "eventos"     : {        
        "montado": function(objeto) {  
            grupos_comunes_salida.montado(forma_id, tipo, grupos_comunes_salida.campos_atributos)
            console.log("retorno envio:", window.$salida_gestion, window.$emergente_gestion)
        },

        "inicializado": function(objeto) {}
    }
}

let componente = forma_objeto.forma_objeto_crud(definicion)

export default componente;