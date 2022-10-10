import visores_archivo  from "../../../../../../librerias/visores_archivo.js"

let metodos = {
    onToolbarPreparing(e) {
        e.toolbarOptions.items.push({
            location: 'after',
            template: 'programarButton'
        })    
        
        e.toolbarOptions.items.push({
            location: 'after',
            template: 'recibirButton'
        })    

        e.toolbarOptions.items.push({
            location: 'after',
            template: 'devolverButton'
        })

        e.toolbarOptions.items.push({
            location: 'after',
            template: 'exportarlogButton'
        }) 
    },

    retorna: function(retorna) {
        console.log("retorna:", retorna)
        this.indicador_visible = false
        this.notify("Operación realizada correctamente", "success")    
        if (retorna.datos.nombre_archivo != undefined) {
            visores_archivo.ver_descarga_archivo({
                archivo_id    : retorna.datos.nombre_archivo,
                tipo_documento: "xlsx", 
                titulo        : "FUID",
                descarga      : 'si',
                operacion     : 'disco_archivo'
            })
        }
    },

    'dobleClick':  function(e) {
        this.$router.push({
            name: "pantalla_transferencia",
            params: {
                "datos": JSON.stringify({
                    "transferencia_id"   : e.data.id,
                    "transferencia_datos": e.data,
                    "modo"            : "modificar"
                })                
            }
        })
    },

    'programar':  function(e) {
        this.$router.push({
            name: "pantalla_transferencia",
            params: {
                "datos": JSON.stringify({
                    "transferencia_id"   : "",
                    "transferencia_datos": {},
                    "modo"            : "crear"
                })
            }            
        })
    },

    'recibir':  function(e) {
        if (this.grid.getSelectedRowKeys().length > 0) {
            let parametros = {
                datos: {
                    "transferencia_id": this.grid.getSelectedRowKeys()
                },
                accion: "recibir_transferencia"
            }
            let urlCompleta        = window.$direcciones.servidorDatos + '/expediente_acciones'   
            this.indicador_visible = true 
            window.$f["http"].llamadoRestPost( urlCompleta, parametros, this.retorna, "")      
        }
        else {
            this.notify("Seleccione una transferencia", "warning") 
        }
    },

    'devolver':  function(e) {
        if (this.grid.getSelectedRowKeys().length > 0) {
            let parametros = {
                datos: {
                    "transferencia_id": this.grid.getSelectedRowKeys()
                },
                accion: "devolver_transferencia"
            }
            let urlCompleta        = window.$direcciones.servidorDatos + '/expediente_acciones'   
            this.indicador_visible = true 
            window.$f["http"].llamadoRestPost( urlCompleta, parametros, this.retorna, "")      
        }
        else {
            this.notify("Seleccione una transferencia", "warning") 
        }
    },

    'retorna_exportar': function(parametros) {
        window.$ocultar_esperar()
      
        visores_archivo.ver_descarga_archivo({
            archivo_id    : parametros.datos,
            tipo_documento: "xlsx", 
            titulo        : "TRANSFERENCIA",
            descarga      : 'si',
            operacion     : 'disco_archivo'
        })
    },

    'exportar_log':  function(e) {
        if (this.grid.getSelectedRowKeys().length > 0) {            
           let parametros = {
                datos: {
                    "fuente_id": this.grid.getSelectedRowKeys(),
                    "fuente"   : "agn_transferencias_trd"
                },
                accion: "exportar_transferencia_log"
            }
            let urlCompleta        = window.$direcciones.servidorDatos + '/expediente_acciones' 
            window.$mostrar_esperar("Por favor espere..")
            window.$f["http"].llamadoRestPost( urlCompleta, parametros, this.retorna_exportar, "")     
        }
        else {
            this.notify("Seleccione una TRANSFERENCIA! ", "warning") 
        }
    },

    onRowUpdating: function(e) {
        this.indicador_visible = true 
        let urlCompleta        = window.$direcciones.servidorDatos + '/expediente_acciones'        

        e.cancel = true
        let parametros = {
            datos: {
                "transferencia_id": e.oldData.id,
                "detalle"         : e.newData.detalle,
            },
            accion: "comentario_transferencia"
        }           
        window.$f["http"].llamadoRestPost( urlCompleta, parametros, this.retorna, "")    
    },
}

export default {
    metodos: metodos
}