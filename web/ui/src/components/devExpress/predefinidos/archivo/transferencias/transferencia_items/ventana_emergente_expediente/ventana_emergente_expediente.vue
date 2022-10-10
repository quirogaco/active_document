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

            <DxScrollView
                width = "100%"
                height= "100%"
            >
                <component v-bind:is="opciones.componente_visible" :opciones = "opciones"></component>
            </DxScrollView>  
                                    
        </DxPopup>

    
</template>

<script>
import { DxPopup } from 'devextreme-vue/popup'
import { DxScrollView } from 'devextreme-vue/scroll-view'

import archivo_expediente from '../componentes_expediente/archivo_expediente.vue'

let ventana =  {
    name: 'ventana_emergente_trd',

    components: {
        DxPopup,
        DxScrollView,
        archivo_expediente
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
        setTimeout(() => {
            window.$ventana_emergente_trd = this
        })
    },

    data() {
        return {
            popupAttributes: {
                id: 'ventana_emergente_documento',
                class: 'bg_tab_panel'
            }
        }
    }
}

export default ventana;

</script>