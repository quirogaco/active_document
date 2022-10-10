
let elemento      = "radicacion_canales"
let accion_remota = '/especifico_acciones'
let urlCompleta   = window.$direcciones.servidorDatos + accion_remota    
            
let metodos = {
    retorna: function(retorna) {
        this.indicador_visible = false
        if (retorna.accion == "leer_radicacion_canales") {
            this.parametros.datos = retorna["datos"]["datos"]
        }
        else {            
            this.notify("Operación realizada correctamente", "success")  
        }      
    },

    boton_click(e) {
        let enviar     = true
        let validacion = this.forma.validate()     
        let datos      = this.forma.option("formData")
        datos["_tipo_"]= elemento 
        let parametros = {
            datos : datos,
            accion: ("salvar_"+elemento)
        }
        
        if ( ( validacion.isValid == true) && (enviar == true) ) {
            this.indicador_visible = true
            window.$f["http"].llamadoRestPost(urlCompleta, parametros, this.retorna, "")   
        }
    
        if ( ( validacion.isValid == false) && (enviar == true ) ) {
            this.notify("Valores invalidos o incompletos", "error")     
        }
    },

    cargar_datos(e) {
        let parametros  = {
            datos : {"_tipo_": elemento},
            accion: ("leer_"+elemento)
        } 
        this.indicador_visible = true
        window.$f["http"].llamadoRestPost(urlCompleta, parametros, this.retorna, "")   
    }
}

let barra_botones = function(grid) {
    return  [       
        {
            widget  : "dxButton",           
            options :{
                icon       : 'fas fa-edit',
                alignment  : 'center',
                hint       : 'salvar',
                type       : 'default',
                text       : 'Salvar',
                stylingMode: "contained",    
                onClick    : grid.boton_click,             
            }
        }      
    ]              
}

export default {
    metodos      : metodos,
    barra_botones: barra_botones
}