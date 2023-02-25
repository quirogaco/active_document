import forma_definiciones from "../../comunes_vue/forma/forma.js"
import fuente from "../../comunes_vue/forma/fuente.js"
import forma_general from "../../comunes_vue/forma/forma.js";

let metodos = {
    montado_especifico: function(basicas) {
        let datos = forma_general.lee_propiedades(
            this.$props, 
            "gestion_datos_consulta"
        ).datos;
        this.parametros = datos;
        
        // // Anexos
        let anexos = datos.gestion.archivos;
        let fuente_anexos = fuente.fuente_arreglo(anexos);
        forma_definiciones.asigna_fuente(
            this, 
            "anexos_radicado", 
            fuente_anexos
        );    
        
        // Anotaciones
        let anotaciones = datos.gestion.atributos_['anotaciones'];
        if (anotaciones == undefined) {
            anotaciones = []
        };
        let contador = 0;
        anotaciones.sort(function (a, b) {
            if (a.fecha < b.fecha) {
              return 1;
            }
            if (a.fecha > b.fecha) {
              return -1;
            }
            
            return 0;
        });
        anotaciones = anotaciones.map(function(anotacion) {
            anotacion["id"] = contador
            anotacion["fecha"] = anotacion["fecha"].substring(0, 19).replace("T", " ")
            contador += 1
            return anotacion
         });

        // Fuente de datos
        let fuente_gestion_comentarios = fuente.fuente_arreglo(anotaciones) 
        forma_definiciones.asigna_fuente(
            this, 
            "gestion_comentarios", 
            fuente_gestion_comentarios
        ); 

        // Trd        
        let trd = datos.gestion.atributos_['trd'];
        let expedientes = [];
        if (trd !== undefined) {
            expedientes.push({
                "id": 0,
                "trd_dependencia_nombre": this.gestion.trd_dependencia_nombre,
                "expediente_nombre": this.gestion.expediente_nombre,
                "tipo_nombre": this.gestion.tipo_nombre
            })
        };
        let fuente_trd = fuente.fuente_arreglo(expedientes);
        forma_definiciones.asigna_fuente(this, "expedientes_tipos", fuente_trd);    
    },

    boton_click(e) {
        let accion = this.define_accion(e.component.option("hint"));
        switch (accion) {
            case 'regresar':       
                this.parametros.call(this);
                break;
        }
    },

    mostrar_todos() {
        let botones = this.barra_botones;
        botones[0].options.visible = false;
        if (this.parametros.llamado_por != undefined) {
            botones[0].options.visible = true;
        }
    }
}

let metodos_totales = Object.assign(
    {}, 
    forma_definiciones.forma_funciones, 
    metodos
)

export default {
    metodos: metodos_totales
}