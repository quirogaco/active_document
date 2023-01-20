import visores_archivo 
from "../../../../../../librerias/visores_archivo.js";

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

    'columna_doble_click':  function(e) {
        let data = e.data;
        if (e.column.dataField == "nro_radicado") {
            if (data.pdf_base.id !== undefined) {
                visores_archivo.ver_descarga_archivo({
                    titulo_general: "Consulta de Documentos/Anexos RADICADO",
                    archivo_id    : data.pdf_base.id, 
                    tipo_documento: data.pdf_base.tipo_archivo, 
                    titulo        : "Información documento",
                    modo          : "leer",
                    descarga      : 'evaluar'
                })  
            }
        }
        else {
            let mostrar = true;
            // let usuario_id = window.$usuario["id"];
            // let usuario_dependencia_id = window.$usuario["dependencia_id"];
            // let reserva = data["reserva"];
            // let gestion_responsable_id = data["gestion_responsable_id"];
            // let gestion_dependencia_id = data["gestion_dependencia_id"];
            // if (reserva == "SI") {
            //     if (usuario_id != gestion_responsable_id) {
            //         mostrar = false
            //     }
            // }

            if (mostrar == true) {                
                let datos = {
                    "id": data.id,
                    "radicado": data,
                    "modo": "consulta",
                    "llamado_por": "grid_gestion_salida"
                };
                $lib.call_component_storage(
                    "forma_salida_consulta",
                    {"datos": datos}
                )            
            }
            else {
                $notify("Documento con reserva!!", "error");
            }
        }
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

    // 'anular':  function(e) {
    //     if (this.grid.getSelectedRowKeys().length > 0) {            
    //         this.emergente_key_anula += 1;            
    //         this.opciones_ventana_anula.alto = 300;
    //         this.opciones_ventana_anula.ancho = 800;
    //         this.opciones_ventana_anula.visible = true;
    //         this.opciones_ventana_anula.accion = "ANULAR";
    //         this.opciones_ventana_anula.titulo_boton = "Anular salida";
    //         // Información del registro
    //         this.opciones_ventana_anula.datos = {
    //             "anula_ids": this.grid.getSelectedRowKeys()
    //         }
    //     }
    //     else {
    //         this.notify("Seleccione un radicado a anular!", "warning");
    //     }
    // },

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