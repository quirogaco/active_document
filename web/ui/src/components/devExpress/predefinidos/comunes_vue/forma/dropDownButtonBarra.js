const dropDownButtonDef = function(attributes) {
    let opciones = {
        'widget'  : 'dxDropDownButton',  
        'location': (
            attributes.location != undefined? 
            attributes.location : 'after'
        ),          
        'options' : {
            'width': (attributes.width != undefined? attributes.width : null),
            // items      : [
            //     { value: 1,  text: 'Imprimir sticker', icon: "fas fa-print" }
            // ],
            'items': (attributes.items != undefined? attributes.items : []), 

            'displayExpr': (
                attributes.displayExpr != undefined? 
                attributes.displayExpr : 'text'
            ),

            'valueExpr': (
                attributes.valueExpr != undefined? 
                attributes.valueExpr : 'value'
            ),

            'icon': (
                attributes.icon != undefined? 
                attributes.icon : "fa-solid fa-rectangle-list"                
            ),

            'stylingMode': (
                attributes.stylingMode != undefined? 
                attributes.stylingMode : 'text'
            ),

            'text': (
                attributes.text != undefined? 
                attributes.text : ''
            ),

            'type': (
                attributes.type != undefined? 
                attributes.type : 'default'
            ),

            'elementAttr': (
                attributes.elementAttr != undefined? 
                attributes.elementAttr : {
                    class: "silver  rounded"
                }
            ),

            'value': (
                attributes.value != undefined? 
                attributes.value : null
            ),
            
            'onItemClick': (
                attributes.onItemClick != undefined? 
                attributes.onItemClick : null
            ),

        }        
    }
    
    return opciones
}

export default {
    campo: dropDownButtonDef
}