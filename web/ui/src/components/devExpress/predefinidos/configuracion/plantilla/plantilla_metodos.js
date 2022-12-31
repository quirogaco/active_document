
let metodos = {
    onToolbarPreparing(e) {
        e.toolbarOptions.items.push({
            location: 'after',
            template: 'crearButton'
        })      
    },

    'dobleClick':  function(e) {
        let data = e.data;
        console.log("e.data:", e.data)
        data.mostrar_archivos = data.archivos[0];
        //console.log("data.mostrar_archivos:", data.mostrar_archivos)
        delete data.archivos;
        $lib.call_component_storage(
            "pantalla_plantilla",
            {                
                "plantilla_id": data.id,
                "plantilla_datos": data,
                "modo": "modificar"                
            }
        )
        // this.$router.push({
        //     name: "pantalla_plantilla",
        //     params: {
        //         "datos": JSON.stringify({
        //             "plantilla_id"   : data.id,
        //             "plantilla_datos": data,
        //             "modo"           : "modificar"
        //         })                
        //     }
        // })
    },

    'crear':  function(e) {
        $lib.call_component_storage(
            "pantalla_plantilla",
            {
                "datos": {
                    "plantilla_id": "",
                    "plantilla_datos": {},
                    "modo": "crear"
                }
            }
        )
        // this.$router.push({
        //     name: "pantalla_plantilla",
        //     params: {
        //         "datos": JSON.stringify({
        //             "plantilla_id"   : "",
        //             "plantilla_datos": {},
        //             "modo"           : "crear"
        //         })
        //     }            
        // })
    },
}

export default {
    metodos: metodos
}