<template >

    <DxLoadPanel
        v-model:visible = "indicador_visible" 
        message         = "Por favor espere"               
        shading-color   = "rgba(0,0,0,0.4)"
    />

    <div class="bg_tab_panel">
        <DxForm
            ref     = "forma"
            enctype = "multipart/form-data"
        >

            <DxSimpleItem
                data-field      = "archivos" 
                editor-type     = "dxFileUploader"                        
                :editor-options = "opciones_anexo"
            >
                <DxLabel text="Archivo electrónico"/>
                <DxRequiredRule message="Archivo obligatorio"/>                                      
            </DxSimpleItem>      

        </DxForm>

        <DxToolbar>
            <DxItem
                :options = "accion_opciones"
                location = "after"
                widget   = "dxButton"
            />
        </DxToolbar>

    </div>  

</template>

<script>
import { 
    DxForm,
    DxSimpleItem,
    DxEmptyItem,
    DxButtonItem,
    DxLabel,
    DxRequiredRule,
    DxStringLengthRule
} from 'devextreme-vue/form'
import { DxLoadPanel }       from 'devextreme-vue/load-panel'
import { DxFileUploader }    from 'devextreme-vue/file-uploader'
import DxToolbar, {DxItem}   from 'devextreme-vue/toolbar'
import DxButton              from 'devextreme-vue/button'
import notify                from 'devextreme/ui/notify'
import { locale, loadMessages, formatMessage } from 'devextreme/localization'

import fuenteDatos from '../../../remoto/fuenteDatos.js'

let comentario_gestion =  {
    name: 'anexo_gestion',
    components: {
        DxForm,
        DxSimpleItem,
        DxEmptyItem,
        DxButtonItem,
        DxLabel,
        DxRequiredRule,
        DxStringLengthRule,

        DxFileUploader,       
        DxButton,
        DxToolbar,
        DxItem,
        DxLoadPanel
    },

    created() {},

    props: {
        datos: {
            type: Object,
            default: () => {
                return {}
            }
        },  
    },

    mounted() {
        this.forma = this.$refs.forma.instance
        //console.log("this.forma:", this.forma)
    },

    methods: {
        retorna: function() {
            this.indicador_visible = false
            this.$parent.$parent.$_instance.hide()
        }
    },

    data() {
        return {
            indicador_visible: false,
            comentario     : null,

            // Carga de archivos
            opciones_anexo: {
                //uploadMode: "useForm",
                uploadMode: "useButtons",
                multiple: true,
                allowCanceling: true
            },  

            accion_opciones: {
                text: this.datos.boton_mensaje,
                type: "success",
                onClick: () => {
                    let datos_forma  = this.forma.option("formData");                    
                    if (datos_forma["archivos"] == undefined) {
                        notify(
                            {
                                message: "Archivo es obligatorio",                             
                                position: {
                                    my: 'center top',
                                    at: 'center top'
                                }
                            },
                            "warning", 
                        )
                    }
                    else {                        
                        let parametros = {
                            peticiones: this.datos.elementos,
                            accion    : this.datos.accion,
                            archivo   : datos_forma["archivos"]
                        }
                        this.indicador_visible = true
                        let urlCompleta = window.$direcciones.servidorDatos + '/gestion_acciones'    
                        window.$f["http"].llamadoRestPost( urlCompleta, parametros, this.retorna, "")   
                        this.$parent.$_instance.option("disabled", true)                           
                    }                    
                }
            }
        }
    }
}

export default comentario_gestion;

</script>