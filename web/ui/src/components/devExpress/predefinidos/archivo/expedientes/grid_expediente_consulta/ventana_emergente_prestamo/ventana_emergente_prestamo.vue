<template>
        <DxPopup
            ref                     = "popup"    
            v-model:visible         = "opciones.visible"        
            :drag-enabled           = "false"
            :close-on-outside-click = "false"
            :show-close-button      = "true"
            :show-title             = "true"            
            :width                  = "opciones.ancho"
            :height                 = "opciones.alto"
            :title                  = "opciones.titulo"            
            :element-attr           = "popupAttributes"
        >        

            <DxLoadPanel
                v-model:visible = "indicador_visible" 
                message         = "Por favor espere"               
                shading-color   = "rgba(0,0,0,0.4)"
            />


            <DxForm
                ref        = "forma"
                id         = "prestamo_expediente"
                :form-data = "opciones.datos"
            >

                <DxSimpleItem
                    data-field  = "motivo"
                    editor-type = "dxTextBox"
                >
                    <DxLabel text="Motivo"/>
                    <DxRequiredRule message="Motivo prestamo"/> 
                    <DxStringLengthRule
                        :max="256"
                        message="Maximo 200 caracteres"
                    />                      
                </DxSimpleItem>

                <DxEmptyItem/>                

            </DxForm>

            <div class="centered">
                <DxButton
                    @click = "solicitar()"
                    icon   = "fas fa-plus-square"
                    text   = "Enviar solicitud"
                    type   = "success"  
                />
            </div>

        </DxPopup>

    
</template>

<script>
import { DxButton } from 'devextreme-vue/button'
import { DxLoadPanel } from 'devextreme-vue/load-panel';
import { DxPopup } from 'devextreme-vue/popup'
import { DxScrollView } from 'devextreme-vue/scroll-view'

import { 
    DxForm,
    DxSimpleItem,
    DxEmptyItem,
    DxButtonItem,
    DxLabel,
    DxRequiredRule,
    DxStringLengthRule
} from 'devextreme-vue/form';
import notify from 'devextreme/ui/notify'

let ventana =  {
    name: 'ventana_emergente_prestamo',

    components: {
        DxLoadPanel,
        DxPopup,
        DxScrollView,
        DxButton,
        DxForm,
        DxSimpleItem,
        DxEmptyItem,
        DxButtonItem,
        DxLabel,
        DxRequiredRule,
        DxStringLengthRule
    },

    created() {},

    props: {
        opciones: {
            type: Object,
            default: () => {
                return {}
            }
        }        
    },

    mounted() {    
        this.forma             = this.$refs.forma.instance
        this.notify            = notify 
        this.indicador_visible = false
        setTimeout(() => {
            window.$ventana_emergente_prestamo = this
        })
    },

    data() {
        return {
            popupAttributes: {
                id: 'ventana_emergente_prestamo',
                class: 'bg_tab_panel'
            },

            indicador_visible: false
        }
    },

    methods: {
        retorna: function(parametros) {   
                this.opciones.visible = false   
                this.notify("Prestamo solicitado", "success") 
                this.indicador_visible = false
        },

        solicitar(e) {
            let valido = this.forma.validate().isValid
            let datos  = this.forma.option("formData")
            if ( valido == true) {
                let parametros = {
                    datos       : {
                        "expedientes_id": datos.expedientes_id,
                        "motivo"        : datos.motivo
                    },
                    accion      : "crear_prestamo"
                }               
            
                let urlCompleta        = window.$direcciones.servidorDatos + '/trd_acciones'   
                this.indicador_visible = true 
                window.$f["http"].llamadoRestPost( urlCompleta, parametros, this.retorna, "")                                      
            }
            else {
                this.notify("Valores invalidos o incompletos", "error")     
            }
        },
    }
}

export default ventana;

</script>