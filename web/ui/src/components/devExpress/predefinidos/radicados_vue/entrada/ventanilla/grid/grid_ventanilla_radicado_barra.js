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
        // $forma.botonBarra({
        //     text : 'Radicar',
        //     icon : 'fas fa-cogs',
        //     click: function(e) {                       
        //         ejecutar(that)
        //     },
        // }),

        $forma.dropDownButtonBarra({
            text: "Acciones",
            width: "150px",
            items: [
                { 
                    value: 1,  
                    text: 'Radicar', 
                    icon: "fa-brands fa-wpforms"
                },
                {
                    value: 2,  
                    text: 'Imprimir sticker', 
                    icon: "fas fa-print"
                }
            ]
        })
    ]
}

export default {
    barraDef: barraDef
}