
let metodos = {   
    onToolbarPreparing(e) {
        e.toolbarOptions.items.push({
            location: 'after',
            template: 'botonEnvio'
        })
    },

    retorna: function(datos) {
        console.log("RETORNA ENVIA.....") 
    },

    envio_salida: function() {
        let parametros = {
            datos : this.selectedItemKeys[0],
            accion: "enviar_correo"
        }
        window.$f["http"].llamadoRestPost( this.urlCompleta, parametros, this.retorna, "")   
        console.log("envio_salida:", this.selectedItemKeys )
    },

    onRowUpdated: function(e) {     
        console.log("onRowUpdated:", e.data)   
        this.registro = e.data      
    }

}

export default {
    metodos: metodos
}