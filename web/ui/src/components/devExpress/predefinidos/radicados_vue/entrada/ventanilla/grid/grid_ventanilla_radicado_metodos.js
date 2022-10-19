
import visores_archivo from "../../../../../../../librerias/visores_archivo.js";

export const methods = {
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
                "id"         : data.id,
                "datos"      : data,
                "modo"       : "consulta",
                "llamado_por": "ventanilla_radicado_grid"
            }
            this.$router.push({
                name: "forma_radicado_consulta",                      
                params: {
                    //"datos": JSON.stringify(datos)     
                    "attributes_str": JSON.stringify(datos)     
                }                            
            })
        }
    },

    'cargar_documento':  function(e) {
        if (this.grid.getSelectedRowKeys().length > 0) {
            this.opciones_ventana_emergente_archivo = {
                visible  : true,
                datos    : {
                    "estructura": "radicados_entrada",
                    "relacion"  : "principal",
                    "origen_id" : this.grid.getSelectedRowKeys()[0]
                },
                atributos: {
                    multiple       : false,
                    permitidos     : ".pdf",
                    label          : "Archivo pdf",
                    titulo_pantalla: "Cargue de archivo Pdf (documento principal)",
                    titulo_boton   : "Cargar archivo PDF",
                    mensaje_retorno: "Cargue de archivo correcto!" 
                }
            }
            this.emergente_key += 1
        }
        else {
            this.notify("Seleccione un radicado ", "warning") 
        }
    },

    'imprime_recorrido':  function(e) {
        this.opciones_ventana_emergente_recorrido.visible = true
        this.emergente_recorrido += 1
    },

    'radicar':  function(e) {
        this.$router.push({
            name  : "ventanilla_radicado_forma",            
            params: {}        
        })
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