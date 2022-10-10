
import visores_archivo    from "../../../../../../librerias/visores_archivo.js"

let metodos = {
    onToolbarPreparing(e) {
        e.toolbarOptions.items.push({
            location: 'after',
            template: 'firmarButton'
        })                    
    },

    'columna_doble_click':  function(e) {
        let data = e.data
        if (e.column.dataField == "nro_radicado") {
            if (data.pdf_base.id !== undefined) {
                visores_archivo.ver_descarga_archivo({
                    titulo_general: "Consulta de Documentos/Anexos RADICADO",
                    archivo_id    : data.pdf_base.id, 
                    tipo_documento: data.pdf_base.tipo_archivo, 
                    titulo        : "Información documento",
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
                "llamado_por": "grid_ventanilla_salida"
            }
            this.$router.push({
                name: "forma_salida_consulta",                      
                params: {
                    "datos": JSON.stringify(datos)                
                }                            
            })
        }
    },

    'firmar':  function(e) {
        if (this.grid.getSelectedRowKeys().length > 0) {            
            this.emergente_key += 1;            
            this.opciones_ventana.alto               = 300
            this.opciones_ventana.ancho              = 800
            this.opciones_ventana.visible            = true
            this.opciones_ventana.accion             = "FIRMA_BORRADOR"
            this.opciones_ventana.titulo_boton       = "Firmar electronicamente"
            // Información del registro
            this.opciones_ventana.datos              = {
                "firmar_ids": this.grid.getSelectedRowKeys()
            }
        }
        else {
            this.notify("Seleccione al menos un radicado a firmar!", "warning") 
        }
    },

    'icono_pdf_template': function(data) {
        let resultado = data.value
        if (data.data.pdf_base.id !== undefined) {
            resultado = '<i class="fas fa-pen-nib fa-lg" style="color:red; cursor: pointer"></i>'
            resultado += '<i class="far fa-file-pdf fa-lg" title="Doble click para ver documento" style="color:blue; cursor: pointer"></i>&nbsp;&nbsp;' + data.value
        }

        return resultado
    }

}

export default {
    metodos: metodos
}