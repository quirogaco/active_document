
let metodos = {
    'dobleClick':  function(e) {  
        window.scroll(0,0);            
        $lib.call_component_storage(
            "gestion_pantalla",
            {"datos": {
                "id"   : e.data.id,
                "datos": e.data
            }}
        )
    },

    'muestra_ventana_emergente_grid': function(parametros){
        let seleccionados = this.$refs.grid.instance.getSelectedRowKeys();
        let datos         = this.$refs.grid.instance.getSelectedRowsData();
        if ( seleccionados.length == 1) {
            this.emergente_key += 1;
            this.opciones_ventana.alto               = parametros.alto 
            this.opciones_ventana.ancho              = parametros.ancho
            this.opciones_ventana.componente_visible = parametros.ventana  
            this.opciones_ventana.titulo             = parametros.titulo   
            this.opciones_ventana.boton_mensaje      = parametros.boton_mensaje    
            this.opciones_ventana.accion             = parametros.accion  
            this.opciones_ventana.fuente             = parametros.fuente 
            this.opciones_ventana.rapida             = parametros.rapida 
            this.opciones_ventana.visible            = true  
            this.opciones_ventana.elementos          = seleccionados              
        }
        else {
            this.notify("Seleccione un documento por favor!", "warning")
        }
    },

    'muestra_ventana_emergente' : function(parametros){
        let seleccionados = this.$refs.grid.instance.getSelectedRowKeys();
        let datos = this.$refs.grid.instance.getSelectedRowsData();
        if ( (seleccionados.length == 1) && (parametros.borrador != true ) ) {
            if (datos[0].origen_tipo == "ENTRADA") {
                this.emergente_key += 1;
                this.opciones_ventana.alto               = parametros.alto 
                this.opciones_ventana.ancho              = parametros.ancho
                this.opciones_ventana.componente_visible = parametros.ventana  
                this.opciones_ventana.titulo             = parametros.titulo   
                this.opciones_ventana.boton_mensaje      = parametros.boton_mensaje    
                this.opciones_ventana.accion             = parametros.accion  
                this.opciones_ventana.fuente             = parametros.fuente 
                this.opciones_ventana.rapida             = parametros.rapida 
                this.opciones_ventana.visible            = true
                this.opciones_ventana.elementos          = seleccionados    
            }
            else {
                this.notify("Seleccione documento de ENTRADA por favor!", "warning")
            }
        }
        else {
            this.emergente_key += 1;
            this.opciones_ventana.alto               = parametros.alto 
            this.opciones_ventana.ancho              = parametros.ancho
            this.opciones_ventana.componente_visible = parametros.ventana  
            this.opciones_ventana.titulo             = parametros.titulo   
            this.opciones_ventana.boton_mensaje      = parametros.boton_mensaje    
            this.opciones_ventana.accion             = parametros.accion  
            this.opciones_ventana.fuente             = parametros.fuente 
            this.opciones_ventana.rapida             = parametros.rapida 
            this.opciones_ventana.visible            = true

        }        
    },

    'plantilla_columna_estado': function(data) {
            let resultado =  ''
            
            // Si tiene borrador o no
            if ( (data.data.borrador_id != null) && ((data.data.borrador_id != "")) ) {
                resultado =  '<i class="fas fa-file-import" style="color:blue"></i>      '
            }
            
            // Estado
            if (data.data.origen_tipo == "ENTRADA") {
                if (data.value == "TERMINOS") {
                    resultado +=  '<i class="fas fa-traffic-light" style="color:green"></i> ' + data.value + " (" + data.data.dias_vencimiento + ")"
                }
                else {
                    resultado +=  '<i class="fas fa-traffic-light" style="color:red"></i> ' + data.value + " (" + data.data.dias_vencimiento + ")"
                }
            }
            else {
                resultado +=  '<i class="fas fa-traffic-light" style="color:green"></i> ' + "TERMINOS"                
            }

            return resultado
    }
}

export default {
    metodos: metodos
}