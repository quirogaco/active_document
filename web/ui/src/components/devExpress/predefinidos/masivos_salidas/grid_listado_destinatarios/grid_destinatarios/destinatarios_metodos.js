
let metodos = {   
    onToolbarPreparing(e) {
        e.toolbarOptions.items.push({
            location: 'after',
            template: 'addButton'
        });

        e.toolbarOptions.items.push({
            location: 'after',
            template: 'deleteButton'
        });

        e.toolbarOptions.items.push({
            location: 'after',
            template: 'planillaButton'
        });
    },

    retorna: function(datos) {
        let accion = datos.accion                        
        if (accion == "crear") {            
            let key = datos.id_temporal
            this.fuente_datos.store().remove(key)
            this.fuente_datos.store().insert(datos).then(
                (dataObj) => {},
                (error) => {}
            )
            this.fuente_datos.reload()       
        }   

        if (accion == "modificar") {            
            let key = datos.id
            this.fuente_datos.store().remove(key)
            this.fuente_datos.store().insert(datos).then(
                (dataObj) => {},
                (error) => {}
            )
            this.fuente_datos.reload()       
        }   
        
        if (accion == "cargar") {      
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

    // Acciones
    deleteRecords: function() {
        this.selectedItemKeys.forEach((key) => {            
            this.enviar_accion("borrar", key)
            this.fuente_datos.store().remove(key);
        });
        this.selectedItemKeys = []
        this.fuente_datos.reload()
    },

    addRecords: function() {
        this.emergente_key += 1;
        this.opciones_ventana.visible = true
    },
    
    nuevos_registros: function(registros) {
        for (let registro of registros) {
            this.fuente_datos.store().insert(registro)
            this.enviar_accion("crear", registro)
        }
        this.fuente_datos.reload()
    },

    crear_planilla: function() {
        this.emergente_planilla_key += 1;
        this.opciones_planilla.visible = true
    },

    onEditorPreparing: function(e) {
        /*
        if (e.parentType == 'dataRow' && e.dataField == 'direccion') {  
            let standardHandler = e.editorOptions.onValueChanged
            e.editorOptions.onValueChanged = (args) => {  
                console.log("cambio", args) 
                standardHandler(e)                        
            }    
        }    
        */ 
    },

    onRowUpdated: function(e) {
        console.log("onRowUpdated:", e)  
        this.enviar_accion("modificar", e.data)      
    }
}

export default {
    metodos: metodos
}