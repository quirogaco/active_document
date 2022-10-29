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

    const call = function(event) {
        console.log("CALL:", event.itemData);
        console.log(that)
        that.re_render_popup();
    }

    return [
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
            ],
            onItemClick: call
        })
    ]
}

export default {
    barraDef: barraDef
}