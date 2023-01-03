import visores_archivo from "../../../../../../librerias/visores_archivo.js"

let metodos = {
    onToolbarPreparing(e) {
        e.toolbarOptions.items.push({
            location: 'after',
            template: 'radicarButton'
        })          
    },

    'radicar':  function(e) {
        $save_params("pqrs_filtro", "PQRSD");
        $save_params("_radica_dependencia_", {"responsable": "pqrs_id"});
        this.$router.push({
            name: "pqrs_radicado_forma",
            params: {
                "datos": JSON.stringify({})                
            }
        })
    },

    'columna_doble_click':  function(e) {
        let data = e.data
        if (e.column.dataField == "clase_radicado") {
            if (data.pdf_base.id !== undefined) {
                visores_archivo.ver_descarga_archivo({
                    titulo_general: "Consulta de Documentos/Anexos RADICADO",
                    archivo_id    : data.pdf_base.id, 
                    tipo_documento: data.pdf_base.tipo_archivo, 
                    titulo        : data.pdf_base.detalle,
                    modo          : "leer",
                    descarga      : 'evaluar'
                })  
            }
        }
        else {
            let datos = {
                "radicado": data,
                "modo": "consulta",
                "llamado_por": "grid_radica_asigna_grid"
            };
            $lib.call_component_storage(
                "forma_radicado_consulta",
                {"datos": datos}
            )
        }
    },

    'icono_pdf_template': function(data) {
        let resultado = data.value
        if (data.data.pdf_base.id !== undefined) {
            resultado =  '<i class="far fa-file-pdf fa-lg" title="Doble click para ver documento" style="color:blue; cursor: pointer" ></i>&nbsp;&nbsp;' + data.value
        }

        return resultado
    }
}

export default {
    metodos: metodos
}