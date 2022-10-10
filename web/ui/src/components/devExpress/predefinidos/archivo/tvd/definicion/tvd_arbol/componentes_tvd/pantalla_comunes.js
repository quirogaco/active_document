import notify from 'devextreme/ui/notify'

let montar_componente = function(componente) {
    const montar = function() {
        this.elemento              = componente
        this.tvd_id                = window.$pantalla_tvd.forma.option("formData")["id"]
        this.seleccionado_padre_id = window.$pantalla_tvd.arbol.seleccionado_padre_id
        this.seleccionado_tipo     = window.$pantalla_tvd.arbol.seleccionado_tipo
        this.seleccionado_id       = window.$pantalla_tvd.arbol.seleccionado_id
        this.seleccionado_nombre   = window.$pantalla_tvd.arbol.seleccionado_nombre        
        this.seleccionado_modo     = window.$pantalla_tvd.arbol.seleccionado_modo
        this.forma                 = this.$refs.forma.instance
        this.barra                 = this.$refs.barra.instance
        this.notify                = notify  
        this.mostrar_botones() 
    }

    return  montar 
}

let metodos = {
    retorna: function(parametros) {   
        // Validar retorno errores
        parametros.datos["tipo"] = this.elemento
        if (this.elemento != "acceso") {
            window.$tvd_arbol.ejecutar_operacion(parametros.boton, parametros.padre_id,  parametros.datos) 
        }      
        window.$ventana_emergente_tvd.opciones.visible = false   
        this.notify("Operación realizada correctamente", "success") 
        this.indicador_visible = false
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
        if ( valido == true) {
            let parametros = {
                tvd_id      : this.tvd_id,
                padre_tipo  : this.seleccionado_tipo,
                padre_nombre: this.seleccionado_nombre,
                modo        : this.seleccionado_modo,
                datos       : datos,
                accion      : accion,
                boton       : boton
            }               
            if (boton == "salvar") {
                parametros["padre_id"] = this.seleccionado_id
            }
            if (boton == "modificar") {
                parametros["padre_id"] = this.seleccionado_padre_id
            }

            let urlCompleta        = window.$direcciones.servidorDatos + '/tvd_acciones'   
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