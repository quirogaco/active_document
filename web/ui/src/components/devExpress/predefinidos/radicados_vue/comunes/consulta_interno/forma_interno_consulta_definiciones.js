import forma_definiciones from "../../../comunes_vue/forma/forma.js";
import fuente from "../../../comunes_vue/forma/fuente.js";
import forma_general from "../../../comunes_vue/forma/forma.js";

let metodos = {
    montado_especifico: function(basicas) {
        let datos = forma_general.lee_propiedades(
            this.$props, 
            "forma_interno_consulta"
        );
        this.parametros = datos.datos;
        this.forma_datos(this.parametros.radicado);

        // Anexos
        let anexos = this.parametros.radicado['archivos']
        let fuente_anexos = fuente.fuente_arreglo(anexos) 
        forma_definiciones.asigna_fuente(this, "anexos_radicado", fuente_anexos)    
        
        // Logs
        let logs = this.parametros.radicado['logs']
        let fuente_logs = fuente.fuente_arreglo(logs) 
        forma_definiciones.asigna_fuente(this, "logs_radicado", fuente_logs)          
    },

    boton_click(e) {
        let accion = this.define_accion(e.component.option("hint"))  
        switch (accion) {
            case 'regresar':       
                window.scroll(0,0);
                this.$router.push(this.parametros.llamado_por)
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