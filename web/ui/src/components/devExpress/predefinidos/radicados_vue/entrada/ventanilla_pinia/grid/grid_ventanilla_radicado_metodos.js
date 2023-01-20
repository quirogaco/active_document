
import {ref} from "vue";
import visores_archivo from "../../../../../../../librerias/visores_archivo.js";

export const methods = {
    'columna_doble_click':  function(e) {
        let data = e.data;
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
            let usuario_id = window.$usuario["id"];
            let usuario_dependencia_id = window.$usuario["dependencia_id"];
            let reserva = data["reserva"];
            let gestion_responsable_id = data["gestion_responsable_id"];
            let gestion_dependencia_id = data["gestion_dependencia_id"];
            let mostrar = true;
            if (reserva == "SI") {
                if (usuario_id != gestion_responsable_id) {
                    mostrar = false
                }
            }

            if (mostrar == true) {
                let datos = {
                    "radicado": data,
                    "modo": "consulta",
                    "llamado_por": "ventanilla_radicado_grid"
                };
                $lib.call_component_storage(
                    "forma_radicado_consulta",
                    {"datos": datos}
                )
            }
            else {
                $notify("Documento con reserva!!", "error");
            }
        }
    },

    'cargar_documento':  function(event) {
        if (this.grid.getSelectedRowKeys().length == 1) {
            this.opciones_ventana_emergente_archivo.value = {
                visible  : true,
                datos: {
                    "estructura": "radicados_entrada",
                    "relacion": "principal",
                    "origen_id": this.grid.getSelectedRowKeys()[0]
                },
                atributos: {
                    multiple: false,
                    permitidos: ".pdf",
                    label: "Archivo pdf",
                    titulo_pantalla: "Cargue de archivo Pdf (documento principal)",
                    titulo_boton: "Cargar archivo PDF",
                    mensaje_retorno: "Cargue de archivo correcto!" 
                }
            }
            this.emergente_key.value += 1;
        }
        else {
            $alertar("Seleccione un (1) radicado, por favor! ", "Alerta");
        }
    },

    'imprime_recorrido':  function(e) {
        this.opciones_ventana_emergente_recorrido.visible = true
        this.emergente_recorrido += 1
    },

    'radicar':  function(event) {
        $lib.call_component_storage(
            "ventanilla_radicado_forma",
            {"datos": {}}
        )
    },

    accion_click: function(e) {        
        console.log("eee:", e)
    },

    'icono_pdf_template': function(data) {
        let resultado = data.value
        if (data.data.pdf_base.id !== undefined) {
            resultado =  '<i class="far fa-file-pdf fa-lg" title="Doble click para ver documento" style="color:blue; cursor: pointer" ></i>&nbsp;&nbsp;' + data.value
        }

        return resultado
    },

    're_render_popup': function() {
        console.log("THIS. render_popup_key-metodo-->>:", this)
        //console.log("render_popup_key-metodo AQUI *****.,....-->>:", this.render_popup_key.value)
        this.attributes_popup.visible = true;
        this.render_popup_key.value += 1;
    }
}