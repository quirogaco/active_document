import { alert } from 'devextreme/ui/dialog'
import forma_definiciones from "../../../comunes_vue/forma/forma.js"
import fuente             from "../../../comunes_vue/forma/fuente.js"

let acciones_especificas = {
    "ruta_remota"  : window.$direcciones.servidorDatos + '/radicados_acciones',
    "mensaje_envio": "Radicando salida"
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
            console.log("salida -> gestion.borrador_id:", gestion.borrador_id)
            this.borrador_id = gestion.borrador_id
            this.gestion_id  = gestion.id

            // Anexos
            let anexos        = gestion.archivos.filter(anexo => anexo.nombre.indexOf("borrador_") == -1)
            let fuente_anexos = fuente.fuente_arreglo(anexos) 
            forma_definiciones.asigna_fuente(this, "anexos_radicado", fuente_anexos)           
            
            if ( this.parametros.gestion.origen_tipo == "ENTRADA") {
                // Asigna informacion de entrada
                let entrada = this.parametros.gestion.entrada
                const campos_tercero = [
                    "tercero_tercero_tipo_id", 
                    "busca_remitente",
                    "tercero_tipo_identificacion_id",
                    "tercero_nro_identificacion",
                    "tercero_razon_social",
                    "tercero_apellidos",
                    "tercero_nombres",
                    "tercero_cargo",
                    "tercero_direccion", 
                    "tercero_codigo_postal",
                    "tercero_telefono",
                    "tercero_telefono_movil",
                    "tercero_fax", 
                    "tercero_ciudad_id"
                ]

                for (const indice in campos_tercero) {
                    let campo = campos_tercero[indice]
                    forma_datos[campo] = entrada[campo]
                }
                forma_datos["radicado_responde"] = entrada["nro_radicado"]
                this.forma_datos(forma_datos)            
            } 
        }
    },

    recargar_forma: function() {
        window.$router.go(0)
    },

    retorna_remoto: function(retorna) {
        console.log("retorna_remoto:", retorna)
        let nro_radicado = retorna.datos.datos.nro_radicado
        window.$ocultar_esperar()
        let resultado    = alert( ("Radicado número " + nro_radicado), "Salida radicada")
        resultado.then(dialogo => {
            if (this.parametros.gestion != undefined) {
                window.$pantalla_gestion.opciones_ventana.visible = false
                this.$router.push({path: "gestion_basica_grid"})
            }        
        })

        /*
        let someJSONdata = [
            {
                name: 'John Doe',
                email: 'john@doe.com',
                phone: '111-111-1111'
            },
            {
                name: 'Barry Allen',
                email: 'barry@flash.com',
                phone: '222-222-2222'
            },
            {
                name: 'Cool Dude',
                email: 'cool@dude.com',
                phone: '333-333-3333'
            }
        ]
        let componente = this
        
        let focuser = setInterval(() => window.dispatchEvent(new Event('focus')), 500)
        window.$print({
            printable         : someJSONdata, 
            properties        : ['name', 'email', 'phone'], 
            type              : 'json', 
            showModal         : true,
            onPrintDialogClose:  () => {
                clearInterval(focuser)
                componente.recargar_forma()
            }
        })
        */
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
        console.log("radica-salida->parametros:", parametros)       
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