import visores_archivo from "../../../../../../../librerias/visores_archivo.js";

let metodos = {
    onToolbarPreparing(e) {
        e.toolbarOptions.items.push({
            location: 'after',
            template: 'crearButton'
        })    
        
        e.toolbarOptions.items.push({
            location: 'after',
            template: 'exportarButton'
        })

        e.toolbarOptions.items.push({
            location: 'after',
            template: 'exportarlogButton'
        })
        
        e.toolbarOptions.items.push({
            location: 'after',
            template: 'importarButton'
        })
    },

    'dobleClick':  async function(e) {       
        let registro = await $lib.leer_registro_id("agn_trd", e.data.id);
        let datos = {
            "id": registro.id,
            "registro": registro,
            "modo": "modificar"
            //"llamado_por": this.retorna_grid
        };
        $lib.call_component_storage(
            "trd_pantalla",   
            {"datos": datos}
        )      


        // $router.push({
        //     name: "trd_pantalla",                      
        //     params: {
        //         "attributes_str": JSON.stringify({
        //             "datos": datos,
        //             "mode": "modificar"
        //         })       
        //     }                            
        //})
    },

    'crear':  function(e) {
        $router.push({
            name: "trd_pantalla",                      
            params: {
                "attributes_str": JSON.stringify({
                    "mode": "crear"
                })
            }                            
        })
    },

    'retorna_exportar': function(parametros) {
        window.$ocultar_esperar();      
        visores_archivo.ver_descarga_archivo({
            archivo_id    : parametros.datos,
            tipo_documento: "xlsx", 
            titulo        : "TRD",
            descarga      : 'si',
            operacion     : 'disco_archivo'
        })
    },

    'exportar':  function(e) {
        if (window.$trd_grid.getSelectedRowKeys().length > 0) {            
           let parametros = {
                datos: {
                    "trd_id": window.$trd_grid.getSelectedRowKeys()
                },
                accion: "exportar_trd",
            }
            let urlCompleta        = window.$direcciones.servidorDatos + '/trd_acciones' 
            window.$mostrar_esperar("Por favor espere..")
            window.$f["http"].llamadoRestPost( urlCompleta, parametros, this.retorna_exportar, "")     
        }
        else {
            this.notify("Seleccione una TRD! ", "warning") 
        }
    },

    'importar_trd':  function(e) {
        this.emergente_key += 1;            
        this.opciones_ventana.visible = true;  
    },

    'exportar_log':  function(e) {
        if (window.$trd_grid.getSelectedRowKeys().length > 0) {            
           let parametros = {
                datos: {
                    "fuente_id": window.$trd_grid.getSelectedRowKeys(),
                    "fuente"   : "agn_trd"
                },
                accion: "exportar_trd_log",
            }
            let urlCompleta        = window.$direcciones.servidorDatos + '/trd_acciones' 
            window.$mostrar_esperar("Por favor espere..")
            window.$f["http"].llamadoRestPost( urlCompleta, parametros, this.retorna_exportar, "")     
        }
        else {
            this.notify("Seleccione una TRD! ", "warning") 
        }
    }   
}

export default {
    metodos: metodos
}