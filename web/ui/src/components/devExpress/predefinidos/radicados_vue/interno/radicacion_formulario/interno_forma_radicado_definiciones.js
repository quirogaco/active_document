import { alert } from 'devextreme/ui/dialog'
import forma_definiciones from "../../../comunes_vue/forma/forma.js"
import fuente             from "../../../comunes_vue/forma/fuente.js"

let acciones_especificas = {
    "ruta_remota"  : window.$direcciones.servidorDatos + '/radicados_acciones',
    "mensaje_envio": "Radicando interno"
}

let metodos = {
    //regresar_visual: function() {},
    //error_accion: function(error_datos) {},

    montado_especifico: function(basicas) {
        let forma_datos = this.forma_datos()     
        
        // Radicado desde gestión
        if ( this.parametros.gestion != undefined) {
            // Información gestión
            let gestion      = this.parametros.gestion.gestion
            console.log("interno -> gestion.borrador_id:", gestion.borrador_id)
            this.borrador_id = gestion.borrador_id
            this.gestion_id  = gestion.id

            // Anexos
            let anexos        = gestion.archivos.filter(anexo => anexo.nombre.indexOf("borrador_") == -1)
            let fuente_anexos = fuente.fuente_arreglo(anexos) 
            forma_definiciones.asigna_fuente(this, "anexos_radicado", fuente_anexos)                       
        }
    },

    recargar_forma: function() {
        window.$router.go(0)
    },

    retorna_remoto: function(retorna) {
        console.log("retorna_remoto:", retorna)
        let nro_radicado = retorna.datos.datos.nro_radicado
        window.$ocultar_esperar()
        let resultado    = alert( ("Radicado número " + nro_radicado), "Interno radicado")
        resultado.then(dialogo => {
            if (this.parametros.gestion != undefined) {
                window.$pantalla_gestion.opciones_ventana.visible = false
                this.$router.push({path: "gestion_basica_grid"})
            }        
        })
    },

    boton_click(e) {
        let accion = this.define_accion(e.component.option("hint"))        
        let valida = this.forma_validacion()       
        let datos = this.forma_datos()
        // Borrador word de respuesta
        datos["borrador_id"] = this.borrador_id
        datos["gestion_id"]  = this.gestion_id
        console.log("this.borrador_id, this.gestion_id :", this.borrador_id, this.gestion_id)  
        let parametros = {
            "accion": accion,
            "datos" : datos
        }
        console.log("radica-interno->parametros:", parametros)       
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