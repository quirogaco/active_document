
let metodos = {
    'dobleClick':  function(e) {
        console.log("e.data:", e.data)
        window.$correo_datos = {
            "tercero_correo_electronico": e.data["correo_origen"],
            "asunto"                    : e.data["asunto"],
            "fecha_documento"           : e.data["fecha_correo"],
            "archivos_anexos"           : e.data["archivos"]
        }
        this.$router.push({
            name: "ventanilla_radicado_forma",
            params: {
                peticion_id  : e.data.id
            }
        })        
    },
}

export default {
    metodos: metodos
}