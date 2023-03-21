import { confirm }      from 'devextreme/ui/dialog'
import visores_archivo  from "../../../../../../librerias/visores_archivo.js"

let metodos = {
    onToolbarPreparing(e) {
        e.toolbarOptions.items.push({
            template: 'acciones',
            location: 'after'
        })    
    },

    retorna: function(retorna) {
        that.indicador_visible = false;
        that.grid.refresh();
        that.notify("Operación realizada correctamente", "success"); 
    },

    'dobleClick':  function(e) {
        let mostrar = true
        if ( (e.data.acceso_modo == "RESERVADA") || (e.data.acceso_modo == "CLASIFICADA") ) {
            mostrar = false
        }
        if (mostrar == true) {
            let urlCompleta = window.$direcciones.servidorDatos + '/expediente_acciones'  
             let parametros = {
                datos : e.data,
                accion: "consulta_expediente"
            }
            window.$f["http"].llamadoRestPost( urlCompleta, parametros, function(){}, "")

            let datos = {
                "expediente_id": e.data.id,
                "expediente_datos": e.data,
                "modo": "modificar"
            };
            $lib.call_component_storage(
                "pantalla_expediente",   
                {"datos": datos}
            ) 
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

    'indice_electronico': function(that) {
        window.$mostrar_esperar("Por favor espere..")
        // Url
        let urlCompleta = window.$direcciones.servidorDatos + '/expediente_acciones'  

        // Datos        
        let parametros = {
            datos : that.grid.getSelectedRowKeys(),
            accion: "expediente_indice"
        }
        window.$f["http"].llamadoRestPost( urlCompleta, parametros, that.retorna_indice_electronico, "")
    },

    'retorna_indice_electronico_excel': function(parametros) {
        window.$ocultar_esperar()
      
        visores_archivo.ver_descarga_archivo({
            archivo_id    : parametros.datos,
            tipo_documento: "xlsx", 
            titulo        : "TRD",
            descarga      : 'si',
            operacion     : 'disco_archivo'
        })
    },

    'indice_electronico_excel': function(that) {
        if (that.grid.getSelectedRowsData().length > 0) {            
            let parametros = {
                 datos: {
                     "expediente": that.grid.getSelectedRowsData()[0]
                 },
                 accion: "indice_electronico_excel"
             }
             let urlCompleta        = window.$direcciones.servidorDatos + '/expediente_acciones' 
             window.$mostrar_esperar("Por favor espere..")
             window.$f["http"].llamadoRestPost( urlCompleta, parametros, that.retorna_exportar, "")     
         }
         else {
             that.notify("Seleccione un EXPEDIENTE! ", "warning") 
         }
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

    'control':  function(that) {
        if (that.grid.getSelectedRowsData().length > 0) {            
           let parametros = {
                datos: {
                    "expediente": that.grid.getSelectedRowsData()[0]
                },
                accion: "imprimir_control"
            }
            let urlCompleta        = window.$direcciones.servidorDatos + '/expediente_acciones' 
            window.$mostrar_esperar("Por favor espere..")
            window.$f["http"].llamadoRestPost( urlCompleta, parametros, that.retorna_exportar, "")     
        }
        else {
            that.notify("Seleccione un EXPEDIENTE! ", "warning") 
        }
    },

    'exportar_log':  function(that) {
        if (that.grid.getSelectedRowKeys().length > 0) {            
           let parametros = {
                datos: {
                    "fuente_id": that.grid.getSelectedRowKeys(),
                    "fuente"   : "agn_expedientes_trd"
                },
                accion: "exportar_expediente_log"
            }
            let urlCompleta        = window.$direcciones.servidorDatos + '/expediente_acciones' 
            window.$mostrar_esperar("Por favor espere..")
            window.$f["http"].llamadoRestPost( urlCompleta, parametros, that.retorna_exportar, "")     
        }
        else {
            that.notify("Seleccione un EXPEDIENTE! ", "warning") 
        }
    },

    'fuid':  function(that) {
        var expedientes = that.grid.getDataSource().items()
        let parametros = {
            datos: {
                "expedientes": expedientes
            },
            accion: "imprimir_fuid"
        }
        let urlCompleta        = window.$direcciones.servidorDatos + '/expediente_acciones' 
        window.$mostrar_esperar("Por favor espere..")
        window.$f["http"].llamadoRestPost( urlCompleta, parametros, that.retorna_exportar, "")                   
    },

    'crear':  function(that) {
        that.$router.push({
            name: "pantalla_expediente",
            params: {
                "parametros_texto": JSON.stringify({
                    "expediente_id"   : "",
                    "expediente_datos": {},
                    "modo"            : "crear"
                })
            }            
        })
    },

    'accesos':  function(that) {
        if (that.grid.getSelectedRowKeys().length > 0) {
            that.emergente_key += 1;            
            that.opciones_ventana.alto               = 300
            that.opciones_ventana.ancho              = 800
            that.opciones_ventana.visible            = true
            // Información del registro
            that.opciones_ventana.datos              = {
                "seleccionados_id": that.grid.getSelectedRowKeys(),
                "padre_tipo"      : "expediente" 
            }
        }
        else {
            that.notify("Seleccione un expediente ", "warning") 
        }
    },

    'cerrar':  function(that) {
        if (that.grid.getSelectedRowKeys().length > 0) {            
            let resultado = confirm(("Al cerrar quedan disponibles para transferencia, está seguro de cerrarlos ?"), "EXPEDIENTE")
            resultado.then(dialogo => {
                if (dialogo == true) {
                    let parametros = {
                        datos: {
                            "expediente_id": that.grid.getSelectedRowKeys()
                        },
                        accion: "cerrar_expediente",
                    }
                    let urlCompleta        = window.$direcciones.servidorDatos + '/expediente_acciones'   
                    that.indicador_visible = true 
                    window.$f["http"].llamadoRestPost( urlCompleta, parametros, that.retorna, "")     
                }
            })            
        }
        else {
            that.notify("Seleccione un expediente ", "warning") 
        }
    },

    'abrir':  function(that) {
        let resultado = confirm(("Al abrir NO quedan disponibles para transferencia, está seguro de abrirlos ?"), "EXPEDIENTE")
            resultado.then(dialogo => {
                if (dialogo == true) {
                    if (that.grid.getSelectedRowKeys().length > 0) {            
                        let parametros = {
                            datos: {
                                "expediente_id": that.grid.getSelectedRowKeys()
                            },
                            accion: "abrir_expediente"
                        }
                        let urlCompleta        = window.$direcciones.servidorDatos + '/expediente_acciones'   
                        that.indicador_visible = true 
                        window.$f["http"].llamadoRestPost( urlCompleta, parametros, that.retorna, "")          
                    }
                    else {
                        that.notify("Seleccione un expediente ", "warning") 
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
        that.indicador_visible = true 
        window.$f["http"].llamadoRestPost( urlCompleta, parametros, that.retorna, "")    
    }

}

export default {
    metodos: metodos
}