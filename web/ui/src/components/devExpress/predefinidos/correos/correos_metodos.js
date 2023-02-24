
let metodos = {
    'dobleClick':  function(e) {
        console.log("e.data CORRESO:", e.data)
        let datos = {
            "_modo_": "CORREO",
            "tercero_correo_electronico": e.data["correo_origen"],
            "asunto": e.data["asunto"],
            "fecha_documento": e.data["fecha_correo"],
            "archivos_anexos": e.data["archivos"]
        }

        $lib.call_component_storage(
            "ventanilla_radicado_forma",
            {"datos": datos}
        )
    }
}

export default {
    metodos: metodos
}