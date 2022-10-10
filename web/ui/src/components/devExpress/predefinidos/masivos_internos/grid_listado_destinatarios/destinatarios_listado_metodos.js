
let metodos = {   
    onToolbarPreparing(e) {
        e.toolbarOptions.items.push({
            location: 'after',
            template: 'crearButton'
        })      
    },

    'dobleClick':  function(e) {
        let datos = {
            "id"            : e.data.id,
            "dependencia_id": e.data.dependencia_id,
            "detalle"       : e.data.detalle,
            "destinatarios" : e.data.destinatarios
        }
        console.log("e.data:", e.data.destinatarios)
        this.$router.push(
            {
                name: "ventana_listado_interno",
                params: {
                    "datos": JSON.stringify({
                        "listado_datos": datos,
                        "modo"         : 'modificar'
                    })
                }
            }
        )
    },

    crear: function(e) {
        this.$router.push(
            {
                name: "ventana_listado_interno",
                params: {
                    "datos": JSON.stringify({
                        "listado_datos": {},
                        "modo": 'crear'
                    })
                }
            }
        )
    },

}

export default {
    metodos: metodos
}