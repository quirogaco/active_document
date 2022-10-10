
let metodos = {
    onToolbarPreparing(e) {
        e.toolbarOptions.items.push({
            location: 'after',
            template: 'crearButton'
        })      
    },

    'dobleClick':  function(e) {
        // Pasar ela arbol no tiene sentido y es demasiado pesado., debe cargarse en la pantalla
        this.$router.push({
            name: "tvd_pantalla",
            params: {
                "datos": JSON.stringify({
                    "tvd_id"   : e.data.id,
                    "tvd_datos": e.data,
                    "modo"     : "modificar"
                })                
            }
        })
    },

    'crear':  function(e) {
        this.$router.push({
            name: "tvd_pantalla",
            params: {
                "datos": JSON.stringify({
                    "tvd_id"   : "",
                    "tvd_datos": {},
                    "modo"     : "crear"
                })
            }            
        })
    },
}

export default {
    metodos: metodos
}