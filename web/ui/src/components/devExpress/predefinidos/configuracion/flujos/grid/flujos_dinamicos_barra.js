const ejecutar = function(that) {
    let parametros = {
        "id"   : null,
        "datos": {},         
        "mode" : "nuevo",
        "return": that.name    
    } 
    that.llamar_forma(parametros);
}

let barraDef = function(that) {
    return [
        $forma.botonBarra({
            text : 'Crea flujo',
            icon : 'fas fa-cogs',
            click: function(e) {
                //let seleccion = that.DataGridCmp.selectedRecords(1);
                //if (seleccion.status == true) {
                //    ejecutar(seleccion, that)
                //}          
                ejecutar(that)
            },
        }),
    ]
}

export default {
    barraDef: barraDef
}