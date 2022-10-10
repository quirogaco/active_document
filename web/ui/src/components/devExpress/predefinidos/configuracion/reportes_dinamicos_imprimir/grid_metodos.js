let formulario = "formulario_reportes_imprime"

let metodos = {
    'dobleClick':  function(e) {
        let data = e.data
        this.$router.push({
            name: formulario,
            params: {
                "datos": JSON.stringify({
                    "datos_id": data.id,
                    "datos"   : data
                })                
            }
        })
    }
}

export default {
    metodos: metodos
}