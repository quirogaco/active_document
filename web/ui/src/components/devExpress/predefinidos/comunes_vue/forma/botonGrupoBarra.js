import basicos      from './basicos.js'
import eventos      from './eventos.js'
import validaciones from './validaciones.js'

// Definición devexpress de un boton para barra de herrammientas
const botonGrupoBarraDef = function(atributos) {
    let opciones = {
        'widget'  : 'dxButtonGroup',  
        'location': (atributos.location != undefined? atributos.location : 'after'),  
        'options' : {
            'width'  : (atributos.width != undefined? atributos.width : null),
            'items'  : (atributos.items != undefined? atributos.items : []),   
            'text'   : (atributos.text != undefined? atributos.text : '...'),  
            'icon'   : (atributos.icon != undefined? atributos.icon : null),  
            'type'   : (atributos.type != undefined? atributos.type : 'default'),  
            'onClick': (atributos.click != undefined? atributos.click : null), 
        }        
    }
    
    return opciones
}

export default {
    campo: botonGrupoBarraDef
}