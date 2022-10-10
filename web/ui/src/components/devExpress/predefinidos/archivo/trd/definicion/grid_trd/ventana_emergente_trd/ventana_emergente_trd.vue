<template>
    <DxPopup
        ref                     = "popup"
        width                   = 1000
        height                  = 550        
        title                   = "Datos de la trd"        
        v-model:visible         = "opciones.visible"
        :drag-enabled           = "false"
        :close-on-outside-click = "true"
        :show-close-button      = "true"
        :show-title             = "true"
        container               = ".dx-viewport" 
        :element-attr           = "popupAttributes"
    >
        <DxScrollView
            width = "100%"
            height= "100%"
        >
            <trd_pantalla :attributes_str="opciones.attributes_str"/>
        </DxScrollView>
    </DxPopup>
</template>

<script>
import { DxPopup } from 'devextreme-vue/popup';
import { DxScrollView } from 'devextreme-vue/scroll-view';

import trd_pantalla from "../../pantalla_trd/pantalla_trd.vue";

// Ventana emergente
let ventana =  {
    name: 'ventana_emergente_trd',

    components: {
        DxPopup,
        DxScrollView,
        trd_pantalla
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
            window.$ventana_emergente_trd_importa = this            
        })        
    },

    data() {
        return {}
    }
}

export default ventana;

</script>