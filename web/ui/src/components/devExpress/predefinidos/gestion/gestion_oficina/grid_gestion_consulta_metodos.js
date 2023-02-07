import visores_archivo 
from "../../../../../librerias/visores_archivo.js";

import estructuras from '../../../../../librerias/estructuras.js';
// import ventanilla_salida_forma 
// from '../../radicados_vue/salida/radicacion_formulario/salida_forma_radicado.vue';
// import ventanilla_interno_forma 
// from '../../radicados_vue/interno/radicacion_formulario/interno_forma_radicado.vue';
// import gestion_datos_consulta 
// from '../gestion_datos/gestion_datos_consulta.vue';
// import ventanilla_radicado_consulta 
//     from '../../radicados_vue/comunes/consulta/forma_radicado_consulta.vue';

let metodos = {
    onToolbarPreparing(e) {
        e.toolbarOptions.items.push({
            location: 'after',
            template: 'notificarButton'
        })    
        
        // e.toolbarOptions.items.push({
        //     location: 'after',
        //     template: 'anularButton'
        // })    
    },

    'columna_doble_click': async function(e) {
        let data = e.data;
        let estructura = "radicados_entrada";
        let forma = "forma_radicado_consulta";

        console.log("data:", e.data)
        if (e.data.tipo_radicado == "SALIDA") {
            estructura = "radicados_salida";
            forma = "forma_salida_consulta";
        };

        if (e.data.tipo_radicado == "INTERNO") {
            estructura = "radicados_interno";
            forma = "forma_interno_consulta";
        };

        let registro = await estructuras.leer_registro_id(
            estructura, 
            e.data.id
        );
                  
        let datos = {
            "id": data.id,
            "radicado": registro,
            "modo": "consulta",
            "llamado_por": "grid_gestion_consulta"
        };
        $lib.call_component_storage(
            forma,
            {"datos": datos}
        )            
    },

    'notificar':  function(e) {
        if (this.grid.getSelectedRowKeys().length > 0) {            
            this.emergente_key += 1;            
            this.opciones_ventana.alto = 300;
            this.opciones_ventana.ancho = 800;
            this.opciones_ventana.visible = true;
            this.opciones_ventana.accion = "NOTIFICAR";
            this.opciones_ventana.titulo_boton = "Notificar via correo";
            // Información del registro
            this.opciones_ventana.datos = {
                "notificar_ids": this.grid.getSelectedRowKeys()
            }
        }
        else {
            this.notify("Seleccione un radicado a notificar!", "warning");
        }
    },

    'icono_pdf_template': function(data) {
        let resultado = data.value
        if (data.data.pdf_base.id !== undefined) {
            resultado = '<i class="far fa-file-pdf fa-lg" title="Doble click para ver documento" style="color:blue; cursor: pointer"></i>&nbsp;&nbsp;' + data.value
        }

        return resultado
    }

}

export default {
    metodos: metodos
}