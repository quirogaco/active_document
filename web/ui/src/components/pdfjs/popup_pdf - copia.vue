<template>

    <DxPopup
        ref                     = "popup"    
        v-model:visible         = "visible"        
        :drag-enabled           = "false"
        :close-on-outside-click = "true"
        :show-close-button      = "true"
        :show-title             = "true"            
        :width                  = "ancho"
        :height                 = "alto"
        :title                  = "titulo"            
        :element-attr           = "popupAttributes"
    >     

        <DxScrollView
            width     = "90%"
            height    = "90%"
            direction = "both"
            :useNative = "true"
        >
                
            <pdf_componente 
                :nombrePdf   = "nombrePdf" 
                :buscarTexto = "buscarTexto" 
                :operacion   = "operacion" 
                :clase       = "clase" 
                :descarga    = "descarga"
                :datos       = "datos" 
            />
                
        </DxScrollView>  

    </DxPopup>    
    
</template>

<script>    
    import pdf_componente   from './pdf_componente.vue'
    import DxButton         from 'devextreme-vue/button'
    import { DxPopup }      from 'devextreme-vue/popup'
    import { DxScrollView } from 'devextreme-vue/scroll-view'

    import librerias from '../../librerias/librerias.js'

    import { 
        onMounted,    
        getCurrentInstance,
        ref
    } from 'vue'

    export default {
        components: {        
            DxPopup,
            DxButton,
            DxScrollView,
            pdf_componente
        },

        methods: {
            mostrarPdf(e) { 
                this.visible     = true
                this.nombrePdf   = e.idArchivo
                this.buscarTexto = e.buscarTexto
                this.operacion   = e.operacion           
                this.clase       = e.clase
                this.descarga    = e.descarga
                this.titulo      = e.titulo
                this.datos       = librerias.cargaAtributo(e, "datos", {})             
            }
        },

        setup(props, context) {    

            onMounted(() => {
                let unoMismo = getCurrentInstance().ctx;
                window.$emitter.on(
                    'mostrar_pdf_sistema', 
                    function(e) {    
                        unoMismo.mostrarPdf(e); 
                    }  
                )      
            }) 

            return { 
                visible    : ref(false),
                nombrePdf  : ref(''), 
                buscarTexto: ref(''), 
                operacion  : ref(''), 
                clase      : ref(''), 
                descarga   : ref(''),
                datos      : {},
                ancho      : ref("90%"), 
                alto       : ref("90%"), 
                titulo     : ref('Visor de Pdf'), 
                popupAttributes: {
                    id: 'ventana_emergente_visor_pdf',
                    class: 'bg_tab_panel'
                }
            }
        }
    }
</script>