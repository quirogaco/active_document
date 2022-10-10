let metodos = {   
    onToolbarPreparing(e) {
        e.toolbarOptions.items.push({
            location: 'after',
            template: 'botonBuscar'
        })
    },

    buscar_terceros: function() {
        this.emergente_key += 1;
        this.opciones_ventana.visible = true;
    },

    nuevos_registros: function(registros) {
        for (let registro of registros) {
            this.fuente_datos.store().insert(registro)
        }
        this.fuente_datos.reload()
    },
}

export default {
    metodos: metodos
}