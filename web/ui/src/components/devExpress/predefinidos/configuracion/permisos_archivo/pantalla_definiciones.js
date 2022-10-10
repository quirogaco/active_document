
let grid_basico   = "permisos_archivo_grid"
let elemento      = "permisos_archivo"
let accion_remota = '/gestion_archivo'

let metodos = {
    retorna: function(retorna) {
        let accion             = retorna["accion"]
        this.indicador_visible = false
        this.notify("Operación realizada correctamente", "success")    
        this.$router.push(grid_basico)
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
            this.arbol_visible = true        
        }

        this.barra.repaint()
    },

    boton_click(e) {
        let boton      = e.component.option("hint")
        let enviar     = true
        let validacion = this.forma.validate()     
        let parametros = {
            datos: this.forma.option("formData")
        }
        switch (boton) {
            case 'crear': 
                parametros["accion"] = ("crear_"+elemento)
                break;

            case 'modificar':  
                parametros["accion"] = ("modificar_"+elemento)              
                break;
            
            case 'borrar':      
                parametros["accion"] = ("borrar_"+elemento)              
                break;

            case 'regresar':       
                enviar = false         
                this.$router.push(grid_basico)
                break;
        }

        if ( ( validacion.isValid == true) && (enviar == true) ) {
            this.indicador_visible = true
            let urlCompleta        = window.$direcciones.servidorDatos + accion_remota    
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
            options :{ //0
                icon       : 'fas fa-plus-square',
                alignment  : 'center',
                hint       : 'crear',
                type       : 'success',
                text       : 'Crear', 
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
                text       : 'Modificar',
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
                text       : 'Borrar',
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
                type       : 'normal',
                text       : 'Regresar',   
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