import { confirm }        from 'devextreme/ui/dialog'
import visores_archivo    from "../../../../../../../librerias/visores_archivo.js"
import forma_definiciones from "../../../../comunes_vue/forma/forma.js"

let acciones_especificas = {
    "ruta_remota": window.$direcciones.servidorDatos + '/radicados_acciones',
    "mensaje_envio": "Radicando DOCUMENTO"
}

let metodos_forma = function(that) {
    let metodos = {
        recargar_forma: function() {
            window.scroll(0,0);  
            $lib.call_component_storage(
                that.retorna, 
                {"datos": {}}
            )
        },

        retorna_remoto: function(retorna) {
            window.$ocultar_esperar()        
            let nro_radicado = retorna.datos.datos.nro_radicado
            let llamar_funcion = that.recargar_forma
            let resultado = confirm(
                "Descarga PDF con información registrada ?", 
                "Petición " + nro_radicado
            )
            resultado.then(dialogo => {
                if (dialogo == true) {
                    visores_archivo.ver_descarga_archivo(
                        {
                            archivo_id: ("ENTRADA__" + nro_radicado), 
                            tipo_documento: "pdf", 
                            descarga: 'si',
                            operacion: 'radicado_pdf',
                            llamar_funcion: llamar_funcion
                        },                     
                    )   
                }
                //else {
                    that.recargar_forma()
                //}
            })
        },

        boton_click(e) {
            let accion = e.component.option("hint");    
            let valida = that.forma_validacion();
            let datos = that.forma_datos();
            datos["clase_radicado"] = datos["es_pqrs"];
            datos["formulario_web"] = null;            
            // OJO CON CORREOS//
            switch (accion) {
                case 'radicar_ventanilla':
                    let parametros = {
                        "accion": accion,
                        "datos" : datos
                    }
                    // Datos OK
                    if (valida == true) {  
                        // Envio de datos
                        let urlCompleta = acciones_especificas.ruta_remota                            
                        window.$f["http"].llamadoRestPost( 
                            urlCompleta, 
                            parametros, 
                            that.retorna_remoto, 
                            "", 
                            that.error_remoto
                        )         
                        // Mensaje
                        window.$mostrar_esperar(
                            acciones_especificas.mensaje_envio + 
                            ", por favor espere.."
                        )
                    }
                    else {
                        $sistema["notifica"](
                            "Datos invalidos o incompletos !!", 
                            "error"
                        )
                    }
                    break;

                case 'regresar':       
                    window.scroll(0,0);  
                    let dat_p = $get_params("ventanilla_radicado_forma")?.datos;
                    if (dat_p) {
                        $lib.call_component_storage(
                            that.retorna, 
                            {"datos": {}}
                        );
                    }
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

export default {
    metodos_forma: metodos_forma
}