
let metodos = {   
    
    retorna: function(datos) {
        let accion = datos.accion                        
        if (accion == "modificar") {            
            let key = datos.id
            this.fuente_datos.store().remove(key)            
            this.fuente_datos.store().insert(datos).then(
                (dataObj) => {},
                (error) => {}
            )
            this.fuente_datos.reload()       
        }   
        
        if (accion == "cargar_envios") {      
            let registros = datos.registros   
            for (let registro of registros) {
                this.fuente_datos.store().insert(registro)
            }
            this.fuente_datos.reload()     
        } 
    },

    enviar_accion: function(accion, datos) {
        let parametros = {
            datos : datos,
            accion: accion
        }
        window.$f["http"].llamadoRestPost( this.urlCompleta, parametros, this.retorna, "")   
    },

    onRowUpdated: function(e) {
        this.enviar_accion("modificar", e.data)      
    }
}

export default {
    metodos: metodos
}