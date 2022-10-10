import notify from 'devextreme/ui/notify'

let metodos = {
    retorna: function(parametros) {     
        this.indicador_visible = false;
        $expediente_archivos.opciones_ventana.visible = false;
        notify("Operación realizada correctamente, en unos segundos la información estara disponible!!", "success");
        window.$grid_archivos_expediente.refresh()
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
        if (this.parametros.modo == "crear") {
            botones[1].options.visible = false
            botones[2].options.visible = false
        }        
        if (this.parametros.modo == "modificar") {
            botones[0].options.visible = false
        }

        this.barra.repaint()
    },

    boton_click(e) {
        let boton  = e.component.option("hint"); 
        let accion = boton + "_archivo";
        let valido = this.forma.validate().isValid;
        let datos  = this.forma.option("formData");
        if ( valido == true) {            
            let parametros = {
                expediente_id: this.parametros.datos.expediente_id,
                datos        : datos,
                accion       : accion,
                boton        : boton
            }               
            let urlCompleta        = window.$direcciones.servidorDatos + '/expediente_acciones'   
            this.indicador_visible = true 
            window.$f["http"].llamadoRestPost( urlCompleta, parametros, this.retorna, "")                     
        }
        else {
            notify("Valores invalidos o incompletos", "error")     
        }
    },

    mostrar_padre: function() {
        return (this.parametros.modo == 'crear')
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
    barra_botones    : barra_botones
}