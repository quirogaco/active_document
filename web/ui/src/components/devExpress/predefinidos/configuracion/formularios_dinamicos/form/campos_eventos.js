import { on }  from "devextreme/events"

// Drag eventos para los campos
const drag_eventos = function(forma, campo_id, datos) {
    let campo = document.getElementById(campo_id)
    on(
        campo, 
        "dxdragstart", 
        { value: datos }, 
        function (event, extraParameters) {     
            const cursorStyle = document.createElement('style')
            // Si es un campo de la forma
            if (event.data.value != undefined)  { 
                //let nombre_origen = event.draggingElement.id                
                //if (nombre_origen.search("_contiene_") > -1) {   
                    cursorStyle.innerHTML = '*{cursor: move !important;}'
                //}
                
            }
            else { 
                // Es un elemento de diseño
                // Imagenes especificas
                cursorStyle.innerHTML = '*{cursor: move !important;}'
            }
            cursorStyle.id        = 'cursor-style'
            document.head.appendChild(cursorStyle)
        }
    )

    on(
        campo, 
        "dxdragend", 
        { value: datos }, 
        function (event, extraParameters) {
            document.getElementById('cursor-style').remove()
            forma.datos_drag = null 
            // Si es un campo de la forma
            if (event.data.value != undefined)  { 
                forma.datos_drag = event.data.value
            }
            else {
            }
        }
    )
}

const campo_posicion = function(forma, campo_id) {
    let posicion = -1
    for (const indice in forma.campos) {
        let campo = forma.campos[indice]
        if (campo.name == campo_id) posicion = indice;
    }

    return posicion
}

const campo_mover = function(forma, nombre_origen, datos) {
    // Debe existir mas de uno 
    if (forma.campos.length > 1) {
        let campo_id       = nombre_origen.replace("_contiene_", "")
        let posicion       = campo_posicion(forma, campo_id) 
        // No se mueve sobre si mismo     
        let nueva_posicion = parseInt(datos.posicion)  
        if ( posicion != nueva_posicion ) {
            let campo_datos = forma.campos[posicion]
            forma.campos.splice(posicion, 1)
            if (nueva_posicion == 0) {
                forma.campos.splice(0, 0, campo_datos) 
            }
            else {                
                if (datos.sobre == true) {
                    forma.campos.splice(nueva_posicion, 0, campo_datos) 
                }
                else {
                    forma.campos.splice((nueva_posicion+1), 0, campo_datos) 
                }
            }
            forma.forma_diseno.repaint()
        }
    }  
}

export default {
    campo_mover   : campo_mover,
    drag_eventos  : drag_eventos
}