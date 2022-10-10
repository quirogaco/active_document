<template>
    <DxPopup
        ref                     = "popup"
        v-model:visible         = "opciones.visible"
        :drag-enabled           = "false"
        :close-on-outside-click = "false"
        :show-close-button      = "true"
        :show-title             = "true"
        :title                  = "titulo"
        container               = ".dx-viewport" 
        :element-attr           = "popupAttributes"
    >
        <DxScrollView
            width = "100%"
            height= "100%"
        >
        
            <div class="full-width-content ">
                <div class="dx-fieldset">
                    <div class="dx-field">
                        <div class="dx-field-label">Detalle planilla:</div>
                        <div class="dx-field-value">
                            <DxTextArea
                                :height       = "90"
                                v-model:value = "detalle"
                            />
                        </div>
                    </div>

                </div>

            </div>  

            <DxToolbar>
                <DxItem
                    :options = "accion_opciones"
                    location = "after"
                    widget   = "dxButton"
                />
            </DxToolbar>
            
        </DxScrollView>
    </DxPopup>
</template>

<script>
import { DxPopup } from 'devextreme-vue/popup'
import { DxScrollView } from 'devextreme-vue/scroll-view'

import DxTextArea from 'devextreme-vue/text-area'
import DxButton from 'devextreme-vue/button'
import DxToolbar, { DxItem } from 'devextreme-vue/toolbar'

let ventana_planilla =  {
    name: 'ventana_planilla',

    created() {
        locale("es")
    },

    components: {
        DxPopup,
        DxScrollView,
        DxTextArea,       
        DxButton,
        DxToolbar,
        DxItem
    },

    created() {},

    props: {
        opciones: {
            type: Object,
            default: () => {
                return {}
            }
        },  
    },

    mounted() {

    },

    methods: {
        retorna: function() {
            this.opciones.visible = false
            window.$router.push({path: "planilla_grid"})
        }
    },

    data() {
        return {
            titulo         : "Creación de planilla",
            detalle        : null,
            accion_opciones: {
                text: "Crear planilla",
                type: "success",
                onClick: () => {
                    let parametros = {
                        accion: "crear_planilla",
                        datos : this.detalle,
                    }
                    let urlCompleta = window.$direcciones.servidorDatos + '/envio_acciones'    
                    window.$f["http"].llamadoRestPost( urlCompleta, parametros, this.retorna)
                }
            },

            popupAttributes: {
                id: 'ventana_planilla',
                class: 'bg_tab_panel'
            }
        }
    }
}

export default ventana_planilla;

</script>