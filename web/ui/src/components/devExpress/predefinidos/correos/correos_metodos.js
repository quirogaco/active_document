import estructuras from '../../../../librerias/estructuras.js';

let metodos = {
    'dobleClick':  async function(e) {        
        let record = await estructuras.leer_registro_id("correos_descargados", e.data.id)
        //console.log("record CORRESO:", record)
        let datos = {
            "_modo_": "CORREO",
            "tercero_correo_electronico": record["correo_origen"],
            "asunto": record["asunto"],
            "fecha_documento": record["fecha_correo"],
            "archivos_anexos": record["archivos"]
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