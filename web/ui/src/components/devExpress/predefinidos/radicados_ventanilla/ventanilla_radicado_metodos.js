
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

    'dobleClick':  function(e) {
        let datos = {
            "id"   : e.data.id,
            "datos": e.data,
            "modo" : "consulta"
        }
        window.$datos_por_ahora = datos
        this.$router.push({
            name: "ventanilla_radicado_consulta",            
            params: {
                "datos": JSON.stringify(datos)                
            }            
        })
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
    }

}

export default {
    metodos: metodos
}