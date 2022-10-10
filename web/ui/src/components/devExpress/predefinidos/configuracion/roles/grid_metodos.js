let formulario = "roles_formulario"

let metodos = {
    onToolbarPreparing(e) {
        e.toolbarOptions.items.push({
            location: 'after',
            template: 'crearButton'
        })      
    },

    'dobleClick':  function(e) {
        let data = e.data
        this.$router.push({
            name: formulario,
            params: {
                "datos": JSON.stringify({
                    "datos_id": data.id,
                    "datos"   : data,
                    "modo"    : "modificar"
                })                
            }
        })
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