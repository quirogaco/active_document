
// Definición devexpress de un boton para barra de herrammientas
const botonBarraDef = function(atributos) {
    let opciones = {
        'widget'  : 'dxButton',  
        'location': (atributos.location != undefined? atributos.location : 'after'),  
        'options' : {
            'width'  : (atributos.width != undefined? atributos.width : null),
            'text'   : (atributos.text != undefined? atributos.text : '...'),  
            'icon'   : (atributos.icon != undefined? atributos.icon : null),  
            'type'   : (atributos.type != undefined? atributos.type : 'default'),  
            'onClick': (atributos.click != undefined? atributos.click : null), 
        }        
    }
    
    return opciones
}

export default {
    campo: botonBarraDef
}