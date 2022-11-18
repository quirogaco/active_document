import { confirm }        from 'devextreme/ui/dialog'
import visores_archivo    from "../../../../../../../librerias/visores_archivo.js"
import forma_definiciones from "../../../../comunes_vue/forma/forma.js"

let acciones_especificas = {
    "ruta_remota"  : window.$direcciones.servidorDatos + '/radicados_acciones',
    "mensaje_envio": "Radicando DOCUMENTO"
}

let metodos_forma = function(that) {
    let metodos = {
        //regresar_visual: function() {},
        //error_accion: function(error_datos) {},
        //montado_especifico: function(basicas) {},

        recargar_forma: function() {
            window.scroll(0,0);                  
            that.$router.push("ventanilla_radicado_grid")
        },

        retorna_remoto: function(retorna) {
            window.$ocultar_esperar()        
            let nro_radicado   = retorna.datos.datos.nro_radicado
            let llamar_funcion = that.recargar_forma
            let resultado    = confirm(("Descarga PDF con información registrada ?"), "Petición " + nro_radicado)
            resultado.then(dialogo => {
                if (dialogo == true) {
                    visores_archivo.ver_descarga_archivo(
                        {
                            archivo_id    : ("ENTRADA__" + nro_radicado), 
                            tipo_documento: "pdf", 
                            descarga      : 'si',
                            operacion     : 'radicado_pdf',
                            llamar_funcion: llamar_funcion
                        },                     
                    )   
                }
                else {
                    that.recargar_forma()
                }
            })
        },

        boton_click(e) {
            let accion = e.component.option("hint");
            console.log(e.component.option("hint"))
            
            //let accion = that.define_accion(e.component.option("hint"))        
            let valida = that.forma_validacion();
            let datos = that.forma_datos();
            datos["clase_radicado"] = "VENTANILLA";
            datos["formulario_web"] = null;
            switch (accion) {
                case 'radicar_ventanilla': 
                    let parametros = {
                        "accion": accion,
                        "datos" : datos
                    }
                    console.log("parametros:", parametros)       
                    // Datos OK
                    if (valida == true) {  
                        // Envio de datos
                        let urlCompleta = acciones_especificas.ruta_remota                            
                        window.$f["http"].llamadoRestPost( urlCompleta, parametros, that.retorna_remoto, "", that.error_remoto)         
                        // Mensaje
                        window.$mostrar_esperar(acciones_especificas.mensaje_envio + ", por favor espere..")
                    }
                    else {
                        $sistema["notifica"]("Datos invalidos o incompletos !!", "error")
                    }
                    break;

                case 'regresar':       
                    window.scroll(0,0);  
                    $lib.call_component_storage(
                        "ventanilla_radicado_grid", 
                        {"datos": {}}
                    );
                    break;
            }
        },

        mostrar_todos() {
            let botones = that.barra_botones
            botones[0].options.visible = true
            botones[1].options.visible = true
        }
    };

    return  Object.assign({}, forma_definiciones.forma_funciones, metodos)
}

//let metodos_totales = Object.assign({}, forma_definiciones.forma_funciones, metodos)

export default {
    //metodos: metodos_totales
    metodos_forma: metodos_forma
}