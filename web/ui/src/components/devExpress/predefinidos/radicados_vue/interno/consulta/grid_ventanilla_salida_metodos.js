
import visores_archivo    from "../../../../../../librerias/visores_archivo.js"

let metodos = {
    onToolbarPreparing(e) {
        e.toolbarOptions.items.push({
            location: 'after',
            template: 'radicarButton'
        })     
        
        e.toolbarOptions.items.push({
            location: 'after',
            template: 'cargarDocumento'
        })  

        e.toolbarOptions.items.push({
            location: 'after',
            template: 'cargarAnexo'
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

    'cargar_anexo':  function(e) {
        this.opciones_ventana_emergente_archivo.visible = true
        this.emergente_key += 1
    },

    'radicar':  function(e) {
        window.$router.push({
            name: "ventanilla_radicado_forma",
            /*
            params: {
                "datos": JSON.stringify({
                    "trd_id"   : e.data.id,
                    "trd_datos": e.data,
                    "modo"     : "modificar"
                })                
            }
            */
        })
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