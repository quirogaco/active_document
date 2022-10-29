import forma_definiciones from "../../../comunes_vue/forma/forma.js";
import fuente from "../../../comunes_vue/forma/fuente.js";
import forma_general from "../../../comunes_vue/forma/forma.js"

let metodos = {
    //regresar_visual: function() {},
    //error_accion: function(error_datos) {},
    montado_especifico: function(basicas) {
        console.log("]>>>this.$props:", this.$props)
        this.parametros = forma_general.lee_propiedades(this.$props, "ventanilla_radicado_consulta");
        console.log("]>>>this.parametros:", this.parametros)
        this.forma_datos(parametros.datos);

        // Anexos
        let anexos        = this.parametros.datos['archivos']
        let fuente_anexos = fuente.fuente_arreglo(anexos) 
        forma_definiciones.asigna_fuente(this, "anexos_radicado", fuente_anexos)    
        
        // Logs
        let logs        = this.parametros.datos['logs']
        let fuente_logs = fuente.fuente_arreglo(logs) 
        forma_definiciones.asigna_fuente(this, "logs_radicado", fuente_logs)        
        
        // Con copia
        let con_copia    = this.parametros.datos['con_copia']
        let fuente_copia = fuente.fuente_arreglo(con_copia) 
        forma_definiciones.asigna_fuente(this, "con_copia", fuente_copia)    
    },

    boton_click(e) {
        let accion = this.define_accion(e.component.option("hint"))  
        switch (accion) {
            case 'regresar':       
                window.scroll(0,0); 
                if (this.parametros._visible != undefined) {
                    this.parametros._visible = false;
                }
                else {
                    this.$router.push(this.parametros.llamado_por)
                }
                break;
        }
    },

    mostrar_todos() {
        let botones = this.barra_botones
        botones[0].options.visible = false
        if (this.parametros.llamado_por != undefined) {
            botones[0].options.visible = true
        }
    }
}

let metodos_totales = Object.assign({}, forma_definiciones.forma_funciones, metodos)

export default {
    metodos: metodos_totales
}