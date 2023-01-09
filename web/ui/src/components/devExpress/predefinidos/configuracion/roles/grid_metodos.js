let formulario = "roles_formulario"

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
            "datos": e.data,
            "datos_id": data.id,
            "modo": "modificar"
        };
        $lib.call_component_storage(
            "roles_formulario",
            {"datos": datos}
        )
    },

    'crear':  function(e) {
        this.$router.push({
            name: formulario,
            params: {
                "datos": JSON.stringify({
                    "datos_id": "",
                    "datos"   : {},
                    "modo"    : "crear"
                })
            }            
        })
    },
}

export default {
    metodos: metodos
}