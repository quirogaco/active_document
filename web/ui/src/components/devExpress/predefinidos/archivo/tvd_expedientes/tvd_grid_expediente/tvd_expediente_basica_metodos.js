
let metodos = {
    onToolbarPreparing(e) {
        e.toolbarOptions.items.push({
            location: 'after',
            template: 'crearButton'
        })    
        
        e.toolbarOptions.items.push({
            location: 'after',
            template: 'accesosButton'
        })            
    },

    retorna: function(retorna) {
        this.indicador_visible = false
        this.notify("Operación realizada correctamente", "success")    
    },

    'dobleClick':  function(e) {
        this.$router.push({
            name: "tvd_pantalla_expediente",
            params: {
                "datos": JSON.stringify({
                    "expediente_id"   : e.data.id,
                    "tvd_expediente_datos": e.data,
                    "modo"            : "modificar"
                })                
            }
        })
    },

    'crear':  function(e) {
        this.$router.push({
            name: "tvd_pantalla_expediente",
            params: {
                "datos": JSON.stringify({
                    "expediente_id"   : "",
                    "tvd_expediente_datos": {},
                    "modo"            : "crear"
                })
            }            
        })
    },

    'accesos':  function(e) {
        if (this.grid.getSelectedRowKeys().length > 0) {
            this.emergente_key += 1;            
            this.opciones_ventana.alto               = 300
            this.opciones_ventana.ancho              = 800
            this.opciones_ventana.visible            = true
            // Información del registro
            this.opciones_ventana.datos              = {
                "seleccionados_id": this.grid.getSelectedRowKeys(),
                "padre_tipo"      : "expediente" 
            }
        }
        else {
            this.notify("Seleccione un expediente ", "warning") 
        }
    },
}

export default {
    metodos: metodos
}