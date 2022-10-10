import { confirm }        from 'devextreme/ui/dialog'
import visores_archivo    from "../../../../../../librerias/visores_archivo.js"
import forma_definiciones from "../../../comunes_vue/forma/forma.js"

let acciones_especificas = {
    "ruta_remota"  : window.$direcciones.servidorDatos + '/radicados_acciones',
    "mensaje_envio": "Radicando PQRS"
}

let metodos = {
    //regresar_visual: function() {},
    //error_accion: function(error_datos) {},
    //montado_especifico: function(basicas) {},

    recargar_forma: function() {        
        //window.scroll(0,0);                  
        //this.$router.push("grid_radica_asigna_grid")
    },

    retorna_remoto: function(retorna) {
        window.$ocultar_esperar()        
        let nro_radicado   = retorna.datos.datos.nro_radicado
        let llamar_funcion = this.recargar_forma
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
                this.recargar_forma()
            }
        })
    },

    boton_click(e) {
        let accion = this.define_accion(e.component.option("hint"))        
        let valida = this.forma_validacion()       
        let datos = this.forma_datos()
        console.log("DATOS:", datos);
        datos["clase_radicado"] = "PQRS"
        datos["formulario_web"] = null
        switch (accion) {
            case 'radicar_pqrs': 
                let parametros = {
                    "accion": accion,
                    "datos" : datos
                }
                // Datos OK
                if (valida == true) {  
                    // Envio de datos
                    let urlCompleta = acciones_especificas.ruta_remota                            
                    window.$f["http"].llamadoRestPost( urlCompleta, parametros, this.retorna_remoto, "", this.error_remoto)         
                    // Mensaje
                    window.$mostrar_esperar(acciones_especificas.mensaje_envio + ", por favor espere..")
                }
                else {
                    $sistema["notifica"]("Datos invalidos o incompletos !!", "error")
                }
                break;

            case 'regresar':       
                window.scroll(0,0);  
                this.$router.push("grid_radica_asigna_grid")
                break;
        }
    },

    mostrar_todos() {
        let botones = this.barra_botones
        botones[0].options.visible = true
        botones[1].options.visible = true
    }
}

let metodos_totales = Object.assign({}, forma_definiciones.forma_funciones, metodos)

export default {
    metodos: metodos_totales
}