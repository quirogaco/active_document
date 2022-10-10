import { confirm }      from 'devextreme/ui/dialog'
import visores_archivo  from "../../../../../../librerias/visores_archivo.js"

let metodos = {
    onToolbarPreparing(e) {
        e.toolbarOptions.items.push({
            location: 'after',
            template: 'abrirButton'
        })  

        e.toolbarOptions.items.push({
            location: 'after',
            template: 'fuidButton'
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
                    "datos": JSON.stringify({
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

    'fuid':  function(e) {
        var expedientes = this.grid.getDataSource().items()
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

    'abrir':  function(e) {
        let resultado = confirm(("Al abrir este expediente NO quedara disponible para transferencia, está seguro de abrirlo ?"), "EXPEDIENTE")
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
        this.indicador_visible = true 
        let urlCompleta        = window.$direcciones.servidorDatos + '/expediente_acciones'        

        console.log("e.newData:", e.newData)  
        e.cancel = true
        let parametros = {
            datos: {
                "expediente_id"     : e.oldData.id,
                "caja_transferencia": e.newData.caja_transferencia,
                "anotacion"         : e.newData.anotacion
            },
            accion: "actualiza_caja_anotacion"
        }           
        window.$f["http"].llamadoRestPost( urlCompleta, parametros, this.retorna, "")    
    },
}

export default {
    metodos: metodos
}