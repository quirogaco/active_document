
let metodos = {
    onToolbarPreparing(e) {
        e.toolbarOptions.items.push({
            location: 'after',
            template: 'prestamoButton'
        })      
    },

    'dobleClick':  function(e) {},

    'solicitar':  function(e) {
        if (this.grid.getSelectedRowKeys().length > 0) {
            console.log("this.grid.getSelectedRowKeys():", this.grid.getSelectedRowKeys())
            this.emergente_key += 1;            
            this.opciones_ventana.alto               = 200
            this.opciones_ventana.ancho              = 800
            this.opciones_ventana.visible            = true
            // Información del registro
            this.opciones_ventana.datos              = {
                "expedientes_id": this.grid.getSelectedRowKeys()
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