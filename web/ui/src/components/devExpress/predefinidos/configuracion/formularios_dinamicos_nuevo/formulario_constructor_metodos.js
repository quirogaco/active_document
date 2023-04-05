import { on }             from "devextreme/events"
import campos_constructor from './campos_constructor.js'

const calcula_posiciones = function(forma, drop_x, drop_y) {
    let distancia = 999999
    let posicion  = -1
    let sobre     = false
    for (const indice in forma.campos) { 
        let campo           = forma.campos[indice]                                
        let elemento_actual = document.getElementById(campo.name).getBoundingClientRect()                      
        const x2 = elemento_actual.x + elemento_actual.width
        const y2 = elemento_actual.y + elemento_actual.height
        const x_distancia = drop_x - x2
        const y_distancia = drop_y - y2

        const distancia_actual = Math.sqrt(
            (x_distancia * x_distancia) + (y_distancia * y_distancia)
        )
    
        if (distancia_actual < distancia ) {
            sobre       = false
            posicion    = indice
            distancia   = distancia_actual
            const ancho = elemento_actual.x + elemento_actual.width
            const alto  = elemento_actual.y + elemento_actual.height
            if ( (drop_x > elemento_actual.x ) &&  (drop_x < ancho ) ) {
                if ( (drop_y > elemento_actual.y ) &&  (drop_y < alto ) ) {
                    sobre = true
                }
            }
        }
    }    
    
    return {"distancia": distancia, "posicion": posicion, "sobre": sobre}
}

// Drop forma
const drop_forma = function(forma) {
    let forma_elemento = document.getElementById("constructor_forma_id")   

    on(
        forma_elemento, 
        "dxdrop", 
        { value: "SOBRE LA FORMA" }, 
        function (event, extraParameters) {
            console.log("drop forma", forma.datos_drag)
            let nombre_origen = event.draggingElement.id
            let datos = calcula_posiciones(forma, event.x, event.y) 
            if (nombre_origen.search("_contiene_") > -1) {                
                campos_constructor.campo_mover(forma, nombre_origen, datos)
            }
            else {
                campos_constructor.campo_insertar(forma, datos)
            }   
        }
    )
}

// Calcula tamano de forma
const calcula_forma_tamano = function(forma) {
    let clase_base = "container-fluid border border-2 p-1 col-sm-"
    let columnas   = 7

    // Si muestra tipos de campos
    if (forma.muestra_elementos == false) columnas += 2;
    // Si muestra atributos de campos
    if (forma.muestra_atributos == false) columnas += 3;

    forma.clase_forma = (clase_base + columnas)
}

let metodos = {
    forma_lista(objeto) {},

    grupo_botones_listo(objeto) {
        for (const indice in this.campos_tipo) {
            let campo = this.campos_tipo[indice]
            campos_constructor.drag_eventos(this, campo.elementAttr.id, campo)       
        }
    }
}    

export default {
    metodos             : metodos,
    drop_forma          : drop_forma,
    calcula_forma_tamano: calcula_forma_tamano
}