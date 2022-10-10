
let metodos = {
    onToolbarPreparing(e) {        
        e.toolbarOptions.items.push({
            location: 'after',
            template: 'entregarButton'
        })    
        
        e.toolbarOptions.items.push({
            location: 'after',
            template: 'negarButton'
        })  

        e.toolbarOptions.items.push({
            location: 'after',
            template: 'recibirButton'
        })  
    },

    'dobleClick':  function(e) {},

    'negar':  function(e) {
        if (this.grid.getSelectedRowKeys().length > 0) {
            this.emergente_key += 1;            
            this.opciones_ventana.alto               = 300
            this.opciones_ventana.ancho              = 800
            this.opciones_ventana.visible            = true
            this.opciones_ventana.accion             = "negar_prestamo"
            this.opciones_ventana.titulo_boton       = "Negar prestamo"
            // Información del registro
            this.opciones_ventana.datos              = {
                "prestamos_id": this.grid.getSelectedRowKeys()
            }
        }
        else {
            this.notify("Seleccione un expediente ", "warning") 
        }
    },

    'entregar':  function(e) {
        if (this.grid.getSelectedRowKeys().length > 0) {
            this.emergente_key += 1;            
            this.opciones_ventana.alto               = 300
            this.opciones_ventana.ancho              = 800
            this.opciones_ventana.visible            = true
            this.opciones_ventana.accion             = "entregar_prestamo"
            this.opciones_ventana.titulo_boton       = "Funcionario recibe expediente"
            // Información del registro
            this.opciones_ventana.datos              = {
                "prestamos_id": this.grid.getSelectedRowKeys()
            }
        }
        else {
            this.notify("Seleccione un expediente ", "warning") 
        }
    },

    'recibir':  function(e) {
        if (this.grid.getSelectedRowKeys().length > 0) {
            this.emergente_key += 1;            
            this.opciones_ventana.alto               = 300
            this.opciones_ventana.ancho              = 800
            this.opciones_ventana.visible            = true
            this.opciones_ventana.accion             = "recibir_prestamo"
            this.opciones_ventana.titulo_boton       = "Funcionario devuelve expediente"
            // Información del registro
            this.opciones_ventana.datos              = {
                "prestamos_id": this.grid.getSelectedRowKeys()
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