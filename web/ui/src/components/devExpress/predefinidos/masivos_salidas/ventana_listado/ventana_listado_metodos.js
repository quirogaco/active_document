const metodos = {
    cargar_datos: function(datos) {
        this.dependencia_id = datos.dependencia_id
        this.detalle        = datos.detalle
        setTimeout(() => {
            for (let indice in datos.destinatarios) {
                window.$grid_destinatarios.fuente_datos.store().insert( datos.destinatarios[indice] ).then(
                    (dataObj) => {},
                    (error) => {}
                )
            }
            window.$grid_destinatarios.fuente_datos.reload()
        }, 3000)       
    },

    // Botones de acción
    es_visible: function(boton) { 
        let visible = false
        let parametros = JSON.parse(this.datos)   
        // Boton crear
        if ( (boton=="salvar") && (parametros.modo=="crear") ) {
            visible = true
        }

        // Boton modificar
        if ( (boton=="modificar") && (parametros.modo=="modificar") ) {
            visible = true
        }

        // Boton salvar
        if ( (boton=="borrar") && (parametros.modo=="modificar") ) {
            visible = true
        }

        return visible
    },

    // Retorna a llamado remoto
    retorna: function(datos) {
        this.notify("Operación realizada correctamente", "success")
        this.$router.push("destinatarios_listado_grid")
    },

    // Envia datos y acción al servidor
    enviar: function(accion, datos) {                
        let parametros = {
            "accion": accion,
            "datos" : datos
        }    
        window.$f["http"].llamadoRestPost( this.urlCompleta, parametros, this.retorna, "")   
    },

    // Salvar listado
    salvar: function() {                    
        let datos = {
            "origen"        : "SALIDA",
            "dependencia_id": this.dependencia_id,
            "detalle"       : this.detalle,
            "destinatarios" : window.$grid_destinatarios.fuente_datos._items
        }
        this.enviar("salvar", datos)
    },

    // Modificar listado
    modificar: function() {                    
        let datos = {
            "listado_id"    : this.parametros["listado_datos"]["id"],
            "origen"        : "SALIDA",
            "dependencia_id": this.dependencia_id,
            "detalle"       : this.detalle,
            "destinatarios" : window.$grid_destinatarios.fuente_datos._items
        }
        this.enviar("modificar", datos)
    },

    // Borrar listado
    borrar: function() {    
        let datos = {
            "listado_id": this.parametros["listado_datos"]["id"]
        }
        this.enviar("borrar", datos)        
    },

    // Retorna a grid listado
    regresar: function() {  
        this.$router.push("destinatarios_listado_grid")
    }
}

export default {
    metodos: metodos
}