<template>

    <DxPopup
        ref                     = "popup"    
        v-model:visible         = "opciones.visible"           
        :drag-enabled           = "false"
        :close-on-outside-click = "true"
        :show-close-button      = "true"
        :show-title             = "true"            
        :width                  = "ancho"
        :height                 = "alto"
        :title                  = "titulo"            
        :element-attr           = "popupAttributes"
    >     

        <div class="col-12 shadow p-3 rounded">
        
            <onlyoffice_editor 
                ref             = "onlyoffice"                 
                :opciones       = "opciones.editor"
            />
        
        </div> 

    </DxPopup>    

</template>

<script>    
    import { DxPopup }       from 'devextreme-vue/popup'
    import DxButton          from 'devextreme-vue/button'
    import { DxScrollView }  from 'devextreme-vue/scroll-view'
    import onlyoffice_editor from "./onlyoffice_editor.vue"
    import { 
        ref
    } from 'vue'

    import opciones_base_editor from "./opciones_base.js"

    import librerias from '../../librerias/librerias.js'

    export default {
        components: {      
            DxPopup,
            DxButton,
            DxScrollView,                 
            onlyoffice_editor   
        },

        props: {
            opciones: {
                type: Object,
                default: () => {
                    return {}
                }
            }        
        },

        data() {
            return {
                // Pasar a global para ser usado en varias partes
                opciones_editor: {},
                visible    : ref(false),
                ancho      : ref("95%"), 
                alto       : ref("95%"), 
                titulo     : ref('Editor/Visor archivos'), 
                popupAttributes: {
                    id   : 'ventana_emergente_visor_archivos',
                },
                emergente_key: 1
            }
        },

        mounted() {
            let self = this
            this.editor = this.$refs.onlyoffice            
            if (this.opciones.visible == true) {
                this.mostrar_visor(this.opciones.editor)
            }
        },

        methods: {
            mostrar_visor(parametros) { 
                // Titulo Popup
                this.titulo          = (parametros.titulo != undefined)? parametros.titulo: this.titulo
                let copia_base       = Object.assign({}, opciones_base_editor)
                let parametros_visor = librerias.mezcla_profunda({}, copia_base, parametros)
                this.editor.mostrar_editor(parametros_visor)               
            }
        }
    }
</script>