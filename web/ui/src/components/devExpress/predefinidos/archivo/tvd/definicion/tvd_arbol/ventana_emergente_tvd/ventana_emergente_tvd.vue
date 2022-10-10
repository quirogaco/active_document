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

import dependencia_tvd from '../componentes_tvd/dependencia_tvd.vue'
import serie_tvd       from '../componentes_tvd/serie_tvd.vue'
import subserie_tvd    from '../componentes_tvd/subserie_tvd.vue'
import acceso_tvd      from '../componentes_tvd/acceso_tvd.vue'

// Ventana emergente
let ventana =  {
    name: 'ventana_emergente_tvd',

    components: {
        DxPopup,
        DxScrollView,
        dependencia_tvd,
        serie_tvd,
        subserie_tvd,
        acceso_tvd
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
            window.$ventana_emergente_tvd = this
        })
    },

    data() {
        return {
            popupAttributes: {
                id: 'ventana_emergente_tvd',
                class: 'bg_tab_panel'
            }
        }
    }
}

export default ventana;

</script>