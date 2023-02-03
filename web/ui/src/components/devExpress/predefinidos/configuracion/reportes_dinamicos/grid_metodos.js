let formulario = "formulario_reportes_dinamicos";

let metodos = {
    onToolbarPreparing(e) {
        e.toolbarOptions.items.push({
            location: 'after',
            template: 'crearButton'
        })      
    },

    'dobleClick':  function(e) {
        let data = e.data;
        let datos = {
            "reporte": data,
            "modo": "modificar"            
            //"modo": "consulta",
            //"llamado_por": "ventanilla_radicado_grid"
        };
        $lib.call_component_storage(
            formulario,
            {"datos": datos}
        )

        // this.$router.push({
        //     name: formulario,
        //     params: {
        //         "datos": JSON.stringify({
        //             "datos_id": data.id,
        //             "datos"   : data,
        //             "modo"    : "modificar"
        //         })                
        //     }
        // })
    },

    'crear':  function(e) {
        let datos = {
            "reporte": {},
            "modo": "crear"
        };
        $lib.call_component_storage(
            formulario,
            {"datos": datos}
        )

        // this.$router.push({
        //     name: formulario,
        //     params: {
        //         "datos": JSON.stringify({
        //             "datos_id": "",
        //             "datos"   : {},
        //             "modo"    : "crear"
        //         })
        //     }            
        // })
    },
}

export default {
    metodos: metodos
}