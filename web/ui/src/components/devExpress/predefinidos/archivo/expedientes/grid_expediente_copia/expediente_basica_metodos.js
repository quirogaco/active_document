import { confirm }      from 'devextreme/ui/dialog'
import visores_archivo  from "../../../../../../librerias/visores_archivo.js"

let metodos = {
    onToolbarPreparing(e) {
        e.toolbarOptions.items.push({
            location: 'after',
            template: 'crearButton'
        })    
        
        e.toolbarOptions.items.push({
            location: 'after',
            template: 'accesosButton'
        })    

        e.toolbarOptions.items.push({
            location: 'after',
            template: 'cerrarButton'
        })  

        e.toolbarOptions.items.push({
            location: 'after',
            template: 'abrirButton'
        })  

        e.toolbarOptions.items.push({
            location: 'after',
            template: 'indice_electronico'
        })  

        e.toolbarOptions.items.push({
            location: 'after',
            template: 'exportarlogButton'
        }) 

        e.toolbarOptions.items.push({
            location: 'after',
            template: 'fuidButton'
        }) 

        e.toolbarOptions.items.push({
            location: 'after',
            template: 'controlButton'
        }) 
    },

    retorna: function(retorna) {
        this.indicador_visible = false
        this.notify("Operación realizada correctamente", "success")    
    },

    'dobleClick':  function(e) {
        let mostrar = true
        if ( (e.data.acceso_modo == "RESERVADA") || (e.data.acceso_modo == "CLASIFICADA") ) {
            mostrar = false
        }
        if (mostrar == true) {
            this.$router.push({
                name: "pantalla_expediente",
                params: {
                    "parametros_texto": JSON.stringify({
                        "expediente_id"   : e.data.id,
                        "expediente_datos": e.data,
                        "modo"            : "modificar"
                    })                
                }
            })
        }
        else {
            this.notify(("Expediente con información " + e.data.acceso_modo), "warning") 
        }
    },

    'retorna_indice_electronico': function(parametros) {        
        window.$ocultar_esperar()
       
        visores_archivo.ver_descarga_archivo({
            archivo_id: parametros.datos.nombre_archivo, 
            operacion : 'pdf_disco', 
            titulo    : "INDICE ELECTRONICO",
        })
    },

    'indice_electronico': function() {
        window.$mostrar_esperar("Por favor espere..")
        // Url
        let urlCompleta = window.$direcciones.servidorDatos + '/expediente_acciones'  

        // Datos        
        let parametros = {
            datos : this.grid.getSelectedRowKeys(),
            accion: "expediente_indice"
        }
        window.$f["http"].llamadoRestPost( urlCompleta, parametros, this.retorna_indice_electronico, "")
    },

    'retorna_exportar': function(parametros) {
        window.$ocultar_esperar()
      
        visores_archivo.ver_descarga_archivo({
            archivo_id    : parametros.datos,
            tipo_documento: "xlsx", 
            titulo        : "TRD",
            descarga      : 'si',
            operacion     : 'disco_archivo'
        })
    },

    'control':  function(e) {
        if (this.grid.getSelectedRowsData().length > 0) {            
           let parametros = {
                datos: {
                    "expediente": this.grid.getSelectedRowsData()[0]
                },
                accion: "imprimir_control"
            }
            let urlCompleta        = window.$direcciones.servidorDatos + '/expediente_acciones' 
            window.$mostrar_esperar("Por favor espere..")
            window.$f["http"].llamadoRestPost( urlCompleta, parametros, this.retorna_exportar, "")     
        }
        else {
            this.notify("Seleccione un EXPEDIENTE! ", "warning") 
        }
    },

    'exportar_log':  function(e) {
        if (this.grid.getSelectedRowKeys().length > 0) {            
           let parametros = {
                datos: {
                    "fuente_id": this.grid.getSelectedRowKeys(),
                    "fuente"   : "agn_expedientes_trd"
                },
                accion: "exportar_expediente_log"
            }
            let urlCompleta        = window.$direcciones.servidorDatos + '/expediente_acciones' 
            window.$mostrar_esperar("Por favor espere..")
            window.$f["http"].llamadoRestPost( urlCompleta, parametros, this.retorna_exportar, "")     
        }
        else {
            this.notify("Seleccione un EXPEDIENTE! ", "warning") 
        }
    },

    'fuid':  function(e) {
        var expedientes = this.grid.getDataSource().items()
        console.log("expedientes:", expedientes)        
        let parametros = {
            datos: {
                "expedientes": expedientes
            },
            accion: "imprimir_fuid"
        }
        let urlCompleta        = window.$direcciones.servidorDatos + '/expediente_acciones' 
        window.$mostrar_esperar("Por favor espere..")
        window.$f["http"].llamadoRestPost( urlCompleta, parametros, this.retorna_exportar, "")                   
    },

    'crear':  function(e) {
        this.$router.push({
            name: "pantalla_expediente",
            params: {
                "datos": JSON.stringify({
                    "expediente_id"   : "",
                    "expediente_datos": {},
                    "modo"            : "crear"
                })
            }            
        })
    },

    'accesos':  function(e) {
        if (this.grid.getSelectedRowKeys().length > 0) {
            this.emergente_key += 1;            
            this.opciones_ventana.alto               = 300
            this.opciones_ventana.ancho              = 800
            this.opciones_ventana.visible            = true
            // Información del registro
            this.opciones_ventana.datos              = {
                "seleccionados_id": this.grid.getSelectedRowKeys(),
                "padre_tipo"      : "expediente" 
            }
        }
        else {
            this.notify("Seleccione un expediente ", "warning") 
        }
    },

    'cerrar':  function(e) {
        if (this.grid.getSelectedRowKeys().length > 0) {            
            let resultado = confirm(("Al cerrar este expediente queda disponible para transferencia, est� seguro de cerrarlo ?"), "EXPEDIENTE")
            resultado.then(dialogo => {
                if (dialogo == true) {
                    let parametros = {
                        datos: {
                            "expediente_id": this.grid.getSelectedRowKeys()
                        },
                        accion: "cerrar_expediente",
                    }
                    let urlCompleta        = window.$direcciones.servidorDatos + '/expediente_acciones'   
                    this.indicador_visible = true 
                    window.$f["http"].llamadoRestPost( urlCompleta, parametros, this.retorna, "")     
                }
            })            
        }
        else {
            this.notify("Seleccione un expediente ", "warning") 
        }
    },

    'abrir':  function(e) {
        let resultado = confirm(("Al abrir este expediente NO quedara disponible para transferencia, est� seguro de abrirlo ?"), "EXPEDIENTE")
            resultado.then(dialogo => {
                if (dialogo == true) {
                    if (this.grid.getSelectedRowKeys().length > 0) {            
                        let parametros = {
                            datos: {
                                "expediente_id": this.grid.getSelectedRowKeys()
                            },
                            accion: "abrir_expediente"
                        }
                        let urlCompleta        = window.$direcciones.servidorDatos + '/expediente_acciones'   
                        this.indicador_visible = true 
                        window.$f["http"].llamadoRestPost( urlCompleta, parametros, this.retorna, "")          
                    }
                    else {
                        this.notify("Seleccione un expediente ", "warning") 
                    }
                }
            })  
    },

    onRowUpdating: function(e) {
        console.log("onRowUpdating:", e)  
        e.cancel = true
        let parametros = {
            datos: {
                "expediente_id"     : e.oldData.id,
                "caja_transferencia": e.newData.caja_transferencia
            },
            accion: "asignar_caja"
        }
        let urlCompleta        = window.$direcciones.servidorDatos + '/expediente_acciones'   
        this.indicador_visible = true 
        window.$f["http"].llamadoRestPost( urlCompleta, parametros, this.retorna, "")    
    }

}

export default {
    metodos: metodos
}