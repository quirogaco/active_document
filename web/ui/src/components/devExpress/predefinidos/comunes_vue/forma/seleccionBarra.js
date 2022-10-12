
// Definición devexpress de un boton para barra de herrammientas
const seleccionBarraDef = function(atributos) {
    let opciones = {
        'widget': 'dxSelectBox',  
        'location': (
            atributos.location != undefined? atributos.location : 'after'
        ),  
        'options': {
            'width': (atributos.width != undefined? atributos.width : null),
            // 'items': [{
            //     value: 'CustomerStoreState',
            //     text: 'Grouping by State',
            //   }, {
            //     value: 'Employee',
            //     text: 'Grouping by Employee',
            //   }],
            'items': (atributos.items != undefined? atributos.items : []),   
            'displayExpr': (
                atributos.displayExpr != undefined? 
                atributos.displayExpr : 'text'
            ),
            'valueExpr': (
                atributos.valueExpr != undefined? 
                atributos.valueExpr : 'value'
            ),
            'value': (
                atributos.value != undefined? 
                atributos.value : null
            ),
            'onValueChanged': (
                atributos.onValueChanged != undefined? 
                atributos.onValueChanged : null
            )
        }        
    }
    
    return opciones
}

export default {
    campo: seleccionBarraDef
}