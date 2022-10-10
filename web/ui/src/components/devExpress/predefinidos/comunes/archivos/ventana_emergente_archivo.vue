<template>
    
        <DxPopup
            ref                     = "popup"    
            v-model:visible         = "opciones.visible"        
            :drag-enabled           = "false"
            :close-on-outside-click = "true"
            :show-close-button      = "true"
            :show-title             = "true"            
            :width                  = "800"
            :height                 = "500"
            :title                  = "opciones.titulo"            
            :element-attr           = "popupAttributes"
        >        

            <DxScrollView
                width = "100%"
                height= "100%"
            >
                <cargar_archivo :opciones="opciones"/>
            </DxScrollView>  
                                    
        </DxPopup>
    
</template>

<script>
import { DxPopup }      from 'devextreme-vue/popup'
import { DxScrollView } from 'devextreme-vue/scroll-view'

import cargar_archivo from './cargar_archivo.vue'

let ventana_emergente_archivo =  {
    name: 'ventana_emergente_archivo',

    components: {
        DxPopup,
        DxScrollView,
        cargar_archivo
    },

    created() {},

    props: {
        opciones: {
            type: Object,
            default: () => {
                return {
                    visible : false,
                    datos   : {},
                    atributos: {
                        titulo_pantalla: "Cargar archivo",
                        titulo_boton   : "Seleccione archivo",
                        mensaje_retorno: "Envio de archivo correcto!" 
                    }
                }
            }
        }        
    },
    
    mounted() {
        setTimeout(() => {
            window.$ventana_emergente_archivos = this
        })
    },

    data() {
        return {
            popupAttributes: {
                id   :  'ventana_emergente_archivo',
                class: 'bg_tab_panel'
            }
        }
    }
}

export default ventana_emergente_archivo;
</script>