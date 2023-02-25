
import visores_archivo    from "../../../../../../librerias/visores_archivo.js"

let metodos = {
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
            let archivos = window.$librerias.elimina_atributo(e.data, 'archivos'); 
            let data = e.data;
            console.log("RDAICADO INFO:", data)
            data['anexos_radicado'] = archivos;
            // Datos de gestion ya que e.data asigna en blanco.
            data['gestion_prioridad'] = 'MEDIA';  
            data['gestion_horas_dias'] = 'DIAS';       
            data['reserva'] = 'NO';
            // data['es_ventanilla'] = 'NO';
            // data['es_pqrs'] = 'NO';
            // data['resuelto_inmediato'] = 'NO';
            $save_params("_radica_dependencia_", {
                "responsable": "correspondencia_id"
            });
            $save_params("pqrs_filtro", "DOCUMENTO");
            $lib.call_component_storage(
                "forma_ventanilla_asigna",
                {"datos": {
                    "id"   : e.data.id,
                    "radicado": e.data,
                    "modo" : "asigna"
                }}
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