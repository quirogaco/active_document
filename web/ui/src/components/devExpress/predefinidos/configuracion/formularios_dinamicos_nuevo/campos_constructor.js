import { on }      from "devextreme/events"
import { confirm } from 'devextreme/ui/dialog'

import campos_tipo from './campos_tipo.js'

// Drag eventos para los campos
const drag_eventos = function(forma, campo_id, datos) {
    let campo = document.getElementById(campo_id)
    on(
        campo, 
        "dxdragstart", 
        { value: datos }, 
        function (event, extraParameters) {     
            console.log("dxdragstart-0:", event.data.value)
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
            console.log("dxdragend:", event.data.value)
            document.getElementById('cursor-style').remove()
            forma.datos_drag = null 
            // Si es un campo de la forma
            if (event.data.value != undefined)  { 
                console.log("DISEÑO................")
                forma.datos_drag = event.data.value
            }
            else {
                console.log("CAMPO..........")
            }
        }
    )
}

// Item creado
const item_listo_forma = function(forma) {
    const item_listo = function(objeto) {
        let componente = objeto.component
        let nombre     = componente.option("name")
        drag_eventos(forma, "_contiene_" + nombre)
    }

    return item_listo
}

// Foco del item
const item_foco = function(objeto) {
    let componente = objeto.component
    let nombre     = componente.option("name")
}

// Pierde Foco del item
const item_pierde_foco = function(objeto) {
    let componente = objeto.component
    let nombre     = componente.option("name")
}

const click_campo_accion = function(forma, tipo, campo_accion) {
    // Icono editar de un campo
    const click_campo_editar = function(objeto) {
        console.log("click_campo_edita ->:", campo,  objeto)    
    }

    // Icono borrar de un campo
    const click_campo_borrar = function(objeto) {
        let borrar = -1
        for (const indice in forma.campos) {
            let campo = forma.campos[indice]
            if (campo.name == campo_accion.name) borrar = indice;
        }
    
        if (borrar != -1) {            
            let resultado = confirm("Esta seguro borrar ? <b>" + campo_accion.name + "</b>", "Borrar campo!" );
            resultado.then((dialogo_resultado) => {
                if (dialogo_resultado == true) {
                    forma.campos.splice(borrar, 1)
                    forma.forma_diseno.repaint()  
                }
            })
        }
    }

    let accion = null
    if (tipo == "editar") accion = click_campo_editar;
    if (tipo == "borrar") accion = click_campo_borrar;

    return accion
}

let contador = 0

const campo_nuevo = function(forma, datos) {
    contador   += 1
    let nombre =  "campo_" + contador
    
    // Crea campo
    let nuevo_campo = campos_tipo.crear_definicion(nombre, forma.datos_drag)
    console.log("nuevo_campo:", nuevo_campo)
    
    //Asign botones editar, borrar
    nuevo_campo.editorOptions.botones = [                
        {
            location: "after",
            name    : "editar",
            options : {
                icon   : "fas fa-pen-square",
                onClick: click_campo_accion(forma, "editar", nuevo_campo)
            }
        },

        {
            location: "after",
            name    : "borrar",
            options : {
                icon   : "fas fa-trash-alt",
                onClick: click_campo_accion(forma, "borrar", nuevo_campo)
            }
        }
    ]
    nuevo_campo.editorOptions.onContentReady = item_listo_forma(forma)
    nuevo_campo.editorOptions.onFocusIn      = item_foco
    nuevo_campo.editorOptions.onFocusOut     = item_pierde_foco

    return nuevo_campo
}

const campo_insertar = function(forma, datos) {
    let nuevo_campo = campo_nuevo(forma, datos)
    
    if (forma.campos.length == 0) {
        forma.campos.push(nuevo_campo)
    }
    else {
        if (datos.sobre == true) {
            forma.campos.splice(datos.posicion, 0, nuevo_campo) 
        }
        else {
            forma.campos.splice((datos.posicion+1), 0, nuevo_campo) 
        }
    }        
    forma.forma_diseno.repaint()        
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
            //console.log("MOVER:", campo_datos, nombre_origen, campo_id, posicion, datos)
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
    campo_insertar: campo_insertar,
    campo_mover   : campo_mover,
    drag_eventos  : drag_eventos
}