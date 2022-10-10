
let metodos = {   
    onToolbarPreparing(e) {
        e.toolbarOptions.items.push({
            location: 'after',
            template: 'planillaButton'
        })

        e.toolbarOptions.items.push({
            location: 'after',
            template: 'planillaImprime'
        })      
    },

    'dobleClick':  function(e) {
        this.$router.push(
            {
                name: "devoluciones_grid",
                params: {
                    planilla_id: e.data.id
                }
            }
        )
    },

    retorna: function(datos) {
        this.notify("Operación realizada correctamente", "success")
    },

    abre_planilla: function() {
        //window.$router.push({path: "envios_grid"})
        this.$router.push({path: "envios_grid"})
    },

    imprimir_planilla: function() {
        let parametros = {
            datos : this.selectedItemKeys,
            accion: "imprimir_planilla"
        }
        let urlCompleta = window.$direcciones.servidorDatos + '/envio_acciones'
        
        $librerias.descargar_archivo_remoto(urlCompleta, parametros, "planilla") 
    },

}

export default {
    metodos: metodos
}