import forma_definiciones from "../../../comunes_vue/forma/forma.js"
import forma_general from "../../../comunes_vue/forma/forma.js";
import fuente from "../../../comunes_vue/forma/fuente.js";

let acciones_especificas = {
    "ruta_remota"  : window.$direcciones.servidorDatos + '/radicados_acciones',
    "mensaje_envio": "Asignando radicado"
}

let metodos = {
    montado_especifico: function(basicas) {
        let datos = forma_general.lee_propiedades(
            this.$props, 
            "forma_pqrs_asigna"
        );
        this.parametros = datos.datos;
        // Anexos
        let anexos = this.parametros.radicado['anexos_radicado'];
        let fuente_anexos = fuente.fuente_arreglo(anexos) 
        forma_definiciones.asigna_fuente(
            this, 
            "anexos_radicado", 
            fuente_anexos
        )
     },

    recargar_forma: function() {
        window.$router.go(0)
    },

    retorna_remoto: function(retorna) {
        window.$ocultar_esperar()
        $sistema["notifica"]("Operación realizada correctamente", "success")    
        this.$router.push("grid_pqrs_asigna_grid")
    },

    boton_click(e) {
        let accion = this.define_accion(e.component.option("hint"))        
        let valida = this.forma_validacion()       
        let datos  = this.forma_datos()      
        switch (accion) {
            case 'asigna_pqrs':                
                let parametros = {
                    "accion": accion,
                    "datos" : datos
                }        
                if (valida == true) {  
                    let urlCompleta = acciones_especificas.ruta_remota                            
                    window.$f["http"].llamadoRestPost( urlCompleta, parametros, this.retorna_remoto, "", this.error_remoto)         
                    window.$mostrar_esperar(acciones_especificas.mensaje_envio + ", por favor espere..")
                }
                else {
                    $sistema["notifica"]("Datos invalidos o incompletos !!", "error")
                }
                break;

            case 'regresar':    
                window.scroll(0,0);  
                this.$router.push("grid_pqrs_asigna_grid")
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