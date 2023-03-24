let metodos = function(that) {
    return {
        retorna: function(retorna) {
            let accion = retorna["accion"]
            that.indicador_visible = false
            that.notify("Operación realizada correctamente", "success")  
            console.log("retorna:", retorna)  
            that.dataForm.formData(retorna)
            
            if (accion=="crear_expediente") {
                that.parametros.modo = "modificar"            
                that.mostrar_botones();
                $lib.call_component_storage(
                    "expediente_basica_grid",   
                    {}
                )          
            }

            if (accion=="borrar_expediente") {
                $lib.call_component_storage(
                    "expediente_basica_grid",   
                    {}
                )    
            }
        },

        mostrar_todos() {
            let botones = that.barra_botones
            botones[0].options.visible = true
            botones[1].options.visible = true
            botones[2].options.visible = true
            botones[3].options.visible = true
        },

        mostrar_botones() {
            that.mostrar_todos()
            let botones = that.barra_botones
            if (that.parametros.modo == "crear") {
                botones[1].options.visible = false
                botones[2].options.visible = false
            }

            if (that.parametros.modo == "modificar") {
                botones[0].options.visible = false    
                that.expediente_archivos_visible = true        
            }

            that.barra.repaint()
        },

        boton_click(e) {
            let boton = e.component.option("hint")
            console.log("boton", boton)
            let enviar = true        
            let parametros = {
                datos: that.dataForm.formData()
            }
            let validacion;
            if (boton != "regresar") {
                validacion = that.dataForm.validateData();
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
                    $lib.call_component_storage(
                        "expediente_basica_grid",   
                        {}
                    )
                    break;
            }

            if (boton != "regresar") {
                if ( ( validacion.isValid == true) && (enviar == true) ) {
                    that.indicador_visible = true
                    let urlCompleta        = window.$direcciones.servidorDatos + '/expediente_acciones'    
                    window.$f["http"].llamadoRestPost( urlCompleta, parametros, that.retorna, "")   
                }
            
                if ( ( validacion.isValid == false) && (enviar == true ) ) {
                    that.notify("Valores invalidos o incompletos", "error")     
                }
            }
        }
    }
}

let barra_botones = function(that) {
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
                onClick    : that.boton_click,
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
                onClick    : that.boton_click,             
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
                onClick    : that.boton_click,            
            }
        },

        {
            widget  : "dxButton",           
            options :{ //3
                icon       : 'fas fa-angle-double-left',
                alignment  : 'center',
                hint       : 'regresar',
                text       : 'Regresar',  
                type       : 'normal', 
                stylingMode: "contained",  
                onClick    : that.boton_click,         
            }
        },
                    
    ]              
}


export default {
    metodos: metodos,
    barra_botones: barra_botones
}