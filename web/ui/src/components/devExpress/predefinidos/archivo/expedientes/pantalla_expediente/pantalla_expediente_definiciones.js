let metodos = {
    retorna: function(retorna) {
        let accion = retorna["accion"]
        this.indicador_visible = false
        this.notify("Operación realizada correctamente", "success")    
        this.forma.formData(retorna)
        
        if (accion=="crear_expediente") {
            this.parametros.modo = "modificar"            
            this.mostrar_botones();
            this.$router.push("expediente_basica_grid");           
        }

        if (accion=="borrar_expediente") {
            this.$router.push("expediente_basica_grid")         
        }
    },

    mostrar_todos() {
        let botones = this.barra_botones
        botones[0].options.visible = true
        botones[1].options.visible = true
        botones[2].options.visible = true
        botones[3].options.visible = true
    },

    mostrar_botones() {
        this.mostrar_todos()
        let botones = this.barra_botones
        if (this.parametros.modo == "crear") {
            botones[1].options.visible = false
            botones[2].options.visible = false
        }

        if (this.parametros.modo == "modificar") {
            botones[0].options.visible = false    
            this.expediente_archivos_visible = true        
        }

        this.barra.repaint()
    },

    boton_click(e) {
        let boton      = e.component.option("hint")
        let enviar     = true        
        let parametros = {
            datos: this.forma.formData()
        }
        let validacion;
        if (boton != "regresar") {
            validacion = this.forma.validateData();
        }
        switch (boton) {
            case 'crear': 
                parametros["accion"] = "crear_expediente"
                break;

            case 'modificar':  
                parametros["accion"] = "modificar_expediente"              
                break;
            
            case 'borrar':      
                parametros["accion"] = "borrar_expediente"              
                break;

            case 'regresar':       
                enviar = false         
                this.$router.push("expediente_basica_grid")
                break;
        }

        if (boton != "regresar") {
            if ( ( validacion.isValid == true) && (enviar == true) ) {
                this.indicador_visible = true
                let urlCompleta        = window.$direcciones.servidorDatos + '/expediente_acciones'    
                window.$f["http"].llamadoRestPost( urlCompleta, parametros, this.retorna, "")   
            }
        
            if ( ( validacion.isValid == false) && (enviar == true ) ) {
                this.notify("Valores invalidos o incompletos", "error")     
            }
        }
    },

    // Funcion llamada por evento mounted DataForma
    dataFormaMounted(DataForma) {}
}

let barra_botones = function(grid) {
    return  [       
        { 
            widget  : "dxButton",           
            options :{ //0
                icon       : 'fas fa-plus-square',
                alignment  : 'center',
                hint       : 'crear',
                type       : 'success',
                text       : 'Crear Expediente', 
                stylingMode: "contained", 
                onClick    : grid.boton_click,
            } 
        },
        {
            widget  : "dxButton",           
            options :{ //1
                icon       : 'fas fa-edit',
                alignment  : 'center',
                hint       : 'modificar',
                type       : 'default',
                text       : 'Modificar Expediente',
                stylingMode: "contained",    
                onClick    : grid.boton_click,             
            }
        },

        {
            widget  : "dxButton",           
            options :{ //2
                icon       : 'fas fa-times-circle',
                alignment  : 'center',
                hint       : 'borrar',
                type       : 'danger',
                text       : 'Borrar Expediente',
                stylingMode: "contained",   
                onClick    : grid.boton_click,            
            }
        },

        {
            widget  : "dxButton",           
            options :{ //3
                icon       : 'fas fa-angle-left',
                alignment  : 'center',
                hint       : 'regresar',
                type       : 'back',
                text       : 'Regresar',   
                stylingMode: "contained",  
                onClick    : grid.boton_click,         
            }
        },
                    
    ]              
}


export default {
    metodos      : metodos,
    barra_botones: barra_botones
}