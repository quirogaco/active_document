import visores_archivo    from "../../../../../../librerias/visores_archivo.js"

let metodos = {
    onToolbarPreparing(e) {
        e.toolbarOptions.items.push({
            location: 'after',
            template: 'radicarButton'
        })          
    },

    'radicar':  function(e) {
        this.$router.push({
            name: "pqrs_radicado_forma",
            params: {
                "datos": JSON.stringify({})                
            }
        })
    },

    'columna_doble_click':  function(e) {
        let data = e.data
        if (e.column.dataField == "clase_radicado") {
            if (data.pdf_base.id !== undefined) {
                visores_archivo.ver_descarga_archivo({
                    titulo_general: "Consulta de Documentos/Anexos RADICADO",
                    archivo_id    : data.pdf_base.id, 
                    tipo_documento: data.pdf_base.tipo_archivo, 
                    titulo        : data.pdf_base.detalle,
                    modo          : "leer",
                    descarga      : 'evaluar'
                })  
            }
        }
        else {
            //let archivos = $lib.elimina_atributo(data, 'archivos');
            console.log("DATA-XXXXX:", data)
            //e.data['anexos_radicado'] = archivos
            this.$router.push({
                name: "forma_radicado_consulta",
                params: {                     
                    "attributes_str": JSON.stringify({
                        "id"         : e.data.id,
                        "datos"      : e.data,
                        "modo"       : "consulta",
                        "llamado_por": "grid_radica_asigna_grid"
                    })                
                }
            })
        }
    },

    'icono_pdf_template': function(data) {
        let resultado = data.value
        if (data.data.pdf_base.id !== undefined) {
            resultado =  '<i class="far fa-file-pdf fa-lg" title="Doble click para ver documento" style="color:blue; cursor: pointer" ></i>&nbsp;&nbsp;' + data.value
        }

        return resultado
    }
}

export default {
    metodos: metodos
}