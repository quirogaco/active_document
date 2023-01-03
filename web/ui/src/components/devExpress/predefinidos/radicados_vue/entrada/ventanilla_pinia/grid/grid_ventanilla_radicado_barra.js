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
        switch (event.itemData.value) {
            case 1:  
                $save_params("pqrs_filtro", "DOCUMENTO");   
                that.radicar(event)
                break
                
            case 2:     
                that.cargar_documento(event)
                break
        }
    }

    return [
         $forma.dropDownButtonBarra({
            text: "Acciones",
            width: "200px",
            items: [
                { 
                    value: 1,  
                    text: 'Radicar', 
                    icon: "fa-brands fa-wpforms"
                },

                {
                    value: 2,  
                    text: 'Cargar PDF principal', 
                    icon: "fas fa-file-upload"
                },

                // {
                //     value: 2,  
                //     text: 'Imprimir sticker', 
                //     icon: "fas fa-print"
                // }
            ],
            onItemClick: call
        })
    ]
}

export default {
    barraDef: barraDef
}