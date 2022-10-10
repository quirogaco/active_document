
let metodos = {
    onToolbarPreparing(e) {
        e.toolbarOptions.items.push({
            location: 'after',
            template: 'crearButton'
        })      
    },

    'dobleClick':  function(e) {
        let data = e.data
        data.mostrar_archivos = data.archivos[0]
        delete data.archivos
        this.$router.push({
            name: "pantalla_plantilla",
            params: {
                "datos": JSON.stringify({
                    "plantilla_id"   : data.id,
                    "plantilla_datos": data,
                    "modo"           : "modificar"
                })                
            }
        })
    },

    'crear':  function(e) {
        this.$router.push({
            name: "pantalla_plantilla",
            params: {
                "datos": JSON.stringify({
                    "plantilla_id"   : "",
                    "plantilla_datos": {},
                    "modo"           : "crear"
                })
            }            
        })
    },
}

export default {
    metodos: metodos
}