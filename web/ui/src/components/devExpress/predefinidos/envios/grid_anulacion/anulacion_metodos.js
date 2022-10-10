
let metodos = {   
    onToolbarPreparing(e) {
        e.toolbarOptions.items.push({
            location: 'after',
            template: 'botonAprueba'
        })

        e.toolbarOptions.items.push({
            location: 'after',
            template: 'botonNiega'
        })
    },

    retorna: function(datos) {
        console.log("RETORNA ENVIA.....") 
    },

    aprueba_anulacion: function() {
        let parametros = {
            datos : this.selectedItemKeys[0],
            accion: "aprueba_anulacion"
        }
        window.$f["http"].llamadoRestPost( this.urlCompleta, parametros, this.retorna, "")   
    },

    niega_anulacion: function() {
        let parametros = {
            datos : this.selectedItemKeys[0],
            accion: "niega_anulacion"
        }
        window.$f["http"].llamadoRestPost( this.urlCompleta, parametros, this.retorna, "")   
    },

    onRowUpdated: function(e) {
        this.registro = e.data      
    }
}

export default {
    metodos: metodos
}