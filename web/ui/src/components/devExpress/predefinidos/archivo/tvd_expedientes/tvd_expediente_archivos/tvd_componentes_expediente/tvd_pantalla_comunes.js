import notify from 'devextreme/ui/notify'

let montar_componente = function(componente) {
    const montar = function() {
        this.elemento       = componente
        this.expediente_id  = window.$tvd_pantalla_expediente.forma.option("formData")["id"]
        this.forma          = this.$refs.forma.instance
        this.barra          = this.$refs.barra.instance
        this.notify         = notify
        this.mostrar_botones() 
        window.$archivo_expediente_tvd       = this
        window.$archivo_expediente_tvd_forma = this.forma
    }

    return  montar 
}

let metodos = {
    retorna: function(parametros) {     
        // Validar retorno errores
        this.indicador_visible   = false   
        parametros.datos["tipo"] = this.elemento
        window.$ventana_emergente_tvd.opciones.visible = false            
        this.notify("Operación realizada correctamente, en unos segundos la información estara disponible", "success")           
        window.$tvd_grid_archivos_expediente.refresh()
    },

    mostrar_todos() {
        let botones = this.barra_botones
        botones[0].options.visible = true
        botones[1].options.visible = true
        botones[2].options.visible = true
    },

    mostrar_botones() {
        this.mostrar_todos()
        let botones = this.barra_botones
        if (this.opciones.modo == "crear") {
            botones[1].options.visible = false
            botones[2].options.visible = false
        }        
        if (this.opciones.modo == "modificar") {
            botones[0].options.visible = false
        }

        this.barra.repaint()
    },

    boton_click(e) {
        let boton  = e.component.option("hint")   
        let accion = boton + "_" + this.elemento         
        let valido = this.forma.validate().isValid
        let datos  = this.forma.option("formData")
        console.log("datos:", datos)
        if ( valido == true) {
            let parametros = {
                expediente_id: this.expediente_id,
                datos        : datos,
                accion       : accion,
                boton        : boton
            }               
            let urlCompleta        = window.$direcciones.servidorDatos + '/tvd_expediente_acciones'   
            this.indicador_visible = true 
            window.$f["http"].llamadoRestPost( urlCompleta, parametros, this.retorna, "")               
        }
        else {
            this.notify("Valores invalidos o incompletos", "error")     
        }
        
    },

    mostrar_padre: function() {
        return (this.opciones.modo == 'crear')
    }
}

let barra_botones = function(forma) {
    return  [       
        { 
            widget  : "dxButton",           
            options :{ //0
                icon       : 'fas fa-plus-square',
                hint       : 'salvar',
                type       : 'success',
                text       : 'Salvar', 
                onClick    : forma.boton_click,
            } 
        },

        { 
            widget  : "dxButton",           
            options :{ //1
                icon       : 'fas fa-plus-square',
                hint       : 'modificar',
                type       : 'success',
                text       : 'Modificar', 
                onClick    : forma.boton_click,
            } 
        },

        {
            widget  : "dxButton",           
            options :{ //2
                icon       : 'fas fa-times-circle',
                hint       : 'borrar',
                type       : 'danger',
                text       : 'Borrar',
                onClick    : forma.boton_click,            
            }
        }             
    ]              
}

export default {
    metodos          : metodos,
    barra_botones    : barra_botones,
    montar_componente: montar_componente
}