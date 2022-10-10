<template>
    <DxPopup
        ref                     = "popup"
        v-model:visible         = "opciones.visible"
        :drag-enabled           = "false"
        :close-on-outside-click = "true"
        :show-close-button      = "true"
        :show-title             = "true"
        :width                  = "opciones.ancho"
        :height                 = "opciones.alto"
        :title                  = "opciones.titulo"
        container               = ".dx-viewport" 
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

import dependencia_trd from '../componentes_trd/dependencia_trd.vue'
import serie_trd       from '../componentes_trd/serie_trd.vue'
import subserie_trd    from '../componentes_trd/subserie_trd.vue'
import tipo_trd        from '../componentes_trd/tipo_trd.vue'
import acceso_trd      from '../componentes_trd/acceso_trd.vue'

// Ventana emergente
let ventana =  {
    name: 'ventana_emergente_trd',

    components: {
        DxPopup,
        DxScrollView,
        dependencia_trd,
        serie_trd,
        subserie_trd,
        tipo_trd,
        acceso_trd
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
                id: 'ventana_emergente_trd',
                class: 'bg_tab_panel'
            }
        }
    }
}

export default ventana;

</script>