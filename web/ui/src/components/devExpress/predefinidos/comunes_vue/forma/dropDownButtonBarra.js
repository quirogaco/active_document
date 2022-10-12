const dropDownButtonDef = function(atributos) {
    let opciones = {
        'widget'  : 'dxDropDownButton',  
        'location': (atributos.location != undefined? atributos.location : 'after'),  
        'options' : {
            'width': (atributos.width != undefined? atributos.width : null),
            // items      : [
            //     { value: 1,  text: 'Imprimir sticker', icon: "fas fa-print" }
            // ],
            'items': (atributos.items != undefined? atributos.items : []),   
            'displayExpr': (
                atributos.displayExpr != undefined? 
                atributos.displayExpr : 'text'
            ),
            'keyExpr': (
                atributos.valueExpr != undefined? 
                atributos.valueExpr : 'value'
            ),
            'icon': (
                atributos.icon != undefined? 
                atributos.icon : "fa-solid fa-rectangle-list"                
            ),
            'onItemClick': (
                atributos.onItemClick != undefined? 
                atributos.onItemClick : null
            ),
            'stylingMode': (
                atributos.stylingMode != undefined? 
                atributos.stylingMode : 'text'
            ),
            'text': (
                atributos.text != undefined? 
                atributos.text : ''
            ),
            'type': (
                atributos.type != undefined? 
                atributos.type : 'default'
            ),
            'elementAttr': (
                atributos.elementAttr != undefined? 
                atributos.elementAttr : {
                    class: "silver  rounded"
                }
            )
        }        
    }
    
    return opciones
}

export default {
    campo: dropDownButtonDef
}