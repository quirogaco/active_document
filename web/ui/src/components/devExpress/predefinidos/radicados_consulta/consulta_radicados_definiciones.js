
let elemento      = "radicado"
let accion_remota = '/especifico_acciones'
let urlCompleta   = window.$direcciones.servidorDatos + accion_remota    
            
let metodos = {
    retorna: function(retorna) {
        this.indicador_visible = false
        let forma_datos        = this.forma.option("formData")
        let datos   = retorna["datos"]["datos"]     
        let mensaje = retorna["datos"]["mensaje"]        
        if (mensaje == "") {
            this.grupo_datos_visible = true
            forma_datos["gestion_estado"]             = datos["gestion_estado"]
            forma_datos["gestion_inicio"]             = datos["gestion_inicio"]
            forma_datos["gestion_dependencia_nombre"] = datos["gestion_dependencia_nombre"]
        }
        else {
            this.notify(mensaje, "success")  
        }      
    },

    boton_click(e) {
        this.grupo_datos_visible = false
        let enviar     = true
        let validacion = this.forma.validate()     
        let datos      = this.forma.option("formData")
        datos["_tipo_"]= elemento 
        let parametros = {
            datos : datos,
            accion: ("consultar_"+elemento)
        }
        
        if ( ( validacion.isValid == true) && (enviar == true) ) {
            this.indicador_visible = true
            window.$f["http"].llamadoRestPost(urlCompleta, parametros, this.retorna, "")   
        }
    
        if ( ( validacion.isValid == false) && (enviar == true ) ) {
            this.notify("Valores invalidos o incompletos", "error")     
        }
    }
}

let barra_botones = function(grid) {
    return  [       
        {
            widget  : "dxButton",           
            options :{
                icon       : 'fas fa-edit',
                alignment  : 'center',
                hint       : 'consultar',
                type       : 'default',
                text       : 'Consultar',
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